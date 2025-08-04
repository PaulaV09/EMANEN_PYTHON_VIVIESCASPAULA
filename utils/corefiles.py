import json
from typing import Dict

def readJson(fileName: str)->Dict:
    try:
        with open(fileName, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def writeJson(fileName: str,  data : Dict)->Dict:
    with open(fileName, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)