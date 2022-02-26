from ai import answer

def get_answer(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        AI's response to given prompt
    """
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return answer(request.args.get('message'))
    elif request_json and 'message' in request_json:
        return answer(request_json['message'])
    else:
        return f'No prompt given.'
