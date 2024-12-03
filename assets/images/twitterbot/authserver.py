import random
import string
import urllib.parse
import base64
import requests
from flask import Flask, request

# Replace these with your app's configuration
CLIENT_ID = "CLIENT_ID_HERE"
CLIENT_SECRET = "CLIENT_SECRET_HERE"
CALLBACK_URI = "http://127.0.0.1:5000/callback"
SCOPES = ["tweet.read", "tweet.write", "users.read", "offline.access"]

# Flask App
app = Flask(__name__)

# Globals
authorization_code = None
code_verifier = None
access_token = None
refresh_token = None

# Helper: Generate Random String
def generate_random_string(length=32):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Step 1: Generate Authorization URL
@app.route("/")
def generate_authorization_url():
    global code_verifier
    session_id = generate_random_string()
    code_verifier = generate_random_string()  # Code challenge = code verifier for simplicity
    authorization_url = (
        'https://twitter.com/i/oauth2/authorize'
        f'?response_type=code'
        f'&client_id={CLIENT_ID}'
        f'&redirect_uri={urllib.parse.quote(CALLBACK_URI)}'
        f'&scope={"+".join(SCOPES)}'
        f'&state={session_id}'
        f'&code_challenge={code_verifier}'
        '&code_challenge_method=plain'
    )
    return f"<h1>Visit this URL to authorize the app:</h1><a href='{authorization_url}'>{authorization_url}</a>"

# Step 2: Handle Callback and Exchange for Access Token
@app.route("/callback")
def handle_callback():
    global authorization_code, access_token, refresh_token
    authorization_code = request.args.get("code")
    print(f"Code Verifier: {code_verifier}")
    if authorization_code:
        # Exchange authorization code for access token
        token_url = 'https://api.twitter.com/2/oauth2/token'
        credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
        b64_encoded_credentials = base64.b64encode(credentials.encode()).decode()
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f'Basic {b64_encoded_credentials}',
        }
        data = {
            'code': authorization_code,
            'grant_type': 'authorization_code',
            'redirect_uri': CALLBACK_URI,
            'code_verifier': code_verifier,
        }
        response = requests.post(token_url, headers=headers, data=data)
        token_response = response.json()
        access_token = token_response.get("access_token")
        refresh_token = token_response.get("refresh_token")

        # Print retrieved tokens
        print(f"Authorization Code: {authorization_code}")
        print(f"Code Verifier: {code_verifier}")
        print(f"Access Token: {access_token}")
        print(f"Refresh Token: {refresh_token}")

        # Test Post
        post_url = "https://api.twitter.com/2/tweets"
        post_headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }
        post_data = {"text": "TESTING REFRESH TOKEN RETREIVAL"}
        post_response = requests.post(post_url, headers=post_headers, json=post_data)
        post_result = post_response.json()
        print(f"Test POST Response: {post_result}")

        return (
            f"<h1>Authorization Code Received:</h1>"
            f"<p>{authorization_code}</p>"
            f"<h1>Code Verifier:</h1>"
            f"<p>{code_verifier}</p>"
            f"<h1>Access Token:</h1>"
            f"<p>{access_token}</p>"
            f"<h1>Refresh Token:</h1>"
            f"<p>{refresh_token}</p>"
            f"<h1>Test POST Response:</h1>"
            f"<pre>{post_result}</pre>"
        )
    else:
        return "<h1>Error:</h1><p>No authorization code received.</p>"

# Run the Flask App
if __name__ == "__main__":
    app.run(port=5000)
