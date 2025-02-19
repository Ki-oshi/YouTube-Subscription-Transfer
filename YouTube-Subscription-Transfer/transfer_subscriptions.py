import os
import pickle
import google.auth
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# OAuth 2.0 scopes
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def authenticate_youtube():
    """ Authenticate YouTube API and return a service instance. """
    flow = InstalledAppFlow.from_client_secrets_file("client_secrets.json", SCOPES)
    credentials = flow.run_local_server(port=8080)
    
    with open("token.pickle", "wb") as token:
        pickle.dump(credentials, token)
    
    return build("youtube", "v3", credentials=credentials)

def get_subscriptions(youtube):
    """ Get a list of channel IDs the source account is subscribed to. """
    subscriptions = []
    request = youtube.subscriptions().list(part="snippet", mine=True, maxResults=50)
    
    while request:
        response = request.execute()
        for item in response["items"]:
            channel_id = item["snippet"]["resourceId"]["channelId"]
            subscriptions.append(channel_id)
        request = youtube.subscriptions().list_next(request, response)
    
    return subscriptions

def subscribe_to_channels(youtube, channel_ids):
    """ Subscribe to the same channels on the target account. """
    for channel_id in channel_ids:
        try:
            request = youtube.subscriptions().insert(
                part="snippet",
                body={"snippet": {"resourceId": {"kind": "youtube#channel", "channelId": channel_id}}},
            )
            request.execute()
            print(f"Subscribed to {channel_id}")
        except Exception as e:
            print(f"Error subscribing to {channel_id}: {e}")

if __name__ == "__main__":
    print("🔵 Authenticating Source Account...")
    source_youtube = authenticate_youtube()
    
    print("📥 Fetching subscriptions...")
    channel_ids = get_subscriptions(source_youtube)
    
    print("🔴 Authenticate Target Account...")
    target_youtube = authenticate_youtube()
    
    print("📤 Subscribing to channels...")
    subscribe_to_channels(target_youtube, channel_ids)
    
    print("✅ Transfer Complete!")
