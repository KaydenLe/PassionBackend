ty_olsen = {
    "name": "Ty Olsen",
    "jersey_number": "#5",
    "plays": "Football",
    "class_year": "Junior - 2025",
    "teams": "Del Norte Varsity Football",
    "position": "Wide Receiver",
    "measurements": {
        "height": "6'2\"",
        "weight": "190 lbs"
    },
    "stats": {
        "yards": 2957,
        "touchdowns": 38,
        "yards_per_game": 87.0
    }
}

print("Name: " + ty_olsen["name"])
print("Jersey Number: " + ty_olsen["jersey_number"])
print("Plays: " + ty_olsen["plays"])
print("Class Year: " + ty_olsen["class_year"])
print("Teams: " + ty_olsen["teams"])
print("Position: " + ty_olsen["position"])
print("Measurements:")
print("Height: " + ty_olsen["measurements"]["height"])
print("Weight: " + ty_olsen["measurements"]["weight"])
print("Stats:")
print("Yards: " + str(ty_olsen["stats"]["yards"]))
print("Touchdowns: " + str(ty_olsen["stats"]["touchdowns"]))
print("Yards per Game: " + str(ty_olsen["stats"]["yards_per_game"]))
