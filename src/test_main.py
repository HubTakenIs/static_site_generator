import unittest
import os
from block_markdown import markdown_to_html_node

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

    def test_reading_file(self):
        base_path = "/home/hub/github/static_site_generator/"
        from_path = os.path.join(base_path,"content/index.md")
        template_path = os.path.join(base_path,"template.html")
        destination = os.path.abspath("public/index.html")
        f = open(from_path)
        markdown = f.read()
        f.close()
        #print(f"markdown:\n {markdown}\n end of markdown \n\n")
        html_node = markdown_to_html_node(markdown)
        #print(f"converted_html_nodes: \n {html_node}\n\n")
        html_content = html_node.to_html()
        #print(f"html_content:\n{html_content}\n\n")


if __name__ == "__main__":
    unittest.main()
