from enum import Enum
from htmlnode import ParentNode, LeafNode
from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import text_to_textnodes

class BlockType(Enum):
    PARAGRAPH = "paragraph",
    HEADING = "heading",
    CODE = "code",
    QUOTE = "quote",
    UNORDERED_LIST = "unordered_list",
    ORDERED_LIST = "ordered_list"


def markdown_to_html_node(markdown):
    # split code into blocks
    blocks = markdown_to_blocks(markdown)
    out = ParentNode("div",[])
    # loop over blocks
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            count = 0
            for char in block:
                if char == "#":
                    count += 1
            children = text_to_children(block[count+1:])
            parent = ParentNode(f"h{count}",children)
            out.children.append(parent)
            continue

        elif block_type == BlockType.CODE:
            text = block.removeprefix("```").removesuffix("```")
            code = LeafNode("code",text)
            pre = ParentNode("pre",[code])
            out.children.append(pre)
            continue

        elif block_type == BlockType.ORDERED_LIST:
            split = block.split("\n")
            count = 1
            line_items = []
            for line in split:
                if line.startswith(f"{count}. "):
                    text = line.removeprefix(f"{count}. ")
                    line_children = text_to_children(text)
                    line_item = ParentNode("li", children=line_children)
                    line_items.append(line_item)
                    count +=1

            parent = ParentNode("ol",line_items)
            out.children.append(parent)
            continue

        elif block_type == BlockType.UNORDERED_LIST:
            split = block.split("\n")
            line_items = []
            for line in split:
                if line.startswith(f"- "):
                    text = line.removeprefix(f"- ")
                    line_children = text_to_children(text)
                    line_item = ParentNode("li", children=line_children)
                    line_items.append(line_item)

            parent = ParentNode("ul",line_items)
            out.children.append(parent)
            continue

        elif block_type == BlockType.QUOTE:
            text = block.removeprefix("> ")
            children = text_to_children(text)
            parent = ParentNode(f"blockquote", children)
            out.children.append(parent)
            continue

        elif block_type == BlockType.PARAGRAPH:
            children = text_to_textnodes(block)
            parent = ParentNode("p",children)
            out.children.append(parent)
            continue
        else:
            # something went wrong
            pass
    return out

    # determine block type and create a htmlnode to represent it
    # assign proper html node children to block nodes.
    # make sure all block nodes are children of a div and return div.

def text_to_children(text):
    # string of text to list of htmlnodes that represent inline markdown 
    out = []
    text_nodes = text_to_textnodes(text)
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        out.append(html_node)
    return out

def markdown_to_blocks(markdown):
    sections = markdown.split("\n\n")
    out = []
    for section in sections:
        if section == "":
            continue
        section = section.strip()
        out.append(section)
    return out

def block_to_block_type(markdown_block):
    # if heading
    if markdown_block.startswith(("#", "##", "###", "####", "#####", "######")):
        return BlockType.HEADING

    # if code
    if markdown_block.startswith("```\n") and markdown_block.endswith("```"):
        return BlockType.CODE

    split = markdown_block.split("\n")

    #if quote
    if markdown_block.startswith("> "):
        for line in split:
            if not line.startswith("> "):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    # if list
    if markdown_block.startswith("- "):
        for line in split:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    # if list
    counter = 1
    if markdown_block.startswith(f"{counter}. "):
        for line in split:
            if not line.startswith(f"{counter}. "):
                return BlockType.PARAGRAPH
            counter += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
