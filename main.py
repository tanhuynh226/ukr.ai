from ai import answer

def get_answer(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        AI's response to given prompt
    """
    user_prompt = str(request.get_data())
    result = answer(user_prompt)
    return result