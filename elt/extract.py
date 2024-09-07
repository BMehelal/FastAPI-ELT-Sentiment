from googleapiclient.discovery import build
from dotenv import load_dotenv
import os


load_dotenv(override=True)

api_service_name = os.getenv('API_SERVICE_NAME')
api_version = os.getenv('API_VERSION')
api_key = os.getenv("API_KEY")


def extract_elt(video_id):

    if not api_service_name or not api_version or not api_key:
        raise Exception("Credentials not found")

    youtube = build(
        api_service_name, api_version, developerKey=api_key)
    all_comments = []
    
    request = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=2
    )
    response = request.execute()
    all_comments.extend(response['items'])

    while 'nextPageToken' in response and len(all_comments) < 5:
        request = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=2,
            pageToken=response['nextPageToken']
        )
        response = request.execute()
        all_comments.extend(response['items'])
    
    if all_comments:
        all_comments.pop(0)
    return all_comments



