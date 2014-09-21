from __future__ import unicode_literals

# TODO: Comment in if you need to register GStreamer elements below, else
# remove entirely
#import pygst
#pygst.require('0.10')
#import gst
#import gobject

import os
from mopidy import ext, config


__version__ = '0.1.0'


class Extension(ext.Extension):
    dist_name = 'Mopidy-16x2LCD'
    ext_name = '16x2LCD'
    version = __version__

    def setup(self, registry):
        from .actor import LCDFrontend
        registry.add('frontend', LCDFrontend)

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)
