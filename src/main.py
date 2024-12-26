from textnode import TextNode, TextType


def main():
    text_node = TextNode(
        text="This is a text node", text_type=TextType.BOLD, url="https://www.boot.dev"
    )
    print(text_node)


if __name__ == "__main__":
    main()
