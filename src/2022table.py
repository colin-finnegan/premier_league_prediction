import json
import pandas as pd

with open("data/raw/fixtures_39_2022.json", "r") as f:
    data = json.load(f)        

def fetch_games():
    matches = []
    for game in data["response"]:
        goals = game["goals"]
        teams = game["teams"]
        home_goals = goals["home"]
        away_goals = goals["away"]
        home_gd = int(goals["home"]) - int(goals["away"])
        away_gd = int(goals["away"]) - int(goals["home"])
        if home_goals > away_goals:
            home_pts = 3
            away_pts = 0
        elif home_goals < away_goals:
            home_pts = 0
            away_pts = 3
        else:
            home_pts = away_pts = 1
        matches.append({
            "home_team": teams["home"]["name"],
            "away_team": teams["away"]["name"],
            
            "home_goals": home_goals,
            "away_goals": away_goals,

            "home_gd": home_gd,
            "away_gd": away_gd,
                                 
            "home_pts": home_pts,
            "away_pts": away_pts
        })
    
    return pd.DataFrame(matches)

def build_table():
    start = fetch_games()
    home_teams = start[["home_team", "home_goals", "home_gd", "home_pts"]].rename(columns={"home_team": "team", "home_goals": "goals", "home_gd": "gd", "home_pts": "points"})
    away_teams = start[["away_team", "away_goals", "away_gd", "away_pts"]].rename(columns={"away_team": "team", "away_goals": "goals", "away_gd": "gd", "away_pts": "points"})
    combine = pd.concat([home_teams, away_teams])
    table = combine.groupby("team").sum()
    table = table.sort_values(by=["points", "gd", "goals"], ascending=[False, False, False])

    return table

def main():
    print(build_table())

if __name__ == "__main__":
    main()