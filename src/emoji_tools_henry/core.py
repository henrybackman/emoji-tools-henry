import os
import json

# read the human_emojis.json file and store it into a dictionary
HUMAN_EMOJIS = {}
file_path = os.path.join(os.path.dirname(__file__), '../static/human_emojis.json')
with open(file_path, 'r') as file:
    HUMAN_EMOJIS = json.load(file)


FITZPATRICK_SCALES = {
    1: u"\U0001F3FB", # light skin tone
    2: u"\U0001F3FB", # light skin tone
    3: u"\U0001F3FC", # medium-light skin tone
    4: u"\U0001F3FD", # medium skin tone
    5: u"\U0001F3FE", # medium-dark skin tone
    6: u"\U0001F3FF", # dark skin tone
}

def strip_emoji_skin_tone(text: str) -> str:
    """
    Strip emoji skin-tone modifiers from input text
    """
    output_text = ""
    for char in text:
        if char in FITZPATRICK_SCALES.values(): # remove the skin tone modifiers
            continue
        output_text += char # build output character by character
    return output_text


def extract_human_emojis(text: str) -> list:
    """
    Extract human emojis from input text
    """
    # to identify human emojis, check if the emoji is in the HUMAN_EMOJIS dictionary
    # first, need to collect the characters properly from the text, by combining the utf8 codes
    # with the skin tone modifiers
    # for example 👍🏿 is combination of \udc4d and \udfff
    human_emojis = []
    prev_char = None
    for char in list(text) + [None]: # add None to the end to make sure the last character is processed
        if not prev_char:
            prev_char = char
            continue
        if prev_char + str(char) in HUMAN_EMOJIS: # skin toned emoji is found
            human_emojis.append(prev_char + char)
            prev_char = None
            continue
        if prev_char in HUMAN_EMOJIS: # base emoji is found
            human_emojis.append(prev_char)
        prev_char = char

    return human_emojis


def colour_emojis(text: str, fitzpatrick_scale: int) -> str:
    """
    Colour emojis in text using the specified Fitzpatrick scale
    """
    assert fitzpatrick_scale in FITZPATRICK_SCALES

    output_text = ""
    # build output character by character
    for char in text:
        if char in FITZPATRICK_SCALES.values(): # remove the existing skin tone modifiers
            continue
        if char in HUMAN_EMOJIS: # add the skin tone modifier
            output_text += char + FITZPATRICK_SCALES[fitzpatrick_scale]
            continue
        output_text += char # add the rest of the characters as is

    return output_text
