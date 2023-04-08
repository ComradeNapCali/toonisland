import sys

from panda3d.core import *

if __debug__:
    if len(sys.argv) == 2 and sys.argv[1] == '--dummy':
        loadPrcFile('dependencies/panda3d/general.prc')
        loadPrcFile('dependencies/panda3d/dev.prc')

        # The VirtualFileSystem, which has already initialized, doesn't see the mount
        # directives in the panda3d(s) yet. We have to force it to load those manually:
        vfs = VirtualFileSystem.getGlobalPtr()
        mounts = ConfigVariableList('vfs-mount')
        for mount in mounts:
            mountFile, mountPoint = (mount.split(' ', 2) + [None, None, None])[:2]
            vfs.mount(Filename(mountFile), Filename(mountPoint), 0)

import builtins

class game:
    name = 'toontown'
    process = 'client'


builtins.game = game()
import time
import os
import random
import builtins
try:
    launcher
except:
    from toontown.launcher.TIADummyLauncher import TIADummyLauncher
    launcher = TIADummyLauncher()
    builtins.launcher = launcher

launcher.setRegistry('EXIT_PAGE', 'normal')
pollingDelay = 0.5
print('ToontownStart: Polling for game2 to finish...')
while not launcher.getGame2Done():
    time.sleep(pollingDelay)

print('ToontownStart: Game2 is finished.')
print('ToontownStart: Starting the game.')
if launcher.isDummy():
    http = HTTPClient()
else:
    http = launcher.http
tempLoader = Loader()
backgroundNode = tempLoader.loadSync(Filename('phase_3/models/gui/loading-background'))
from direct.gui import DirectGuiGlobals
print('ToontownStart: setting default font')
from . import ToontownGlobals
DirectGuiGlobals.setDefaultFontFunc(ToontownGlobals.getInterfaceFont)
launcher.setPandaErrorCode(7)
from . import ToonBase
ToonBase.ToonBase()
from toontown.toonbase.TTFrameRateMeter import *
TTFrameRateMeter()
from toontown.distributed.DiscordRPC import *
try:
    Discord = DiscordRPC()
    Discord.Launching()
except:
    pass
if base.win == None:
    print('Unable to open window; aborting.')
    sys.exit()
launcher.setPandaErrorCode(0)
launcher.setPandaWindowOpen()
ConfigVariableDouble('decompressor-step-time').setValue(0.01)
ConfigVariableDouble('extractor-step-time').setValue(0.01)
backgroundNodePath = aspect2d.attachNewNode(backgroundNode, 0)
backgroundNodePath.setPos(0.0, 0.0, 0.0)
backgroundNodePath.setScale(aspect2d, VBase3(1.33, 1, 1))
backgroundNodePath.find('**/fg').setBin('fixed', 20)
backgroundNodePath.find('**/bg').setBin('fixed', 10)
backgroundNodePath.find('**/bg').setScale(aspect2d, VBase3(base.getAspectRatio(), 1, 1))
base.graphicsEngine.renderFrame()
DirectGuiGlobals.setDefaultRolloverSound(base.loader.loadSfx('phase_3/audio/sfx/GUI_rollover.ogg'))
DirectGuiGlobals.setDefaultClickSound(base.loader.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.ogg'))
DirectGuiGlobals.setDefaultDialogGeom(loader.loadModel('phase_3/models/gui/dialog_box_gui'))
from . import TTLocalizer
from otp.otpbase import OTPGlobals
OTPGlobals.setDefaultProductPrefix(TTLocalizer.ProductPrefix)
if base.musicManagerIsValid:
    music = base.musicManager.getSound('phase_3/audio/bgm/tt_theme.ogg')
    if music:
        music.setLoop(1)
        music.setVolume(0.9)
        music.play()
    print('ToontownStart: Loading default gui sounds')
    DirectGuiGlobals.setDefaultRolloverSound(base.loader.loadSfx('phase_3/audio/sfx/GUI_rollover.ogg'))
    DirectGuiGlobals.setDefaultClickSound(base.loader.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.ogg'))
else:
    music = None
from . import ToontownLoader
from direct.gui.DirectGui import *
serverVersion = base.config.GetString('server-version', 'no_version_set')
print('ToontownStart: serverVersion: ', serverVersion)
version = OnscreenText(serverVersion, pos=(-1.3, -0.975), scale=0.07, fg=Vec4(0, 1, 0, 0.8), align=TextNode.ARight, font=ToontownGlobals.getSignFont())
loader.beginBulkLoad('init', TTLocalizer.LoaderLabel, 138, 0, TTLocalizer.TIP_NONE, 0)
version.setPos(-0.03, 0.03)
version.reparentTo(base.a2dBottomRight)
gameAlphaText = "Pre-Alpha Test"
alphaText = OnscreenText(gameAlphaText, pos=(0, 0), scale=0.07, fg=Vec4(1, 1, 1, 1), align=TextNode.ALeft, font=ToontownGlobals.getSignFont())
alphaText.setPos(0.03, 0.03)
alphaText.reparentTo(base.a2dBottomLeft)
from .ToonBaseGlobal import *
from direct.showbase.MessengerGlobal import *
from toontown.distributed import ToontownClientRepository
cr = ToontownClientRepository.ToontownClientRepository(serverVersion, launcher)
cr.music = music
del music
base.initNametagGlobals()
base.cr = cr
loader.endBulkLoad('init')
from otp.friends import FriendManager
from otp.distributed.OtpDoGlobals import *
cr.generateGlobalObject(OTP_DO_ID_FRIEND_MANAGER, 'FriendManager')
if not launcher.isDummy():
    base.startShow(cr, launcher.getGameServer())
else:
    base.startShow(cr)
backgroundNodePath.reparentTo(hidden)
backgroundNodePath.removeNode()
del backgroundNodePath
del backgroundNode
del tempLoader
version.cleanup()
del version
base.loader = base.loader
builtins.loader = base.loader
autoRun = ConfigVariableBool('toontown-auto-run', 1)
if autoRun and launcher.isDummy() and (not Thread.isTrueThreads() or __name__ == '__main__'):
    try:
        base.run()
    except SystemExit:
        raise
    except:
        from otp.otpbase import PythonUtil
        print(PythonUtil.describeException())
        raise
