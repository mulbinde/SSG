from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

def main():
    node= TextNode("This is a TextNode","bold","https://www.boot.dev")
    print(node)

def t2h(text_node):
    match text_node.text_type:
        case "text":
            return LeafNode("pre",text_node.text,{})
        case "bold":
            return LeafNode("b",text_node.text,{})
        case "italic":
            return LeafNode("i",text_node.text,{})
        case "code":
            return LeafNode("code",text_node.text,{})
        case "link":
            return LeafNode("a",text_node.text,{'href': text_node.url})
        case "image":
            return LeafNode("img","",{'src': text_node.url, 'alt': text_node.text})
    raise Exception("text type not recognized")
        
        


print("hello world")

main()