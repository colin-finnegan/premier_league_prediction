import json
import pandas as pd

with open("data/raw/fixtures_39_2022.json", "r") as f:
    data = json.load(f)        

def fetch_games():
    matches = []
    for game in data["response"]:
        goals = game["goals"]
        teams = game["teams"]
        home_gf = goals["home"]
        away_gf = goals["away"]
        home_gd = goals["home"] - goals["away"]
        away_gd = goals["away"] - goals["home"]
        home_ga = home_gf - home_gd
        away_ga = away_gf - away_gd
        home_win = 0
        home_tie = 0
        home_loss = 0
        away_win = 0
        away_tie = 0
        away_loss = 0
        if home_gf > away_gf:
            home_pts = 3
            home_win += 1
            away_pts = 0
            away_loss += 1
        elif home_gf < away_gf:
            home_pts = 0
            home_loss += 1
            away_pts = 3
            away_win += 1
        else:
            home_pts = away_pts = 1
            home_tie += 1
            away_tie += 1
        matches.append({
            "home_team": teams["home"]["name"],
            "away_team": teams["away"]["name"],
            
            "home_gf": home_gf,
            "away_gf": away_gf,

            "home_ga": home_ga,
            "away_ga": away_ga,

            "home_gd": home_gd,
            "away_gd": away_gd,
                                 
            "home_pts": home_pts,
            "away_pts": away_pts,

            "home_win": home_win,
            "home_tie": home_tie,
            "home_loss": home_loss,

            "away_win": away_win,
            "away_tie": away_tie,
            "away_loss": away_loss
        })
    
    return pd.DataFrame(matches)

def build_table():
    start = fetch_games()
    home_teams = (
        start[["home_team", "home_win", "home_tie", "home_loss", "home_gf", "home_ga", "home_gd","home_pts"]]
        .rename(
            columns={
                "home_team": "Team", 
                "home_win": "W",
                "home_tie": "D",
                "home_loss": "L",
                "home_gf": "GF", 
                "home_ga": "GA", 
                "home_gd": "GD",                 
                "home_pts": "Pts"
            }
        )
    )
    away_teams = (
        start[["away_team", "away_win", "away_tie", "away_loss", "away_gf", "away_ga", "away_gd", "away_pts"]]
        .rename(
            columns={
                "away_team": "Team", 
                "away_win": "W",
                "away_tie": "D",
                "away_loss": "L",
                "away_gf": "GF", 
                "away_ga": "GA", 
                "away_gd": "GD", 
                "away_pts": "Pts"
            }
        )
    )
    combine = pd.concat([home_teams, away_teams])
    table = combine.groupby("Team").sum()
    table = table.sort_values(by=["Pts", "GD", "GF"], ascending=[False, False, False])

    return table

def main():
    print(build_table())

if __name__ == "__main__":
    main()