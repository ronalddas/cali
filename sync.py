import gflags
import httplib2
import google_api_secrets as gas

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run





class CalenderAPI():

    def __init__(self):
        global service,page_token
        print("called")
        self.FLAGS = gflags.FLAGS

        self.FLOW = OAuth2WebServerFlow(
            client_id=gas.api_key(),
            client_secret=gas.client_secret(),
            scope='https://www.googleapis.com/auth/calendar',
            user_agent='cali/alpha 1')

        self.storage = Storage('calendar.dat')
        self.credentials = self.storage.get()
        if self.credentials is None or self.credentials.invalid == True:
          self.credentials = run(self.FLOW, self.storage)


        self.http = httplib2.Http()
        self.http = self.credentials.authorize(self.http)

        service = build(serviceName='calendar', version='v3', http=self.http,
            developerKey=gas.dev_key())



    def get_events(self):
         page_token = None
         while True:
          events = service.events().list(calendarId='primary', pageToken=page_token).execute()
          for event in events['items']:
            print('-------------------------')
            for i in event:
                print i,":",event[i]
          page_token = events.get('nextPageToken')
          if not page_token:
            break
