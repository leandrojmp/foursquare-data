import json
import requests
import time
from sys import argv

data = json.load(open('checkins.json','r'))

with open('db.log','r') as db:
    checkin_db = {}
    for l in db:
        d = json.loads(l.strip('\n'))
        for k, v in d.items():
            checkin_db[k] = v

total_checkins = []
with open('locations.json','a') as output_file:
    for c in data['items']:
        if 'venue' in c:
            checkin = {}
            checkin['_id'] = c['id']
            checkin['timestamp'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(c['createdAt'])))
            checkin['venue_id'] = c['venue']['id']
            checkin['venue_name'] = c['venue']['name']
            checkin['geolocation'] = checkin_db[checkin['venue_id']]
            json.dump(checkin, output_file)
            output_file.write('\n')