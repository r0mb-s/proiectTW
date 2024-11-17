from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from os import getenv
from dotenv import load_dotenv
load_dotenv()
# Scopes needed for accessing Google Classroom
SCOPES = ['https://www.googleapis.com/auth/classroom.courses.readonly']

def authenticate_user():
    """Authenticate the user and return Google Classroom API service."""
    flow = InstalledAppFlow.from_client_secrets_file(
        getenv('GOOGLE_CLIENT_SECRET'), SCOPES)  # Replace with your client secrets file
    creds = flow.run_local_server(port=0)  # Prompts the user to login and grant permissions
    service = build('classroom', 'v1', credentials=creds)
    return service
