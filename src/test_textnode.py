import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_eq_full(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        self.assertEqual(node1, node2)

    def test_eq_one_missing_url(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        self.assertNotEqual(node1, node2)

    def test_default_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNone(node.url)

    def test_eq_different_text(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_eq_different_text_type(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_eq_different_url(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "http://example.com")
        self.assertNotEqual(node1, node2)

    def test_eq_different_text_type_url(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        node2 = TextNode("This is a text node", TextType.CODE, "http://example.com")
        self.assertNotEqual(node1, node2)

    def test_eq_different_text_text_type(self):
        node1 = TextNode("This is text node", TextType.BOLD, "https://example.com")
        node2 = TextNode("This is a text node", TextType.CODE, "https://example.com")
        self.assertNotEqual(node1, node2)

    def test_eq_different_text_text_type_url(self):
        node1 = TextNode("This is text node", TextType.BOLD, "https://example.com")
        node2 = TextNode("This is a text node", TextType.CODE, "http://example.com")
        self.assertNotEqual(node1, node2)

    def test_wrong_text_type(self):
        TextNode("This is a text node", "BOLD")
        self.assertRaises(TypeError)

    def test_undefined_text_type(self):
        with self.assertRaises(AttributeError):
            TextNode("This is a text node", TextType.BOLD_ITALIC)


if __name__ == "__main__":
    unittest.main()
