import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


def g_auth(scopes, service_type, version):
    creds = None

    if os.path.exists(f'MAIN_DIRECTORY_WHERE_CODE_WILL_LIVE/auth/token.json'):
        creds = Credentials.from_authorized_user_file(f'/MAIN_DIRECTORY_WHERE_CODE_WILL_LIVE/auth/token.json', scopes)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(f'MAIN_DIRECTORY_WHERE_CODE_WILL_LIVE/auth/credentials.json', scopes)
            creds = flow.run_local_server(port=0)
        with open(f'MAIN_DIRECTORY_WHERE_CODE_WILL_LIVE/auth/token.json', 'w') as token:
            token.write(creds.to_json())

    service = build(service_type, version, credentials=creds)

    return service
