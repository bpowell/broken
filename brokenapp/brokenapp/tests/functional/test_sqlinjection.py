from brokenapp.tests import *

class TestSqlinjectionController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='sqlinjection', action='index'))
        # Test response...
