import json as json_parser


class JSObject:
    """Allow to use json as an Python object with attributes"""

    def __init__(self, json):
        if isinstance(json, str):
            json = json_parser.loads(json)
        self.json = json

    def __getattr__(self, attr):

        if not self.json:
            return JSObject(None)

        try:
            val = self.json[attr]
        except KeyError or IndexError:
            return JSObject(None)

        if isinstance(val, (list, dict)):
            return JSObject(val)
        if isinstance(val, (str, int, float)):
            return val

    def __getitem__(self, item):
        return self.__getattr__(item)

    def __str__(self):
        return str(self.json)
