import base64
import csv
import random
import requests
from urllib.parse import quote
from requests_oauthlib import OAuth1
from groq import Groq

# Configuration file path
CONFIG_FILE = "codes"
CSV_FILE = "YuGiOh_Card_List.csv"  # Path to your card list
CARD_API_URL = "https://db.ygoprodeck.com/api/v7/cardinfo.php?name={}"
MEDIA_UPLOAD_URL = "https://upload.twitter.com/1.1/media/upload.json"
TWEET_CREATE_URL = "https://api.twitter.com/2/tweets"
token_endpoint = 'https://api.twitter.com/2/oauth2/token'

# Function to read configuration from the file
def read_config(file_path):
    config = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=', 1)
            config[key] = value.strip('"')  # Remove surrounding double quotes
    return config

# Function to write updated configuration to the file
def write_config(file_path, config):
    with open(file_path, 'w') as file:
        for key, value in config.items():
            file.write(f'{key}="{value}"\n')  # Enclose values in double quotes

# Function to refresh access token
def refresh_access_token(refresh_token, token_endpoint, encoded_credentials):
    headers = {
        'Authorization': f'Basic {encoded_credentials}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token
    }
    response = requests.post(token_endpoint, headers=headers, data=data)
    if response.status_code == 200:
        tokens = response.json()
        new_access_token = tokens.get('access_token')
        new_refresh_token = tokens.get('refresh_token', refresh_token)  # Default to old refresh token if no new one is provided
        print(f"New Access Token: {new_access_token}")
        print(f"New Refresh Token: {new_refresh_token}")
        return new_access_token, new_refresh_token
    else:
        print(f"Failed to refresh token. Status code: {response.status_code}")
        print(f"Response: {response.text}")
        return None, refresh_token

# Function to upload media to Twitter
def upload_media_v1(file_path):
    """Upload media to Twitter using v1 API."""
    auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    with open(file_path, 'rb') as file:
        files = {"media": file}
        response = requests.post(MEDIA_UPLOAD_URL, auth=auth, files=files)
    if response.status_code == 200:
        media_id = response.json()["media_id_string"]
        print(f"Media uploaded successfully. Media ID: {media_id}")
        return media_id
    else:
        print(f"Failed to upload media: {response.status_code} - {response.text}")
        return None

# Function to get random card, fetch trivia, download artwork, and post it
def get_random_card_and_post(csv_file, groq_client, access_token):
    try:
        # Step 1: Fetch a random card
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            cards = list(reader)
        if not cards:
            raise ValueError("The CSV file is empty or improperly formatted.")
        random_card = random.choice(cards)[0]  # Get a random card name
        print(f"Selected random card: {random_card}")

        # Step 2: Fetch card details from the API
        encoded_card_name = quote(random_card)
        response = requests.get(CARD_API_URL.format(encoded_card_name))
        if response.status_code != 200:
            raise ValueError(f"Failed to fetch card details for {random_card}")
        card_data = response.json()
        if 'data' not in card_data or len(card_data['data']) == 0:
            raise ValueError(f"No data found for card {random_card}")

        # Step 3: Download card artwork
        image_url = card_data['data'][0]['card_images'][0]['image_url']
        file_name = f"{random_card.replace(' ', '')}_art.jpg"
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            with open(file_name, 'wb') as img_file:
                img_file.write(image_response.content)
            print(f"Artwork downloaded: {file_name}")
        else:
            raise ValueError(f"Failed to download artwork for {random_card}")

        # Step 4: Generate trivia using Groq
        chat_completion = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"please give me a piece of trivia about the YuGiOh card '{random_card}' in a terse and factual style, with no hashtags. have it fit into 240 characters.",
                }
            ],
            model="llama3-8b-8192",
        )
        trivia = chat_completion.choices[0].message.content
        print(f"Generated trivia: {trivia}")

        # Step 5: Post the trivia and artwork
        media_id = upload_media_v1(file_name)
        if media_id:
            make_post(access_token, trivia, media_id)
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to make a post with media
def make_post(access_token, tweet_text, media_id):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    data = {
        "text": tweet_text,
        "media": {
            "media_ids": [media_id]
        }
    }
    response = requests.post(TWEET_CREATE_URL, headers=headers, json=data)
    if response.status_code == 201:
        print(f"Successfully posted: {tweet_text}")
    else:
        print(f"Failed to post: {tweet_text}")
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.text}")

# Read the configuration from the file
config = read_config(CONFIG_FILE)
client_id = config['client_id']
client_secret = config['client_secret']
refresh_token = config['refresh_token']
current_access_token = config['current_access_token']
API_KEY = config['API_KEY']
API_SECRET = config['API_SECRET']
ACCESS_TOKEN = config['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = config['ACCESS_TOKEN_SECRET']

# Refresh tokens and update config
encoded_credentials = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
new_access_token, refresh_token = refresh_access_token(refresh_token, token_endpoint, encoded_credentials)
if new_access_token:
    config['refresh_token'] = refresh_token
    config['current_access_token'] = new_access_token
    write_config(CONFIG_FILE, config)

# Initialize Groq client
groq_client = Groq(api_key=config['groq_api_key'])

if __name__ == "__main__":
    # Post a random card trivia with artwork
    get_random_card_and_post(CSV_FILE, groq_client, new_access_token)
