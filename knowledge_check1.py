import requests
import json

# headers = { 
#   "apikey": "90283200-390c-11ed-8053-5d97ba040711"}

# params = (
#    ("season_id","496"),
#    ("date_from","2020-09-19"),
# )

# response = requests.get('https://app.sportdataapi.com/api/v1/soccer/matches', headers=headers, params=params);
# print(response.text)



headers = { 
  "apikey": "90283200-390c-11ed-8053-5d97ba040711"}

params = (
   ("continent","Europe"),
)

response = requests.get('https://app.sportdataapi.com/api/v1/soccer/countries', headers=headers, params=params)

r = response.json()

data = r['data']

england_val = []

for key,value in data.items():

	if value['name'] == 'England':
	
		england_val.append(value['country_id'])

eng_id = england_val[0]


# print(data)