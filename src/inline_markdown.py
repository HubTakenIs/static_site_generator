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

def split_nodes_image(old_nodes):
    out = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.IMAGE:
            out.append(old_node)
            continue
        if not old_node.text:
            continue
        split_nodes = []
        matches = extract_markdown_links(old_node.text)
        # error handling for matches. as it can be empty
        sections = old_node.text.split(f"![{match[0]}]({match[1]})",1)
        while len(sections) == 3:
            # sec1 is before image, sec2 is image, sec3 is after image
            nodes = [TextNode(section[0],TextType.TEXT),
                     TextNode(section[1], TextType.IMAGE),
                    ]
            split_nodes.extend(nodes)
            sections = section[2].split(f"![{match[0]}]({match[1]})",1)
        split_nodes.append(sections,TextType.TEXT)
        out.extend(split_nodes)



    return out

def split_nodes_link(old_nodes):
    pass

