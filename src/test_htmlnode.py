import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode()
        self.assertEqual("HTMLNode(None, None, children:None, None)",repr(node))
    
    def test_props(self):
        props = { "href": "https://www.google.com",
                 "target": "_blank",}
        node = HTMLNode(props=props)
        self.assertEqual(' href="https://www.google.com" target="_blank"', node.props_to_html())

    def test_values(self):
        node = HTMLNode(
                "div",
                "I wish I could read",
                )
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "I wish I could read")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)


if __name__ == "__main__":
    unittest.main()
