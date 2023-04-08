from pandac.PandaModules import *
from direct.gui.DirectGui import *
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.hood import ZoneUtil
import random

LOADING_SCREEN_SORT_INDEX = 4000


class ToontownLoadingScreen:
    defaultTex = 'phase_3/maps/loading_bg_clouds.jpg'
    zone2picture = {
        ToontownGlobals.GoofySpeedway: 'phase_3.5/maps/loading/gs.jpg',
        ToontownGlobals.ToonIslandCentral: 'phase_3.5/maps/loading/ttc.jpg',
        ToontownGlobals.BeachballBoulevard: 'phase_3.5/maps/loading/ttc_ss.jpg',
        ToontownGlobals.AlohaAvenue: 'phase_3.5/maps/loading/ttc_ll.jpg',
        ToontownGlobals.PineapplePlace: 'phase_3.5/maps/loading/ttc_pp.jpg',
        ToontownGlobals.SeashellStreet: 'phase_3.5/maps/loading/ttc_pp.jpg',
    }

    def __init__(self):
        self.__expectedCount = 0
        self.__count = 0
        # self.tip = DirectLabel(guiId='ToontownLoadingScreenTip', parent=self.banner, relief=None, text='', text_scale=TTLocalizer.TLStip, textMayChange=1, pos=(-1.2, 0.0, 0.1), text_fg=(0.4, 0.3, 0.2, 1), text_wordwrap=13, text_align=TextNode.ALeft)
        self.gui = loader.loadModel('phase_3/models/gui/progress-background.bam')
        self.title = DirectLabel(guiId='ToontownLoadingScreenTitle', relief=None, pos=(0, 0, 0.24),
                                 text='', textMayChange=1, text_scale=0.13, text_fg=(0.2, 1.0, 0, 0.8),
                                 text_shadow=(0, 0, 0, 5), text_align=TextNode.ACenter,
                                 text_font=ToontownGlobals.getSignFont())
        self.waitBar = DirectWaitBar(guiId='ToontownLoadingScreenWaitBar', parent=self.gui, frameSize=(
        base.a2dLeft + (base.a2dRight / 4.95), base.a2dRight - (base.a2dRight / 4.95), 0, -0.10), pos=(0, 0, 0.20),
                                     text='', frameColor=(1, 1, 1, 0.75), barColor=(0.2, 1.0, 0, 0.8))
        self.waitBar.setTransparency(TransparencyAttrib.MAlpha)
        logoScale = 0.5625  # Scale for our locked aspect ratio (2:1).
        self.logo = OnscreenImage(
            image='phase_3/maps/toontown-logo.png',
            scale=(logoScale * 2.0, 1, logoScale))
        self.logo.reparentTo(hidden)
        self.logo.setTransparency(TransparencyAttrib.MAlpha)
        scale = self.logo.getScale()
        # self.logo.setPos(scale[0], 0, -scale[2])
        self.logo.setPos(0, 0, -scale[2])

    def destroy(self):
        # self.tip.destroy()
        self.title.destroy()
        self.gui.removeNode()
        self.logo.removeNode()

    def getTip(self, tipCategory):
        return TTLocalizer.TipTitle + '\n' + random.choice(TTLocalizer.TipDict.get(tipCategory))

    def begin(self, range, label, gui, tipCategory, zoneId):
        self.waitBar['range'] = range
        # self.tip['text'] = self.getTip(tipCategory)
        self.title['text'] = label
        if ToontownGlobals.BossbotHQ <= zoneId <= ToontownGlobals.LawbotHQ:
            self.title['text_font'] = ToontownGlobals.getSuitFont()
        else:
            self.title['text_font'] = ToontownGlobals.getSignFont()
        loadingScreenTex = self.zone2picture.get(ZoneUtil.getBranchZone(zoneId), self.defaultTex)
        self.background = loader.loadTexture(loadingScreenTex)
        self.__count = 0
        self.__expectedCount = range
        if gui:
            self.title.setPos(0, 0, 0.26)
            self.gui.setPos(0, -0.1, 0)
            self.gui.reparentTo(aspect2d, LOADING_SCREEN_SORT_INDEX)
            self.gui.setTexture(self.background, 1)
            if loadingScreenTex == self.defaultTex:
                self.logo.reparentTo(base.a2dpTopCenter, LOADING_SCREEN_SORT_INDEX)
        else:
            self.gui.reparentTo(hidden)
            self.logo.reparentTo(hidden)
        self.title.reparentTo(base.a2dpBottomCenter, LOADING_SCREEN_SORT_INDEX)
        self.waitBar.reparentTo(base.a2dpBottomCenter, LOADING_SCREEN_SORT_INDEX)
        self.waitBar.update(self.__count)

    def end(self):
        self.waitBar.finish()
        self.waitBar.reparentTo(self.gui)
        self.title.reparentTo(self.gui)
        self.gui.reparentTo(hidden)
        self.logo.reparentTo(hidden)
        return (self.__expectedCount, self.__count)

    def abort(self):
        self.gui.reparentTo(hidden)

    def tick(self):
        self.__count = self.__count + 1
        self.waitBar.update(self.__count)
        self.waitBar.update(self.__count)
