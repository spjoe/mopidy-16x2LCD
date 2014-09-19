from __future__ import unicode_literals

import unittest
import mopidy
import time

from mock import Mock, patch
from mopidy_16x2LCD import actor as lib


class ExtensionTest(unittest.TestCase):
        def test_frontend_classes(self):
        ext = Extension()
        frontend_classes = ext.get_frontend_classes()
        self.assertIn(lib.LCDFrontend, frontend_classes)

