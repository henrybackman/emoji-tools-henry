# read human_emojis.json as python dictionary
import os
import sys
import json

def read_human_emojis():
    file_path = os.path.join(os.path.dirname(__file__), '../static/human_emojis.json')
    with open(file_path, 'r') as file:
        human_emojis = json.load(file)
        
    for k, v in human_emojis.items():
        print(f"{k}: {v}")
        print(len(k))
        break

    assert '👍🏿' in human_emojis


def main():
    read_human_emojis()

if __name__ == "__main__":
    main()
    sys.exit(0)