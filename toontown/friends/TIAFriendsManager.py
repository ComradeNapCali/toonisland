import json
import base64

from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal


class TIAFriendsManager(DistributedObjectGlobal):
    notify = DirectNotifyGlobal.directNotify.newCategory('TIAFriendsManager')

    def d_getAvatarDetails(self, avId):
        self.sendUpdate('getAvatarDetails', [avId])

    def avatarDetailsResp(self, avId, details):
        fields = json.loads(details)
        for currentField in fields:
            if currentField[0] in (
                    'setDNAString', 'setMailboxContents', 'setAwardMailboxContents', 'setGiftSchedule',
                    'setDeliverySchedule', 'setAwardSchedule'):
                currentField[1] = base64.b64decode(currentField[1])

        base.cr.handleGetAvatarDetailsResp(avId, fields=fields)

    def d_getFriendsListRequest(self):
        self.sendUpdate('getFriendsListRequest')

    def friendsListRequestResp(self, resp):
        base.cr.handleGetFriendsList(resp)

    def friendOnline(self, id, commonChatFlags, whitelistChatFlags, alert=True):
        base.cr.handleFriendOnline(id, commonChatFlags, whitelistChatFlags, alert)

    def d_removeFriend(self, friendId):
        self.sendUpdate('removeFriend', [friendId])

    def friendOffline(self, id):
        base.cr.handleFriendOffline(id)
