import pandas as pd
from odds import get_odds_data

# An api key is emailed to you when you sign up to a plan
# Get a free API key at https://api.the-odds-api.com/

game_odds_df = get_odds_data()

##Find and print TWO descriptive statistics about your data. This can be absolutely anything, from the mean() or sum() of a column to the number of different categories, to the number of null values in a column. We just want to see two pieces of information.
riskiest_bet = game_odds_df.loc[game_odds_df['win_away_team'] == game_odds_df['win_away_team'].max()]
safest_bet = game_odds_df.loc[game_odds_df['win_home_team'] == game_odds_df['win_home_team'].max()]
print('The riskests bet is: ', riskiest_bet)
print('The safest bet is: ', safest_bet)

##Write a query in Pandas to select a particular set of your data. You can use a mask or with .query(), but we want you to pull out a subset based on any parameter you like. This could be "show me every row where HTTPS=False" or anything else.

interesting_away_games = game_odds_df.query('win_away_team > win_home_team')
print(interesting_away_games)

#Select and print the SECOND AND THIRD columns of your data frame.

print(game_odds_df.iloc[2:4,:])

#Select and print the FIRST 4 rows of you data frame.

print(game_odds_df.head(4))



