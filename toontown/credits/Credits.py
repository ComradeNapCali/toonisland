from panda3d.core import *
from pandac.PandaModules import CardMaker
from direct.interval.IntervalGlobal import *
from direct.fsm import State
from toontown.toon import Toon, ToonDNA
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import ToonBase

class Credits:

    def __init__(self):
        #setup
        self.showCredits = None
        self.text = None
        self.roleText = None
        cm = CardMaker('screen-cover')
        cm.setFrameFullscreenQuad()
        self.screenCover = aspect2d.attachNewNode(cm.generate())
        self.screenCover.show()
        self.screenCover.setScale(100)
        self.screenCover.setColor((0, 0, 0, 1))
        self.screenCover.setTransparency(1)

        #run
        self.credits = '''
\1limeText\1Credits\2

\1limeText\1Management Team\2
Nayla | Director

\1limeText\1Technical Team\2
Prof. Robin | Game & Web Developer

\1limeText\1Creative Team\2
April | Concept Artist, Moderator
Sheogorath | Concepts, Creative
Pizza Taco Burger | Storyline Writer
The Player Zero | Creaive
Tom Bumberpop | Composer

\1limeText\1Contributors\2
Supertricky | Sellbot Fatal Factory
Leo, Rocket | Seashell Street, FPS Meter
Pythology | Click To Start
Shaping Insanity | Toon Island Logo

\1limeText\1Special Thanks To\2
Toon Island: Aftermath | Various Concepts and Ideas
Toontown Event Horizons | Axolotl Inspiration
satire6 | Pandora and Anesidora
Contributors of Panda3D
Contributors of Astron
Toontown Rewritten | Reviving the spirit of Toontown
Disney VR Studios | Creating a game for years to come
Jesse Schell | Fighting for Toontown's Offical Return
You | Playing the game and supporting it

\1limeText\Thanks for everything!\2
        '''
        self.text = OnscreenText(text = self.credits, style = 3, fg = (1, 1, 1, 1), align = TextNode.ACenter, scale = 0.08, wordwrap = 30, parent = aspect2d)
        self.text.setPos(0, -1)
        self.text.setColorScale(1, 1, 1, 0)
        self.logo = OnscreenImage(image = 'phase_3/maps/toontown-logo.png',
                                  scale = (0.8 * (4.0 / 3.0), 0.8, 0.8 / (4.0 / 3.0)))
        self.logo.setTransparency(TransparencyAttrib.MAlpha)
        self.logo.reparentTo(self.text)
        self.logo.setPos(0, 0, 0)
        self.logo.setColorScale(1, 1, 1, 1)
        self.startCredits()
        base.transitions.fadeScreen(0)
        base.accept('space', self.removeCredits)
        base.accept('escape', self.removeCredits)

    def startCredits(self):
        self.creditsMusic = base.loader.loadMusic('phase_3.5/audio/bgm/hall_of_fame.ogg')
        base.playMusic(self.creditsMusic, looping=0, volume=0.9)

        self.showCredits = Sequence(
        LerpColorScaleInterval(self.screenCover, 1, Vec4(1, 1, 1, 1), startColorScale = Vec4(1, 1, 1, 0)),
        LerpColorScaleInterval(self.text, 1, Vec4(1, 1, 1, 1), startColorScale = Vec4(1, 1, 1, 0)),
        Wait(1),
        self.text.posInterval(35, Point3(0, 0, 6)),
        Wait(1),
        LerpColorScaleInterval(self.screenCover, 1, Vec4(1, 1, 1, 0), startColorScale = Vec4(1, 1, 1, 1)),
        Func(self.removeCredits)
        ).start()

    def removeCredits(self):
        base.ignore('space')
        base.ignore('escape')
        base.transitions.noFade()
        self.creditsMusic = base.loader.loadMusic('phase_3/audio/bgm/tt_theme.ogg')
        base.playMusic(self.creditsMusic, looping=1, volume=0.9)
        if self.showCredits:
            self.showCredits.finish()
            self.showCredits = None
        if self.text:
            self.text.destroy()
            self.text = None
        if self.screenCover:
            self.screenCover.removeNode()
            self.screenCover = None