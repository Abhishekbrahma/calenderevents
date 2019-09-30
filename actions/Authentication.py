import getopt
import sys
import json
import re
from adal import AuthenticationContext
class MyAction(Action):

    username = 'abhisheknihilent.outlook.com'
    password = 'M1cr0123'
    authority = 'OtAGIIR.FzCR6G5N]ra.j@H5OWF7zN.R'
    resource = ''

    clientId = 'e1502f9c-87a4-4b8b-acf0-c41e1658624c'

    if username == '' or password == '' or authority == '' or resource == '' or clientId == '':
        printUsage()
        sys.exit(-1)

  # Find everything after the last '/' and replace it with 'token'
    if not authority.endswith('token'):
        regex = re.compile('^(.*[\/])')
        match = regex.match(authority)
        authority = match.group()
        authority = authority + username.split('@')[1]

    auth_context = AuthenticationContext(authority)
    token = auth_context.acquire_token_with_username_password(resource, username, password, clientId)
    print(token["accessToken"])
