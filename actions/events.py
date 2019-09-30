import sys
from st2common.runners.base_action import Action
import requests
from urllib.parse import quote, urlencode
import base64
import json
import time
class MyAction(Action):
    def run(self ):
        client_id = 'e1502f9c-87a4-4b8b-acf0-c41e1658624c'
        client_secret = 'YOUR APP PASSWORD HERE'
        # Constant strings for OAuth2 flow
        # The OAuth authority
        authority = 'https://login.microsoftonline.com'

        # The authorize URL that initiates the OAuth2 client credential flow for admin consent
        authorize_url = '{0}{1}'.format(authority, '/common/oauth2/v2.0/authorize?{0}')

        # The token issuing endpoint
        token_url = '{0}{1}'.format(authority, '/common/oauth2/v2.0/token')

        # The scopes required by the app
        scopes = [ 'openid',
                'User.Read',
            'Mail.Read' ]
        access_token="e1502f9c-87a4-4b8b-acf0-c41e1658624c"

        #get_events_url= "https://outlook.office.com/api/v2.0/me/calendarview?startdatetime=2015-01-01T00:00:00Z&enddatetime=2015-04-10T00:00:00Z"
        get_events_url="https://graph.microsoft.com/v1.0/me/events/hxv?OPANLDz3_zf4pLfs_b94??6bN4[C?$select=subject,body,bodyPreview,organizer,attendees,start,end,location"
        r = requests.get(get_events_url,headers=headers,verify=False)
        #"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize?client_id=e1502f9c-87a4-4b8b-acf0-c41e1658624c&response_type=code&redirect_uri=https://127.0.0.1&response_mode=query&scope=openid%20offline_access%20https%3A%2F%2Fgraph.microsoft.com%2Fuser.read&state=12345"
        #r = make_api_call('GET', get_events_url, access_token, parameters = query_parameters)

        if (r.status_code == requests.codes.ok):
            return r.json()
        else:
            return "{0}: {1}".format(r.status_code, r.text)