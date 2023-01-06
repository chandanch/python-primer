import json
from pathlib import Path

players = [
    {
        "name": "Chandio",
        "score": 12223
    },
    {
        "name": "Sam",
        "score": 112
    }
]

# serialize array of dictionaries to json str
json_data = json.dumps(players)
# write data to a JSON file
# Path("players.json").write_text(json_data)

# read data from a JSON file
data = Path("players.json").read_text()
# de-serialize the data using json.loads()
print(json.loads(data))
