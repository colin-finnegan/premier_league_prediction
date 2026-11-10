"""
Example simulation to get the basics down
Author: Colin Finnegan
Version: 11/9/2026

"""

import numpy as np

rng = np.random.default_rng()
n = 10_000 #number of simulations to run

home_lambda = 1.8 #home xg
away_lambda = 1.1 #away xg

home_goals = rng.poisson(home_lambda, n) #array of n numbers from n simulations
away_goals = rng.poisson(away_lambda, n) #array of n numbers from n simulations

home_win = (home_goals > away_goals).mean() # fraction of simmed matches where home_goals[n] > away_goals[n]
draw = (home_goals == away_goals).mean() # fraction of simmed matches where home_goals[n] == away_goals[n]
away_win = (home_goals < away_goals).mean() # fraction of simmed matches where home_goals[n] < away_goals[n]

print(f"Home wins: {home_win:.1%}, Draw: {draw:.1%}, Away wins: {away_win:.1%}")
print(f"Avg goals: home {home_goals.mean():.2f}, away: {away_goals.mean():.2f}")