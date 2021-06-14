import sys
sys.path.append('/Users/stanleyhoucke/coding_projects/euros_predictor/app/')

import os
from dotenv import load_dotenv
import json
import requests
import repositories.match_repository as match_repository
import repositories.team_repository as team_repository
import repositories.group_repository as group_repository

def fetch_results():
    load_dotenv()

    url = "https://v3.football.api-sports.io/fixtures?league=4&season=2020"
    api_key = os.environ.get('FOOTBALL_API_KEY')

    payload={}
    headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': 'v3.football.api-sports.io'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = json.loads(response.text)
    # print(data["response"][0]["goals"]["home"])

    all_matches = match_repository.select_all()

    for match in all_matches:
        for item in data["response"]:
            if item["teams"]["home"]["name"] == "FYR Macedonia":
                item["teams"]["home"]["name"] = "North Macedonia"
            elif item["teams"]["away"]["name"] == "FYR Macedonia":
                item["teams"]["away"]["name"] = "North Macedonia"

            if item["teams"]["home"]["name"] == match.team_1.name and item["teams"]["away"]["name"] == match.team_2.name:
                match.goals["home"] = item["goals"]["home"]
                match.goals["away"] = item["goals"]["away"]
                match_repository.update(match)


# fetch_results()
