# pandas statistics

import requests

# download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
# target_csv_path = "nba_all_elo.csv"

# response = requests.get(download_url)
# response.raise_for_status()    # Check that the request was successful
# with open(target_csv_path, "wb") as f:
#     f.write(response.content)
# print("Download ready.")

import pandas as pd 
import numpy as np 

nba = pd.read_csv('nba_all_elo.csv')
# print(type(nba),'\n')
# print(len(nba),'\n')
# print(nba.shape,'\n')
# print(nba.head,'\n')
pd.set_option('display.max.columns',None)
pd.set_option('display.precision',2)
# print(nba.info,'\n')
# print(nba.describe,'\n') 
# print(nba.describe(include=np.object),'\n')

unique_teams = nba['team_id'].unique()
print(len(unique_teams))
unique_franchises = nba['fran_id'].unique()
print(unique_franchises)
games_per_team = nba['fran_id'].value_counts()
print("Games played by each team: \n",games_per_team)
# print(nba['fran_id'].value_counts)

lakers = nba.loc[nba['fran_id']=='Lakers', 'team_id'].value_counts()
print(lakers)
# print(nba.loc[nba['team_id']=='MNL', 'date_game'].agg(('min', 'max')))