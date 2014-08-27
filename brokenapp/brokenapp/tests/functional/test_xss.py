from brokenapp.tests import *

class TestXssController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='xss', action='index'))
        # Test response...
