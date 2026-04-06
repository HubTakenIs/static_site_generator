class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        out = ""
        if not self.props:
            return out
        for key in self.props.keys():
            out += f' {key}="{self.props[key]}"'
        return out
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children:{self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self,tag, value, props=None):
        super().__init__(value=value, tag=tag,props=props)

    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if not self.tag:
            raise ValueError
        if not self.children:
            raise ValueError
        # recursive method 
        out = f"<{self.tag}>"
        for child in self.children:
            if type(child) == LeafNode:
                out += child.to_html()
            if type(child) == ParentNode:
                out += child.to_html()
        out += f"</{self.tag}>"
        return out
        

