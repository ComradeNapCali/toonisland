##################################################
# The Toontown Infinite ClickToStart
##################################################
# Author: Pythology
# Copyright: Copyright 2016, Toontown Infnite
##################################################

from direct.gui.DirectGui import OnscreenImage, OnscreenText
from panda3d.core import TransparencyAttrib, Point3, Vec4, Vec3, TextNode, CardMaker, Texture
from direct.interval.IntervalGlobal import LerpPosInterval, Wait, Func
from direct.interval.IntervalGlobal import Sequence, LerpColorScaleInterval
from direct.interval.IntervalGlobal import LerpScaleInterval
from direct.showbase.DirectObject import DirectObject
from direct.showbase.ShowBase import ShowBase
from toontown.toonbase import TTLocalizer, ToontownGlobals

class ClickToStart(DirectObject):
    notify = directNotify.newCategory('ClickToStart')

    def __init__(self, version = 'n/a'):
        DirectObject.__init__(self)
        clickToStartText = TTLocalizer.ClickToStartLabel
        font = ToontownGlobals.getMinnieFont()
        self.label = OnscreenText(clickToStartText, parent=base.a2dBottomCenter, font=font, fg=Vec4(0.0, 0.0, 0, 0.8), scale=0.13, align=TextNode.ACenter)
        self.label.setZ(0.35)
        self.versionLabel = OnscreenText('\x01black_shadow\x01%s\x02' % version, parent=base.a2dBottomRight, font=ToontownGlobals.getMinnieFont(), fg=Vec4(0, 0, 0, 1), scale=0.06, align=TextNode.ARight)
        self.versionLabel.setPos(-0.025, 0.025)
        self.setColorScale(Vec4(0, 0, 0, 0))
        # very hacky but works
        screen_width = base.win.getProperties().getXSize()
        screen_height = base.win.getProperties().getYSize()
        self.background = OnscreenImage(parent=base.a2dTopCenter, image='phase_3/maps/loading_bg_clouds.jpg', scale=(screen_width / 400, 1, screen_height / 300), pos=(0, 0, 0))
        
        self.logo = OnscreenImage(parent=base.a2dTopCenter, image='phase_3/maps/toontown-logo.png', scale=(1, 1, 0.4), pos=(9, 0, -0.9))
        self.logo.setTransparency(TransparencyAttrib.MAlpha)
        self.fadeTrack = None
        self.logoPosTrack = None
        self.logoScaleTrack = None
        self.labelPosTrack = None
        self.labelColorScaleTrack = None
        return
        


    def delete(self):
        if self.labelColorScaleTrack is not None:
            self.labelColorScaleTrack.finish()
            self.labelColorScaleTrack = None
        if self.labelPosTrack is not None:
            self.labelPosTrack.finish()
            self.labelPosTrack = None
        if self.logoScaleTrack is not None:
            self.logoScaleTrack.finish()
            self.logoScaleTrack = None
        if self.logoPosTrack is not None:
            self.logoPosTrack.finish()
            self.logoPosTrack = None
        if self.fadeTrack is not None:
            self.fadeTrack.finish()
            self.fadeTrack = None
        if self.versionLabel is not None:
            self.versionLabel.destroy()
            self.versionLabel = None
        if self.label is not None:
            self.label.destroy()
            self.label = None
        if self.logo is not None:
            self.logo.destroy()
            self.logo = None
        if self.background is not None:
            self.background.destroy()
            self.background = None
        return

    def start(self):
        base.transitions.fadeOut(t=0)
        self.setColorScale(Vec4(0, 0, 0, 1))
        if self.fadeTrack is not None:
            self.fadeTrack.finish()
            self.fadeTrack = None
        self.fadeTrack = base.transitions.getFadeInIval(t=2)
        self.fadeTrack.start()
        if self.logoScaleTrack is not None:
            self.logoScaleTrack.finish()
            self.logoScaleTrack = None
        self.logoScaleTrack = Sequence(LerpScaleInterval(self.logo, 2, Vec3(1, 1, 0.45), Vec3(0.9, 1, 0.4), blendType='easeInOut'), LerpScaleInterval(self.logo, 2, Vec3(0.9, 1, 0.4), Vec3(1, 1, 0.45), blendType='easeInOut'))
        if self.logoPosTrack is not None:
            self.logoPosTrack.finish()
            self.logoPosTrack = None
        self.logoPosTrack = Sequence(LerpPosInterval(self.logo, 2, Point3(0, 0, -0.9), Point3(0, 0, -0.7), blendType='easeOut'), Func(self.logoScaleTrack.loop))
        self.logoPosTrack.start()
        if self.labelColorScaleTrack is not None:
            self.labelColorScaleTrack.finish()
            self.labelColorScaleTrack = None
        self.labelColorScaleTrack = Sequence(LerpColorScaleInterval(self.label, 1, Vec4(1, 1, 1, 0.6), Vec4(1, 1, 1, 1)), LerpColorScaleInterval(self.label, 1, Vec4(1, 1, 1, 1), Vec4(1, 1, 1, 0.6)))
        if self.labelPosTrack is not None:
            self.labelPosTrack.finish()
            self.labelPosTrack = None
        self.labelPosTrack = Sequence(LerpPosInterval(self.label, 2, Point3(0, 0, 0.35), Point3(0, 0, 0.15), blendType='easeOut'), Func(self.labelColorScaleTrack.loop))
        self.labelPosTrack.start()
        self.acceptOnce('mouse1', self.begin)
        return

    def stop(self):
        self.ignore('mouse1')
        if self.labelPosTrack is not None:
            self.labelPosTrack.finish()
            self.labelPosTrack = None
        if self.labelColorScaleTrack is not None:
            self.labelColorScaleTrack.finish()
            self.labelColorScaleTrack = None
        if self.logoPosTrack is not None:
            self.logoPosTrack.finish()
            self.logoPosTrack = None
        if self.logoScaleTrack is not None:
            self.logoScaleTrack.finish()
            self.logoScaleTrack = None
        if self.fadeTrack is not None:
            self.fadeTrack.finish()
            self.fadeTrack = None
        if self.background is not None:
            self.background.destroy()
            self.background = None
        self.setColorScale(Vec4(0, 0, 0, 0))
        return

    def begin(self):
        base.cr.introDone = True
        if self.fadeTrack is not None:
            self.fadeTrack.finish()
            self.fadeTrack = None
        self.fadeTrack = base.transitions.getFadeOutIval(t=2)
        Sequence(Func(self.fadeTrack.start), Wait(2), Func(self.delete), Func(base.cr.introduction.delete), Func(base.cr.loginFSM.request, 'chooseAvatar', [base.cr.avList]), Func(base.transitions.fadeIn, 2)).start()
        return

    def setColorScale(self, *args, **kwargs):
        self.label.setColorScale(*args, **kwargs)
        self.versionLabel.setColorScale(*args, **kwargs)