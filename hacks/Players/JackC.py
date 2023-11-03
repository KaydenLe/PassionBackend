jack_christensen = {
    "name": "Jack Christensen",
    "jersey_number": "#9",
    "plays": "Football",
    "class_year": "Senior - 2024",
    "teams": "Del Norte Varsity Football",
    "position": "Corner Back",
    "measurements": {
        "height": "5'10\"",
        "weight": "175 lbs"
    },
    "stats": {
        "solo_tackles": 32,
        "interceptions": 1,
        "tackles_per_game": 2.7
    }
}

print("Name: " + jack_christensen["name"])
print("Jersey Number: " + jack_christensen["jersey_number"])
print("Plays: " + jack_christensen["plays"])
print("Class Year: " + jack_christensen["class_year"])
print("Teams: " + jack_christensen["teams"])
print("Position: " + jack_christensen["position"])
print("Measurements:")
print("Height: " + jack_christensen["measurements"]["height"])
print("Weight: " + jack_christensen["measurements"]["weight"])
print("Stats:")
print("Solo Tackles: " + str(jack_christensen["stats"]["solo_tackles"]))
print("Interceptions: " + str(jack_christensen["stats"]["interceptions"]))
print("Tackles per Game: " + str(jack_christensen["stats"]["tackles_per_game"]))
