import unittest

from main import extract_title

class TestMain(unittest.TestCase):
    def test_single_line(self):
        markdown = "# hello world"
        expected = "hello world"
        actual = extract_title(markdown)
        self.assertEqual(expected, actual)

    def test_multi_line(self):
        markdown = "# this is how I met your mother\n\n sikes. I didn't'"
        expected = "this is how I met your mother"
        actual = extract_title(markdown)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
