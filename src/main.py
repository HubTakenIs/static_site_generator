from textnode import TextNode, TextType
def main():
    testnode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(testnode)


main()
