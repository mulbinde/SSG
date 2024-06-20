import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_p2h(self):
        leaf = LeafNode("span", "Hello, world!", {"class": "highlight"})
        parent = ParentNode("div", [leaf], {"id": "container"})
        print(parent.to_html())


if __name__ == "__main__":
    unittest.main()