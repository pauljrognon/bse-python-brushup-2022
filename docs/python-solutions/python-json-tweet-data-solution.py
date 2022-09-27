import json

def load_tweets(filepath):
    with open(filepath) as f:
        lines = f.readlines()
    return [json.loads(line) for line in lines]