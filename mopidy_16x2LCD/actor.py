import pykka
import logging

logger = logging.getLogger('mopidy_16x2LCD')


class LCDFrontend(pykka.ThreadingActor):
    def __init__(self, config, core):
        super(LCDFrontend, self).__init__()
        self.core = core

    def on_start(self):
        logger.info('16x2LCD started')

    def on_stop(self):
        logger.info('16x2LCD stopped')

    def on_failure(self):
        logger.warning('16x2LCD failing')
