import os

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

import secrets
import string
import re


SCOPES = ['https://www.googleapis.com/auth/admin.directory.user', 'https://www.googleapis.com/auth/admin.directory.group']
curr_file = os.path.realpath(__file__)
current_directory = os.path.dirname(curr_file)

def get_users():
    page_token = None
    emails_users = []
    users = []

    creds = Credentials.from_authorized_user_file(current_directory + '/token.json', SCOPES)
    service = build('admin', 'directory_v1', credentials=creds)
    while True:

        results = service.users().list(customer='my_customer', pageToken=page_token).execute()
        users.extend(results.get('users', []))

        page_token = results.get('nextPageToken')
        if not page_token:
            break

    for user in users:
        # print(user['a'])
        emaildata = []
        emails = user['emails']
        for email in emails:

            emaildata.append(email['address'])

        emails_users.append(emaildata)

    return emails_users









