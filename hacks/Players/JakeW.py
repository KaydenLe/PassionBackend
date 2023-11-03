jake_warren = {
    "name": "Jake Warren",
    "jersey_number": "#8",
    "plays": "Football",
    "class_year": "Senior - 2024",
    "teams": "Del Norte Varsity Football",
    "position": "Strong Safety",
    "measurements": {
        "height": "5'11\"",
        "weight": "155 lbs"
    },
    "stats": {
        "solo_tackles": 50,
        "interceptions": 1,
        "tackles_per_game": 3.4
    }
}

print("Name: " + jake_warren["name"])
print("Jersey Number: " + jake_warren["jersey_number"])
print("Plays: " + jake_warren["plays"])
print("Class Year: " + jake_warren["class_year"])
print("Teams: " + jake_warren["teams"])
print("Position: " + jake_warren["position"])
print("Measurements:")
print("Height: " + jake_warren["measurements"]["height"])
print("Weight: " + jake_warren["measurements"]["weight"])
print("Stats:")
print("Solo Tackles: " + str(jake_warren["stats"]["solo_tackles"]))
print("Interceptions: " + str(jake_warren["stats"]["interceptions"]))
print("Tackles per Game: " + str(jake_warren["stats"]["tackles_per_game"]))
