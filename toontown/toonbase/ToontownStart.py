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
while not launcher.getGame2Done():
    time.sleep(pollingDelay)

print('Starting Toon Island Aftermath...')
if launcher.isDummy():
    http = HTTPClient()
else:
    http = launcher.http
from direct.gui import DirectGuiGlobals
from toontown.toonbase import ToontownGlobals
DirectGuiGlobals.setDefaultFontFunc(ToontownGlobals.getInterfaceFont)
launcher.setPandaErrorCode(7)
from toontown.toonbase import ToonBase
ToonBase.ToonBase()
if base.win is None:
    notify.error('Unable to open window; aborting.')
launcher.setPandaErrorCode(0)
launcher.setPandaWindowOpen()
from panda3d.core import Vec4
base.setBackgroundColor(Vec4(0, 0, 0, 0))
base.graphicsEngine.renderFrame()
DirectGuiGlobals.setDefaultRolloverSound(base.loadSfx('phase_3/audio/sfx/GUI_rollover.ogg'))
DirectGuiGlobals.setDefaultClickSound(base.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.ogg'))
DirectGuiGlobals.setDefaultDialogGeom(loader.loadModel('phase_3/models/gui/dialog_box_gui.bam'))
#from toontown.toon import Toon
#Toon.preload()
#from toontown.suit import Suit
#Suit.preload()
#Removed this.
#from toontown.login import AvatarChooser
#AvatarChooser.preload()
#from toontown.shtiker import ShtikerGUI
#ShtikerGUI.preload()
from toontown.clicktostart.Introduction import Introduction
introduction = Introduction()
from toontown.clicktostart.ClickToStart import ClickToStart
version = ConfigVariableString('server-version', 'n/a')
clickToStart = ClickToStart(version=version.getValue())
clickToStart.setColorScale(0, 0, 0, 0)
music = None
if base.musicManagerIsValid:
    music = base.loadMusic('phase_3/audio/bgm/tt_theme.ogg')
    if music:
        music.setLoop(1)
        music.setVolume(0.9)
        music.play()
    DirectGuiGlobals.setDefaultRolloverSound(base.loadSfx('phase_3/audio/sfx/GUI_rollover.ogg'))
    DirectGuiGlobals.setDefaultClickSound(base.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.ogg'))
else:
    music = None
from toontown.toonbase import TTLocalizer
from otp.otpbase import OTPLocalizer
from otp.otpgui import OTPDialog

def syncLoginFSM(task = None):
    stateName = base.cr.loginFSM.getCurrentState().getName()
    if introduction.getCurrentOrNextState() != 'Label' and introduction.label.getText() != TTLocalizer.LoaderLabel:
            introduction.request('Label', TTLocalizer.LoaderLabel)
            taskMgr.doMethodLater(1, syncLoginFSM, 'syncLoginFSM-task')
    elif stateName in ('connect', 'login', 'waitForGameList', 'waitForShardList'):
        introduction.request('Label', OTPLocalizer.CRConnecting)
    elif stateName == 'failedToConnect':
        url = base.cr.serverList[0]
        if base.cr.bootedIndex in (1400, 1403, 1405):
            message = OTPLocalizer.CRNoConnectProxyNoPort % (url.getServer(), url.getPort(), url.getPort())
            style = OTPDialog.CancelOnly
        else:
            message = OTPLocalizer.CRNoConnectTryAgain % (url.getServer(), url.getPort())
            style = OTPDialog.TwoChoice
        if style == OTPDialog.CancelOnly:
            introduction.request('ExitDialog', message, base.cr.loginFSM.request, ['shutdown'])
        else:
            introduction.request('YesNoDialog', message, base.cr.loginFSM.request, ['connect', [base.cr.serverList]], base.cr.loginFSM.request, ['shutdown'])
    elif stateName == 'noConnection':
        if base.cr.bootedIndex is not None and base.cr.bootedIndex in OTPLocalizer.CRBootedReasons:
            message = OTPLocalizer.CRBootedReasons[base.cr.bootedIndex]
        elif base.cr.bootedIndex == 155:
            message = base.cr.bootedText
        elif base.cr.bootedText is not None:
            message = OTPLocalizer.CRBootedReasonUnknownCode % base.cr.bootedIndex
        else:
            message = OTPLocalizer.CRLostConnection
        if base.cr.bootedIndex == 152:
            message %= {'name': base.cr.bootedText}
        introduction.request('ExitDialog', message, base.cr.loginFSM.request, ['shutdown'])
    elif stateName == 'missingGameRootObject':
        introduction.request('YesNoDialog', OTPLocalizer.CRMissingGameRootObject, base.cr.loginFSM.request, ['waitForGameList'], base.cr.loginFSM.request, ['shutdown'])
    elif stateName == 'noShards':
        introduction.request('YesNoDialog', OTPLocalizer.CRNoDistrictsTryAgain, base.cr.loginFSM.request, ['noShardsWait'], base.cr.loginFSM.request, ['shutdown'])
    else:
        introduction.request('ClickToStart')
    if task is not None:
        return task.done
    else:
        return



from direct.interval.IntervalGlobal import Sequence, Func, Wait
presentsTrack = Sequence(Func(introduction.request, 'Presents'), Wait(7), Func(syncLoginFSM))
disclaimerTrack = Sequence(Func(introduction.request, 'Disclaimer'), Wait(7), Func(presentsTrack.start))
from toontown.distributed import ToontownClientRepository
base.cr = ToontownClientRepository.ToontownClientRepository(version.getValue(), launcher)
base.cr.music = music
base.cr.introduction = introduction
base.cr.clickToStart = clickToStart
base.initNametagGlobals()
from otp.distributed.OtpDoGlobals import OTP_DO_ID_FRIEND_MANAGER
base.cr.generateGlobalObject(OTP_DO_ID_FRIEND_MANAGER, 'FriendManager')
if not launcher.isDummy():
    base.startShow(launcher.getGameServer())
else:
    base.startShow()
builtins.loader = base.loader
disclaimerTrack.start()
#if music is not None:
    #music.play()

def skip():
    if disclaimerTrack.isPlaying():
        disclaimerTrack.finish()
    elif presentsTrack.isPlaying():
        presentsTrack.finish()


base.accept('mouse1', skip)
#gc.enable()
#gc.collect()
try:
    if config.GetBool('want-leak-graph-client', False):
        from toontown.debug import LeakGraph
        LeakGraph.outputLeaking()
    base.run()
except SystemExit:
    pass
except Exception:
    import traceback
    traceback.print_exc()