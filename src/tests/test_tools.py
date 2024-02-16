import unittest
import emoji_tools_henry as emoji_tools

class TestEmojiTools(unittest.TestCase):

    def test_strip(self):
        text = '👍🏿test👍🏽👍🏻test👍🏼👍🏾'
        target_result = '👍test👍👍test👍👍'
        self.assertEqual(emoji_tools.strip_emoji_skin_tone(text), target_result, "Should be " + target_result)

if __name__ == '__main__':
    unittest.main()