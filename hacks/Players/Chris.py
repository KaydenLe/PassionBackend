chris_guzman = {
    "name": "Chris Guzman",
    "jersey_number": "#6",
    "plays": "Football",
    "class_year": "Senior - 2024",
    "teams": "Del Norte Varsity Football",
    "position": "Running Back",
    "measurements": {
        "height": "5'7\"",
        "weight": "160 lbs"
    },
    "stats": {
        "yards": 1981,
        "touchdowns": 20,
        "yards_per_game": 55.5
    }
}

print("Name: " + chris_guzman["name"])
print("Jersey Number: " + chris_guzman["jersey_number"])
print("Plays: " + chris_guzman["plays"])
print("Class Year: " + chris_guzman["class_year"])
print("Teams: " + chris_guzman["teams"])
print("Position: " + chris_guzman["position"])
print("Measurements:")
print("Height: " + chris_guzman["measurements"]["height"])
print("Weight: " + chris_guzman["measurements"]["weight"])
print("Stats:")
print("Yards: " + str(chris_guzman["stats"]["yards"]))
print("Touchdowns: " + str(chris_guzman["stats"]["touchdowns"]))
print("Yards per Game: " + str(chris_guzman["stats"]["yards_per_game"]))
