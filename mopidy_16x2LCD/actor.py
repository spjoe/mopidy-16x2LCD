import pykka
import logging
import time
import random
from thread import start_new_thread
from AdafruitCharLCD.Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from mopidy.core import CoreListener

logger = logging.getLogger('mopidy_16x2LCD')


class LCDFrontend(pykka.ThreadingActor, CoreListener):
    def __init__(self, config, core):
        super(LCDFrontend, self).__init__()
        self.core = core

    def on_start(self):
        logger.debug('16x2LCD started')
        self.displayRenderer = DisplayRenderer()
        self.displayRenderer.setState("M Started")

    def on_stop(self):
        logger.debug('16x2LCD stopped')
        self.displayRenderer.setState("M Stopped")
        self.displayRenderer.stopRenderer()

    def on_failure(self):
        logger.warning('16x2LCD failing')
        self.displayRenderer.setState("M Failed")

    def on_event(self, event, **kwargs):
        if event == "IRButtonPressed":
            logger.debug("Button pressed: " + str(kwargs))
            if kwargs['button'] == "power":
                logger.debug('on_event: calls toggle disco')
                self.displayRenderer.toggleDisco()
        return CoreListener.on_event(self, event, **kwargs)

    def track_playback_started(self, tl_track):
        logger.debug('started' + str(tl_track))
        self.updateTrackInfo(tl_track.track)       
        self.displayRenderer.setState("playing")

    def track_playback_paused(self, tl_track, time_position):
        logger.debug('paused')
        self.displayRenderer.setState("paused")

    def track_playback_resumed(self, tl_track, time_position):
        logger.debug('resumed')
        self.updateTrackInfo(tl_track.track)    
        self.displayRenderer.setState("playing")

    def track_playback_ended(self, tl_track, time_position):
        logger.debug('stopped')
        self.updateTrackInfo(tl_track.track)    
        self.displayRenderer.setState("stopped")

    def updateTrackInfo(self, track):
        logger.debug('updateTrackInfo: ' + str(track))
        try:
            trackinfo = ""
            if track is not None:
                if track.name is not None:
                    trackinfo = track.name
                if track.artists is not None and len(track.artists) > 0 and next(iter(track.artists)).name is not None:
                    trackinfo = trackinfo + " - " + next(iter(track.artists)).name
                if track.album is not None and track.album.name is not None:
                    trackinfo = trackinfo + " - " + track.album.name
            logger.debug('trackinfo: ' + trackinfo)
            self.displayRenderer.setTrackInfo(trackinfo)
        except Exception as e:
            logger.warning("Exception: " + str(e))

    def volume_changed(self, volume):
        logger.debug('volume changed')
        self.displayRenderer.setVolume(volume)

    def mute_changed(self, mute):
        logger.debug('mute changed')
        if mute:
            self.displayRenderer.setVolume(0)
        else:
            self.displayRenderer.setVolume(self.core.playback.volume.get())


class DisplayRenderer:
    def __init__(self):
        self.lcdPanel = Adafruit_CharLCDPlate()
        self.volumeString = "100%"
        self.trackInfo = "No track is currently played"
        self.state = ""
        self.line1 = ""
        self.line2 = ""
        self.backColor = self.lcdPanel.BLUE
        self.disco = False
        self._recalculateLines()
        self._startTickerThread()

    def _startTickerThread(self):
        self.tickerStarted = True
        start_new_thread(self._tickerLoop, ())

    def _tickerLoop(self):
        while self.tickerStarted:
            time.sleep(0.5)
            self.handleTimerTick()

    def stopRenderer(self):
        self.tickerStarted = False
        self.disco = False

    def setTrackInfo(self, trackinfo):
        self.trackInfo = trackinfo
        self.Invalidate()

    def setVolume(self, volume):
        self.volumeString = str(volume) + "%"
        self.Invalidate()

    def setState(self, state):
        self.state = state
        self.Invalidate()

    def toggleDisco(self):
        if self.disco == False:
            self.disco = True
            start_new_thread(self._discoLoop, ())
        else:
            self.disco = False

    def _discoLoop(self):
        while self.disco:
            time.sleep(0.2)
            self.backColor = random.randint(1, 7)
            self.RenderDisplayTexts()

    def Invalidate(self):
        self._recalculateLines()
        self.RenderDisplayTexts()

    def handleTimerTick(self):
        self.line1position = self._incPos(self.line1position, self.line1)
        self.RenderDisplayTexts()

    def _incPos(self, oldPosition, line):
        if len(line) - oldPosition < 16:
            return 0
        else:
            return oldPosition + 1

    def _recalculateLines(self):
        newline1 = self.trackInfo
        n = 16 - len(self.state) - len(self.volumeString)
        newline2 = self.state + (n * " ") + self.volumeString

        if newline1 != self.line1:
            self.line1position = 0

        if newline2 != self.line2:
            self.line2position = 0

        self.line1 = newline1
        self.line2 = newline2

    def RenderDisplayTexts(self):
        self.lcdPanel.clear()
        logger.debug("Showing on line 1: " + self.line1)
        logger.debug("Showing on line 2: " + self.line2)
        self.lcdPanel.message(
            self.line1[self.line1position:] + "\n" +
            self.line2[self.line2position:])
        self.lcdPanel.backlight(self.backColor)
