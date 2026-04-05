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
        out = f"<{self.tag}"
        if not self.props:
            out += f">{self.value}</{self.tag}>"
        else:
            # finish this?
            out1 = ""
            for prop in self.props:
                out1 += f' {prop}="{self.props[prop]}"'
            out += f"{out1}>{self.value}</{self.tag}>"

        return out
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"
