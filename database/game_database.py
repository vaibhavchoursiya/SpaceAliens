from pathlib import Path

import json

path = Path("database/game_db.json")

# Read Data from json
def read_data():
    """Read Data from json file."""
    # Read
    # Json single string
    contents = path.read_text()

    # Json object to python object
    highscore = json.loads(contents)
    return str(highscore)

# Write Data in json file
def write_data(data):
    """Write Data on json file."""    
    # it will create file if it not exits and if exitst it will
    # override that file
    w = json.dumps(data)
    path.write_text(w)