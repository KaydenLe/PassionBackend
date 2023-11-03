
football_player = {
    "plays": "Football",
    "class_year": "Senior - 2024",
    "teams": "Del Norte Varsity Football",
    "position": "Quarterback",
    "measurements": {
        "height": "6'0\"",
        "weight": "170 lbs"
    },
    "stats": {
        "yards": 6687,
        "touchdown_passes": 76,
        "yards_per_game": 196.7
    }
}
print("Plays: " + football_player["plays"])
print("Class Year: " + football_player["class_year"])
print("Teams: " + football_player["teams"])
print("Position: " + football_player["position"])
print("Measurements:")
print("Height: " + football_player["measurements"]["height"])
print("Weight: " + football_player["measurements"]["weight"])
print("Stats:")
print("Yards: " + str(football_player["stats"]["yards"]))
print("Touchdown Passes: " + str(football_player["stats"]["touchdown_passes"]))
print("Yards per Game: " + str(football_player["stats"]["yards_per_game"]))
