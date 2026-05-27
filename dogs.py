import json
import requests
import sys

if len(sys.argv) != 2:
    print("enter the right number of arguments")

response = requests.get("https://openwhyd.org/adrien/playlist/10?format=json&limit=" + sys.argv[1])
print(json.dumps(response.json(), indent=3))

for name in response.json():     
    print(name["name"])