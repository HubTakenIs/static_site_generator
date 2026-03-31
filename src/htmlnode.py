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
        return f"tag:{self.tag} value:{self.value} children:{self.children} props:{self.props}"

