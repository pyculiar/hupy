import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_default_children_props_none(self):
        node = HTMLNode("p", "This is some text")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_props(self):
        props = {
            "href": "https://example.com",
            "target": "_blank",
        }
        node = HTMLNode("a", "This is a link", None, props)
        expected_attrs = ' href="https://example.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_attrs)

    def test_child_props(self):
        props = {
            "href": "https://example.com",
            "target": "_blank",
        }
        cnode = HTMLNode("a", "This is a link", None, props)
        node = HTMLNode("p", "This is some text.", [cnode])
        expected_attrs = ' href="https://example.com" target="_blank"'
        self.assertIsNone(node.props)
        self.assertEqual(node.children[0].props_to_html(), expected_attrs)
        self.assertIsNone(node.children[0].children)


class TestLeafNode(unittest.TestCase):
    def test_only_value(self):
        node = LeafNode(tag=None, value="This is raw text")
        expected = "This is raw text"
        self.assertEqual(node.to_html(), expected)
    def test_tag_with_props(self):
        props = {
            "href": "https://example.com",
            "target": "_blank",
        }
        node = LeafNode("a", "This is a link", props)
        expected = '<a href="https://example.com" target="_blank">This is a link</a>'
        self.assertEqual(node.to_html(), expected)
    def test_tag_without_props(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), expected)
    def test_value_none(self):
        node = LeafNode(tag="p", value=None)
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
