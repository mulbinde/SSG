class HTMLNode():
    def __init__(self, tag, value="", children=None, props=None):
        self.tag = tag if tag else "pre"
        self.value = value if value else ""
        self.children = children if children else []
        self.props = props if props else {}

    def to_html(self):
        raise NotImplementedError("implemented by subclass or else!")

    def props_to_html(self):
        s=''
        for k,v in self.props.items():
            s+=f' {k}="{v}"'
        return s

    def __repr__(self):
        return f'HTMLNode({self.tag}, "{self.value}", {self.children}, {self.props})'
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, [], props)

    def to_html(self):
        if self.value is None: raise ValueError("leaf must have value")
        p=self.props_to_html()
        t=self.tag
        return f"<{t}{p}>{self.value}</{t}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, "", children, props)

    def to_html(self):
        if self.tag is None: raise ValueError("tagless parent")
        if not self.children: raise ValueError("childless parent")

        p=self.props_to_html()
        c= ''.join(child.to_html() for child in self.children)
        return f"<{self.tag}{p}>{c}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"