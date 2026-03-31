import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode()
        self.assertEqual("tag:None value:None children:None props:None",repr(node))
    
    def test_props(self):
        props = { "href": "https://www.google.com",
                 "target": "_blank",}
        node = HTMLNode(props=props)
        self.assertEqual(' href="https://www.google.com" target="_blank"', node.props_to_html())

if __name__ == "__main__":
    unittest.main()
