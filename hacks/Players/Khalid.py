khalid_farah = {
    "name": "Khalid Farah",
    "jersey_number": "#4",
    "plays": "Football",
    "class_year": "Senior - 2024",
    "teams": "Del Norte Varsity Football",
    "position": "Outside Linebacker",
    "measurements": {
        "height": "6'2\"",
        "weight": "195 lbs"
    },
    "stats": {
        "solo_tackles": 108,
        "sacks": 3,
        "tackles_per_game": 8.6
    }
}

print("Name: " + khalid_farah["name"])
print("Jersey Number: " + khalid_farah["jersey_number"])
print("Plays: " + khalid_farah["plays"])
print("Class Year: " + khalid_farah["class_year"])
print("Teams: " + khalid_farah["teams"])
print("Position: " + khalid_farah["position"])
print("Measurements:")
print("Height: " + khalid_farah["measurements"]["height"])
print("Weight: " + khalid_farah["measurements"]["weight"])
print("Stats:")
print("Solo Tackles: " + str(khalid_farah["stats"]["solo_tackles"]))
print("Sacks: " + str(khalid_farah["stats"]["sacks"]))
print("Tackles per Game: " + str(khalid_farah["stats"]["tackles_per_game"]))
