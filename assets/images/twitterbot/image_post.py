import requests
from requests_oauthlib import OAuth1

# Replace with your credentials
API_KEY = "OAUTH1_API_KEY"
API_SECRET = "OAUTH1_API_SECRET"
ACCESS_TOKEN = "OAUTH1_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "OAUTH1_ACCESS_TOKEN_SECRET"

BASE_URL = "https://upload.twitter.com/1.1/media/upload.json"
TWEET_URL = "https://api.twitter.com/1.1/statuses/update.json"

def upload_media(file_path):
    """Upload media to Twitter."""
    auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    
    with open(file_path, 'rb') as file:
        files = {"media": file}
        response = requests.post(BASE_URL, auth=auth, files=files)
    
    if response.status_code == 200:
        media_id = response.json()["media_id_string"]
        print(f"Media uploaded successfully. Media ID: {media_id}")
        return media_id
    else:
        print(f"Failed to upload media: {response.status_code} - {response.text}")
        return None

def post_tweet(media_id, tweet_text):
    """Post a tweet with media."""
    auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    payload = {"status": tweet_text, "media_ids": media_id}
    response = requests.post(TWEET_URL, auth=auth, data=payload)
    
    if response.status_code == 200:
        print("Tweet posted successfully!")
    else:
        print(f"Failed to post tweet: {response.status_code} - {response.text}")

if __name__ == "__main__":
    file_path = "IMAGE_TO_UPLOAD"  # Update with your image path
    tweet_text = "Your tweet text here"  # Update with your tweet text

    # Upload media and post tweet
    media_id = upload_media(file_path)
    if media_id:
        post_tweet(media_id, tweet_text)
