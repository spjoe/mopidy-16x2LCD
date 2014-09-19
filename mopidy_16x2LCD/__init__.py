from __future__ import unicode_literals

import os

# TODO: Comment in if you need to register GStreamer elements below, else
# remove entirely
#import pygst
#pygst.require('0.10')
#import gst
#import gobject

from mopidy import config, ext


__version__ = '0.1.0'


class Extension(ext.Extension):
    dist_name = 'Mopidy-16x2LCD'
    ext_name = '16x2LCD'
    version = __version__
    
    def get_frontend_classes(self):
        from .actor import LCDFrontend
        return [LCDFrontend]
