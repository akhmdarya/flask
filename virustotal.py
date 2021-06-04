
import json
import requests


def AntiVirus(url):
  api_url = 'https://www.virustotal.com/vtapi/v2/url/scan'
  params = dict(apikey='dbd8762dded803419d94e689928f6c23950ac43820a5810a65652d69d3879030', resource=url, scan=0)
  response = requests.post(api_url, params=params)
  if response.status_code == 200:
    
    
    result=response.json()
    #print("\nResult" + json.dumps(result, sort_keys=False, indent=4))
    #print("\nResult" + json.dumps(result, sort_keys=False, indent=4))
    #return str(response.request.headers)
    return str(json.dumps(result, sort_keys=False, indent=4))

