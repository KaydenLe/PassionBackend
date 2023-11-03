charlie_bowers = {
    "name": "Charlie Bowers",
    "jersey_number": "#20",
    "plays": "Football",
    "class_year": "Junior - 2025",
    "teams": "Del Norte Varsity Football",
    "position": "Corner Back",
    "measurements": {
        "height": "6'00\"",
        "weight": "170 lbs"
    },
    "stats": {
        "solo_tackles": 36,
        "interceptions": 1,
        "tackles_per_game": 2.5
    }
}

print("Name: " + charlie_bowers["name"])
print("Jersey Number: " + charlie_bowers["jersey_number"])
print("Plays: " + charlie_bowers["plays"])
print("Class Year: " + charlie_bowers["class_year"])
print("Teams: " + charlie_bowers["teams"])
print("Position: " + charlie_bowers["position"])
print("Measurements:")
print("Height: " + charlie_bowers["measurements"]["height"])
print("Weight: " + charlie_bowers["measurements"]["weight"])
print("Stats:")
print("Solo Tackles: " + str(charlie_bowers["stats"]["solo_tackles"]))
print("Interceptions: " + str(charlie_bowers["stats"]["interceptions"]))
print("Tackles per Game: " + str(charlie_bowers["stats"]["tackles_per_game"]))
