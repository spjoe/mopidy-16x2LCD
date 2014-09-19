from __future__ import unicode_literals

import unittest
import mopidy_16x2LCD

from mopidy_16x2LCD import actor

class ExtensionTest(unittest.TestCase):
    def test_frontend_classes(self):
        ext = mopidy_16x2LCD.Extension()
        frontend_classes = ext.get_frontend_classes()
        self.assertIn(actor.LCDFrontend, frontend_classes)
