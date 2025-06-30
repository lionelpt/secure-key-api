# auth.py
API_KEY = "1234567890SECRET"

def verify_api_key(request):
    key = request.headers.get("x-api-key")
    return key == API_KEY