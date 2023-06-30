from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal


class TIAChatManager(DistributedObjectGlobal):
    notify = DirectNotifyGlobal.directNotify.newCategory("TIAChatManager")

    def sendChatMessage(self, message):
        self.sendUpdate("chatMessage", [message])

    def sendWhisperMessage(self, message, receiverAvId):
        self.sendUpdate("whisperMessage", [message, receiverAvId])
