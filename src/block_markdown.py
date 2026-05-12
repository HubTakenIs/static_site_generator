from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph",
    HEADING = "heading",
    CODE = "code",
    QUOTE = "quote",
    UNORDERED_LIST = "unordered_list",
    ORDERED_LIST = "ordered_list"


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
