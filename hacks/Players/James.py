james_armstrong = {
    "name": "James Armstrong",
    "jersey_number": "#53",
    "plays": "Football",
    "class_year": "Senior - 2024",
    "teams": "Del Norte Varsity Football",
    "position": "Defensive Lineman",
    "measurements": {
        "height": "5'7\"",
        "weight": "185 lbs"
    },
    "stats": {
        "plays": 7,
        "pancaked": 3,
        "bench": "135 lbs",
        "squat": "225 lbs"
    }
}

print("Name: " + james_armstrong["name"])
print("Jersey Number: " + james_armstrong["jersey_number"])
print("Plays: " + james_armstrong["plays"])
print("Class Year: " + james_armstrong["class_year"])
print("Teams: " + james_armstrong["teams"])
print("Position: " + james_armstrong["position"])
print("Measurements:")
print("Height: " + james_armstrong["measurements"]["height"])
print("Weight: " + james_armstrong["measurements"]["weight"])
print("Stats:")
print("Plays: " + str(james_armstrong["stats"]["plays"]))
print("Pancaked: " + str(james_armstrong["stats"]["pancaked"]) + " times")
print("Bench: " + james_armstrong["stats"]["bench"])
print("Squat: " + james_armstrong["stats"]["squat"])
