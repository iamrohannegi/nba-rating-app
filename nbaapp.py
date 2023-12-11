import requests, pprint

# teams = [
#     'Boston Celtics': 'Bos',
#     'Los Angeles'
# ]

data = requests.get('http://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams', 
                    headers={'User-agent': 'learning python'})

data.raise_for_status()


pprint.pprint(data.json()['sports'][0]['leagues'][0]['teams'][0]['team'])