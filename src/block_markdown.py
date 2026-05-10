def markdown_to_blocks(markdown):
    sections = markdown.split("\n\n")
    out = []
    for section in sections:
        if section == "":
            continue
        section = section.strip()
        out.append(section)
    return out
