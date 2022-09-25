import requests
from config import *
import pandas as pd



API_KEY = ODDS_API_KEY  # Get a free API key at https://api.the-odds-api.com/


def get_odds_data():
    '''
        With a valid API key, this function retrieves the any live games as well as the next 8 upcoming games across 
        the English Premier League. (Soccer ;)
    '''
    sports_response = requests.get(
        'https://api.the-odds-api.com/v4/sports/soccer_epl/odds/?regions=uk&bookmakers=williamhill', 
        params={
            'api_key': API_KEY,        
        }
    )

    if sports_response.status_code != 200:
        return {'message':f'Failed to get sports data: status_code {sports_response.status_code}, response body {sports_response.text}'}

    else:
        all_odds = sports_response.json()
        prem_odds =[]

        for value in all_odds:

            prem_odds.append({'home_team': value['home_team'],
                'away_team': value['away_team'],
                'match_start':value['commence_time'],
                'win_home_team': value['bookmakers'][0]['markets'][0]['outcomes'][0]['price'],
                'win_away_team':value['bookmakers'][0]['markets'][0]['outcomes'][1]['price'],
                'tie':value['bookmakers'][0]['markets'][0]['outcomes'][2]['price'],
            })
            
        odds_df = pd.DataFrame(prem_odds)

        odds_df['match_start'] = pd.to_datetime(odds_df['match_start'])
        odds_df['match_start'] = odds_df['match_start'].dt.tz_convert('EST')

        return odds_df


### MOVED AWAY FROM THE BELOW API. - KEEPING CODE FOR RECORDS SAKE.


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