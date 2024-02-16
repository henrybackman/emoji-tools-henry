import unittest
import src.core as emoji_tools

class TestEmojiTools(unittest.TestCase):

    def test_strip(self):
        text = '👍🏿test👍🏽👍🏻test👍🏼👍🏾'
        target_result = '👍test👍👍test👍👍'
        self.assertEqual(emoji_tools.strip_emoji_skin_tone(text), target_result, "Should be " + target_result)

    def test_extract_human_emojis(self):
        text = '👍🏿😊test👍test👍🏽🐶test👍🏻'
        target_result = ['👍🏿', '👍', '👍🏽', '👍🏻']
        self.assertEqual(emoji_tools.extract_human_emojis(text), target_result, "Should be " + str(target_result))

    def test_colour_emojis(self):
        input_text = 'test👍test'
        test_cases = [
            (1, 'test👍🏻test'),
            (2, 'test👍🏻test'),
            (3, 'test👍🏼test'),
            (4, 'test👍🏽test'),
            (5, 'test👍🏾test'),
            (6, 'test👍🏿test'),
        ]
        for scale, expected in test_cases:
            with self.subTest(scale=scale):
                self.assertEqual(emoji_tools.colour_emojis(input_text, scale), expected, f"Should be {expected} for scale {scale}")

if __name__ == '__main__':
    unittest.main()