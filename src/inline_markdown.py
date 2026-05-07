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
        if old_node.text_type != TextType.TEXT:
            out.append(old_node)
            continue
        # can fail
        extracts = extract_markdown_images(old_node.text)
        if not extracts:
            out.append(old_node)
            continue
        text_to_split = old_node.text
        for image in extracts:
            split = text_to_split.split(f"![{image[0]}]({image[1]})", 1)
            if split[0]:
                out.append(TextNode(split[0],TextType.TEXT))
            out.append(TextNode(image[0],TextType.IMAGE, image[1]))
            text_to_split = split[1]
        if text_to_split:
            out.append(TextNode(text_to_split, TextType.TEXT))

    return out

def split_nodes_link(old_nodes): 
    out = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            out.append(old_node)
            continue
        # can fail.
        extracts = extract_markdown_links(old_node.text)
        if not extracts:
            out.append(old_node)
            continue
        text_to_split = old_node.text
        for link in extracts:
            split = text_to_split.split(f"[{link[0]}]({link[1]})", 1)
            if split[0]:
                out.append(TextNode(split[0],TextType.TEXT))
            out.append(TextNode(link[0],TextType.LINK, link[1]))
            text_to_split = split[1]
        if text_to_split:
            out.append(TextNode(text_to_split, TextType.TEXT))

    return out

def text_to_textnodes(text):
    node = TextNode(text,TextType.TEXT)
    output = split_nodes_delimiter([node] , "**", TextType.BOLD)
    output = split_nodes_delimiter(output, "_",TextType.ITALIC)
    output = split_nodes_delimiter(output, "`", TextType.CODE)
    output = split_nodes_image(output)
    output = split_nodes_link(output)
    return output
