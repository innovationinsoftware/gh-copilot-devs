# python -m unittest test_text_utils.py

import unittest
from text_utils import count_words

class TestTextUtils(unittest.TestCase):
    def test_simple_sentence(self):
        self.assertEqual(count_words("Hello world"), 2)

    def test_newlines(self):
        # Should count 3 words, but buggy code returns 1
        self.assertEqual(count_words("Hello\nworld\nagain"), 3)

    def test_tabs_and_spaces(self):
        # Tabs should be treated like spaces
        self.assertEqual(count_words("One\tTwo Three"), 3)

if __name__ == "__main__":
    unittest.main()
