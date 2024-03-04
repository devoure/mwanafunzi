import requests
import json

def authenticate():
    client_id = 'St0JEz7hb1XUmMX547BXIsW0IQpclrtrY8H4ucyiIxoAKG93'
    client_secret = '0mUBFEcQsck6TRdvHVnS4NAJC14mxF91DSYctGVOR2m1Azv18qmKI9ZuTdgTJ08Q'

    token_endpoint = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    # Send a GET request to the token endpoint with client ID and secret
    response = requests.get(token_endpoint, auth=(client_id, client_secret))

    # Parse the response JSON and extract the access token
    if response.status_code == 200:
        access_token = response.json().get('access_token')
        return access_token
    else:
        return None
