from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self,text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self,other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href":text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Unrecognised Text Type")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    out = []

    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            out.append(old_node)
            continue
        nodes = []
        split = old_node.split(delimiter, 2)
        if len(split) == 3:
            nodes.append(
                    TextNode(split[0], TextType.TEXT),
                    TextNode(split[1], text_type),
                    TextNode(split[2], TextType.Text),)
            out.extend(nodes)
        else:
            raise expection("invalid markdown syntax")
    return out
