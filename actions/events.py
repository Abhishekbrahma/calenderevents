from urllib.parse import *
import sys
from st2common.runners.base_action import Action
import requests
import base64
import json
import time

class MyAction(Action):
    def run(self ):

        client_id = 'e1502f9c-87a4-4b8b-acf0-c41e1658624c'
        client_secret = 'OtAGIIR.FzCR6G5N]ra.j@H5OWF7zN.R'
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
        params = { 'client_id': client_id,
             'redirect_uri': redirect_uri,
             'response_type': 'code',
             'scope': ' '.join(str(i) for i in scopes)
            }

        signin_url = authorize_url.format(urlencode(params))
        print(signin_url)