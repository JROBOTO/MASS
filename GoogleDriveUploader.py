#This file will upload the video to Google Drive
#Author: Joshua Roberts

import os
import pprint
import httplib2

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient.http import MediaFileUpload

CLIENTSECRET = "ClientSecret.json"
SCOPES = 'https://www.googleapis.com/auth/drive'
APPLICATION_NAME = 'Drive API Python Quickstart'

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


def getCredentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'drive-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENTSECRET, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)

    return credentials

credentials = getCredentials()

def uploadVideo(timeStamp):
    "Upload the stated video to Google Drive"
    
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)

    videoPath = timeStamp + ".mp4"
    
    os.chdir("/home/pi/MASS/Videos")
    videoFile = MediaFileUpload(videoPath, mimetype = "video/mp4", resumable = True)

    body = {"name": videoPath, "description": "Intrusion at " + timeStamp, "mimetype": "video/mp4"}

    file = service.files().create(body=body, media_body=videoFile).execute()
    pprint.pprint(file)
    os.chdir("/home/pi/MASS")

    print("Video uploaded")
 
