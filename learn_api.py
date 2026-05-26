import sys

import requests

# if len(sys.argv) != 2:
#     print("enter the right number of arguments")

resp = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6")

dec = resp.json()

for key, value in dec.items():
    print(f"{key}: {value}")

draw = requests.get("https://deckofcardsapi.com/api/deck/" + dec["deck_id"] + "/draw/?count=4")

print(draw.json())