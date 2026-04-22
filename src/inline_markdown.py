import re

from textnode import (
        TextType,
        TextNode,
        )

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    out = []

    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            out.append(old_node)
            continue
        split_nodes = []
        split = old_node.text.split(delimiter)
        if len(split) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(split)):
            if split[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(split[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(split[i], text_type))
        out.extend(split_nodes)
    return out

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

