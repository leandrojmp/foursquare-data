import json
import requests
import time
from sys import argv

# read api credentials
config = json.load(open('config.json','r'))

params = dict(
    client_id = config['credentials']['id'],
    client_secret = config['credentials']['secret'],
    v='20190101'
)

data = json.load(open('checkins.json','r'))
checkins = []
with open('db.log','a') as output_file:
    for c in data['items']:
        if 'venue' in c:
            checkins.append(c['venue']['id'])
    venues = list(set(checkins))
    for v in venues:
        url = 'https://api.foursquare.com/v2/venues/{}'.format(v)
        resp = requests.get(url=url, params=params)
        result = json.loads(resp.text)
        checkin = {}
        checkin[v] = str(result['response']['venue']['location']['lat']) + "," + str(result['response']['venue']['location']['lng'])
        json.dump(checkin, output_file)
        output_file.write('\n')