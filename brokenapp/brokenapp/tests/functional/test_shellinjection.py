from brokenapp.tests import *

class TestShellinjectionController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='shellinjection', action='index'))
        # Test response...
