import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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


class TestParentNode(unittest.TestCase):
    def test_parent_with_leafs(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        result = node.to_html()
        self.assertEqual(result, expected)

    def test_headings(self):
        h3node = ParentNode("h3", [LeafNode(None, "This is heading 3")])
        h2node = ParentNode("h2", [LeafNode(None, "This is heading 2"), h3node])
        h1node = ParentNode("h1", [LeafNode(None, "This is heading 1"), h2node])
        expected = "<h1>This is heading 1<h2>This is heading 2<h3>This is heading 3</h3></h2></h1>"
        result = h1node.to_html()
        self.assertEqual(result, expected)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings_again(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


if __name__ == "__main__":
    unittest.main()
