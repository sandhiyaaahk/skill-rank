import json
file = open('ex5.json', 'r')
stack = json.load(file)
file.close()  
for donut in stack:
    if donut["name"] == "Old Fashioned":
        donut["batters"]["batter"].append({"id": "5001", "type": "Tea"})
        break

file = open('ex5.json', 'w')
json.dump(stack, file, indent=4)
file.close()  
