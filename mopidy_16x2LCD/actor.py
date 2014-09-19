import pykka
import logging
from AdafruitCharLCD.Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from mopidy.core import CoreListener

logger = logging.getLogger('mopidy_16x2LCD')


class LCDFrontend(pykka.ThreadingActor, CoreListener):
    def __init__(self, config, core):
        super(LCDFrontend, self).__init__()
        self.core = core

    def on_start(self):
        logger.info('16x2LCD started')
        self.lcd = Adafruit_CharLCDPlate()
        self.lcd.clear()
        self.lcd.message("Mopidy Started")
        self.lcd.backlight(self.lcd.GREEN)

    def on_stop(self):
        logger.info('16x2LCD stopped')
        self.lcd.clear()
        self.lcd.message("Mopidy Stopped")
        self.lcd.backlight(self.lcd.RED)

    def on_failure(self):
        logger.warning('16x2LCD failing')
        self.lcd.clear()
        self.lcd.message("ERROR")
        self.lcd.backlight(self.lcd.RED)
        
    def track_playback_started(self, tl_track):
        logger.debug('Display name of new track on LCD')
        if tl_track is not None:
            logger.debug("tl_track is defined");
            if tl_track.name is not None:
                logger.debug("tl_track.name is defined");

        self.lcd.clear()
        self.lcd.message("fun fun fun")
        self.lcd.backlight(self.lcd.BLUE)
