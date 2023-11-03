esteban_limon = {
    "name": "Esteban Limon",
    "jersey_number": "#77",
    "plays": "Football",
    "class_year": "Senior - 2024",
    "teams": "Del Norte Varsity Football",
    "position": "Noseguard/Offensive Lineman",
    "measurements": {
        "height": "6'1\"",
        "weight": "285 lbs"
    },
    "stats": {
        "solo_tackles": 35,
        "sacks": 3,
        "tackles_per_game": 5.3
    }
}

print("Name: " + esteban_limon["name"])
print("Jersey Number: " + esteban_limon["jersey_number"])
print("Plays: " + esteban_limon["plays"])
print("Class Year: " + esteban_limon["class_year"])
print("Teams: " + esteban_limon["teams"])
print("Position: " + esteban_limon["position"])
print("Measurements:")
print("Height: " + esteban_limon["measurements"]["height"])
print("Weight: " + esteban_limon["measurements"]["weight"])
print("Stats:")
print("Solo Tackles: " + str(esteban_limon["stats"]["solo_tackles"]))
print("Sacks: " + str(esteban_limon["stats"]["sacks"]))
print("Tackles per Game: " + str(esteban_limon["stats"]["tackles_per_game"]))
