from .base import PgObject, inspect_node


class Value(PgObject):
    def to_string(self):
        node_type = inspect_node(self.val)
        if node_type == "String":
            return repr(self.val["val"]["str"].string())
        else:
            return self.val["val"]["ival"].string()


class String(Value):
    def to_string(self):
        return repr(self.val["sval"].string())
