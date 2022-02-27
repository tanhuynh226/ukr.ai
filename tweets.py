import requests
import re
import os
from dotenv import load_dotenv
from urllib.parse import urlparse
from dotenv import load_dotenv

"""This module contains methods related to fetching and processing tweets"""

load_dotenv()
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
ENDPOINT = 'https://api.twitter.com/2/tweets'

def _create_headers(bearer_token):
    headers = {"Authorization": f"Bearer {bearer_token}"}
    return headers


def _fetch_response(headers, params):
    response = requests.get(ENDPOINT, headers=headers, params=params)
    
    if response.status_code != 200:
            raise Exception(response.status_code, response.text)
    
    return response


# Makes Twitter API request for tweets with ids
# Returns list of tweets as dictionaries
def fetch_tweets_from_ids(ids):

    def format_ids(ids):
        """Takes input of nparray of IDs and outputs comma separated strings"""
        return ','.join(str(id) for id in ids)

    params = {
        'ids': format_ids(ids),
        'tweet.fields': 'entities'
    }

    return _fetch_response(_create_headers(BEARER_TOKEN), params).json()['data']


# Makes Twitter API request for tweets with url
# Returns one tweets as dictionaries
def fetch_tweets_from_url(url):
    def id_from_url(url):
        return urlparse(url).path.split('/')[-1]

    params = {
        'ids': id_from_url(url),
        'tweet.fields': 'entities'
    }
    return _fetch_response(_create_headers(BEARER_TOKEN), params).json()['data'][0]


# Takes tweet as a dictionary
# Returns string with mentions and links in tweet text removed 
def clean_text(tweet):
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