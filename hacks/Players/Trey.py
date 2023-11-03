trey_coleman = {
    "name": "Trey Coleman",
    "jersey_number": "#15",
    "plays": "Football",
    "class_year": "Senior - 2024",
    "teams": "Del Norte Varsity Football",
    "position": "Kicker/Punter",
    "measurements": {
        "height": "5'11\"",
        "weight": "175 lbs"
    },
    "stats": {
        "field_goals": 16,
        "yards_kicked_for_punt": 693
    }
}

print("Name: " + trey_coleman["name"])
print("Jersey Number: " + trey_coleman["jersey_number"])
print("Plays: " + trey_coleman["plays"])
print("Class Year: " + trey_coleman["class_year"])
print("Teams: " + trey_coleman["teams"])
print("Position: " + trey_coleman["position"])
print("Measurements:")
print("Height: " + trey_coleman["measurements"]["height"])
print("Weight: " + trey_coleman["measurements"]["weight"])
print("Stats:")
print("Field Goals: " + str(trey_coleman["stats"]["field_goals"]))
print("Yards Kicked for Punt: " + str(trey_coleman["stats"]["yards_kicked_for_punt"]))
