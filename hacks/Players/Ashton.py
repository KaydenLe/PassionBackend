ashton_tomlinson = {
    "name": "Ashton Tomlinson",
    "jersey_number": "#1",
    "plays": "Football",
    "class_year": "Senior - 2024",
    "teams": "Del Norte Varsity Football",
    "position": "Wide Receiver",
    "measurements": {
        "height": "5'11\"",
        "weight": "160 lbs"
    },
    "stats": {
        "yards": 570,
        "yard_average": 16.3,
        "touchdowns": 1
    }
}

print("Name: " + ashton_tomlinson["name"])
print("Jersey Number: " + ashton_tomlinson["jersey_number"])
print("Plays: " + ashton_tomlinson["plays"])
print("Class Year: " + ashton_tomlinson["class_year"])
print("Teams: " + ashton_tomlinson["teams"])
print("Position: " + ashton_tomlinson["position"])
print("Measurements:")
print("Height: " + ashton_tomlinson["measurements"]["height"])
print("Weight: " + ashton_tomlinson["measurements"]["weight"])
print("Stats:")
print("Yards: " + str(ashton_tomlinson["stats"]["yards"]))
print("Yard Average: " + str(ashton_tomlinson["stats"]["yard_average"]))
print("Touchdowns: " + str(ashton_tomlinson["stats"]["touchdowns"]))
