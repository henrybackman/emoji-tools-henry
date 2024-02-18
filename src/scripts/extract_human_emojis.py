# read the emoji-modifier-sequences.txt file and extract the human emojis
# and write them to a file
import os
import sys
import json

def extract_human_emojis():
    # read the emoji-modifier-sequences.txt file
    # example row: 
    # 261D 1F3FB    ; RGI_Emoji_Modifier_Sequence  ; index pointing up: light skin tone  # E1.0   [1] (☝🏻)
    # at this point only interesting thing really is the utf8 codes of the human emojis
    # leaving the rest of the info for now as is
    file_path = os.path.join(os.path.dirname(__file__), '../static/emoji-modifier-sequences.txt')
    human_emojis = {}
    with open(file_path, 'r') as file:
        content = file.read()
        for row in content.split('\n'):
            # extract the human emojis
            utf8_code_parts, _, info = row.split(';')
            # transform the utf8 code string to proper utf8 characters
            utf8_chars = ''.join([chr(int(part.strip(), 16)) for part in utf8_code_parts.split()])
            # clean the info a bit by removing white space characters
            human_emojis[utf8_chars] = " ".join(info.strip().split())

    # this file contains the skin tone modifiers for the human emojis, but not the base versions
    # add the base versions of the human emojis to the dictionary
    base_emojis = set([emoji[0] for emoji in human_emojis.keys()]) # distinct list of base emojis
    for base_emoji in base_emojis:
        human_emojis[base_emoji] = "Base version of " + base_emoji

    # save the human emojis as a json file
    file_path = os.path.join(os.path.dirname(__file__), '../static/human_emojis.json')
    with open(file_path, 'w') as file:
        json.dump(human_emojis, file, indent=4)

def main():
    extract_human_emojis()

if __name__ == "__main__":
    main()
    sys.exit(0)