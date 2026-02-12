import unittest
from src.utils import clean_text


class TestCleanText(unittest.TestCase):

    def test_remove_url(self):
        text = "check this https://example.com now"
        cleaned = clean_text(text)
        self.assertNotIn("http", cleaned)

    def test_lowercase(self):
        text = "HELLO WORLD"
        cleaned = clean_text(text)
        self.assertEqual(cleaned, "hello world")

    def test_remove_extra_whitespace(self):
        text = "hello     world   test"
        cleaned = clean_text(text)
        self.assertEqual(cleaned, "hello world test")

    def test_remove_exclamation(self):
        text = "wow!!! amazing!"
        cleaned = clean_text(text, remove_punct=True)
        self.assertNotIn("!", cleaned)

    def test_none_input(self):
        cleaned = clean_text(None)
        self.assertEqual(cleaned, "")


if __name__ == "__main__":
    unittest.main()
