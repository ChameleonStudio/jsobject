import unittest
from jsobject import JSObject


class JSObjectTest(unittest.TestCase):

    def setUp(self):
        self.jso = JSObject({'attr1': {'attr2': 'val1'}, 'attr3': ['val2', {'attr4': 'val3'}]})

    def test_get_attr(self):
        pass

    def test_get_attr_chain(self):
        pass

    def test_get_no_existing_attr(self):
        pass

    def test_get_no_existing_attr_chain(self):
        pass

    def test_set_attr(self):
        pass

    def test_set_attr_chain(self):
        pass

    def test_set_no_existing_attr_chain(self):
        pass
