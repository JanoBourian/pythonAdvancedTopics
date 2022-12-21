from Widget import Widget
import unittest

class WidgetTestCase(unittest.TestCase):
    
    def setUp(self):
        self.widget = Widget("The widget")
    
    def test_default_widget(self):
        self.assertEqual(self.widget.size(), (50,50), "Incorrect default size")
    
    def test_widget_resize(self):
        self.assertEqual(self.widget.resize(100,150), (100,150), "incorrect resize process")
        self.assertEqual(self.widget.size(), (100,150), "wrong size after resize")
        
    def tearDown(self):
        self.widget.dispose()