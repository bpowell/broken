from brokenapp.tests import *

class TestLogtoobigController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='logtoobig', action='index'))
        # Test response...
