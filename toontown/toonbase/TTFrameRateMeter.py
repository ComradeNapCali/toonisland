from panda3d.core import TextNode
from toontown.toonbase import ToontownGlobals
import random

class TTFrameRateMeter(TextNode):

    def __init__(self, name='frameRateMeter'):
        TextNode.__init__(self, name)
        self.lastFrameRate = None
        self.setText("0.0 FPS")
        self.setTextColor(0, .8, .4, 1)
        self.setCardColor(1, 1, 1, .6)
        self.setCardAsMargin(0.5, 0.5, 0.5, 0.5)
        self.setShadow(0.05, 0.05)
        self.setShadowColor(0, 0, 0, 1)
        self.setCardDecal(True)
        self.setAlign(TextNode.ARight)
        self.setFont(ToontownGlobals.getSignFont())
        self.frameRateMeter = base.a2dTopRight.attachNewNode(self)
        self.frameRateMeter.setBin("gui-popup", 10000)
        self.frameRateMeter.setScale(0.075)
        self.frameRateMeter.setPos(-0.050, 0, -0.110)
        taskMgr.doMethodLater(0.5, self.update, 'update-frame-rate')

    def update(self, task=None):
        averageFrameRate = round(globalClock.getAverageFrameRate(), 1)
        if not self.lastFrameRate == averageFrameRate:
            if globalClock.getAverageFrameRate() <= 60:
                self.setTextColor(0, .8, .4, 1)
            if globalClock.getAverageFrameRate() <= 45:
                self.setTextColor(1, 0.9, 0, 1)
            if globalClock.getAverageFrameRate() <= 30:
                self.setTextColor(1, 0, 0, 1)
            self.lastFrameRate = averageFrameRate
            self.setText("{0} FPS".format(self.lastFrameRate))
        task.delayTime = 0.25
        return task.again

    def destroy(self):
        taskMgr.remove('update-frame-rate')
        self.frameRateMeter.removeNode()
        del self.frameRateMeter