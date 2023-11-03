ryan_remigio = {
    "name": "Ryan Remigio",
    "jersey_number": "#34",
    "plays": "Football",
    "class_year": "Junior - 2025",
    "teams": "Del Norte Varsity Football",
    "position": "Running Back",
    "measurements": {
        "height": "5'7\"",
        "weight": "150 lbs"
    },
    "stats": {
        "yards": 259,
        "yards_per_game": 25.9,
        "touchdowns": 2
    }
}

print("Name: " + ryan_remigio["name"])
print("Jersey Number: " + ryan_remigio["jersey_number"])
print("Plays: " + ryan_remigio["plays"])
print("Class Year: " + ryan_remigio["class_year"])
print("Teams: " + ryan_remigio["teams"])
print("Position: " + ryan_remigio["position"])
print("Measurements:")
print("Height: " + ryan_remigio["measurements"]["height"])
print("Weight: " + ryan_remigio["measurements"]["weight"])
print("Stats:")
print("Yards: " + str(ryan_remigio["stats"]["yards"]))
print("Yards per Game: " + str(ryan_remigio["stats"]["yards_per_game"]))
print("Touchdowns: " + str(ryan_remigio["stats"]["touchdowns"]))
