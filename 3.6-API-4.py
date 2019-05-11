import requests
import json

CLIENT_ID = '56aa74f4de43c0c41be3'
CLIENT_SECRET = '7f157297be247e8e4bd3e709400dfbf2'

authors = []

res = requests.post("https://api.artsy.net/api/tokens/xapp_token", data={
                      "client_id": CLIENT_ID,
                      "client_secret": CLIENT_SECRET
                  })

j = json.loads(res.text)

token = j["token"]

headers = {"X-Xapp-Token": token}

with open('dataset_24476_4.txt', 'r') as file:
    for artist_id in file:
        artist_id = artist_id.strip()

        res = requests.get("https://api.artsy.net/api/artists/{}".format(artist_id), headers=headers)
        res.encoding = 'utf-8'
        data = json.loads(res.text)

        authors.append({'name': data['sortable_name'], 'birthday': data['birthday']})

for artist in sorted(authors, key=lambda x: (x['birthday'], x['name'])):
    print(artist['name'])
