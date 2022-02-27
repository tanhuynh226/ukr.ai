from ai import answer
from tweets import fetch_tweets_from_url, clean_text
from flask import jsonify
import requests

def handle_text(request):
    """Responds to any HTTP request.
    Args:
        payload of request (flask.Request): HTTP request object.
    Returns:
        AI's response to given text
    """
    user_prompt = str(request)
    result = answer(user_prompt)
    response = {
        'classification' : parse_label(result),
        'probability' : ''
    }
    return response

def handle_tweet(request):
    """Responds to any HTTP request.
    Args:
        payload of request (flask.Request): HTTP request object.
    Returns:
        AI's response to given tweet
    """
    user_prompt = str(clean_text(fetch_tweets_from_url(request)))
    result = answer(user_prompt)
    response = {
        'classification' : parse_label(result),
        'probability' : ''
    }
    return response

def parse_label(label):
    if label == "Misinformed_or_potentially_misleading":
        label = "Misleading"
    elif label == "Not_misleading":
        label = "Not misleading"
    else:
        label = "Unrelated"
    return label

def handler(request):
    frontend = request.json['type']
    if frontend == "twitter":
        response = handle_tweet(request.json['payload'])
    elif frontend == "text":
        response = handle_text(request.json['payload'])
    return jsonify(response)
