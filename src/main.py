from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode
import re

def main():
    node= TextNode("This is a TextNode","bold","https://www.boot.dev")
    print(node)
    print("---------")
    run_tests()
        
def split_nodes_delimiter(old_nodes,delimiter,text_type):
    vtypes=["text","bold","italic","code","link","image"]
    new_nodes=[]
    for n in old_nodes:
        if not n.text_type=="text": new_nodes.append(n)
           
        elif "**" in n.text:
            l=n.text.split("**")
            if len(l)%2==0: raise Exception("closing delimiter missing")
            new_nodes.append(TextNode(l[0],"text",n.url))
            new_nodes.append(TextNode(l[1],"bold",n.url))
            new_nodes.append(TextNode(l[2],"text",n.url))

        elif "*" in n.text:
            l=n.text.split("*")
            if len(l)%2==0: raise Exception("closing delimiter missing")
            new_nodes.append(TextNode(l[0],"text",n.url))
            new_nodes.append(TextNode(l[1],"italic",n.url))
            new_nodes.append(TextNode(l[2],"text",n.url))

        elif "``" in n.text:
            l=n.text.split("``")
            if len(l)%2==0: raise Exception("closing delimiter missing")
            new_nodes.append(TextNode(l[0],"text",n.url))
            new_nodes.append(TextNode(l[1],"code",n.url))
            new_nodes.append(TextNode(l[2],"text",n.url))


        elif "](" in n.text:
            l=n.text.split("*")
            if len(l)%2==0: raise Exception("closing delimiter missing")
            new_nodes.append(TextNode(l[0],"text",n.url))
            new_nodes.append(TextNode(l[1],"link",n.url))
            new_nodes.append(TextNode(l[2],"text",n.url))
        
    return new_nodes

def run_tests():
    test_cases = [
        ([TextNode("This is **bold** text", "text")], "**", "bold", 
         [TextNode("This is ", "text"), TextNode("bold", "bold"), TextNode(" text", "text")]),

        ([TextNode("This is *italic* text", "text")], "*", "italic", 
         [TextNode("This is ", "text"), TextNode("italic", "italic"), TextNode(" text", "text")]),

        ([TextNode("This is ``code`` text", "text")], "``", "code", 
         [TextNode("This is ", "text"), TextNode("code", "code"), TextNode(" text", "text")]),

    ]

    for i, (input_nodes, delimiter, text_type, expected_output) in enumerate(test_cases):
        try:
            result = split_nodes_delimiter(input_nodes, delimiter, text_type)
            assert result == expected_output, f"Test case {i + 1} failed: {result} != {expected_output}"
            print(f"Test case {i + 1} passed")
        except Exception as e:
            print(f"Test case {i + 1} failed with exception: {e}")

main()