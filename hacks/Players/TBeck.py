tyler_becker = {
    "name": "Tyler Becker",
    "jersey_number": "#11",
    "plays": "Football",
    "class_year": "Senior - 2024",
    "teams": "Del Norte Varsity Football",
    "position": "Wide Receiver",
    "measurements": {
        "height": "6'2\"",
        "weight": "180 lbs"
    },
    "stats": {
        "yards": 415,
        "touchdowns": 4,
        "yards_per_game": 21.8
    }
}

print("Name: " + tyler_becker["name"])
print("Jersey Number: " + tyler_becker["jersey_number"])
print("Plays: " + tyler_becker["plays"])
print("Class Year: " + tyler_becker["class_year"])
print("Teams: " + tyler_becker["teams"])
print("Position: " + tyler_becker["position"])
print("Measurements:")
print("Height: " + tyler_becker["measurements"]["height"])
print("Weight: " + tyler_becker["measurements"]["weight"])
print("Stats:")
print("Yards: " + str(tyler_becker["stats"]["yards"]))
print("Touchdowns: " + str(tyler_becker["stats"]["touchdowns"]))
print("Yards per Game: " + str(tyler_becker["stats"]["yards_per_game"]))
