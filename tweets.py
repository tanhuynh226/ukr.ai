import requests
import re

"""This module contains methods related to fetching and processing tweets"""

ENDPOINT = 'https://api.twitter.com/2/tweets'


def _fetch_response(header, params):
    response = requests.get(ENDPOINT, headers=header, params=params)
    
    if response.status_code != 200:
            raise Exception(response.status_code, response.text)
    
    return response


# Makes Twitter API request containing header and params
# Returns list of tweets as dictionaries
def fetch_tweets(header, params):
    return _fetch_response(header, params).json()['data']


# Takes tweet as a dictionary
# Returns string with mentions and links in tweet text removed 
def get_clean_text(tweet):
    if 'entities' not in tweet:
        return tweet['text']

    text = tweet['text']
    # Remove links
    if 'urls' in tweet['entities']:
        for url in tweet['entities']['urls']:
            text = re.sub(fr'{url["url"]}+', ' ', str(text))
    # Remove mentions
    if 'mentions' in tweet['entities']:
        for mention in tweet['entities']['mentions']:
            text = re.sub(fr'@{mention["username"]}+', ' ', str(text))

    return text

