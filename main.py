from ai import answer
from tweets import fetch_tweets_from_url, clean_text
from flask import jsonify

def handle_prompt(prompt):
    result = answer(prompt)
    response = {
        'content' : prompt,
        'classification' : parse_label(result['label']),
        'misleading' : result['Misinformed_or_potentially_misleading'],
        'not_misleading' : result['Not_misleading'],
        'unknown' : result['Unknown']
    }

    if result['label'] == 'Unknown':
        response['content'] = ''

    return response


def handle_text(request):
    """Responds to any HTTP request.
    Args:
        payload of request (flask.Request): HTTP request object.
    Returns:
        AI's response to given text
    """
    return handle_prompt(str(request))
    

def handle_tweet(request):
    """Responds to any HTTP request.
    Args:
        payload of request (flask.Request): HTTP request object.
    Returns:
        AI's response to given tweet
    """
    return handle_prompt(str(clean_text(fetch_tweets_from_url(request))))


def parse_label(label):
    if label == "Misinformed_or_potentially_misleading":
        label = "misleading"
    elif label == "Not_misleading":
        label = "not_misleading"
    else:
        label = "unknown"
    return label


def handler(request):
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)

    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    
    frontend = request.json['type']
    response = {
        'classification': 'Unknown',
        'content': '',
        'misleading': 0.0,
        'not_misleading': 0.0,
        'unknown': 0.0
    }
    if frontend == "twitter":
        response = handle_tweet(request.json['payload'])
    elif frontend == "text":
        response = handle_text(request.json['payload'])
    return (jsonify(response), 200, headers)
