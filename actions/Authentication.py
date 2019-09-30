import getopt
import sys
import json
import re
from adal import AuthenticationContext
from microsoftgraph.client import Client
class MyAction(Action):
    def run(self ):

    username = 'abhisheknihilent.outlook.com'
    password = 'M1cr0123'
    authority = 'OtAGIIR.FzCR6G5N]ra.j@H5OWF7zN.R'
    resource = ''

    clientId = 'e1502f9c-87a4-4b8b-acf0-c41e1658624c'
    client = Client('e1502f9c-87a4-4b8b-acf0-c41e1658624c', 'OtAGIIR.FzCR6G5N]ra.j@H5OWF7zN.R', account_type='by defect common')
    url = client.authorization_url(redirect_uri, scope, state=None)
    print(url)
