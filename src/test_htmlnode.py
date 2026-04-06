import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_leaf_to_html_p(self):
        node = LeafNode("p","Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None,"Hello, world!")
        self.assertEqual(node.to_html(),"Hello, world!")

    def test_parent_to_hmtl_leafs(self):
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
        
if __name__ == "__main__":
    unittest.main()
