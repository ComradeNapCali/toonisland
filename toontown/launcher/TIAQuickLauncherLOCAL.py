import os
from direct.showbase.EventManagerGlobal import *
from toontown.launcher.TIALauncherBase import TIALauncherBase
from toontown.toonbase import TTLocalizer

class TIAQuickLauncherLOCAL(TIALauncherBase):
    GameName = 'Toon Island: Aftermath'
    ForegroundSleepTime = 0.001
    Localizer = TTLocalizer

    def __init__(self):
        print('Running: TIAQuickLauncher')
        TIALauncherBase.__init__(self)
        self.useTIASpecificLogin = config.GetBool('TIA-specific-login', 0)
        if self.useTIASpecificLogin:
            self.TIAPlayTokenKey = 'TIA_PLAYCOOKIE'
        else:
            self.TIAPlayTokenKey = 'TIA_PLAYCOOKIE'
        print('useTIASpecificLogin=%s' % self.useTIASpecificLogin)
        self.parseWebAcctParams()
        self.showPhase = -1
        self.maybeStartGame()
        self.mainLoop()

    def getValue(self, key, default = None):
        return os.environ.get(key, default)

    def setValue(self, key, value):
        os.environ[key] = str(value)

    def getTestServerFlag(self):
        return self.getValue('IS_TEST_SERVER', 0)

    def getGameServer(self):
        return '127.0.0.1'
    def getLogFileName(self):
        return 'TIA'

    def parseWebAcctParams(self):
        # these aren't ever used, as self.useTIASpecificLogin should
        # always be true. in the event that it isn't, however, we do
        # not want the client to crash on us. might as well put them here.
        self.secretNeedsParentPasswordKey = 0
        self.chatEligibleKey = 1

    def getBlue(self):
        return None

    def getPlayToken(self):
        playToken = self.getValue(self.TIAPlayTokenKey)
        self.setValue(self.TIAPlayTokenKey, '')
        if playToken == 'NO PLAYTOKEN':
            playToken = None
        return playToken

    def setRegistry(self, name, value):
        pass

    def getRegistry(self, name, missingValue = None):
        self.notify.info('getRegistry %s' % ((name, missingValue),))
        self.notify.info('checking env' % os.environ)
        if missingValue == None:
            missingValue = ''
        value = os.environ.get(name, missingValue)
        try:
            value = int(value)
        except:
            pass

        return value

    def getAccountServer(self):
        return ''

    def getGame2Done(self):
        return True

    def getNeedPwForSecretKey(self):
        if self.useTIASpecificLogin:
            self.notify.info('getNeedPwForSecretKey using TIA-specific-login')
            return False
        else:
            return self.secretNeedsParentPasswordKey

    def getParentPasswordSet(self):
        if self.useTIASpecificLogin:
            self.notify.info('getParentPasswordSet using TIA-specific-login')
            return True
        else:
            return self.chatEligibleKey

    def startGame(self):
        self.newTaskManager()
        eventMgr.restart()
        from toontown.toonbase import ToontownStart
