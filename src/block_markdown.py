from enum import Enum
from htmlnode import ParentNode
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
            h_count = 0
            for char in block:
                if char != "#":
                    break
                h_count +=1
            
            # I need to extract title
            text_node = TextNode(block[h_count+1:],TextType.TEXT )
            print(f"heading count {h_count}, text = {block[h_count+1:]}")
            print(text_node)
            node = ParentNode(f"h{h_count}",[text_node_to_html_node(text_node)])
            out.children.append(node)

        if block_type == BlockType.PARAGRAPH:
            text_nodes = text_to_textnodes(block)
            child_nodes = []
            for text_node in text_nodes:
                child_nodes.append(text_node_to_html_node(text_node))
            node = ParentNode("p",child_nodes)
            out.children.append(node)
        if block_type == BlockType.CODE:
            pass
        if block_type == BlockType.Quote:
            pass
        if block_type == BlockType.UNORDERED_LIST:
            pass
        if block_type == BlockType.ORDERED_LIST:
            pass

        
    return out

    # determine block type and create a htmlnode to represent it
    # assign proper html node children to block nodes.
    # make sure all block nodes are children of a div and return div.

def text_to_children(text):
    # string of text to list of htmlnodes that represent inline markdown 
    pass

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
