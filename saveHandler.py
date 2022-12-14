import json
import os


def load() -> dict:
    if 'save.json' in os.listdir():
        with open('save.json', 'r') as f:
            return json.load(f)
    else:
        return {}


def save(data):
    if 'save.json' in os.listdir():
        with open('save.json', 'w') as f:
            json.dump(data, f)
    else:
        with open('save.json', 'w') as f:
            json.dump(data, f)
