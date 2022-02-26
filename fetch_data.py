import pandas as pd
import requests
import re
from statistics import mode


#tans: BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAIKlZgEAAAAA%2FPzTUcIMxE%2F1YSRh2b60shhO6C4%3DJFNP2ksUXD7qgTGxmhmkG6DHiCL4FvwNHR9gfLujioOff430au' 
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAHCXZgEAAAAAsFWHTYPNRHdi7ogP8CUBN%2FoM9QQ%3D1Id3Z7UFSoiCrknB7zA2BucLTzdpwgG3hdMY4cz5a5IvrzRYoL'
DATA_FILE = 'notes-00000.tsv'
ENDPOINT = 'https://api.twitter.com/2/tweets'


def read_data(filename):
    data = pd.read_csv(filename, sep='\t')
    return data


def create_headers(bearer_token):
    headers = {"Authorization": f"Bearer {bearer_token}"}
    return headers


def query(ids):

    def format_ids(ids):
        """Takes input of nparray of IDs and outputs comma separated strings"""
        return ','.join(str(id) for id in ids)

    params = {
        'ids': format_ids(ids),
        'tweet.fields': 'entities'
    }
    return params


def get_label_by_id(data, id):
    return ''.join(mode(data[data.tweetId == int(id)].classification))


def process_data(data):
    ids = data.tweetId.values

    with open("keywords.txt") as file:
        keywords = file.read().lower()
        keywords = keywords.split('\n')

    def chunk(lst, n):
        """Yield successive n-sized chunks"""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    fetched_data = {'text':[], 
                    'label':[], 
                    'metadata':[]}        
                    
    id_list = chunk(ids, 100)
    for id_chunk in id_list:
        # Send one request per 100 tweets
        response = requests.get(ENDPOINT, headers=create_headers(BEARER_TOKEN), params=query(id_chunk))

        if response.status_code != 200:
            raise Exception(response.status_code, response.text)

        for tweet in response.json()['data']:
            if tweet['id'] not in fetched_data['metadata'] and any(f' {x} ' in tweet['text'].lower() for x in keywords):
                text = tweet['text']
                if 'entities' in tweet:
                    # Remove links
                    if 'urls' in tweet['entities']:
                        for url in tweet['entities']['urls']:
                            text = re.sub(fr'{url["url"]}+', ' ', str(text))
                    
                    # Remove mentions
                    if 'mentions' in tweet['entities']:
                        for mention in tweet['entities']['mentions']:
                            text = re.sub(fr'@{mention["username"]}+', ' ', str(text))

                fetched_data['text'].append(text)
                fetched_data['label'].append(get_label_by_id(data, tweet['id']))
                fetched_data['metadata'].append(tweet['id'])

    del fetched_data['metadata'] # TODO: remove metadata?
    return pd.DataFrame(fetched_data)


if __name__ == '__main__':
    process_data(read_data(DATA_FILE)).to_csv("training_data.csv", encoding='utf-8', index=False)

