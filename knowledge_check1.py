### MOVED AWAY FORM THIS API 




# import requests
# import json
# import pandas as pd
# import datetime as dt
# from config import *
# import pytz

# today = pd.to_datetime(dt.date.today())


# headers = { 
#   "apikey":SPORTS_API_KEY }


# params = (
#    ("season_id","3161"),
#    ("date_from","2020-09-19"),
#    ("status_code", 0),
   
# )

# response = requests.get('https://app.sportdataapi.com/api/v1/soccer/matches', headers=headers, params=params);


# r = response.json()

# data = r['data']

# prem_matches =[]

# for value in data:
# 	if (value['status']=='notstarted' ) & (pd.to_datetime(value['match_start']) >= today):
		
# 		match_dic={'match_id':value['match_id'],
# 			'match_start':value['match_start'],
# 			'home_team': value['home_team']['name'],
# 			'away_team': value['away_team']['name'],
# 			'status': value['status'],
# 			'ft_score': value['stats']['ft_score'],
# 			}
		
# 		prem_matches.append(match_dic)


# one_match = prem_matches[0]

# print(len(prem_matches))

# prem_df = pd.DataFrame(prem_matches)
# prem_df['match_start'] = pd.to_datetime(prem_df['match_start'])
# prem_df['match_start'] = prem_df['match_start'].dt.tz_localize('EST')
# prem_df['prem_day'] = prem_df['match_start'].dt.to_period('B')

# print(prem_df.head(1))

# odds_obj = [{'home_team': 'Arsenal', 'away_team': 'Tottenham Hotspur', 'match_start': '2022-10-01T11:30:00Z', 'win_home_team': 2.0, 'win_away_team': 3.5, 'tie': 3.6}]

# odds_df = pd.DataFrame(odds_obj)

# odds_df['match_start'] = pd.to_datetime(odds_df['match_start'])
# odds_df['match_start'] = odds_df['match_start'].dt.tz_convert('EST')
# odds_df['odds_day'] = odds_df['match_start'].dt.to_period('B')

# # odds_df['odds_year'] = odds_df['match_start'].dt.to_period('Y')
# # odds_df['odds_month'] = odds_df['match_start'].dt.to_period('M')
# # odds_df['odds_day'] = odds_df['match_start'].dt.to_period('B')

# print(odds_df)