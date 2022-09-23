import requests
import json
import pandas as pd


headers = { 
  "apikey": "90283200-390c-11ed-8053-5d97ba040711"}

# params = (
#    ("continent","Europe"),
# )

# response = requests.get('https://app.sportdataapi.com/api/v1/soccer/countries', headers=headers, params=params)

# r = response.json()

# data = r['data']

# england_val = []

# for key,value in data.items():

# 	if value['name'] == 'England':
	
# 		england_val.append(value['country_id'])

# eng_id = str(england_val[0])


# params = (
#    ("country_id",eng_id),
# )

# response = requests.get('https://app.sportdataapi.com/api/v1/soccer/leagues', headers=headers, params=params);

# r = response.json()

# data = r['data']

# england_data = []

# for key,value in data.items():

# 	if value['name'] == 'Premier League':
	
# 		england_data.append(value['league_id'])

# prem_id = str(england_data[0])


# params = (
#    ("league_id",prem_id),
# )

# response = requests.get('https://app.sportdataapi.com/api/v1/soccer/seasons', headers=headers, params=params);

# r = response.json()

# data = r['data']

# season_data = []


# for value in data:
# 	if value['is_current'] == 1:
# 		season_data.append(value['season_id'])

# season_id = str(season_data[0])


params = (
   ("season_id","3161"),
   ("date_from","2020-09-19"),
   ("status_code", 0),
   
)

# response = requests.get('https://app.sportdataapi.com/api/v1/soccer/matches', headers=headers, params=params);


# r = response.json()

# data = r['data']

# man_utd_matches =[]

# for value in data:

# 	if (value['home_team']['name'] == 'Manchester United') &(value['status']=='notstarted' ):
# 		man_utd_matches.append(value)
# 		print(value['match_id'])


# one_match = man_utd_matches[-1]

# print(one_match)

# df = pd.read_json(man_utd_matches)

# print(df.head())

one_match = {'match_id': 452990, 'status_code': 0, 'status': 'notstarted', 'match_start': '2023-05-28 17:00:00', 'match_start_iso': '2023-05-28T17:00:00+00:00', 'minute': None, 'league_id': 237, 'season_id': 3161, 'stage': {'stage_id': 1, 'name': 'Regular Season'}, 'group': {'group_id': 5038, 'group_name': 'Premier League 22/23'}, 'round': {'round_id': 49647, 'name': '38', 'is_current': None}, 'referee_id': None, 'home_team': {'team_id': 2523, 'name': 'Manchester United', 'short_code': 'MNU', 'common_name': '', 'logo': 'https://cdn.sportdataapi.com/images/soccer/teams/100/19.png', 'country': {'country_id': 42, 'name': 'England', 'country_code': 'en', 'continent': 'Europe'}}, 'away_team': {'team_id': 12429, 'name': 'Fulham FC', 'short_code': 'FUL', 'common_name': 'Fulham (R)', 'logo': 'https://cdn.sportdataapi.com/images/soccer/teams/100/6214.png', 'country': {'country_id': 42, 'name': 'England', 'country_code': 'en', 'continent': 'Europe'}}, 'stats': {'home_score': 0, 'away_score': 0, 'ht_score': None, 'ft_score': None, 'et_score': None, 'ps_score': None}, 'venue': {'venue_id': 1204, 'name': 'Old Trafford', 'capacity': 75635, 'city': 'Manchester', 'country_id': 42}}

# print(list(one_match.keys())[:8])
# print(list(one_match.values())[:8])

# print(list(one_match.values())[9:])

cols_basic = []
rows_basic =[]

combined_dics ={}

for item in list(one_match)[:8]:

	
	cols_basic.append(item)
		# print(item.values())
		# combined_dics |= item

for item in list(one_match.values())[:8]:

	
	rows_basic.append(item)

basic_dic = {cols_basic[i]: rows_basic[i] for i in range(len(cols_basic))}

# print(basic_dic)

for item in list(one_match.values())[9:]:
	if item != None:
		# print(item.keys())
		# print(item.values())
		combined_dics |= item
# print(combined_dics)

total_dic = basic_dic | combined_dics

df = pd.DataFrame(total_dic)
# df.reset_index(inplace=True)
df.drop_duplicates(subset=['match_id'],keep='last', inplace=True)

# df.to_excel('test.xlsx')

print(df)