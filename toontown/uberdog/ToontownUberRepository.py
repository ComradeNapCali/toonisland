from direct.directnotify import DirectNotifyGlobal

from otp.distributed.DistributedDirectoryAI import DistributedDirectoryAI
from otp.distributed.OtpDoGlobals import *
from toontown.distributed.ToontownInternalRepository import ToontownInternalRepository


class ToontownUberRepository(ToontownInternalRepository):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToontownUberRepository')

    def __init__(self, baseChannel, serverId):
        ToontownInternalRepository.__init__(self, baseChannel, serverId, dcSuffix='UD')
        self.gameServicesManager = None
        self.TIAFriendsManager = None
        self.chatManager = None
        self.deliveryManager = None

    def handleConnected(self):
        ToontownInternalRepository.handleConnected(self)

        rootObj = DistributedDirectoryAI(self)
        rootObj.generateWithRequiredAndId(self.getGameDoId(), 0, 0)

        self.createGlobals()

        self.notify.info('Done.')

    def createGlobals(self):
        self.gameServicesManager = self.generateGlobalObject(OTP_DO_ID_TOONTOWN_GAME_SERVICES_MANAGER,
                                                             'TTGameServicesManager')
        self.TIAFriendsManager = self.generateGlobalObject(OTP_DO_ID_TIA_FRIENDS_MANAGER, 'TIAFriendsManager')
        self.chatManager = self.generateGlobalObject(OTP_DO_ID_CHAT_MANAGER, 'TIAChatManager')
        self.deliveryManager = self.generateGlobalObject(OTP_DO_ID_TOONTOWN_DELIVERY_MANAGER,
                                                         'DistributedDeliveryManager')
