import sys
from st2common.runners.base_action import Action
import requests
class MyAction(Action):
    def run(self):
        query_parameters = {'$top': '10',
                      '$select': 'subject,start,end',
                      '$orderby': 'start/dateTime ASC'}
        access_token="e1502f9c-87a4-4b8b-acf0-c41e1658624c"
        get_events_url="https://graph.microsoft.com/v1.0/me/events/4P3Sw-/d.=7ro40s8[[jODCUJAZOv]B@?$select=subject,body,bodyPreview,organizer,attendees,start,end,location"
        resp = requests.get(get_events_url,verify=False)

        #r = make_api_call('GET', get_events_url, access_token, parameters = query_parameters)
        if (resp.status_code == requests.codes.ok):
            return resp.json()
        else:
            return "{0}: {1}".format(resp.status_code, resp.text)