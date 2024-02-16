import re
import emoji

def get_default_emoji(e: str) -> str:
    """
    Get the base emoji without skin-tone modifiers
    """
    assert e in emoji.EMOJI_DATA # assert that it is a valid emoji
    return e[0]

def strip_emoji_skin_tone(text: str) -> str:
    """
    Strip emoji skin-tone modifiers from input text
    """
    emojis_in_text = emoji.analyze(text)
    output_text = text
    for e in emojis_in_text:
        default_emoji = get_default_emoji(e.chars)
        output_text = output_text.replace(e.chars, default_emoji)
    return output_text

def extract_human_emojis(text: str) -> list:
    """
    Extract human emojis from input text
    """
    # to identify human emojis, we can check if it has skin tone modifier
    # this however doesn't capture the unmodified human emojis
    # TODO best way would be to define the list of human emojis and check against that, don't have time to build
    # such a list now
    emojis_in_text = emoji.analyze(text)
    human_emojis = []
    for e in emojis_in_text:
        if len(e.chars) > 1:
            human_emojis.append(e.value.emoji)
    return human_emojis

FITZPATRICK_SCALES = {
    1: u"\U0001F3FB", # light skin tone
    2: u"\U0001F3FB", # light skin tone
    3: u"\U0001F3FC", # medium-light skin tone
    4: u"\U0001F3FD", # medium skin tone
    5: u"\U0001F3FE", # medium-dark skin tone
    6: u"\U0001F3FF", # dark skin tone
}

def colour_emojis(text: str, fitzpatrick_scale: int) -> str:
    """
    Colour emojis in text using the specified Fitzpatrick scale
    """
    assert fitzpatrick_scale in FITZPATRICK_SCALES
    emojis_in_text = emoji.analyze(text)
    output_text = text
    for e in emojis_in_text:
        default_emoji = get_default_emoji(e.chars)
        output_text = output_text.replace(e.chars, default_emoji + FITZPATRICK_SCALES[fitzpatrick_scale])
    return output_text


if __name__ == "__main__":
    print(strip_emoji_skin_tone("👍🏿test👍🏽👍🏻test👍🏼👍🏾")) # prints 👍👍👍👍👍

    print(extract_human_emojis("👍🏿👍🏽👍🏻👍🏼👍🏾👍")) # prints ['👍🏿', '👍🏽', '👍🏻', '👍🏼', '👍🏾']

    # test with mix of emojis
    print(extract_human_emojis("👍🏿👍😈"))

    # colour emojis
    print(colour_emojis("👍", 1))
    print(colour_emojis("👍", 2))
    print(colour_emojis("👍", 3))
    print(colour_emojis("👍", 4))
    print(colour_emojis("👍", 5))
    print(colour_emojis("👍", 6))