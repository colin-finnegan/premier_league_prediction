"""
Functions for reading/fetching the data
Author: Colin Finnegan
Version: 11/10/2026

"""
import os
import requests
import json
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
api_key = os.getenv("API_KEY")

LEAGUE_ID = 39 #Premier League
SEASON = 2022
url = "https://v3.football.api-sports.io/fixtures"
headers = {'x-apisports-key': api_key}
params = {"league": LEAGUE_ID, "season": SEASON}

r = requests.get(url, headers=headers, params=params)
data = r.json()

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"

RAW_DIR.mkdir(parents=True, exist_ok=True) # makes the folder if its missing

if not data.get("errors"):
    with open(RAW_DIR / f"fixtures_{LEAGUE_ID}_{SEASON}.json", "w") as f:
        json.dump(data, f, indent=2)
        print("Saved", data["results"], "fixtures")
else:
    print("API ERRORS", data["errors"])