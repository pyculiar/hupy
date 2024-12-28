import unittest

from htmlnode import HTMLNode


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



if __name__ == "__main__":
    unittest.main()
