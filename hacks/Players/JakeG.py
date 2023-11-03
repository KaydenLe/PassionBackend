jake_gregory = {
    "name": "Jake Gregory",
    "jersey_number": "#12",
    "plays": "Football",
    "class_year": "Senior - 2024",
    "teams": "Del Norte Varsity Football",
    "position": "Linebacker/Safety",
    "measurements": {
        "height": "5'10\"",
        "weight": "175 lbs"
    },
    "stats": {
        "solo_tackles": 52,
        "interceptions": 2,
        "tackles_per_game": 3.9
    }
}

print("Name: " + jake_gregory["name"])
print("Jersey Number: " + jake_gregory["jersey_number"])
print("Plays: " + jake_gregory["plays"])
print("Class Year: " + jake_gregory["class_year"])
print("Teams: " + jake_gregory["teams"])
print("Position: " + jake_gregory["position"])
print("Measurements:")
print("Height: " + jake_gregory["measurements"]["height"])
print("Weight: " + jake_gregory["measurements"]["weight"])
print("Stats:")
print("Solo Tackles: " + str(jake_gregory["stats"]["solo_tackles"]))
print("Interceptions: " + str(jake_gregory["stats"]["interceptions"]))
print("Tackles per Game: " + str(jake_gregory["stats"]["tackles_per_game"]))
