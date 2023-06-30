from otp.otpbase import OTPGlobals
from toontown.toonbase import ToontownBattleGlobals
from toontown.toonbase import ToontownGlobals
from toontown.battle import SuitBattleGlobals
from toontown.coghq import CogDisguiseGlobals
import random
from toontown.toon import NPCToons
import copy, string
from toontown.hood import ZoneUtil
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import TTLocalizer
from direct.showbase import PythonUtil
import time, types, random

notify = DirectNotifyGlobal.directNotify.newCategory("Quests")
ItemDict = TTLocalizer.QuestsItemDict
CompleteString = TTLocalizer.QuestsCompleteString
NotChosenString = TTLocalizer.QuestsNotChosenString
DefaultGreeting = TTLocalizer.QuestsDefaultGreeting
DefaultIncomplete = TTLocalizer.QuestsDefaultIncomplete
DefaultIncompleteProgress = TTLocalizer.QuestsDefaultIncompleteProgress
DefaultIncompleteWrongNPC = TTLocalizer.QuestsDefaultIncompleteWrongNPC
DefaultComplete = TTLocalizer.QuestsDefaultComplete
DefaultLeaving = TTLocalizer.QuestsDefaultLeaving
DefaultReject = TTLocalizer.QuestsDefaultReject
DefaultTierNotDone = TTLocalizer.QuestsDefaultTierNotDone
DefaultQuest = TTLocalizer.QuestsDefaultQuest
DefaultVisitQuestDialog = TTLocalizer.QuestsDefaultVisitQuestDialog
GREETING = 0
QUEST = 1
INCOMPLETE = 2
INCOMPLETE_PROGRESS = 3
INCOMPLETE_WRONG_NPC = 4
COMPLETE = 5
LEAVING = 6
Any = 1
OBSOLETE = "OBSOLETE"
Start = 1
Cont = 0
Anywhere = 1
NA = 2
Same = 3
AnyFish = 4
AnyCashbotSuitPart = 5
AnyLawbotSuitPart = 6
AnyBossbotSuitPart = 7
ToonTailor = 999
ToonHQ = 1000
QuestDictTierIndex = 0
QuestDictStartIndex = 1
QuestDictDescIndex = 2
QuestDictFromNpcIndex = 3
QuestDictToNpcIndex = 4
QuestDictRewardIndex = 5
QuestDictNextQuestIndex = 6
QuestDictDialogIndex = 7
VeryEasy = 100
Easy = 75
Medium = 50
Hard = 25
VeryHard = 20
Impossible = 10
TT_TIER = (
    0  # 0: Toontorial - 1: Toontorial Pt2 - 2: Main Taskline - 3: Final Gag Training
)
WW_TIER = 4  # 4: Gag Training - 5: Main Taskline - 6: Final Gag Training
RR_TIER = 7  # 7: Gag Training - 8: Main Taskline - 9: Final Gag Training
CC_TIER = 10  # 10: Gag Training - 11: Main Taskline - 12: Final Gag Training
FF_TIER = 13  # 13: Sellbot Suit Explanation - 14: Main Taskline - 15: Final Sellbot Suit Piece
OO_TIER = 16  # 16: Cashbot Suit Explanation - 17: Main Taskline - 18: Final Cashbot Suit Piece
UNK_TIER = (
    19  # 19: Lawbot Suit Explanation - 20: Main Taskline - 21: Final Lawbot Suit Piece
)
MM_TIER = 22  # 22: Bossbot Suit Explantaion - 23: Main Taskline - 24: Final Bossbot Suit Piece
CZ_TIER = 25  # 25: Stoogebot Suit Explanation - 26: Main Taskline - 27: Final Stoogebot Suit Piece
ELDER_TIER = 28
LOOPING_FINAL_TIER = ELDER_TIER
VISIT_QUEST_ID = 1000
TROLLEY_QUEST_ID = 110
FIRST_COG_QUEST_ID = 145
FRIEND_QUEST_ID = 150
PHONE_QUEST_ID = 175
NEWBIE_HP = 25
SELLBOT_HQ_NEWBIE_HP = 50
CASHBOT_HQ_NEWBIE_HP = 85
from toontown.toonbase.ToontownGlobals import FT_FullSuit, FT_Leg, FT_Arm, FT_Torso

QuestRandGen = random.Random()


def seedRandomGen(npcId, avId, tier, rewardHistory):
    QuestRandGen.seed(npcId * 100 + avId + tier + len(rewardHistory))


def seededRandomChoice(seq):
    return QuestRandGen.choice(seq)


def getCompleteStatusWithNpc(questComplete, toNpcId, npc):
    if questComplete:
        if npc:
            if npcMatches(toNpcId, npc):
                return COMPLETE
            else:
                return INCOMPLETE_WRONG_NPC
        else:
            return COMPLETE
    elif npc:
        if npcMatches(toNpcId, npc):
            return INCOMPLETE_PROGRESS
        else:
            return INCOMPLETE
    else:
        return INCOMPLETE


def npcMatches(toNpcId, npc):
    return (
        toNpcId == npc.getNpcId()
        or toNpcId == Any
        or toNpcId == ToonHQ
        and npc.getHq()
        or toNpcId == ToonTailor
        and npc.getTailor()
    )


def calcRecoverChance(numberNotDone, baseChance, cap=1):
    chance = baseChance
    avgNum2Kill = 1.0 / (chance / 100.0)
    if numberNotDone >= avgNum2Kill * 1.5 and cap:
        chance = 1000
    elif numberNotDone > avgNum2Kill * 0.5:
        diff = float(numberNotDone - avgNum2Kill * 0.5)
        luck = 1.0 + abs(diff / (avgNum2Kill * 0.5))
        chance *= luck
    return chance


def simulateRecoveryVar(numNeeded, baseChance, list=0, cap=1):
    numHave = 0
    numTries = 0
    greatestFailChain = 0
    currentFail = 0
    capHits = 0
    attemptList = {}
    while numHave < numNeeded:
        numTries += 1
        chance = calcRecoverChance(currentFail, baseChance, cap)
        test = random.random() * 100
        if chance == 1000:
            capHits += 1
        if test < chance:
            numHave += 1
            if currentFail > greatestFailChain:
                greatestFailChain = currentFail
            if attemptList.get(currentFail):
                attemptList[currentFail] += 1
            else:
                attemptList[currentFail] = 1
            currentFail = 0
        else:
            currentFail += 1

    print(
        "Test results: %s tries, %s longest failure chain, %s cap hits"
        % (numTries, greatestFailChain, capHits)
    )
    if list:
        print("failures for each succes %s" % attemptList)


def simulateRecoveryFix(numNeeded, baseChance, list=0):
    numHave = 0
    numTries = 0
    greatestFailChain = 0
    currentFail = 0
    attemptList = {}
    while numHave < numNeeded:
        numTries += 1
        chance = baseChance
        test = random.random() * 100
        if test < chance:
            numHave += 1
            if currentFail > greatestFailChain:
                greatestFailChain = currentFail
            if attemptList.get(currentFail):
                attemptList[currentFail] += 1
            else:
                attemptList[currentFail] = 1
            currentFail = 0
        else:
            currentFail += 1

    print(
        "Test results: %s tries, %s longest failure chain"
        % (numTries, greatestFailChain)
    )
    if list:
        print("failures for each succes %s" % attemptList)


class Quest:
    _cogTracks = [Any, "c", "l", "m", "s"]
    _factoryTypes = [Any, FT_FullSuit, FT_Leg, FT_Arm, FT_Torso]

    def check(self, cond, msg):
        pass

    def checkLocation(self, location):
        locations = [Anywhere] + list(TTLocalizer.GlobalStreetNames.keys())
        self.check(location in locations, "invalid location: %s" % location)

    def checkNumCogs(self, num):
        self.check(1, "invalid number of cogs: %s" % num)

    def checkNewbieLevel(self, level):
        self.check(1, "invalid newbie level: %s" % level)

    def checkCogType(self, type):
        types = [Any] + list(SuitBattleGlobals.SuitAttributes.keys())
        self.check(type in types, "invalid cog type: %s" % type)

    def checkCogTrack(self, track):
        self.check(track in self._cogTracks, "invalid cog track: %s" % track)

    def checkCogLevel(self, level):
        self.check(level >= 1 and level <= 12, "invalid cog level: %s" % level)

    def checkNumSkelecogs(self, num):
        self.check(1, "invalid number of cogs: %s" % num)

    def checkSkelecogTrack(self, track):
        self.check(track in self._cogTracks, "invalid cog track: %s" % track)

    def checkSkelecogLevel(self, level):
        self.check(level >= 1 and level <= 12, "invalid cog level: %s" % level)

    def checkNumSkeleRevives(self, num):
        self.check(1, "invalid number of cogs: %s" % num)

    def checkNumForemen(self, num):
        self.check(num > 0, "invalid number of foremen: %s" % num)

    def checkNumVPs(self, num):
        self.check(num > 0, "invalid number of VPs: %s" % num)

    def checkNumSupervisors(self, num):
        self.check(num > 0, "invalid number of supervisors: %s" % num)

    def checkNumCFOs(self, num):
        self.check(num > 0, "invalid number of CFOs: %s" % num)

    def checkNumBuildings(self, num):
        self.check(1, "invalid num buildings: %s" % num)

    def checkBuildingTrack(self, track):
        self.check(track in self._cogTracks, "invalid building track: %s" % track)

    def checkBuildingFloors(self, floors):
        self.check(floors >= 1 and floors <= 5, "invalid num floors: %s" % floors)

    def checkNumFactories(self, num):
        self.check(1, "invalid num factories: %s" % num)

    def checkFactoryType(self, type):
        self.check(type in self._factoryTypes, "invalid factory type: %s" % type)

    def checkNumMints(self, num):
        self.check(1, "invalid num mints: %s" % num)

    def checkNumCogParts(self, num):
        self.check(1, "invalid num cog parts: %s" % num)

    def checkNumGags(self, num):
        self.check(1, "invalid num gags: %s" % num)

    def checkGagTrack(self, track):
        self.check(
            track >= ToontownBattleGlobals.MIN_TRACK_INDEX
            and track <= ToontownBattleGlobals.MAX_TRACK_INDEX,
            "invalid gag track: %s" % track,
        )

    def checkGagItem(self, item):
        self.check(
            item >= ToontownBattleGlobals.MIN_LEVEL_INDEX
            and item <= ToontownBattleGlobals.MAX_LEVEL_INDEX,
            "invalid gag item: %s" % item,
        )

    def checkDeliveryItem(self, item):
        self.check(item in ItemDict, "invalid delivery item: %s" % item)

    def checkNumItems(self, num):
        self.check(1, "invalid num items: %s" % num)

    def checkRecoveryItem(self, item):
        self.check(item in ItemDict, "invalid recovery item: %s" % item)

    def checkPercentChance(self, chance):
        self.check(chance > 0 and chance <= 100, "invalid percent chance: %s" % chance)

    def checkRecoveryItemHolderAndType(self, holder, holderType="type"):
        holderTypes = ["type", "level", "track"]
        self.check(
            holderType in holderTypes,
            "invalid recovery item holderType: %s" % holderType,
        )
        if holderType == "type":
            holders = [Any, AnyFish] + list(SuitBattleGlobals.SuitAttributes.keys())
            self.check(
                holder in holders,
                "invalid recovery item holder: %s for holderType: %s"
                % (holder, holderType),
            )
        elif holderType == "level":
            pass
        elif holderType == "track":
            self.check(
                holder in self._cogTracks,
                "invalid recovery item holder: %s for holderType: %s"
                % (holder, holderType),
            )

    def checkTrackChoice(self, option):
        self.check(
            option >= ToontownBattleGlobals.MIN_TRACK_INDEX
            and option <= ToontownBattleGlobals.MAX_TRACK_INDEX,
            "invalid track option: %s" % option,
        )

    def checkNumFriends(self, num):
        self.check(1, "invalid number of friends: %s" % num)

    def checkNumMinigames(self, num):
        self.check(1, "invalid number of minigames: %s" % num)

    def filterFunc(avatar):
        return 1

    filterFunc = staticmethod(filterFunc)

    def __init__(self, id, quest):
        self.id = id
        self.quest = quest

    def getId(self):
        return self.id

    def getType(self):
        return self.__class__

    def getObjectiveStrings(self):
        return [""]

    def getString(self):
        return self.getObjectiveStrings()[0]

    def getRewardString(self, progressString):
        return self.getString() + " : " + progressString

    def getChooseString(self):
        return self.getString()

    def getPosterString(self):
        return self.getString()

    def getHeadlineString(self):
        return self.getString()

    def getDefaultQuestDialog(self):
        return self.getString() + TTLocalizer.Period

    def getNumQuestItems(self):
        return -1

    def addArticle(self, num, oString):
        if len(oString) == 0:
            return oString
        if num == 1:
            return oString
        else:
            return "%d %s" % (num, oString)

    def __repr__(self):
        return "Quest type: %s id: %s params: %s" % (
            self.__class__.__name__,
            self.id,
            self.quest[0:],
        )

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return 0

    def doesVPCount(self, avId, cogDict, zoneId, avList):
        return 0

    def doesCFOCount(self, avId, cogDict, zoneId, avList):
        return 0

    def doesFactoryCount(self, avId, location, avList):
        return 0

    def doesMintCount(self, avId, location, avList):
        return 0

    def doesCogPartCount(self, avId, location, avList):
        return 0

    def getCompletionStatus(self, av, questDesc, npc=None):
        notify.error("Pure virtual - please override me")
        return None


class LocationBasedQuest(Quest):
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)
        self.checkLocation(self.quest[0])

    def getLocation(self):
        return self.quest[0]

    def getLocationName(self):
        loc = self.getLocation()
        if loc == Anywhere:
            locName = ""
        elif loc in ToontownGlobals.hoodNameMap:
            locName = TTLocalizer.QuestInLocationString % {
                "inPhrase": ToontownGlobals.hoodNameMap[loc][1],
                "location": ToontownGlobals.hoodNameMap[loc][-1]
                + TTLocalizer.QuestsLocationArticle,
            }
        elif loc in ToontownGlobals.StreetBranchZones:
            locName = TTLocalizer.QuestInLocationString % {
                "inPhrase": ToontownGlobals.StreetNames[loc][1],
                "location": ToontownGlobals.StreetNames[loc][-1]
                + TTLocalizer.QuestsLocationArticle,
            }
        return locName

    def isLocationMatch(self, zoneId):
        loc = self.getLocation()
        if loc is Anywhere:
            return 1
        if ZoneUtil.isPlayground(loc):
            if loc == ZoneUtil.getCanonicalHoodId(zoneId):
                return 1
            else:
                return 0
        elif loc == ZoneUtil.getCanonicalBranchZone(zoneId):
            return 1
        elif loc == zoneId:
            return 1
        else:
            return 0

    def getChooseString(self):
        return TTLocalizer.QuestsLocationString % {
            "string": self.getString(),
            "location": self.getLocationName(),
        }

    def getPosterString(self):
        return TTLocalizer.QuestsLocationString % {
            "string": self.getString(),
            "location": self.getLocationName(),
        }

    def getDefaultQuestDialog(self):
        return (TTLocalizer.QuestsLocationString + TTLocalizer.Period) % {
            "string": self.getString(),
            "location": self.getLocationName(),
        }


class NewbieQuest:
    def getNewbieLevel(self):
        notify.error("Pure virtual - please override me")

    def getString(
        self,
        newStr=TTLocalizer.QuestsCogNewNewbieQuestObjective,
        oldStr=TTLocalizer.QuestsCogOldNewbieQuestObjective,
    ):
        laff = self.getNewbieLevel()
        if laff <= NEWBIE_HP:
            return newStr % self.getObjectiveStrings()[0]
        else:
            return oldStr % {
                "laffPoints": laff,
                "objective": self.getObjectiveStrings()[0],
            }

    def getCaption(self):
        laff = self.getNewbieLevel()
        if laff <= NEWBIE_HP:
            return TTLocalizer.QuestsCogNewNewbieQuestCaption % laff
        else:
            return TTLocalizer.QuestsCogOldNewbieQuestCaption % laff

    def getNumNewbies(self, avId, avList):
        newbieHp = self.getNewbieLevel()
        num = 0
        for av in avList:
            if av.getDoId() != avId and av.getMaxHp() <= newbieHp:
                num += 1

        return num


class CogQuest(LocationBasedQuest):
    def __init__(self, id, quest):
        LocationBasedQuest.__init__(self, id, quest)
        if self.__class__ == CogQuest:
            self.checkNumCogs(self.quest[1])
            self.checkCogType(self.quest[2])

    def getCogType(self):
        return self.quest[2]

    def getNumQuestItems(self):
        return self.getNumCogs()

    def getNumCogs(self):
        return self.quest[1]

    def getCompletionStatus(self, av, questDesc, npc=None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= self.getNumCogs()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumCogs() == 1:
            return ""
        else:
            return TTLocalizer.QuestsCogQuestProgress % {
                "progress": questDesc[4],
                "numCogs": self.getNumCogs(),
            }

    def getCogNameString(self):
        numCogs = self.getNumCogs()
        cogType = self.getCogType()
        if numCogs == 1:
            if cogType == Any:
                return TTLocalizer.Cog
            else:
                return SuitBattleGlobals.SuitAttributes[cogType]["singularname"]
        elif cogType == Any:
            return TTLocalizer.Cogs
        else:
            return SuitBattleGlobals.SuitAttributes[cogType]["pluralname"]

    def getObjectiveStrings(self):
        cogName = self.getCogNameString()
        numCogs = self.getNumCogs()
        if numCogs == 1:
            text = cogName
        else:
            text = TTLocalizer.QuestsCogQuestDefeatDesc % {
                "numCogs": numCogs,
                "cogName": cogName,
            }
        return (text,)

    def getString(self):
        return TTLocalizer.QuestsCogQuestDefeat % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumCogs():
            return getFinishToonTaskSCStrings(toNpcId)
        cogName = self.getCogNameString()
        numCogs = self.getNumCogs()
        if numCogs == 1:
            text = TTLocalizer.QuestsCogQuestSCStringS
        else:
            text = TTLocalizer.QuestsCogQuestSCStringP
        cogLoc = self.getLocationName()
        return text % {"cogName": cogName, "cogLoc": cogLoc}

    def getHeadlineString(self):
        return TTLocalizer.QuestsCogQuestHeadline

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        questCogType = self.getCogType()
        return (
            (questCogType is Any or questCogType is cogDict["type"])
            and avId in cogDict["activeToons"]
            and self.isLocationMatch(zoneId)
        )


class CogNewbieQuest(CogQuest, NewbieQuest):
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        if self.__class__ == CogNewbieQuest:
            self.checkNumCogs(self.quest[1])
            self.checkCogType(self.quest[2])
            self.checkNewbieLevel(self.quest[3])

    def getNewbieLevel(self):
        return self.quest[3]

    def getString(self):
        return NewbieQuest.getString(self)

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        if CogQuest.doesCogCount(self, avId, cogDict, zoneId, avList):
            return self.getNumNewbies(avId, avList)
        else:
            return 0


class CogTrackQuest(CogQuest):
    trackCodes = ["c", "l", "m", "s"]
    trackNamesS = [
        TTLocalizer.BossbotS,
        TTLocalizer.LawbotS,
        TTLocalizer.CashbotS,
        TTLocalizer.SellbotS,
    ]
    trackNamesP = [
        TTLocalizer.BossbotP,
        TTLocalizer.LawbotP,
        TTLocalizer.CashbotP,
        TTLocalizer.SellbotP,
    ]

    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        if self.__class__ == CogTrackQuest:
            self.checkNumCogs(self.quest[1])
            self.checkCogTrack(self.quest[2])

    def getCogTrack(self):
        return self.quest[2]

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumCogs() == 1:
            return ""
        else:
            return TTLocalizer.QuestsCogTrackQuestProgress % {
                "progress": questDesc[4],
                "numCogs": self.getNumCogs(),
            }

    def getObjectiveStrings(self):
        numCogs = self.getNumCogs()
        track = self.trackCodes.index(self.getCogTrack())
        if numCogs == 1:
            text = self.trackNamesS[track]
        else:
            text = TTLocalizer.QuestsCogTrackDefeatDesc % {
                "numCogs": numCogs,
                "trackName": self.trackNamesP[track],
            }
        return (text,)

    def getString(self):
        return TTLocalizer.QuestsCogTrackQuestDefeat % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumCogs():
            return getFinishToonTaskSCStrings(toNpcId)
        numCogs = self.getNumCogs()
        track = self.trackCodes.index(self.getCogTrack())
        if numCogs == 1:
            cogText = self.trackNamesS[track]
            text = TTLocalizer.QuestsCogTrackQuestSCStringS
        else:
            cogText = self.trackNamesP[track]
            text = TTLocalizer.QuestsCogTrackQuestSCStringP
        cogLocName = self.getLocationName()
        return text % {"cogText": cogText, "cogLoc": cogLocName}

    def getHeadlineString(self):
        return TTLocalizer.QuestsCogTrackQuestHeadline

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        questCogTrack = self.getCogTrack()
        return (
            questCogTrack == cogDict["track"]
            and avId in cogDict["activeToons"]
            and self.isLocationMatch(zoneId)
        )


class CogLevelQuest(CogQuest):
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumCogs(self.quest[1])
        self.checkCogLevel(self.quest[2])

    def getCogType(self):
        return Any

    def getCogLevel(self):
        return self.quest[2]

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumCogs() == 1:
            return ""
        else:
            return TTLocalizer.QuestsCogLevelQuestProgress % {
                "progress": questDesc[4],
                "numCogs": self.getNumCogs(),
            }

    def getObjectiveStrings(self):
        count = self.getNumCogs()
        level = self.getCogLevel()
        name = self.getCogNameString()
        if count == 1:
            text = TTLocalizer.QuestsCogLevelQuestDesc
        else:
            text = TTLocalizer.QuestsCogLevelQuestDescC
        return (text % {"count": count, "level": level, "name": name},)

    def getString(self):
        return TTLocalizer.QuestsCogLevelQuestDefeat % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumCogs():
            return getFinishToonTaskSCStrings(toNpcId)
        count = self.getNumCogs()
        level = self.getCogLevel()
        name = self.getCogNameString()
        if count == 1:
            text = TTLocalizer.QuestsCogLevelQuestDesc
        else:
            text = TTLocalizer.QuestsCogLevelQuestDescI
        objective = text % {"level": level, "name": name}
        location = self.getLocationName()
        return TTLocalizer.QuestsCogLevelQuestSCString % {
            "objective": objective,
            "location": location,
        }

    def getHeadlineString(self):
        return TTLocalizer.QuestsCogLevelQuestHeadline

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        questCogLevel = self.getCogLevel()
        return (
            questCogLevel <= cogDict["level"]
            and avId in cogDict["activeToons"]
            and self.isLocationMatch(zoneId)
        )


class SkelecogQBase:
    def getCogNameString(self):
        numCogs = self.getNumCogs()
        if numCogs == 1:
            return TTLocalizer.ASkeleton
        else:
            return TTLocalizer.SkeletonP

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return (
            cogDict["isSkelecog"]
            and avId in cogDict["activeToons"]
            and self.isLocationMatch(zoneId)
        )


class SkelecogQuest(CogQuest, SkelecogQBase):
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumSkelecogs(self.quest[1])

    def getCogType(self):
        return Any

    def getCogNameString(self):
        return SkelecogQBase.getCogNameString(self)

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return SkelecogQBase.doesCogCount(self, avId, cogDict, zoneId, avList)


class SkelecogNewbieQuest(SkelecogQuest, NewbieQuest):
    def __init__(self, id, quest):
        SkelecogQuest.__init__(self, id, quest)
        self.checkNewbieLevel(self.quest[2])

    def getNewbieLevel(self):
        return self.quest[2]

    def getString(self):
        return NewbieQuest.getString(self)

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        if SkelecogQuest.doesCogCount(self, avId, cogDict, zoneId, avList):
            return self.getNumNewbies(avId, avList)
        else:
            return 0


class SkelecogTrackQuest(CogTrackQuest, SkelecogQBase):
    trackNamesS = [
        TTLocalizer.BossbotSkelS,
        TTLocalizer.LawbotSkelS,
        TTLocalizer.CashbotSkelS,
        TTLocalizer.SellbotSkelS,
    ]
    trackNamesP = [
        TTLocalizer.BossbotSkelP,
        TTLocalizer.LawbotSkelP,
        TTLocalizer.CashbotSkelP,
        TTLocalizer.SellbotSkelP,
    ]

    def __init__(self, id, quest):
        CogTrackQuest.__init__(self, id, quest)
        self.checkNumSkelecogs(self.quest[1])
        self.checkSkelecogTrack(self.quest[2])

    def getCogNameString(self):
        return SkelecogQBase.getCogNameString(self)

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return (
            SkelecogQBase.doesCogCount(self, avId, cogDict, zoneId, avList)
            and self.getCogTrack() == cogDict["track"]
        )


class SkelecogLevelQuest(CogLevelQuest, SkelecogQBase):
    def __init__(self, id, quest):
        CogLevelQuest.__init__(self, id, quest)
        self.checkNumSkelecogs(self.quest[1])
        self.checkSkelecogLevel(self.quest[2])

    def getCogType(self):
        return Any

    def getCogNameString(self):
        return SkelecogQBase.getCogNameString(self)

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return (
            SkelecogQBase.doesCogCount(self, avId, cogDict, zoneId, avList)
            and self.getCogLevel() <= cogDict["level"]
        )


class SkeleReviveQBase:
    def getCogNameString(self):
        numCogs = self.getNumCogs()
        if numCogs == 1:
            return TTLocalizer.Av2Cog
        else:
            return TTLocalizer.v2CogP

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return (
            cogDict["hasRevives"]
            and avId in cogDict["activeToons"]
            and self.isLocationMatch(zoneId)
        )


class SkeleReviveQuest(CogQuest, SkeleReviveQBase):
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumSkeleRevives(self.quest[1])

    def getCogType(self):
        return Any

    def getCogNameString(self):
        return SkeleReviveQBase.getCogNameString(self)

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return SkeleReviveQBase.doesCogCount(self, avId, cogDict, zoneId, avList)


class ForemanQuest(CogQuest):
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumForemen(self.quest[1])

    def getCogType(self):
        return Any

    def getCogNameString(self):
        numCogs = self.getNumCogs()
        if numCogs == 1:
            return TTLocalizer.AForeman
        else:
            return TTLocalizer.ForemanP

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return bool(
            CogQuest.doesCogCount(self, avId, cogDict, zoneId, avList)
            and cogDict["isForeman"]
        )


class ForemanNewbieQuest(ForemanQuest, NewbieQuest):
    def __init__(self, id, quest):
        ForemanQuest.__init__(self, id, quest)
        self.checkNewbieLevel(self.quest[2])

    def getNewbieLevel(self):
        return self.quest[2]

    def getString(self):
        return NewbieQuest.getString(self)

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        if ForemanQuest.doesCogCount(self, avId, cogDict, zoneId, avList):
            return self.getNumNewbies(avId, avList)
        else:
            return 0


class VPQuest(CogQuest):
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumVPs(self.quest[1])

    def getCogType(self):
        return Any

    def getCogNameString(self):
        numCogs = self.getNumCogs()
        if numCogs == 1:
            return TTLocalizer.ACogVP
        else:
            return TTLocalizer.CogVPs

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return 0

    def doesVPCount(self, avId, cogDict, zoneId, avList):
        return self.isLocationMatch(zoneId)


class VPNewbieQuest(VPQuest, NewbieQuest):
    def __init__(self, id, quest):
        VPQuest.__init__(self, id, quest)
        self.checkNewbieLevel(self.quest[2])

    def getNewbieLevel(self):
        return self.quest[2]

    def getString(self):
        return NewbieQuest.getString(self)

    def doesVPCount(self, avId, cogDict, zoneId, avList):
        if VPQuest.doesVPCount(self, avId, cogDict, zoneId, avList):
            return self.getNumNewbies(avId, avList)
        else:
            return 0


class SupervisorQuest(CogQuest):
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumSupervisors(self.quest[1])

    def getCogType(self):
        return Any

    def getCogNameString(self):
        numCogs = self.getNumCogs()
        if numCogs == 1:
            return TTLocalizer.ASupervisor
        else:
            return TTLocalizer.SupervisorP

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return bool(
            CogQuest.doesCogCount(self, avId, cogDict, zoneId, avList)
            and cogDict["isSupervisor"]
        )


class SupervisorNewbieQuest(SupervisorQuest, NewbieQuest):
    def __init__(self, id, quest):
        SupervisorQuest.__init__(self, id, quest)
        self.checkNewbieLevel(self.quest[2])

    def getNewbieLevel(self):
        return self.quest[2]

    def getString(self):
        return NewbieQuest.getString(self)

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        if SupervisorQuest.doesCogCount(self, avId, cogDict, zoneId, avList):
            return self.getNumNewbies(avId, avList)
        else:
            return 0


class CFOQuest(CogQuest):
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumCFOs(self.quest[1])

    def getCogType(self):
        return Any

    def getCogNameString(self):
        numCogs = self.getNumCogs()
        if numCogs == 1:
            return TTLocalizer.ACogCFO
        else:
            return TTLocalizer.CogCFOs

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return 0

    def doesCFOCount(self, avId, cogDict, zoneId, avList):
        return self.isLocationMatch(zoneId)


class CFONewbieQuest(CFOQuest, NewbieQuest):
    def __init__(self, id, quest):
        CFOQuest.__init__(self, id, quest)
        self.checkNewbieLevel(self.quest[2])

    def getNewbieLevel(self):
        return self.quest[2]

    def getString(self):
        return NewbieQuest.getString(self)

    def doesCFOCount(self, avId, cogDict, zoneId, avList):
        if CFOQuest.doesCFOCount(self, avId, cogDict, zoneId, avList):
            return self.getNumNewbies(avId, avList)
        else:
            return 0


class RescueQuest(VPQuest):
    def __init__(self, id, quest):
        VPQuest.__init__(self, id, quest)

    def getNumToons(self):
        return self.getNumCogs()

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumToons() == 1:
            return ""
        else:
            return TTLocalizer.QuestsRescueQuestProgress % {
                "progress": questDesc[4],
                "numToons": self.getNumToons(),
            }

    def getObjectiveStrings(self):
        numToons = self.getNumCogs()
        if numToons == 1:
            text = TTLocalizer.QuestsRescueQuestToonS
        else:
            text = TTLocalizer.QuestsRescueQuestRescueDesc % {"numToons": numToons}
        return (text,)

    def getString(self):
        return TTLocalizer.QuestsRescueQuestRescue % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumToons():
            return getFinishToonTaskSCStrings(toNpcId)
        numToons = self.getNumToons()
        if numToons == 1:
            text = TTLocalizer.QuestsRescueQuestSCStringS
        else:
            text = TTLocalizer.QuestsRescueQuestSCStringP
        toonLoc = self.getLocationName()
        return text % {"toonLoc": toonLoc}

    def getHeadlineString(self):
        return TTLocalizer.QuestsRescueQuestHeadline


class RescueNewbieQuest(RescueQuest, NewbieQuest):
    def __init__(self, id, quest):
        RescueQuest.__init__(self, id, quest)
        self.checkNewbieLevel(self.quest[2])

    def getNewbieLevel(self):
        return self.quest[2]

    def getString(self):
        return NewbieQuest.getString(
            self,
            newStr=TTLocalizer.QuestsRescueNewNewbieQuestObjective,
            oldStr=TTLocalizer.QuestsRescueOldNewbieQuestObjective,
        )

    def doesVPCount(self, avId, cogDict, zoneId, avList):
        if RescueQuest.doesVPCount(self, avId, cogDict, zoneId, avList):
            return self.getNumNewbies(avId, avList)
        else:
            return 0


class BuildingQuest(CogQuest):
    trackCodes = ["c", "l", "m", "s"]
    trackNames = [
        TTLocalizer.Bossbot,
        TTLocalizer.Lawbot,
        TTLocalizer.Cashbot,
        TTLocalizer.Sellbot,
    ]

    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumBuildings(self.quest[1])
        self.checkBuildingTrack(self.quest[2])
        self.checkBuildingFloors(self.quest[3])

    def getNumFloors(self):
        return self.quest[3]

    def getBuildingTrack(self):
        return self.quest[2]

    def getNumQuestItems(self):
        return self.getNumBuildings()

    def getNumBuildings(self):
        return self.quest[1]

    def getCompletionStatus(self, av, questDesc, npc=None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= self.getNumBuildings()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumBuildings() == 1:
            return ""
        else:
            return TTLocalizer.QuestsBuildingQuestProgressString % {
                "progress": questDesc[4],
                "num": self.getNumBuildings(),
            }

    def getObjectiveStrings(self):
        count = self.getNumBuildings()
        floors = TTLocalizer.QuestsBuildingQuestFloorNumbers[self.getNumFloors() - 1]
        buildingTrack = self.getBuildingTrack()
        if buildingTrack == Any:
            type = TTLocalizer.Cog
        else:
            type = self.trackNames[self.trackCodes.index(buildingTrack)]
        if count == 1:
            if floors == "":
                text = TTLocalizer.QuestsBuildingQuestDesc
            else:
                text = TTLocalizer.QuestsBuildingQuestDescF
        elif floors == "":
            text = TTLocalizer.QuestsBuildingQuestDescC
        else:
            text = TTLocalizer.QuestsBuildingQuestDescCF
        return (text % {"count": count, "floors": floors, "type": type},)

    def getString(self):
        return TTLocalizer.QuestsBuildingQuestString % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumBuildings():
            return getFinishToonTaskSCStrings(toNpcId)
        count = self.getNumBuildings()
        floors = TTLocalizer.QuestsBuildingQuestFloorNumbers[self.getNumFloors() - 1]
        buildingTrack = self.getBuildingTrack()
        if buildingTrack == Any:
            type = TTLocalizer.Cog
        else:
            type = self.trackNames[self.trackCodes.index(buildingTrack)]
        if count == 1:
            if floors == "":
                text = TTLocalizer.QuestsBuildingQuestDesc
            else:
                text = TTLocalizer.QuestsBuildingQuestDescF
        elif floors == "":
            text = TTLocalizer.QuestsBuildingQuestDescI
        else:
            text = TTLocalizer.QuestsBuildingQuestDescIF
        objective = text % {"floors": floors, "type": type}
        location = self.getLocationName()
        return TTLocalizer.QuestsBuildingQuestSCString % {
            "objective": objective,
            "location": location,
        }

    def getHeadlineString(self):
        return TTLocalizer.QuestsBuildingQuestHeadline

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return 0

    def doesBuildingCount(self, avId, avList):
        return 1


class BuildingNewbieQuest(BuildingQuest, NewbieQuest):
    def __init__(self, id, quest):
        BuildingQuest.__init__(self, id, quest)
        self.checkNewbieLevel(self.quest[4])

    def getNewbieLevel(self):
        return self.quest[4]

    def getString(self):
        return NewbieQuest.getString(self)

    def getHeadlineString(self):
        return TTLocalizer.QuestsNewbieQuestHeadline

    def doesBuildingCount(self, avId, avList):
        return self.getNumNewbies(avId, avList)


class FactoryQuest(LocationBasedQuest):
    factoryTypeNames = {
        FT_FullSuit: TTLocalizer.Cog,
        FT_Leg: TTLocalizer.FactoryTypeLeg,
        FT_Arm: TTLocalizer.FactoryTypeArm,
        FT_Torso: TTLocalizer.FactoryTypeTorso,
    }

    def __init__(self, id, quest):
        LocationBasedQuest.__init__(self, id, quest)
        self.checkNumFactories(self.quest[1])

    def getNumQuestItems(self):
        return self.getNumFactories()

    def getNumFactories(self):
        return self.quest[1]

    def getFactoryType(self):
        loc = self.getLocation()
        type = Any
        if loc in ToontownGlobals.factoryId2factoryType:
            type = ToontownGlobals.factoryId2factoryType[loc]
        return type

    def getCompletionStatus(self, av, questDesc, npc=None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= self.getNumFactories()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumFactories() == 1:
            return ""
        else:
            return TTLocalizer.QuestsFactoryQuestProgressString % {
                "progress": questDesc[4],
                "num": self.getNumFactories(),
            }

    def getObjectiveStrings(self):
        count = self.getNumFactories()
        factoryType = self.getFactoryType()
        if factoryType == Any:
            type = TTLocalizer.Cog
        else:
            type = FactoryQuest.factoryTypeNames[factoryType]
        if count == 1:
            text = TTLocalizer.QuestsFactoryQuestDesc
        else:
            text = TTLocalizer.QuestsFactoryQuestDescC
        return (text % {"count": count, "type": type},)

    def getString(self):
        return TTLocalizer.QuestsFactoryQuestString % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumFactories():
            return getFinishToonTaskSCStrings(toNpcId)
        factoryType = self.getFactoryType()
        if factoryType == Any:
            type = TTLocalizer.Cog
        else:
            type = FactoryQuest.factoryTypeNames[factoryType]
        count = self.getNumFactories()
        if count == 1:
            text = TTLocalizer.QuestsFactoryQuestDesc
        else:
            text = TTLocalizer.QuestsFactoryQuestDescI
        objective = text % {"type": type}
        location = self.getLocationName()
        return TTLocalizer.QuestsFactoryQuestSCString % {
            "objective": objective,
            "location": location,
        }

    def getHeadlineString(self):
        return TTLocalizer.QuestsFactoryQuestHeadline

    def doesFactoryCount(self, avId, location, avList):
        return self.isLocationMatch(location)


class FactoryNewbieQuest(FactoryQuest, NewbieQuest):
    def __init__(self, id, quest):
        FactoryQuest.__init__(self, id, quest)
        self.checkNewbieLevel(self.quest[2])

    def getNewbieLevel(self):
        return self.quest[2]

    def getString(self):
        return NewbieQuest.getString(self)

    def getHeadlineString(self):
        return TTLocalizer.QuestsNewbieQuestHeadline

    def doesFactoryCount(self, avId, location, avList):
        if FactoryQuest.doesFactoryCount(self, avId, location, avList):
            return self.getNumNewbies(avId, avList)
        else:
            return num


class MintQuest(LocationBasedQuest):
    def __init__(self, id, quest):
        LocationBasedQuest.__init__(self, id, quest)
        self.checkNumMints(self.quest[1])

    def getNumQuestItems(self):
        return self.getNumMints()

    def getNumMints(self):
        return self.quest[1]

    def getCompletionStatus(self, av, questDesc, npc=None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= self.getNumMints()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumMints() == 1:
            return ""
        else:
            return TTLocalizer.QuestsMintQuestProgressString % {
                "progress": questDesc[4],
                "num": self.getNumMints(),
            }

    def getObjectiveStrings(self):
        count = self.getNumMints()
        if count == 1:
            text = TTLocalizer.QuestsMintQuestDesc
        else:
            text = TTLocalizer.QuestsMintQuestDescC % {"count": count}
        return (text,)

    def getString(self):
        return TTLocalizer.QuestsMintQuestString % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumMints():
            return getFinishToonTaskSCStrings(toNpcId)
        count = self.getNumMints()
        if count == 1:
            objective = TTLocalizer.QuestsMintQuestDesc
        else:
            objective = TTLocalizer.QuestsMintQuestDescI
        location = self.getLocationName()
        return TTLocalizer.QuestsMintQuestSCString % {
            "objective": objective,
            "location": location,
        }

    def getHeadlineString(self):
        return TTLocalizer.QuestsMintQuestHeadline

    def doesMintCount(self, avId, location, avList):
        return self.isLocationMatch(location)


class MintNewbieQuest(MintQuest, NewbieQuest):
    def __init__(self, id, quest):
        MintQuest.__init__(self, id, quest)
        self.checkNewbieLevel(self.quest[2])

    def getNewbieLevel(self):
        return self.quest[2]

    def getString(self):
        return NewbieQuest.getString(self)

    def getHeadlineString(self):
        return TTLocalizer.QuestsNewbieQuestHeadline

    def doesMintCount(self, avId, location, avList):
        if MintQuest.doesMintCount(self, avId, location, avList):
            return self.getNumNewbies(avId, avList)
        else:
            return num


class CogPartQuest(LocationBasedQuest):
    def __init__(self, id, quest):
        LocationBasedQuest.__init__(self, id, quest)
        self.checkNumCogParts(self.quest[1])

    def getNumQuestItems(self):
        return self.getNumParts()

    def getNumParts(self):
        return self.quest[1]

    def getCompletionStatus(self, av, questDesc, npc=None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= self.getNumParts()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumParts() == 1:
            return ""
        else:
            return TTLocalizer.QuestsCogPartQuestProgressString % {
                "progress": questDesc[4],
                "num": self.getNumParts(),
            }

    def getObjectiveStrings(self):
        count = self.getNumParts()
        if count == 1:
            text = TTLocalizer.QuestsCogPartQuestDesc
        else:
            text = TTLocalizer.QuestsCogPartQuestDescC
        return (text % {"count": count},)

    def getString(self):
        return TTLocalizer.QuestsCogPartQuestString % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumParts():
            return getFinishToonTaskSCStrings(toNpcId)
        count = self.getNumParts()
        if count == 1:
            text = TTLocalizer.QuestsCogPartQuestDesc
        else:
            text = TTLocalizer.QuestsCogPartQuestDescI
        objective = text
        location = self.getLocationName()
        return TTLocalizer.QuestsCogPartQuestSCString % {
            "objective": objective,
            "location": location,
        }

    def getHeadlineString(self):
        return TTLocalizer.QuestsCogPartQuestHeadline

    def doesCogPartCount(self, avId, location, avList):
        return self.isLocationMatch(location)


class CogPartNewbieQuest(CogPartQuest, NewbieQuest):
    def __init__(self, id, quest):
        CogPartQuest.__init__(self, id, quest)
        self.checkNewbieLevel(self.quest[2])

    def getNewbieLevel(self):
        return self.quest[2]

    def getString(self):
        return NewbieQuest.getString(
            self,
            newStr=TTLocalizer.QuestsCogPartNewNewbieQuestObjective,
            oldStr=TTLocalizer.QuestsCogPartOldNewbieQuestObjective,
        )

    def getHeadlineString(self):
        return TTLocalizer.QuestsNewbieQuestHeadline

    def doesCogPartCount(self, avId, location, avList):
        if CogPartQuest.doesCogPartCount(self, avId, location, avList):
            return self.getNumNewbies(avId, avList)
        else:
            return num


class DeliverGagQuest(Quest):
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)
        self.checkNumGags(self.quest[0])
        self.checkGagTrack(self.quest[1])
        self.checkGagItem(self.quest[2])

    def getGagType(self):
        return (self.quest[1], self.quest[2])

    def getNumQuestItems(self):
        return self.getNumGags()

    def getNumGags(self):
        return self.quest[0]

    def getCompletionStatus(self, av, questDesc, npc=None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        gag = self.getGagType()
        num = self.getNumGags()
        track = gag[0]
        level = gag[1]
        questComplete = (
            npc and av.inventory and av.inventory.numItem(track, level) >= num
        )
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumGags() == 1:
            return ""
        else:
            return TTLocalizer.QuestsDeliverGagQuestProgress % {
                "progress": questDesc[4],
                "numGags": self.getNumGags(),
            }

    def getObjectiveStrings(self):
        track, item = self.getGagType()
        num = self.getNumGags()
        if num == 1:
            text = ToontownBattleGlobals.AvPropStringsSingular[track][item]
        else:
            gagName = ToontownBattleGlobals.AvPropStringsPlural[track][item]
            text = TTLocalizer.QuestsItemNameAndNum % {
                "num": TTLocalizer.getLocalNum(num),
                "name": gagName,
            }
        return (text,)

    def getString(self):
        return TTLocalizer.QuestsDeliverGagQuestString % self.getObjectiveStrings()[0]

    def getRewardString(self, progress):
        return (
            TTLocalizer.QuestsDeliverGagQuestStringLong % self.getObjectiveStrings()[0]
        )

    def getDefaultQuestDialog(self):
        return (
            TTLocalizer.QuestsDeliverGagQuestStringLong % self.getObjectiveStrings()[0]
            + "\x07"
            + TTLocalizer.QuestsDeliverGagQuestInstructions
        )

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumGags():
            return getFinishToonTaskSCStrings(toNpcId)
        track, item = self.getGagType()
        num = self.getNumGags()
        if num == 1:
            text = TTLocalizer.QuestsDeliverGagQuestToSCStringS
            gagName = ToontownBattleGlobals.AvPropStringsSingular[track][item]
        else:
            text = TTLocalizer.QuestsDeliverGagQuestToSCStringP
            gagName = ToontownBattleGlobals.AvPropStringsPlural[track][item]
        return [
            text % {"gagName": gagName},
            TTLocalizer.QuestsDeliverGagQuestSCString,
        ] + getVisitSCStrings(toNpcId)

    def getHeadlineString(self):
        return TTLocalizer.QuestsDeliverGagQuestHeadline


class DeliverItemQuest(Quest):
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)
        self.checkDeliveryItem(self.quest[0])

    def getItem(self):
        return self.quest[0]

    def getCompletionStatus(self, av, questDesc, npc=None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        if npc and npcMatches(toNpcId, npc):
            return COMPLETE
        else:
            return INCOMPLETE_WRONG_NPC

    def getProgressString(self, avatar, questDesc):
        return TTLocalizer.QuestsDeliverItemQuestProgress

    def getObjectiveStrings(self):
        iDict = ItemDict[self.getItem()]
        article = iDict[2]
        itemName = iDict[0]
        return [article + itemName]

    def getString(self):
        return TTLocalizer.QuestsDeliverItemQuestString % self.getObjectiveStrings()[0]

    def getRewardString(self, progress):
        return (
            TTLocalizer.QuestsDeliverItemQuestStringLong % self.getObjectiveStrings()[0]
        )

    def getDefaultQuestDialog(self):
        return (
            TTLocalizer.QuestsDeliverItemQuestStringLong % self.getObjectiveStrings()[0]
        )

    def getSCStrings(self, toNpcId, progress):
        iDict = ItemDict[self.getItem()]
        article = iDict[2]
        itemName = iDict[0]
        return [
            TTLocalizer.QuestsDeliverItemQuestSCString
            % {"article": article, "itemName": itemName}
        ] + getVisitSCStrings(toNpcId)

    def getHeadlineString(self):
        return TTLocalizer.QuestsDeliverItemQuestHeadline


class VisitQuest(Quest):
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)

    def getCompletionStatus(self, av, questDesc, npc=None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        if npc and npcMatches(toNpcId, npc):
            return COMPLETE
        else:
            return INCOMPLETE_WRONG_NPC

    def getProgressString(self, avatar, questDesc):
        return TTLocalizer.QuestsVisitQuestProgress

    def getObjectiveStrings(self):
        return [""]

    def getString(self):
        return TTLocalizer.QuestsVisitQuestStringShort

    def getChooseString(self):
        return TTLocalizer.QuestsVisitQuestStringLong

    def getRewardString(self, progress):
        return TTLocalizer.QuestsVisitQuestStringLong

    def getDefaultQuestDialog(self):
        return random.choice(DefaultVisitQuestDialog)

    def getSCStrings(self, toNpcId, progress):
        return getVisitSCStrings(toNpcId)

    def getHeadlineString(self):
        return TTLocalizer.QuestsVisitQuestHeadline


class RecoverItemQuest(LocationBasedQuest):
    def __init__(self, id, quest):
        LocationBasedQuest.__init__(self, id, quest)
        self.checkNumItems(self.quest[1])
        self.checkRecoveryItem(self.quest[2])
        self.checkPercentChance(self.quest[3])
        if len(self.quest) > 5:
            self.checkRecoveryItemHolderAndType(self.quest[4], self.quest[5])
        else:
            self.checkRecoveryItemHolderAndType(self.quest[4])

    def testRecover(self, progress):
        test = random.random() * 100
        chance = self.getPercentChance()
        numberDone = progress & pow(2, 16) - 1
        numberNotDone = progress >> 16
        returnTest = None
        avgNum2Kill = 1.0 / (chance / 100.0)
        if numberNotDone >= avgNum2Kill * 1.5:
            chance = 100
        elif numberNotDone > avgNum2Kill * 0.5:
            diff = float(numberNotDone - avgNum2Kill * 0.5)
            luck = 1.0 + abs(diff / (avgNum2Kill * 0.5))
            chance *= luck
        if test <= chance:
            returnTest = 1
            numberNotDone = 0
            numberDone += 1
        else:
            returnTest = 0
            numberNotDone += 1
            numberDone += 0
        returnCount = numberNotDone << 16
        returnCount += numberDone
        return (returnTest, returnCount)

    def testDone(self, progress):
        numberDone = progress & pow(2, 16) - 1
        print("Quest number done %s" % numberDone)
        if numberDone >= self.getNumItems():
            return 1
        else:
            return 0

    def getNumQuestItems(self):
        return self.getNumItems()

    def getNumItems(self):
        return self.quest[1]

    def getItem(self):
        return self.quest[2]

    def getPercentChance(self):
        return self.quest[3]

    def getHolder(self):
        return self.quest[4]

    def getHolderType(self):
        if len(self.quest) == 5:
            return "type"
        else:
            return self.quest[5]

    def getCompletionStatus(self, av, questDesc, npc=None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        forwardProgress = toonProgress & pow(2, 16) - 1
        questComplete = forwardProgress >= self.getNumItems()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumItems() == 1:
            return ""
        else:
            progress = questDesc[4] & pow(2, 16) - 1
            return TTLocalizer.QuestsRecoverItemQuestProgress % {
                "progress": progress,
                "numItems": self.getNumItems(),
            }

    def getObjectiveStrings(self):
        holder = self.getHolder()
        holderType = self.getHolderType()
        if holder == Any:
            holderName = TTLocalizer.TheCogs
        elif holder == AnyFish:
            holderName = TTLocalizer.AFish
        elif holderType == "type":
            holderName = SuitBattleGlobals.SuitAttributes[holder]["pluralname"]
        elif holderType == "level":
            holderName = TTLocalizer.QuestsRecoverItemQuestHolderString % {
                "level": TTLocalizer.Level,
                "holder": holder,
                "cogs": TTLocalizer.Cogs,
            }
        elif holderType == "track":
            if holder == "c":
                holderName = TTLocalizer.BossbotP
            elif holder == "s":
                holderName = TTLocalizer.SellbotP
            elif holder == "m":
                holderName = TTLocalizer.CashbotP
            elif holder == "l":
                holderName = TTLocalizer.LawbotP
        item = self.getItem()
        num = self.getNumItems()
        if num == 1:
            itemName = ItemDict[item][2] + ItemDict[item][0]
        else:
            itemName = TTLocalizer.QuestsItemNameAndNum % {
                "num": TTLocalizer.getLocalNum(num),
                "name": ItemDict[item][1],
            }
        return [itemName, holderName]

    def getString(self):
        return TTLocalizer.QuestsRecoverItemQuestString % {
            "item": self.getObjectiveStrings()[0],
            "holder": self.getObjectiveStrings()[1],
        }

    def getSCStrings(self, toNpcId, progress):
        item = self.getItem()
        num = self.getNumItems()
        forwardProgress = progress & pow(2, 16) - 1
        if forwardProgress >= self.getNumItems():
            if num == 1:
                itemName = ItemDict[item][2] + ItemDict[item][0]
            else:
                itemName = TTLocalizer.QuestsItemNameAndNum % {
                    "num": TTLocalizer.getLocalNum(num),
                    "name": ItemDict[item][1],
                }
            if toNpcId == ToonHQ:
                strings = [
                    TTLocalizer.QuestsRecoverItemQuestReturnToHQSCString % itemName,
                    TTLocalizer.QuestsRecoverItemQuestGoToHQSCString,
                ]
            elif toNpcId:
                (
                    npcName,
                    hoodName,
                    buildingArticle,
                    buildingName,
                    toStreet,
                    streetName,
                    isInPlayground,
                ) = getNpcInfo(toNpcId)
                strings = [
                    TTLocalizer.QuestsRecoverItemQuestReturnToSCString
                    % {"item": itemName, "npcName": npcName}
                ]
                if isInPlayground:
                    strings.append(
                        TTLocalizer.QuestsRecoverItemQuestGoToPlaygroundSCString
                        % hoodName
                    )
                else:
                    strings.append(
                        TTLocalizer.QuestsRecoverItemQuestGoToStreetSCString
                        % {"to": toStreet, "street": streetName, "hood": hoodName}
                    )
                strings.extend(
                    [
                        TTLocalizer.QuestsRecoverItemQuestVisitBuildingSCString
                        % (buildingArticle, buildingName),
                        TTLocalizer.QuestsRecoverItemQuestWhereIsBuildingSCString
                        % (buildingArticle, buildingName),
                    ]
                )
            return strings
        holder = self.getHolder()
        holderType = self.getHolderType()
        locName = self.getLocationName()
        if holder == Any:
            holderName = TTLocalizer.TheCogs
        elif holder == AnyFish:
            holderName = TTLocalizer.TheFish
        elif holderType == "type":
            holderName = SuitBattleGlobals.SuitAttributes[holder]["pluralname"]
        elif holderType == "level":
            holderName = TTLocalizer.QuestsRecoverItemQuestHolderString % {
                "level": TTLocalizer.Level,
                "holder": holder,
                "cogs": TTLocalizer.Cogs,
            }
        elif holderType == "track":
            if holder == "c":
                holderName = TTLocalizer.BossbotP
            elif holder == "s":
                holderName = TTLocalizer.SellbotP
            elif holder == "m":
                holderName = TTLocalizer.CashbotP
            elif holder == "l":
                holderName = TTLocalizer.LawbotP
        if num == 1:
            itemName = ItemDict[item][2] + ItemDict[item][0]
        else:
            itemName = TTLocalizer.QuestsItemNameAndNum % {
                "num": TTLocalizer.getLocalNum(num),
                "name": ItemDict[item][1],
            }
        return TTLocalizer.QuestsRecoverItemQuestRecoverFromSCString % {
            "item": itemName,
            "holder": holderName,
            "loc": locName,
        }

    def getHeadlineString(self):
        return TTLocalizer.QuestsRecoverItemQuestHeadline


class TrackChoiceQuest(Quest):
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)
        self.checkTrackChoice(self.quest[0])
        self.checkTrackChoice(self.quest[1])

    def getChoices(self):
        return (self.quest[0], self.quest[1])

    def getCompletionStatus(self, av, questDesc, npc=None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        if npc and npcMatches(toNpcId, npc):
            return COMPLETE
        else:
            return INCOMPLETE_WRONG_NPC

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        else:
            return NotChosenString

    def getObjectiveStrings(self):
        trackA, trackB = self.getChoices()
        trackAName = ToontownBattleGlobals.Tracks[trackA].capitalize()
        trackBName = ToontownBattleGlobals.Tracks[trackB].capitalize()
        return [trackAName, trackBName]

    def getString(self):
        return TTLocalizer.QuestsTrackChoiceQuestString % {
            "trackA": self.getObjectiveStrings()[0],
            "trackB": self.getObjectiveStrings()[1],
        }

    def getSCStrings(self, toNpcId, progress):
        trackA, trackB = self.getChoices()
        trackAName = ToontownBattleGlobals.Tracks[trackA].capitalize()
        trackBName = ToontownBattleGlobals.Tracks[trackB].capitalize()
        return [
            TTLocalizer.QuestsTrackChoiceQuestSCString
            % {"trackA": trackAName, "trackB": trackBName},
            TTLocalizer.QuestsTrackChoiceQuestMaybeSCString % trackAName,
            TTLocalizer.QuestsTrackChoiceQuestMaybeSCString % trackBName,
        ] + getVisitSCStrings(toNpcId)

    def getHeadlineString(self):
        return TTLocalizer.QuestsTrackChoiceQuestHeadline


class FriendQuest(Quest):
    def filterFunc(avatar):
        if len(avatar.getFriendsList()) == 0:
            return 1
        else:
            return 0

    filterFunc = staticmethod(filterFunc)

    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)

    def getCompletionStatus(self, av, questDesc, npc=None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= 1 or len(av.getFriendsList()) > 0
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        else:
            return ""

    def getString(self):
        return TTLocalizer.QuestsFriendQuestString

    def getSCStrings(self, toNpcId, progress):
        if progress:
            return getFinishToonTaskSCStrings(toNpcId)
        return TTLocalizer.QuestsFriendQuestSCString

    def getHeadlineString(self):
        return TTLocalizer.QuestsFriendQuestHeadline

    def getObjectiveStrings(self):
        return [TTLocalizer.QuestsFriendQuestString]

    def doesFriendCount(self, av, otherAv):
        return 1


class FriendNewbieQuest(FriendQuest, NewbieQuest):
    def filterFunc(avatar):
        return 1

    filterFunc = staticmethod(filterFunc)

    def __init__(self, id, quest):
        FriendQuest.__init__(self, id, quest)
        self.checkNumFriends(self.quest[0])
        self.checkNewbieLevel(self.quest[1])

    def getNumQuestItems(self):
        return self.getNumFriends()

    def getNumFriends(self):
        return self.quest[0]

    def getNewbieLevel(self):
        return self.quest[1]

    def getCompletionStatus(self, av, questDesc, npc=None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= self.getNumFriends()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumFriends() == 1:
            return ""
        else:
            return TTLocalizer.QuestsFriendNewbieQuestProgress % {
                "progress": questDesc[4],
                "numFriends": self.getNumFriends(),
            }

    def getString(self):
        return TTLocalizer.QuestsFriendNewbieQuestObjective % self.getNumFriends()

    def getObjectiveStrings(self):
        return [
            TTLocalizer.QuestsFriendNewbieQuestString
            % (self.getNumFriends(), self.getNewbieLevel())
        ]

    def doesFriendCount(self, av, otherAv):
        if otherAv != None and otherAv.getMaxHp() <= self.getNewbieLevel():
            return 1
        return 0


class TrolleyQuest(Quest):
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)

    def getCompletionStatus(self, av, questDesc, npc=None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= 1
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        else:
            return ""

    def getString(self):
        return TTLocalizer.QuestsFriendQuestString

    def getSCStrings(self, toNpcId, progress):
        if progress:
            return getFinishToonTaskSCStrings(toNpcId)
        return TTLocalizer.QuestsTrolleyQuestSCString

    def getHeadlineString(self):
        return TTLocalizer.QuestsTrolleyQuestHeadline

    def getObjectiveStrings(self):
        return [TTLocalizer.QuestsTrolleyQuestString]


class MailboxQuest(Quest):
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)

    def getCompletionStatus(self, av, questDesc, npc=None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= 1
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        else:
            return ""

    def getString(self):
        return TTLocalizer.QuestsMailboxQuestString

    def getSCStrings(self, toNpcId, progress):
        if progress:
            return getFinishToonTaskSCStrings(toNpcId)
        return TTLocalizer.QuestsMailboxQuestSCString

    def getHeadlineString(self):
        return TTLocalizer.QuestsMailboxQuestHeadline

    def getObjectiveStrings(self):
        return [TTLocalizer.QuestsMailboxQuestString]


class PhoneQuest(Quest):
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)

    def getCompletionStatus(self, av, questDesc, npc=None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= 1
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        else:
            return ""

    def getString(self):
        return TTLocalizer.QuestsPhoneQuestString

    def getSCStrings(self, toNpcId, progress):
        if progress:
            return getFinishToonTaskSCStrings(toNpcId)
        return TTLocalizer.QuestsPhoneQuestSCString

    def getHeadlineString(self):
        return TTLocalizer.QuestsPhoneQuestHeadline

    def getObjectiveStrings(self):
        return [TTLocalizer.QuestsPhoneQuestString]


class MinigameNewbieQuest(Quest, NewbieQuest):
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)
        self.checkNumMinigames(self.quest[0])
        self.checkNewbieLevel(self.quest[1])

    def getNumQuestItems(self):
        return self.getNumMinigames()

    def getNumMinigames(self):
        return self.quest[0]

    def getNewbieLevel(self):
        return self.quest[1]

    def getCompletionStatus(self, av, questDesc, npc=None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= self.getNumMinigames()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumMinigames() == 1:
            return ""
        else:
            return TTLocalizer.QuestsMinigameNewbieQuestProgress % {
                "progress": questDesc[4],
                "numMinigames": self.getNumMinigames(),
            }

    def getString(self):
        return TTLocalizer.QuestsMinigameNewbieQuestObjective % self.getNumMinigames()

    def getObjectiveStrings(self):
        return [TTLocalizer.QuestsMinigameNewbieQuestString % self.getNumMinigames()]

    def getHeadlineString(self):
        return TTLocalizer.QuestsNewbieQuestHeadline

    def getSCStrings(self, toNpcId, progress):
        if progress:
            return getFinishToonTaskSCStrings(toNpcId)
        return TTLocalizer.QuestsTrolleyQuestSCString

    def doesMinigameCount(self, av, avList):
        newbieHp = self.getNewbieLevel()
        points = 0
        for toon in avList:
            if toon != av and toon.getMaxHp() <= newbieHp:
                points += 1

        return points


DefaultDialog = {
    GREETING: DefaultGreeting,
    QUEST: DefaultQuest,
    INCOMPLETE: DefaultIncomplete,
    INCOMPLETE_PROGRESS: DefaultIncompleteProgress,
    INCOMPLETE_WRONG_NPC: DefaultIncompleteWrongNPC,
    COMPLETE: DefaultComplete,
    LEAVING: DefaultLeaving,
}


def getQuestFromNpcId(id):
    return QuestDict.get(id)[QuestDictFromNpcIndex]


def getQuestToNpcId(id):
    return QuestDict.get(id)[QuestDictToNpcIndex]


def getQuestDialog(id):
    return QuestDict.get(id)[QuestDictDialogIndex]


def getQuestReward(id, av):
    baseRewardId = QuestDict.get(id)[QuestDictRewardIndex]
    return transformReward(baseRewardId, av)


def isQuestJustForFun(questId, rewardId):
    questEntry = QuestDict.get(questId)
    if questEntry:
        tier = questEntry[QuestDictTierIndex]
        return isRewardOptional(tier, rewardId)
    else:
        return False


NoRewardTierZeroQuests = (101, 110, 121, 131, 141, 145, 150, 160, 161, 162, 163)
RewardTierZeroQuests = ()
PreClarabelleQuestIds = NoRewardTierZeroQuests + RewardTierZeroQuests
QuestDict = {
    # Task 1: Grand Toontorial
    # Reward: +1 Laff (max 16)
    101: (
        TT_TIER,
        Start,
        (CogQuest, Anywhere, 1, "f"),
        Any,
        ToonHQ,
        NA,
        110,
        DefaultDialog,
    ),
    110: (
        TT_TIER,
        Cont,
        (
            RecoverItemQuest,
            ToontownGlobals.ToonIslandCentral,
            1,
            20,
            VeryEasy,
            Any,
            "type",
        ),
        ToonHQ,
        ToonHQ,
        NA,
        111,
        DefaultDialog,
    ),
    # Note: because estates are broken, the below task can not be completed,
    # so we skip it for now. TODO: Reenable task when estates are fixed.
    111: (
        TT_TIER,
        Cont,
        (VisitQuest,),
        Same,
        ToonHQ,
        100,
        112,
        TTLocalizer.QuestDialogDict[111],
    ),
    112: (
        TT_TIER,
        Cont,
        (VisitQuest,),
        Same,
        2005,
        NA,
        113,
        TTLocalizer.QuestDialogDict[112],
    ),
    113: (
        TT_TIER,
        Cont,
        (VisitQuest,),
        Same,
        ToonHQ,
        NA,
        114,
        TTLocalizer.QuestDialogDict[113],
    ),
    114: (
        TT_TIER,
        Cont,
        (VisitQuest,),
        Same,
        ToonHQ,
        NA,
        115,
        TTLocalizer.QuestDialogDict[114],
    ),
    115: (
        TT_TIER,
        Cont,
        (CogQuest, ToontownGlobals.ToonIslandCentral, 3, Any),
        Any,
        ToonHQ,
        100,
        NA,
        TTLocalizer.QuestDialogDict[115],
    ),
    # Task 2: Decisions, Decisions
    # Reward: Gag Training (Toonup or Sound)
    120: (
        TT_TIER + 1,
        Start,
        (VisitQuest,),
        Any,
        2113,
        NA,
        121,
        TTLocalizer.QuestDialogDict[120],
    ),
    121: (
        TT_TIER + 1,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 19, Easy, Any, "l"),
        Any,
        2113,
        Any,
        400,
        TTLocalizer.QuestDialogDict[121],
    ),
    400: (
        TT_TIER + 1,
        Cont,
        (
            TrackChoiceQuest,
            ToontownBattleGlobals.SOUND_TRACK,
            ToontownBattleGlobals.HEAL_TRACK,
        ),
        Same,
        Same,
        400,
        NA,
        TTLocalizer.QuestDialogDict[400],
    ),
    # One Off Tasks: TTC
    1001: (
        TT_TIER + 2,
        Start,
        (CogQuest, ToontownGlobals.ToonIslandCentral, 3, Any),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1002: (
        TT_TIER + 2,
        Start,
        (CogQuest, ToontownGlobals.ToonIslandCentral, 4, Any),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1003: (
        TT_TIER + 2,
        Start,
        (CogQuest, ToontownGlobals.ToonIslandCentral, 5, Any),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1004: (
        TT_TIER + 2,
        Start,
        (CogQuest, ToontownGlobals.ToonIslandCentral, 6, Any),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1005: (
        TT_TIER + 2,
        Start,
        (CogQuest, Anywhere, 6, "f"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1006: (
        TT_TIER + 2,
        Start,
        (CogQuest, Anywhere, 6, "p"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1007: (
        TT_TIER + 2,
        Start,
        (CogQuest, Anywhere, 6, "bf"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1008: (
        TT_TIER + 2,
        Start,
        (CogQuest, Anywhere, 6, "b"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1009: (
        TT_TIER + 2,
        Start,
        (CogQuest, Anywhere, 4, "sc"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1010: (
        TT_TIER + 2,
        Start,
        (CogQuest, Anywhere, 4, "pp"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1011: (
        TT_TIER + 2,
        Start,
        (CogQuest, Anywhere, 4, "cc"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1012: (
        TT_TIER + 2,
        Start,
        (CogQuest, Anywhere, 4, "tm"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1013: (
        TT_TIER + 2,
        Start,
        (CogQuest, Anywhere, 5, "f"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1014: (
        TT_TIER + 2,
        Start,
        (CogQuest, Anywhere, 4, "p"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1015: (
        TT_TIER + 2,
        Start,
        (CogQuest, Anywhere, 4, "bf"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1016: (
        TT_TIER + 2,
        Start,
        (CogQuest, Anywhere, 4, "b"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1017: (
        TT_TIER + 2,
        Start,
        (CogQuest, Anywhere, 4, "ym"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1018: (
        TT_TIER + 2,
        Start,
        (CogQuest, Anywhere, 2, "nd"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1019: (
        TT_TIER + 2,
        Start,
        (CogQuest, Anywhere, 2, "tw"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1020: (
        TT_TIER + 2,
        Start,
        (CogQuest, Anywhere, 2, "dt"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1021: (
        TT_TIER + 2,
        Start,
        (CogLevelQuest, ToontownGlobals.ToonIslandCentral, 2, 2),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1022: (
        TT_TIER + 2,
        Start,
        (CogLevelQuest, ToontownGlobals.ToonIslandCentral, 6, 2),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1023: (
        TT_TIER + 2,
        Start,
        (CogLevelQuest, ToontownGlobals.ToonIslandCentral, 3, 2),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1024: (
        TT_TIER + 2,
        Start,
        (CogLevelQuest, ToontownGlobals.ToonIslandCentral, 4, 2),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1025: (
        TT_TIER + 2,
        Start,
        (CogLevelQuest, ToontownGlobals.ToonIslandCentral, 4, 3),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1026: (
        TT_TIER + 2,
        Start,
        (CogLevelQuest, ToontownGlobals.ToonIslandCentral, 6, 3),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1027: (
        TT_TIER + 2,
        Start,
        (CogTrackQuest, ToontownGlobals.ToonIslandCentral, 2, "m"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1028: (
        TT_TIER + 2,
        Start,
        (CogTrackQuest, ToontownGlobals.ToonIslandCentral, 2, "s"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1029: (
        TT_TIER + 2,
        Start,
        (CogTrackQuest, ToontownGlobals.ToonIslandCentral, 2, "c"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1030: (
        TT_TIER + 2,
        Start,
        (CogTrackQuest, ToontownGlobals.ToonIslandCentral, 2, "l"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1031: (
        TT_TIER + 2,
        Start,
        (CogTrackQuest, ToontownGlobals.ToonIslandCentral, 3, "m"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1032: (
        TT_TIER + 2,
        Start,
        (CogTrackQuest, ToontownGlobals.ToonIslandCentral, 3, "s"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1033: (
        TT_TIER + 2,
        Start,
        (CogTrackQuest, ToontownGlobals.ToonIslandCentral, 3, "c"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1034: (
        TT_TIER + 2,
        Start,
        (CogTrackQuest, ToontownGlobals.ToonIslandCentral, 3, "l"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1035: (
        TT_TIER + 2,
        Start,
        (CogTrackQuest, ToontownGlobals.ToonIslandCentral, 5, "m"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1036: (
        TT_TIER + 2,
        Start,
        (CogTrackQuest, ToontownGlobals.ToonIslandCentral, 5, "s"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1037: (
        TT_TIER + 2,
        Start,
        (CogTrackQuest, ToontownGlobals.ToonIslandCentral, 5, "c"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    1038: (
        TT_TIER + 2,
        Start,
        (CogTrackQuest, ToontownGlobals.ToonIslandCentral, 5, "l"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    # Task 3: Blue Goo that Sticks to You
    # Reward: +2 Laff (max 18)
    1039: (
        TT_TIER + 2,
        Start,
        (VisitQuest,),
        Any,
        2208,
        NA,
        1040,
        TTLocalizer.QuestDialogDict[1039],
    ),
    1040: (
        TT_TIER + 2,
        Cont,
        (VisitQuest,),
        Any,
        2403,
        NA,
        1041,
        TTLocalizer.QuestDialogDict[1040],
    ),
    1041: (
        TT_TIER + 2,
        Cont,
        (CogQuest, Any, 5, Any),
        Same,
        2403,
        NA,
        1042,
        TTLocalizer.QuestDialogDict[1041],
    ),
    1042: (
        TT_TIER + 2,
        Cont,
        (VisitQuest,),
        Any,
        2208,
        NA,
        1043,
        TTLocalizer.QuestDialogDict[1042],
    ),
    1043: (
        TT_TIER + 2,
        Cont,
        (VisitQuest,),
        Any,
        2315,
        NA,
        1044,
        TTLocalizer.QuestDialogDict[1043],
    ),
    1044: (
        TT_TIER + 2,
        Cont,
        (VisitQuest,),
        Any,
        2211,
        NA,
        1045,
        TTLocalizer.QuestDialogDict[1044],
    ),
    1045: (
        TT_TIER + 2,
        Cont,
        (CogQuest, Any, 7, Any),
        Same,
        Same,
        NA,
        1046,
        TTLocalizer.QuestDialogDict[1045],
    ),
    1046: (
        TT_TIER + 2,
        Cont,
        (VisitQuest,),
        Any,
        2208,
        101,
        NA,
        TTLocalizer.QuestDialogDict[1046],
    ),
    # Task 4: Cheating the Cheetah
    # Reward: +1 Laff (max 19)
    1047: (
        TT_TIER + 2,
        Start,
        (VisitQuest,),
        Any,
        2209,
        NA,
        1048,
        TTLocalizer.QuestDialogDict[1047],
    ),
    1048: (
        TT_TIER + 2,
        Cont,
        (CogTrackQuest, Anywhere, 7, "s"),
        Same,
        Same,
        NA,
        1049,
        TTLocalizer.QuestDialogDict[1048],
    ),
    1049: (
        TT_TIER + 2,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 18, Medium, AnyFish),
        2209,
        Same,
        NA,
        1050,
        TTLocalizer.QuestDialogDict[1049],
    ),
    1050: (
        TT_TIER + 2,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 17, Hard, "l", "track"),
        2209,
        Same,
        NA,
        1051,
        TTLocalizer.QuestDialogDict[1050],
    ),
    1051: (
        TT_TIER + 2,
        Cont,
        (VisitQuest,),
        Any,
        ToonHQ,
        NA,
        1052,
        TTLocalizer.QuestDialogDict[1051],
    ),
    1052: (
        TT_TIER + 2,
        Cont,
        (VisitQuest,),
        Any,
        2209,
        100,
        NA,
        TTLocalizer.QuestDialogDict[1052],
    ),
    # Task 5, Lean Mean Jellybean Machine | Yes its a Coach Z Evil Twin's Reference
    # Reward: Carry 50 Beans
    1053: (
        TT_TIER + 2,
        Start,
        (VisitQuest,),
        Any,
        2405,
        NA,
        1054,
        TTLocalizer.QuestDialogDict[1053],
    ),
    1054: (
        TT_TIER + 2,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 16, Hard, Any, "track"),
        2209,
        Same,
        NA,
        1055,
        TTLocalizer.QuestDialogDict[1054],
    ),
    1055: (
        TT_TIER + 2,
        Cont,
        (VisitQuest,),
        Any,
        2221,
        NA,
        1056,
        TTLocalizer.QuestDialogDict[1055],
    ),
    1056: (
        TT_TIER + 2,
        Cont,
        (CogQuest, Any, 10, Any),
        Same,
        2221,
        NA,
        1057,
        TTLocalizer.QuestDialogDict[1056],
    ),
    1057: (
        TT_TIER + 2,
        Cont,
        (VisitQuest,),
        Any,
        2405,
        700,
        NA,
        TTLocalizer.QuestDialogDict[1057],
    ),
    # Task 6: Something Sus-swiss-cious
    # Reward: +3 Laff (max laff 22)
    1058: (
        TT_TIER + 2,
        Start,
        (VisitQuest,),
        Any,
        2312,
        NA,
        1059,
        TTLocalizer.QuestDialogDict[1058],
    ),
    1059: (
        TT_TIER + 2,
        Cont,
        (RecoverItemQuest, Anywhere, 5, 15, Medium, "tm"),
        Same,
        Same,
        NA,
        1060,
        TTLocalizer.QuestDialogDict[1059],
    ),
    1060: (
        TT_TIER + 2,
        Cont,
        (RecoverItemQuest, Anywhere, 3, 14, Medium, "ym"),
        Same,
        Same,
        NA,
        1061,
        TTLocalizer.QuestDialogDict[1060],
    ),
    1061: (
        TT_TIER + 2,
        Cont,
        (VisitQuest,),
        Any,
        2138,
        NA,
        1062,
        TTLocalizer.QuestDialogDict[1061],
    ),
    1062: (
        TT_TIER + 2,
        Cont,
        (RecoverItemQuest, Anywhere, 5, 13, Medium, Any, "track"),
        Same,
        Same,
        NA,
        1063,
        TTLocalizer.QuestDialogDict[1062],
    ),
    1063: (
        TT_TIER + 2,
        Cont,
        (CogQuest, Any, 10, Any),
        Same,
        2138,
        NA,
        1064,
        TTLocalizer.QuestDialogDict[1063],
    ),
    1064: (
        TT_TIER + 2,
        Cont,
        (VisitQuest,),
        Any,
        2312,
        102,
        NA,
        TTLocalizer.QuestDialogDict[1064],
    ),
    # Task 7: Melodious Mathematical Mayhem
    # Reward: +1 Laff (max laff 23)
    1065: (
        TT_TIER + 2,
        Start,
        (VisitQuest,),
        Any,
        2103,
        NA,
        1066,
        TTLocalizer.QuestDialogDict[1065],
    ),
    1066: (
        TT_TIER + 2,
        Cont,
        (CogTrackQuest, Anywhere, 3, "m"),
        Same,
        Same,
        NA,
        1067,
        TTLocalizer.QuestDialogDict[1066],
    ),
    1067: (
        TT_TIER + 2,
        Cont,
        (VisitQuest,),
        Same,
        2309,
        NA,
        1068,
        TTLocalizer.QuestDialogDict[1067],
    ),
    1068: (
        TT_TIER + 2,
        Cont,
        (CogTrackQuest, Anywhere, 2, "s"),
        Same,
        2309,
        NA,
        1069,
        TTLocalizer.QuestDialogDict[1068],
    ),
    1069: (
        TT_TIER + 2,
        Cont,
        (VisitQuest,),
        Any,
        2103,
        NA,
        1070,
        TTLocalizer.QuestDialogDict[1069],
    ),
    1070: (
        TT_TIER + 2,
        Cont,
        (VisitQuest,),
        Any,
        ToonHQ,
        100,
        NA,
        TTLocalizer.QuestDialogDict[1070],
    ),
    # Task 8: Traveling Around The Island
    # Reward: TP Access to TIC
    1071: (
        TT_TIER + 2,
        Start,
        (VisitQuest,),
        Any,
        2123,
        NA,
        1072,
        TTLocalizer.QuestDialogDict[1071],
    ),
    1072: (
        TT_TIER + 2,
        Cont,
        (CogLevelQuest, Any, 6, 2),
        Same,
        Same,
        NA,
        1073,
        TTLocalizer.QuestDialogDict[1072],
    ),
    1073: (
        TT_TIER + 2,
        Cont,
        (CogLevelQuest, Any, 3, 3),
        Same,
        Same,
        NA,
        1074,
        TTLocalizer.QuestDialogDict[1073],
    ),
    1074: (
        TT_TIER + 2,
        Cont,
        (CogLevelQuest, ToontownGlobals.WitheringWoods, 1, 4),
        Same,
        Same,
        300,
        NA,
        TTLocalizer.QuestDialogDict[1074],
    ),
    # Task 9: Gag's O' Plenty
    # Reward: Carry 30 Gags
    1075: (
        TT_TIER + 2,
        Start,
        (VisitQuest,),
        Any,
        2404,
        NA,
        1076,
        TTLocalizer.QuestDialogDict[1075],
    ),
    1076: (
        TT_TIER + 2,
        Cont,
        (CogLevelQuest, Any, 6, 3),
        Same,
        Same,
        NA,
        1077,
        TTLocalizer.QuestDialogDict[1076],
    ),
    1077: (
        TT_TIER + 2,
        Cont,
        (CogQuest, Any, 5, Any),
        Same,
        Same,
        200,
        NA,
        TTLocalizer.QuestDialogDict[1077],
    ),
    # Task 10: More Tasks, More Fun
    # Reward: Carry 2 Tasks
    1078: (
        TT_TIER + 2,
        Start,
        (VisitQuest,),
        Any,
        2103,
        NA,
        1079,
        TTLocalizer.QuestDialogDict[1078],
    ),
    1079: (
        TT_TIER + 2,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 12, Hard, Any, Any),
        Same,
        Same,
        NA,
        1080,
        TTLocalizer.QuestDialogDict[1079],
    ),
    1080: (
        TT_TIER + 2,
        Cont,
        (VisitQuest,),
        Same,
        2213,
        NA,
        1081,
        TTLocalizer.QuestDialogDict[1080],
    ),
    1081: (
        TT_TIER + 2,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 11, Hard, Any, Any),
        Any,
        2213,
        NA,
        1082,
        TTLocalizer.QuestDialogDict[1081],
    ),
    1082: (
        TT_TIER + 2,
        Cont,
        (VisitQuest,),
        Any,
        2103,
        500,
        NA,
        TTLocalizer.QuestDialogDict[1082],
    ),
    # Task 11: Liar, Liar, Baking Contest
    # Reward: +2 Laff
    1083: (
        TT_TIER + 2,
        Start,
        (VisitQuest,),
        Any,
        2117,
        NA,
        1084,
        TTLocalizer.QuestDialogDict[1083],
    ),
    1084: (
        TT_TIER + 2,
        Cont,
        (VisitQuest,),
        Same,
        2407,
        NA,
        1085,
        TTLocalizer.QuestDialogDict[1084],
    ),
    1085: (
        TT_TIER + 2,
        Cont,
        (CogQuest, Any, 12, Any),
        Same,
        2407,
        NA,
        1086,
        TTLocalizer.QuestDialogDict[1085],
    ),
    1086: (
        TT_TIER + 2,
        Cont,
        (CogTrackQuest, Anywhere, 5, "m"),
        Same,
        2407,
        NA,
        1087,
        TTLocalizer.QuestDialogDict[1086],
    ),
    1087: (
        TT_TIER + 2,
        Cont,
        (RecoverItemQuest, Anywhere, 8, 10, Medium, Any, Any),
        Same,
        2407,
        NA,
        1088,
        TTLocalizer.QuestDialogDict[1087],
    ),
    1088: (
        TT_TIER + 2,
        Cont,
        (VisitQuest,),
        Any,
        2117,
        NA,
        1089,
        TTLocalizer.QuestDialogDict[1088],
    ),
    1089: (
        TT_TIER + 2,
        Cont,
        (VisitQuest,),
        Any,
        2407,
        NA,
        1090,
        TTLocalizer.QuestDialogDict[1089],
    ),
    1090: (
        TT_TIER + 2,
        Cont,
        (VisitQuest,),
        Any,
        2117,
        101,
        NA,
        TTLocalizer.QuestDialogDict[1090],
    ),
    # Task 12: Comet Conspiracy
    # Reward: Sound/TU Gags
    1091: (
        TT_TIER + 3,
        Start,
        (VisitQuest,),
        Any,
        2139,
        NA,
        1092,
        TTLocalizer.QuestDialogDict[1091],
    ),
    1092: (
        TT_TIER + 3,
        Cont,
        (RecoverItemQuest, Anywhere, 20, 9, VeryEasy, Any, Any),
        Same,
        2139,
        NA,
        1093,
        TTLocalizer.QuestDialogDict[1092],
    ),
    1093: (
        TT_TIER + 3,
        Cont,
        (VisitQuest,),
        Any,
        ToonHQ,
        NA,
        1094,
        TTLocalizer.QuestDialogDict[1093],
    ),
    1094: (
        TT_TIER + 3,
        Cont,
        (VisitQuest,),
        Any,
        2415,
        NA,
        1095,
        TTLocalizer.QuestDialogDict[1094],
    ),
    1095: (
        TT_TIER + 3,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 8, Medium, "nd"),
        Same,
        2415,
        NA,
        1096,
        TTLocalizer.QuestDialogDict[1095],
    ),
    1096: (
        TT_TIER + 3,
        Cont,
        (VisitQuest,),
        Any,
        2005,
        NA,
        1097,
        TTLocalizer.QuestDialogDict[1096],
    ),
    1097: (
        TT_TIER + 3,
        Cont,
        (VisitQuest,),
        Any,
        2415,
        NA,
        1098,
        TTLocalizer.QuestDialogDict[1097],
    ),
    1098: (
        TT_TIER + 3,
        Cont,
        (VisitQuest,),
        Any,
        2139,
        NA,
        1099,
        TTLocalizer.QuestDialogDict[1098],
    ),
    1099: (
        TT_TIER + 3,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 7, Hard, Any),
        Same,
        2139,
        NA,
        1100,
        TTLocalizer.QuestDialogDict[1099],
    ),
    1100: (
        TT_TIER + 3,
        Cont,
        (VisitQuest,),
        Same,
        2319,
        NA,
        1102,
        TTLocalizer.QuestDialogDict[1100],
    ),
    1101: (
        TT_TIER + 3,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 6, VeryHard, Any, Any),
        Same,
        2319,
        NA,
        1102,
        TTLocalizer.QuestDialogDict[1101],
    ),
    1102: (
        TT_TIER + 3,
        Cont,
        (VisitQuest,),
        Any,
        2139,
        NA,
        1103,
        TTLocalizer.QuestDialogDict[1102],
    ),
    1103: (
        TT_TIER + 3,
        Cont,
        (VisitQuest,),
        Any,
        ToonHQ,
        NA,
        1104,
        TTLocalizer.QuestDialogDict[1103],
    ),
    1104: (
        TT_TIER + 3,
        Cont,
        (BuildingQuest, Anywhere, 1, Any, 1),
        Same,
        2139,
        900,
        NA,
        TTLocalizer.QuestDialogDict[1104],
    ),
    # ==========================
    #      Withering Woods
    # ==========================
    # Task 1
    # Reward: Gag Training
    2001: (
        WW_TIER,
        Start,
        (VisitQuest,),
        Any,
        5201,
        NA,
        2002,
        TTLocalizer.QuestDialogDict[2001],
    ),
    2002: (
        WW_TIER,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 21, Medium, "ds"),
        Same,
        Same,
        NA,
        2003,
        TTLocalizer.QuestDialogDict[2002],
    ),
    2003: (
        WW_TIER,
        Cont,
        (RecoverItemQuest, ToontownGlobals.RainbowRise, 1, 22, Medium, AnyFish),
        Same,
        Same,
        NA,
        401,
        TTLocalizer.QuestDialogDict[2003],
    ),
    401: (
        WW_TIER,
        Cont,
        (
            TrackChoiceQuest,
            ToontownBattleGlobals.DROP_TRACK,
            ToontownBattleGlobals.LURE_TRACK,
        ),
        Same,
        Same,
        400,
        NA,
        TTLocalizer.QuestDialogDict[401],
    ),
    # One off Tasks
    2101: (
        WW_TIER + 1,
        Start,
        (CogQuest, ToontownGlobals.WitheringWoods, 3, Any),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2102: (
        WW_TIER + 1,
        Start,
        (CogQuest, ToontownGlobals.WitheringWoods, 4, Any),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2103: (
        WW_TIER + 1,
        Start,
        (CogQuest, ToontownGlobals.WitheringWoods, 5, Any),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2104: (
        WW_TIER + 1,
        Start,
        (CogQuest, Anywhere, 6, Any),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2105: (
        WW_TIER + 1,
        Start,
        (CogQuest, Anywhere, 7, Any),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2106: (
        WW_TIER + 1,
        Start,
        (CogQuest, Anywhere, 8, Any),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2107: (
        WW_TIER + 1,
        Start,
        (CogQuest, Anywhere, 5, "f"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2108: (
        WW_TIER + 1,
        Start,
        (CogQuest, Anywhere, 4, "p"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2109: (
        WW_TIER + 1,
        Start,
        (CogQuest, Anywhere, 3, "ym"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2110: (
        WW_TIER + 1,
        Start,
        (CogQuest, Anywhere, 2, "mm"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2111: (
        WW_TIER + 1,
        Start,
        (CogQuest, Anywhere, 1, "ds"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2112: (
        WW_TIER + 1,
        Start,
        (CogQuest, Anywhere, 5, "cc"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2113: (
        WW_TIER + 1,
        Start,
        (CogQuest, Anywhere, 4, "tm"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2114: (
        WW_TIER + 1,
        Start,
        (CogQuest, Anywhere, 3, "nd"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2115: (
        WW_TIER + 1,
        Start,
        (CogQuest, Anywhere, 2, "gh"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2116: (
        WW_TIER + 1,
        Start,
        (CogQuest, Anywhere, 1, "ms"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2117: (
        WW_TIER + 1,
        Start,
        (CogQuest, Anywhere, 5, "sc"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2118: (
        WW_TIER + 1,
        Start,
        (CogQuest, Anywhere, 4, "pp"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2119: (
        WW_TIER + 1,
        Start,
        (CogQuest, Anywhere, 3, "tw"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2120: (
        WW_TIER + 1,
        Start,
        (CogQuest, Anywhere, 2, "bc"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2121: (
        WW_TIER + 1,
        Start,
        (CogQuest, Anywhere, 1, "nc"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2122: (
        WW_TIER + 1,
        Start,
        (CogQuest, Anywhere, 5, "bf"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2123: (
        WW_TIER + 1,
        Start,
        (CogQuest, Anywhere, 4, "b"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2124: (
        WW_TIER + 1,
        Start,
        (CogQuest, Anywhere, 3, "dt"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2125: (
        WW_TIER + 1,
        Start,
        (CogQuest, Anywhere, 2, "ac"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2126: (
        WW_TIER + 1,
        Start,
        (CogQuest, Anywhere, 1, "bs"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2127: (
        WW_TIER + 1,
        Start,
        (CogLevelQuest, ToontownGlobals.WitheringWoods, 2, 3),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2128: (
        WW_TIER + 1,
        Start,
        (CogLevelQuest, ToontownGlobals.WitheringWoods, 3, 3),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2129: (
        WW_TIER + 1,
        Start,
        (CogLevelQuest, ToontownGlobals.WitheringWoods, 2, 4),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2130: (
        WW_TIER + 1,
        Start,
        (CogLevelQuest, ToontownGlobals.WitheringWoods, 4, 4),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2131: (
        WW_TIER + 1,
        Start,
        (CogLevelQuest, ToontownGlobals.WitheringWoods, 4, 5),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2132: (
        WW_TIER + 1,
        Start,
        (CogLevelQuest, ToontownGlobals.WitheringWoods, 5, 5),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2133: (
        WW_TIER + 1,
        Start,
        (CogLevelQuest, ToontownGlobals.WitheringWoods, 4, 2),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2134: (
        WW_TIER + 1,
        Start,
        (CogLevelQuest, ToontownGlobals.WitheringWoods, 6, 2),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2135: (
        WW_TIER + 1,
        Start,
        (CogTrackQuest, ToontownGlobals.WitheringWoods, 3, "m"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2136: (
        WW_TIER + 1,
        Start,
        (CogTrackQuest, ToontownGlobals.WitheringWoods, 3, "s"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2137: (
        WW_TIER + 1,
        Start,
        (CogTrackQuest, ToontownGlobals.WitheringWoods, 3, "c"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2138: (
        WW_TIER + 1,
        Start,
        (CogTrackQuest, ToontownGlobals.WitheringWoods, 3, "l"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2139: (
        WW_TIER + 1,
        Start,
        (CogTrackQuest, ToontownGlobals.WitheringWoods, 5, "m"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2140: (
        WW_TIER + 1,
        Start,
        (CogTrackQuest, ToontownGlobals.WitheringWoods, 5, "s"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2141: (
        WW_TIER + 1,
        Start,
        (CogTrackQuest, ToontownGlobals.WitheringWoods, 5, "c"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2142: (
        WW_TIER + 1,
        Start,
        (CogTrackQuest, ToontownGlobals.WitheringWoods, 5, "l"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2143: (
        WW_TIER + 1,
        Start,
        (CogTrackQuest, Anywhere, 7, "m"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2144: (
        WW_TIER + 1,
        Start,
        (CogTrackQuest, Anywhere, 7, "s"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2145: (
        WW_TIER + 1,
        Start,
        (CogTrackQuest, Anywhere, 7, "c"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2146: (
        WW_TIER + 1,
        Start,
        (CogTrackQuest, Anywhere, 7, "l"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2147: (
        WW_TIER + 1,
        Start,
        (BuildingQuest, Anywhere, 1, Any, 1),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2148: (
        WW_TIER + 1,
        Start,
        (BuildingQuest, Anywhere, 1, Any, 2),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2149: (
        WW_TIER + 1,
        Start,
        (BuildingQuest, Anywhere, 2, Any, 1),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2150: (
        WW_TIER + 1,
        Start,
        (BuildingQuest, Anywhere, 2, Any, 2),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2151: (
        WW_TIER + 1,
        Start,
        (BuildingQuest, Anywhere, 1, "m", 1),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2152: (
        WW_TIER + 1,
        Start,
        (BuildingQuest, Anywhere, 1, "s", 1),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2153: (
        WW_TIER + 1,
        Start,
        (BuildingQuest, Anywhere, 1, "c", 1),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2154: (
        WW_TIER + 1,
        Start,
        (BuildingQuest, Anywhere, 1, "l", 1),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    2155: (
        WW_TIER + 1,
        Start,
        (DeliverGagQuest, 2, ToontownBattleGlobals.THROW_TRACK, 1),
        Any,
        Any,
        Any,
        NA,
        DefaultDialog,
    ),
    2156: (
        WW_TIER + 1,
        Start,
        (DeliverGagQuest, 1, ToontownBattleGlobals.THROW_TRACK, 2),
        Any,
        Any,
        Any,
        NA,
        DefaultDialog,
    ),
    2157: (
        WW_TIER + 1,
        Start,
        (DeliverGagQuest, 1, ToontownBattleGlobals.THROW_TRACK, 3),
        Any,
        Any,
        Any,
        NA,
        DefaultDialog,
    ),
    2158: (
        WW_TIER + 1,
        Start,
        (DeliverGagQuest, 2, ToontownBattleGlobals.SQUIRT_TRACK, 1),
        Any,
        Any,
        Any,
        NA,
        DefaultDialog,
    ),
    2159: (
        WW_TIER + 1,
        Start,
        (DeliverGagQuest, 1, ToontownBattleGlobals.SQUIRT_TRACK, 2),
        Any,
        Any,
        Any,
        NA,
        DefaultDialog,
    ),
    2160: (
        WW_TIER + 1,
        Start,
        (DeliverGagQuest, 1, ToontownBattleGlobals.SQUIRT_TRACK, 3),
        Any,
        Any,
        Any,
        NA,
        DefaultDialog,
    ),
    # Task 2: Training with Oak
    # Reward: +2 Laff
    2165: (
        WW_TIER + 1,
        Start,
        (VisitQuest,),
        Any,
        5127,
        NA,
        2166,
        TTLocalizer.QuestDialogDict[2165],
    ),
    2166: (
        WW_TIER + 1,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 23, Medium, "tf"),
        Same,
        Same,
        NA,
        2167,
        TTLocalizer.QuestDialogDict[2166],
    ),
    2167: (
        WW_TIER + 1,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 24, Medium, "nc"),
        Same,
        Same,
        NA,
        2168,
        TTLocalizer.QuestDialogDict[2167],
    ),
    2168: (
        WW_TIER + 1,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 25, Hard, Any),
        Same,
        Same,
        NA,
        2169,
        TTLocalizer.QuestDialogDict[2168],
    ),
    2169: (
        WW_TIER + 1,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 26, Medium, "bw"),
        Same,
        Same,
        101,
        NA,
        TTLocalizer.QuestDialogDict[2169],
    ),
    # Task 3: Food Fright
    # Reward: +2 Laff
    2170: (
        WW_TIER + 1,
        Start,
        (VisitQuest,),
        Any,
        5321,
        NA,
        2171,
        TTLocalizer.QuestDialogDict[2170],
    ),
    2171: (
        WW_TIER + 1,
        Cont,
        (VisitQuest,),
        Any,
        5120,
        NA,
        2172,
        TTLocalizer.QuestDialogDict[2171],
    ),
    2172: (
        WW_TIER + 1,
        Cont,
        (VisitQuest,),
        Any,
        5306,
        NA,
        2173,
        TTLocalizer.QuestDialogDict[2172],
    ),
    2173: (
        WW_TIER + 1,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 27, VeryHard, Any),
        Same,
        Same,
        NA,
        2174,
        TTLocalizer.QuestDialogDict[2173],
    ),
    2174: (
        WW_TIER + 1,
        Cont,
        (VisitQuest,),
        Any,
        5120,
        NA,
        2175,
        TTLocalizer.QuestDialogDict[2174],
    ),
    2175: (
        WW_TIER + 1,
        Cont,
        (VisitQuest,),
        Any,
        5321,
        NA,
        2176,
        TTLocalizer.QuestDialogDict[2175],
    ),
    2176: (
        WW_TIER + 1,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 28, Medium, "le"),
        Same,
        Same,
        101,
        NA,
        TTLocalizer.QuestDialogDict[2176],
    ),
    # Task 4: Got any Grapes
    # Reward: +2 Laff
    2177: (
        WW_TIER + 1,
        Start,
        (VisitQuest,),
        Any,
        5320,
        NA,
        2178,
        TTLocalizer.QuestDialogDict[2177],
    ),
    2178: (
        WW_TIER + 1,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 29, Medium, Any),
        Same,
        Same,
        NA,
        2179,
        TTLocalizer.QuestDialogDict[2178],
    ),
    2179: (
        WW_TIER + 1,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 30, VeryHard, Any),
        Same,
        Same,
        NA,
        2180,
        TTLocalizer.QuestDialogDict[2179],
    ),
    2180: (
        WW_TIER + 1,
        Cont,
        (BuildingQuest, Anywhere, 1, Any, 3),
        Same,
        Same,
        101,
        NA,
        TTLocalizer.QuestDialogDict[2180],
    ),
    # Task 5: House Of Junky
    # Reward: Carry 30 Gags
    2181: (
        WW_TIER + 1,
        Start,
        (VisitQuest,),
        Any,
        5223,
        NA,
        2182,
        TTLocalizer.QuestDialogDict[2181],
    ),
    2182: (
        WW_TIER + 1,
        Cont,
        (RecoverItemQuest, Anywhere, 20, 31, Easy, Any),
        Same,
        Same,
        NA,
        2183,
        TTLocalizer.QuestDialogDict[2182],
    ),
    2183: (
        WW_TIER + 1,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 32, VeryHard, "mb"),
        Same,
        Same,
        201,
        NA,
        TTLocalizer.QuestDialogDict[2183],
    ),
    # Task 6: The Training Of A Warrior
    # Reward: +4 Laff
    2184: (
        WW_TIER + 1,
        Start,
        (VisitQuest,),
        Any,
        5103,
        NA,
        2185,
        TTLocalizer.QuestDialogDict[2184],
    ),
    2185: (
        WW_TIER + 1,
        Cont,
        (CogTrackQuest, Anywhere, 5, "s"),
        Same,
        Same,
        NA,
        2186,
        TTLocalizer.QuestDialogDict[2185],
    ),
    2186: (
        WW_TIER + 1,
        Cont,
        (CogTrackQuest, Anywhere, 10, "c"),
        Same,
        Same,
        NA,
        2187,
        TTLocalizer.QuestDialogDict[2186],
    ),
    2187: (
        WW_TIER + 1,
        Cont,
        (CogTrackQuest, Anywhere, 15, "l"),
        Same,
        Same,
        NA,
        2188,
        TTLocalizer.QuestDialogDict[2187],
    ),
    2188: (
        WW_TIER + 1,
        Cont,
        (BuildingQuest, Anywhere, 1, Any, 4),
        Same,
        Same,
        103,
        NA,
        TTLocalizer.QuestDialogDict[2188],
    ),
    # Task 7: Its Never Ogre
    # Reward: +3 Laff
    2189: (
        WW_TIER + 1,
        Start,
        (VisitQuest,),
        Any,
        5309,
        NA,
        2190,
        TTLocalizer.QuestDialogDict[2189],
    ),
    2190: (
        WW_TIER + 1,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 33, Medium, Any),
        Same,
        Same,
        NA,
        2191,
        TTLocalizer.QuestDialogDict[2190],
    ),
    2191: (
        WW_TIER + 1,
        Cont,
        (VisitQuest,),
        Any,
        5315,
        NA,
        2192,
        TTLocalizer.QuestDialogDict[2191],
    ),
    2192: (
        WW_TIER + 1,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 34, Hard, "bf"),
        Same,
        Same,
        NA,
        2193,
        TTLocalizer.QuestDialogDict[2192],
    ),
    2193: (
        WW_TIER + 1,
        Cont,
        (VisitQuest,),
        Any,
        5309,
        NA,
        2194,
        TTLocalizer.QuestDialogDict[2193],
    ),
    2194: (
        WW_TIER + 1,
        Cont,
        (BuildingQuest, Anywhere, 1, Any, 3),
        Same,
        Same,
        NA,
        2195,
        TTLocalizer.QuestDialogDict[2194],
    ),
    2195: (
        WW_TIER + 1,
        Cont,
        (CogQuest, Anywhere, 1, "mh"),
        Same,
        Same,
        102,
        NA,
        TTLocalizer.QuestDialogDict[2195],
    ),
    # Task 8: The Hunt For "The" Ring
    # Reward: +3 Laff
    2196: (
        WW_TIER + 1,
        Start,
        (VisitQuest,),
        Any,
        5226,
        NA,
        2197,
        TTLocalizer.QuestDialogDict[2196],
    ),
    2197: (
        WW_TIER + 1,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 35, VeryEasy, "cr"),
        Same,
        Same,
        NA,
        2198,
        TTLocalizer.QuestDialogDict[2197],
    ),
    2198: (
        WW_TIER + 1,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 36, Medium, "cr"),
        Same,
        Same,
        NA,
        2199,
        TTLocalizer.QuestDialogDict[2198],
    ),
    2199: (
        WW_TIER + 1,
        Cont,
        (VisitQuest,),
        Any,
        5124,
        NA,
        2200,
        TTLocalizer.QuestDialogDict[2199],
    ),
    2200: (
        WW_TIER + 1,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 37, Hard, Any),
        Same,
        Same,
        NA,
        2201,
        TTLocalizer.QuestDialogDict[2200],
    ),
    2201: (
        WW_TIER + 1,
        Cont,
        (BuildingQuest, Anywhere, 1, Any, 4),
        Same,
        Same,
        NA,
        2202,
        TTLocalizer.QuestDialogDict[2201],
    ),
    2202: (
        WW_TIER + 1,
        Cont,
        (DeliverItemQuest, 36),
        Any,
        5226,
        102,
        NA,
        TTLocalizer.QuestDialogDict[2202],
    ),
    # Task 9: A Little Birdie Told Me
    # Reward: Carry 60 Beans
    2203: (
        WW_TIER + 1,
        Start,
        (VisitQuest,),
        Any,
        5108,
        NA,
        2204,
        TTLocalizer.QuestDialogDict[2203],
    ),
    2204: (
        WW_TIER + 1,
        Cont,
        (VisitQuest,),
        Any,
        5106,
        NA,
        2205,
        TTLocalizer.QuestDialogDict[2204],
    ),
    2205: (
        WW_TIER + 1,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 38, Easy, "pp"),
        Same,
        Same,
        NA,
        2206,
        TTLocalizer.QuestDialogDict[2205],
    ),
    2206: (
        WW_TIER + 1,
        Start,
        (VisitQuest,),
        Any,
        5108,
        NA,
        2207,
        TTLocalizer.QuestDialogDict[2206],
    ),
    2207: (
        WW_TIER + 1,
        Cont,
        (VisitQuest,),
        Any,
        5106,
        NA,
        2208,
        TTLocalizer.QuestDialogDict[2207],
    ),
    2208: (
        WW_TIER + 1,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 39, Hard, Any),
        Same,
        Same,
        701,
        NA,
        TTLocalizer.QuestDialogDict[2208],
    ),
    # Task 10: Taking A Vacation In Withering Woods
    # Reward: TP Access to Withering Woods
    2209: (
        WW_TIER + 1,
        Start,
        (VisitQuest,),
        Any,
        5224,
        NA,
        2210,
        TTLocalizer.QuestDialogDict[2209],
    ),
    2210: (
        WW_TIER + 1,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 40, Easy, "tf"),
        Same,
        Same,
        NA,
        2211,
        TTLocalizer.QuestDialogDict[2210],
    ),
    2211: (
        WW_TIER + 1,
        Cont,
        (DeliverItemQuest, 40),
        Any,
        2125,
        NA,
        2212,
        TTLocalizer.QuestDialogDict[2211],
    ),
    2212: (
        WW_TIER + 1,
        Cont,
        (VisitQuest,),
        Any,
        5224,
        NA,
        2213,
        TTLocalizer.QuestDialogDict[2212],
    ),
    2213: (
        WW_TIER + 1,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 40, Easy, "hh"),
        Same,
        Same,
        NA,
        2214,
        TTLocalizer.QuestDialogDict[2213],
    ),
    2214: (
        WW_TIER + 1,
        Cont,
        (DeliverItemQuest, 40),
        Any,
        4323,
        NA,
        2215,
        TTLocalizer.QuestDialogDict[2214],
    ),
    2215: (
        WW_TIER + 1,
        Cont,
        (VisitQuest,),
        Any,
        5224,
        NA,
        2216,
        TTLocalizer.QuestDialogDict[2215],
    ),
    2216: (
        WW_TIER + 1,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 40, Easy, "m"),
        Same,
        Same,
        NA,
        2217,
        TTLocalizer.QuestDialogDict[2216],
    ),
    2217: (
        WW_TIER + 1,
        Cont,
        (DeliverItemQuest, 40),
        Any,
        9216,
        NA,
        2218,
        TTLocalizer.QuestDialogDict[2217],
    ),
    2218: (
        WW_TIER + 1,
        Cont,
        (VisitQuest,),
        Any,
        5224,
        NA,
        2219,
        TTLocalizer.QuestDialogDict[2218],
    ),
    2219: (
        WW_TIER + 1,
        Cont,
        (RecoverItemQuest, Anywhere, 1, 40, Hard, Any),
        Same,
        Same,
        NA,
        2220,
        TTLocalizer.QuestDialogDict[2219],
    ),
    2220: (
        WW_TIER + 1,
        Cont,
        (DeliverItemQuest, 40),
        Any,
        1313,
        NA,
        2221,
        TTLocalizer.QuestDialogDict[2220],
    ),
    2221: (
        WW_TIER + 1,
        Cont,
        (VisitQuest,),
        Any,
        5224,
        302,
        NA,
        TTLocalizer.QuestDialogDict[2221],
    ),
    # Task 11: The Withering Finale
    # Reward: Last Gag Track Frame
    2222: (
        WW_TIER + 2,
        Start,
        (VisitQuest,),
        Any,
        5201,
        NA,
        2223,
        TTLocalizer.QuestDialogDict[2222],
    ),
    2223: (
        WW_TIER + 2,
        Cont,
        (VisitQuest,),
        Any,
        5319,
        NA,
        2224,
        TTLocalizer.QuestDialogDict[2223],
    ),
    2224: (
        WW_TIER + 2,
        Cont,
        (RecoverItemQuest, ToontownGlobals.WitheringWoods, 1, 41, Medium, Any),
        Same,
        Same,
        NA,
        2225,
        TTLocalizer.QuestDialogDict[2224],
    ),
    2225: (
        WW_TIER + 2,
        Cont,
        (RecoverItemQuest, ToontownGlobals.WitheringWoods, 1, 42, Easy, Any),
        Same,
        Same,
        NA,
        2226,
        TTLocalizer.QuestDialogDict[2225],
    ),
    2226: (
        WW_TIER + 2,
        Cont,
        (RecoverItemQuest, ToontownGlobals.WitheringWoods, 1, 41, VeryHard, "ls"),
        Same,
        Same,
        NA,
        2227,
        TTLocalizer.QuestDialogDict[2226],
    ),
    2227: (
        WW_TIER + 2,
        Cont,
        (BuildingQuest, Anywhere, 3, Any, 3),
        Same,
        Same,
        900,
        NA,
        TTLocalizer.QuestDialogDict[2227],
    ),
    # ==========================
    #       Rainbow Rise
    # ==========================
    # Task 1: Meeting The Captain
    # Reward: Gag Training
    3001: (
        RR_TIER,
        Start,
        (VisitQuest,),
        Any,
        1116,
        NA,
        3002,
        TTLocalizer.QuestDialogDict[3001],
    ),
    3002: (
        RR_TIER,
        Cont,
        (RecoverItemQuest, Anywhere, 5, 43, Medium, "cr"),
        Same,
        Same,
        NA,
        (3003, 3004),
        TTLocalizer.QuestDialogDict[3002],
    ),
    3003: (
        RR_TIER,
        Cont,
        (
            TrackChoiceQuest,
            ToontownBattleGlobals.TRAP_TRACK,
            ToontownBattleGlobals.HEAL_TRACK,
        ),
        Any,
        ToonHQ,
        400,
        NA,
        TTLocalizer.QuestDialogDict[3003],
    ),
    3004: (
        RR_TIER,
        Cont,
        (
            TrackChoiceQuest,
            ToontownBattleGlobals.TRAP_TRACK,
            ToontownBattleGlobals.SOUND_TRACK,
        ),
        Any,
        ToonHQ,
        400,
        NA,
        TTLocalizer.QuestDialogDict[3004],
    ),
    # One off Tasks
    3101: (
        RR_TIER + 1,
        Start,
        (CogQuest, ToontownGlobals.RainbowRise, 4, Any),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3102: (
        RR_TIER + 1,
        Start,
        (CogQuest, ToontownGlobals.RainbowRise, 5, Any),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3103: (
        RR_TIER + 1,
        Start,
        (CogQuest, ToontownGlobals.RainbowRise, 6, Any),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3104: (
        RR_TIER + 1,
        Start,
        (CogQuest, Anywhere, 7, Any),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3105: (
        RR_TIER + 1,
        Start,
        (CogQuest, Anywhere, 8, Any),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3106: (
        RR_TIER + 1,
        Start,
        (CogQuest, Anywhere, 9, Any),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3107: (
        RR_TIER + 1,
        Start,
        (CogQuest, Anywhere, 7, "p"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3108: (
        RR_TIER + 1,
        Start,
        (CogQuest, Anywhere, 5, "ym"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3109: (
        RR_TIER + 1,
        Start,
        (CogQuest, Anywhere, 4, "mm"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3110: (
        RR_TIER + 1,
        Start,
        (CogQuest, Anywhere, 2, "ds"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3111: (
        RR_TIER + 1,
        Start,
        (CogQuest, Anywhere, 1, "hh"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3112: (
        RR_TIER + 1,
        Start,
        (CogQuest, Anywhere, 7, "tm"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3113: (
        RR_TIER + 1,
        Start,
        (CogQuest, Anywhere, 5, "nd"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3114: (
        RR_TIER + 1,
        Start,
        (CogQuest, Anywhere, 4, "gh"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3115: (
        RR_TIER + 1,
        Start,
        (CogQuest, Anywhere, 2, "ms"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3116: (
        RR_TIER + 1,
        Start,
        (CogQuest, Anywhere, 1, "tf"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3117: (
        RR_TIER + 1,
        Start,
        (CogQuest, Anywhere, 7, "pp"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3118: (
        RR_TIER + 1,
        Start,
        (CogQuest, Anywhere, 5, "tw"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3119: (
        RR_TIER + 1,
        Start,
        (CogQuest, Anywhere, 4, "bc"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3120: (
        RR_TIER + 1,
        Start,
        (CogQuest, Anywhere, 2, "nc"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3121: (
        RR_TIER + 1,
        Start,
        (CogQuest, Anywhere, 1, "mb"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3122: (
        RR_TIER + 1,
        Start,
        (CogQuest, Anywhere, 7, "b"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3123: (
        RR_TIER + 1,
        Start,
        (CogQuest, Anywhere, 5, "dt"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3124: (
        RR_TIER + 1,
        Start,
        (CogQuest, Anywhere, 4, "ac"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3125: (
        RR_TIER + 1,
        Start,
        (CogQuest, Anywhere, 2, "bs"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3126: (
        RR_TIER + 1,
        Start,
        (CogQuest, Anywhere, 1, "sd"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3127: (
        RR_TIER + 1,
        Start,
        (CogLevelQuest, ToontownGlobals.RainbowRise, 5, 4),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3128: (
        RR_TIER + 1,
        Start,
        (CogLevelQuest, ToontownGlobals.RainbowRise, 6, 4),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3129: (
        RR_TIER + 1,
        Start,
        (CogLevelQuest, ToontownGlobals.RainbowRise, 4, 5),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3130: (
        RR_TIER + 1,
        Start,
        (CogLevelQuest, ToontownGlobals.RainbowRise, 5, 5),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3131: (
        RR_TIER + 1,
        Start,
        (CogLevelQuest, ToontownGlobals.RainbowRise, 3, 6),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3132: (
        RR_TIER + 1,
        Start,
        (CogLevelQuest, ToontownGlobals.RainbowRise, 2, 6),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3133: (
        RR_TIER + 1,
        Start,
        (CogLevelQuest, ToontownGlobals.RainbowRise, 1, 7),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3134: (
        RR_TIER + 1,
        Start,
        (CogLevelQuest, ToontownGlobals.RainbowRise, 7, 3),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3135: (
        RR_TIER + 1,
        Start,
        (CogTrackQuest, ToontownGlobals.RainbowRise, 3, "m"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3136: (
        RR_TIER + 1,
        Start,
        (CogTrackQuest, ToontownGlobals.RainbowRise, 3, "s"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3137: (
        RR_TIER + 1,
        Start,
        (CogTrackQuest, ToontownGlobals.RainbowRise, 3, "c"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3138: (
        RR_TIER + 1,
        Start,
        (CogTrackQuest, ToontownGlobals.RainbowRise, 3, "l"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3139: (
        RR_TIER + 1,
        Start,
        (CogTrackQuest, ToontownGlobals.RainbowRise, 5, "m"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3140: (
        RR_TIER + 1,
        Start,
        (CogTrackQuest, ToontownGlobals.RainbowRise, 5, "s"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3141: (
        RR_TIER + 1,
        Start,
        (CogTrackQuest, ToontownGlobals.RainbowRise, 5, "c"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3142: (
        RR_TIER + 1,
        Start,
        (CogTrackQuest, ToontownGlobals.RainbowRise, 5, "l"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3143: (
        RR_TIER + 1,
        Start,
        (CogTrackQuest, Anywhere, 8, "m"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3144: (
        RR_TIER + 1,
        Start,
        (CogTrackQuest, Anywhere, 8, "s"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3145: (
        RR_TIER + 1,
        Start,
        (CogTrackQuest, Anywhere, 8, "c"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3146: (
        RR_TIER + 1,
        Start,
        (CogTrackQuest, Anywhere, 8, "l"),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3147: (
        RR_TIER + 1,
        Start,
        (BuildingQuest, Anywhere, 4, Any, 2),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3148: (
        RR_TIER + 1,
        Start,
        (BuildingQuest, Anywhere, 4, Any, 3),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3149: (
        RR_TIER + 1,
        Start,
        (BuildingQuest, Anywhere, 3, Any, 2),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3150: (
        RR_TIER + 1,
        Start,
        (BuildingQuest, Anywhere, 3, Any, 3),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3151: (
        RR_TIER + 1,
        Start,
        (BuildingQuest, Anywhere, 2, "m", 3),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3152: (
        RR_TIER + 1,
        Start,
        (BuildingQuest, Anywhere, 2, "s", 3),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3153: (
        RR_TIER + 1,
        Start,
        (BuildingQuest, Anywhere, 2, "c", 3),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3154: (
        RR_TIER + 1,
        Start,
        (BuildingQuest, Anywhere, 2, "l", 3),
        Any,
        ToonHQ,
        Any,
        NA,
        DefaultDialog,
    ),
    3155: (
        RR_TIER + 1,
        Start,
        (DeliverGagQuest, 5, ToontownBattleGlobals.THROW_TRACK, 2),
        Any,
        Any,
        Any,
        NA,
        DefaultDialog,
    ),
    3156: (
        RR_TIER + 1,
        Start,
        (DeliverGagQuest, 4, ToontownBattleGlobals.THROW_TRACK, 3),
        Any,
        Any,
        Any,
        NA,
        DefaultDialog,
    ),
    3157: (
        RR_TIER + 1,
        Start,
        (DeliverGagQuest, 3, ToontownBattleGlobals.THROW_TRACK, 4),
        Any,
        Any,
        Any,
        NA,
        DefaultDialog,
    ),
    3158: (
        RR_TIER + 1,
        Start,
        (DeliverGagQuest, 5, ToontownBattleGlobals.SQUIRT_TRACK, 2),
        Any,
        Any,
        Any,
        NA,
        DefaultDialog,
    ),
    3159: (
        RR_TIER + 1,
        Start,
        (DeliverGagQuest, 4, ToontownBattleGlobals.SQUIRT_TRACK, 3),
        Any,
        Any,
        Any,
        NA,
        DefaultDialog,
    ),
    3160: (
        RR_TIER + 1,
        Start,
        (DeliverGagQuest, 3, ToontownBattleGlobals.SQUIRT_TRACK, 4),
        Any,
        Any,
        Any,
        NA,
        DefaultDialog,
    ),
    # Task 2: Freaks in Control
    # Reward: +3 Laff Boost
    3161: (
        RR_TIER,
        Start,
        (VisitQuest,),
        Any,
        1313,
        NA,
        3162,
        TTLocalizer.QuestDialogDict[3161],
    ),
    3162: (
        RR_TIER + 1,
        Cont,
        (BuildingQuest, Anywhere, 3, "m", 3),
        Same,
        Same,
        NA,
        3163,
        TTLocalizer.QuestDialogDict[3162],
    ),
    3163: (
        RR_TIER + 1,
        Cont,
        (BuildingQuest, Anywhere, 1, "m", 4),
        Same,
        Same,
        NA,
        3164,
        TTLocalizer.QuestDialogDict[3163],
    ),
    3164: (
        RR_TIER + 1,
        Cont,
        (CogQuest, Anywhere, 1, "tbc"),
        Same,
        Same,
        102,
        NA,
        TTLocalizer.QuestDialogDict[3164],
    ),  # Control Freak Tier 8 Bossbot Change
    # Task 3: You Cant Sea Me
    # Reward: +4 Laff Boost + Invisible Toon Cheesy Effect
    3165: (
        RR_TIER + 1,
        Start,
        (VisitQuest,),
        Any,
        1226,
        NA,
        3166,
        TTLocalizer.QuestDialogDict[3165],
    ),
    3166: (
        RR_TIER + 1,
        Cont,
        (VisitQuest,),
        Same,
        1123,
        NA,
        3167,
        TTLocalizer.QuestDialogDict[3166],
    ),
    3167: (
        RR_TIER + 1,
        Cont,
        (CogQuest, ToontownGlobals.RainbowRise, 15, Any),
        Same,
        Same,
        NA,
        3168,
        TTLocalizer.QuestDialogDict[3167],
    ),
    3168: (
        RR_TIER + 1,
        Cont,
        (VisitQuest,),
        Same,
        1226,
        NA,
        3169,
        TTLocalizer.QuestDialogDict[3168],
    ),
    3169: (
        RR_TIER + 1,
        Cont,
        (RecoverItemQuest, Anywhere, 10, 44, Medium, "bw"),
        Same,
        Same,
        NA,
        3170,
        TTLocalizer.QuestDialogDict[3169],
    ),
    3170: (
        RR_TIER + 1,
        Cont,
        (RecoverItemQuest, Anywhere, 5, 45, Hard, Any),
        Same,
        Same,
        103,
        NA,
        TTLocalizer.QuestDialogDict[3170],
    ),
    # Task 4: A Grassy Accident
    # Reward: +3 Laff Boost
    3171: (
        RR_TIER + 1,
        Start,
        (VisitQuest,),
        Any,
        1104,
        NA,
        3172,
        TTLocalizer.QuestDialogDict[3171],
    ),
    3172: (
        RR_TIER + 1,
        Cont,
        (VisitQuest,),
        Same,
        1312,
        NA,
        3173,
        TTLocalizer.QuestDialogDict[3172],
    ),
    3173: (
        RR_TIER + 1,
        Cont,
        (VisitQuest,),
        Same,
        1104,
        NA,
        3174,
        TTLocalizer.QuestDialogDict[3173],
    ),
    3174: (
        RR_TIER + 1,
        Cont,
        (DeliverItemQuest, 46),
        Same,
        1312,
        NA,
        3175,
        TTLocalizer.QuestDialogDict[3174],
    ),
    3175: (
        RR_TIER + 1,
        Cont,
        (CogQuest, ToontownGlobals.RainbowRise, 20, Any),
        Same,
        Same,
        NA,
        3176,
        TTLocalizer.QuestDialogDict[3175],
    ),
    3176: (
        RR_TIER + 1,
        Cont,
        (VisitQuest,),
        Any,
        1104,
        102,
        NA,
        TTLocalizer.QuestDialogDict[3176],
    ),
}
Tier2QuestsDict = {}
for questId, questDesc in list(QuestDict.items()):
    if questDesc[QuestDictStartIndex] == Start:
        tier = questDesc[QuestDictTierIndex]
        if tier in Tier2QuestsDict:
            Tier2QuestsDict[tier].append(questId)
        else:
            Tier2QuestsDict[tier] = [questId]

Quest2RewardDict = {}
Tier2Reward2QuestsDict = {}
Quest2RemainingStepsDict = {}


def getAllRewardIdsForReward(rewardId):
    if rewardId is AnyCashbotSuitPart:
        return range(4000, 4011 + 1)
    if rewardId is AnyLawbotSuitPart:
        return range(4100, 4113 + 1)
    if rewardId is AnyBossbotSuitPart:
        return range(4200, 4216 + 1)
    return (rewardId,)


def findFinalRewardId(questId):
    finalRewardId = Quest2RewardDict.get(questId)
    if finalRewardId:
        remainingSteps = Quest2RemainingStepsDict.get(questId)
    else:
        try:
            questDesc = QuestDict[questId]
        except KeyError:
            print("findFinalRewardId: Quest ID: %d not found" % questId)
            return -1

        nextQuestId = questDesc[QuestDictNextQuestIndex]
        if nextQuestId == NA:
            finalRewardId = questDesc[QuestDictRewardIndex]
            remainingSteps = 1
        else:
            if type(nextQuestId) == type(()):
                finalRewardId, remainingSteps = findFinalRewardId(nextQuestId[0])
                for id in nextQuestId[1:]:
                    findFinalRewardId(id)

            else:
                finalRewardId, remainingSteps = findFinalRewardId(nextQuestId)
            remainingSteps += 1
        if finalRewardId != OBSOLETE:
            if questDesc[QuestDictStartIndex] == Start:
                tier = questDesc[QuestDictTierIndex]
                tier2RewardDict = Tier2Reward2QuestsDict.setdefault(tier, {})
                rewardIds = getAllRewardIdsForReward(finalRewardId)
                for rewardId in rewardIds:
                    questList = tier2RewardDict.setdefault(rewardId, [])
                    questList.append(questId)

        else:
            finalRewardId = None
        Quest2RewardDict[questId] = finalRewardId
        Quest2RemainingStepsDict[questId] = remainingSteps
    return (finalRewardId, remainingSteps)


for questId in list(QuestDict.keys()):
    findFinalRewardId(questId)


def getStartingQuests(tier=None):
    startingQuests = []
    for questId in list(QuestDict.keys()):
        if isStartingQuest(questId):
            if tier is None:
                startingQuests.append(questId)
            elif questId in Tier2QuestsDict[tier]:
                startingQuests.append(questId)

    startingQuests.sort()
    return startingQuests


def getFinalRewardId(questId, fAll=0):
    if fAll or isStartingQuest(questId):
        return Quest2RewardDict.get(questId)
    else:
        return None
    return None


def isStartingQuest(questId):
    try:
        return QuestDict[questId][QuestDictStartIndex] == Start
    except KeyError:
        return None

    return None


def getNumChoices(tier):
    if tier in (0,):
        return 0
    if tier in (1,):
        return 2
    else:
        return 3


def getAvatarRewardId(av, questId):
    for quest in av.quests:
        if questId == quest[0]:
            return quest[3]

    notify.warning("getAvatarRewardId(): quest not found on avatar")
    return None


def getNextQuest(id, currentNpc, av):
    nextQuest = QuestDict[id][QuestDictNextQuestIndex]
    if nextQuest == NA:
        return (NA, NA)
    elif type(nextQuest) == type(()):
        nextReward = QuestDict[nextQuest[0]][QuestDictRewardIndex]
        nextNextQuest, nextNextToNpcId = getNextQuest(nextQuest[0], currentNpc, av)
        if nextReward == 400 and nextNextQuest == NA:
            nextQuest = chooseTrackChoiceQuest(av.getRewardTier(), av)
        else:
            nextQuest = random.choice(nextQuest)
    if not getQuestClass(nextQuest).filterFunc(av):
        return getNextQuest(nextQuest, currentNpc, av)
    nextToNpcId = getQuestToNpcId(nextQuest)
    if nextToNpcId == Any:
        nextToNpcId = 2004
    elif nextToNpcId == Same:
        if currentNpc.getHq():
            nextToNpcId = ToonHQ
        else:
            nextToNpcId = currentNpc.getNpcId()
    elif nextToNpcId == ToonHQ:
        nextToNpcId = ToonHQ
    return (nextQuest, nextToNpcId)


def filterQuests(entireQuestPool, currentNpc, av):
    if notify.getDebug():
        notify.debug("filterQuests: entireQuestPool: %s" % entireQuestPool)
    validQuestPool = dict([(questId, 1) for questId in entireQuestPool])
    if isLoopingFinalTier(av.getRewardTier()):
        history = [questDesc[0] for questDesc in av.quests]
    else:
        history = av.getQuestHistory()
    if notify.getDebug():
        notify.debug("filterQuests: av quest history: %s" % history)
    currentQuests = av.quests
    for questId in entireQuestPool:
        if questId in history:
            if notify.getDebug():
                notify.debug("filterQuests: Removed %s because in history" % questId)
            validQuestPool[questId] = 0
            continue
        potentialFromNpc = getQuestFromNpcId(questId)
        if not npcMatches(potentialFromNpc, currentNpc):
            if notify.getDebug():
                notify.debug(
                    "filterQuests: Removed %s: potentialFromNpc does not match currentNpc"
                    % questId
                )
            validQuestPool[questId] = 0
            continue
        potentialToNpc = getQuestToNpcId(questId)
        if currentNpc.getNpcId() == potentialToNpc:
            if notify.getDebug():
                notify.debug(
                    "filterQuests: Removed %s because potentialToNpc is currentNpc"
                    % questId
                )
            validQuestPool[questId] = 0
            continue
        if not getQuestClass(questId).filterFunc(av):
            if notify.getDebug():
                notify.debug("filterQuests: Removed %s because of filterFunc" % questId)
            validQuestPool[questId] = 0
            continue
        for quest in currentQuests:
            fromNpcId = quest[1]
            toNpcId = quest[2]
            if potentialToNpc == toNpcId and toNpcId != ToonHQ:
                validQuestPool[questId] = 0
                if notify.getDebug():
                    notify.debug(
                        "filterQuests: Removed %s because npc involved" % questId
                    )
                break

    finalQuestPool = [key for key in list(validQuestPool.keys()) if validQuestPool[key]]
    if notify.getDebug():
        notify.debug("filterQuests: finalQuestPool: %s" % finalQuestPool)
    return finalQuestPool


def chooseTrackChoiceQuest(tier, av, fixed=0):
    def fixAndCallAgain():
        if not fixed and av.fixTrackAccess():
            notify.info("av %s trackAccess fixed: %s" % (av.getDoId(), trackAccess))
            return chooseTrackChoiceQuest(tier, av, fixed=1)
        else:
            return None
        return None

    bestQuest = None
    trackAccess = av.getTrackAccess()
    if tier == RR_TIER:
        if trackAccess[ToontownBattleGlobals.HEAL_TRACK] == 1:
            bestQuest = 3004
        elif trackAccess[ToontownBattleGlobals.SOUND_TRACK] == 1:
            bestQuest = 3003
        else:
            notify.warning(
                "av %s has bogus trackAccess: %s" % (av.getDoId(), trackAccess)
            )
            return fixAndCallAgain()
    elif tier == OO_TIER:
        if trackAccess[ToontownBattleGlobals.TRAP_TRACK] == 1:
            if trackAccess[ToontownBattleGlobals.SOUND_TRACK] == 1:
                if trackAccess[ToontownBattleGlobals.DROP_TRACK] == 1:
                    bestQuest = 5004
                elif trackAccess[ToontownBattleGlobals.LURE_TRACK] == 1:
                    bestQuest = 5003
                else:
                    notify.warning(
                        "av %s has bogus trackAccess: %s" % (av.getDoId(), trackAccess)
                    )
                    return fixAndCallAgain()
            elif trackAccess[ToontownBattleGlobals.HEAL_TRACK] == 1:
                if trackAccess[ToontownBattleGlobals.DROP_TRACK] == 1:
                    bestQuest = 5002
                elif trackAccess[ToontownBattleGlobals.LURE_TRACK] == 1:
                    bestQuest = 5001
                else:
                    notify.warning(
                        "av %s has bogus trackAccess: %s" % (av.getDoId(), trackAccess)
                    )
                    return fixAndCallAgain()
        elif trackAccess[ToontownBattleGlobals.SOUND_TRACK] == 0:
            bestQuest = 5005
        elif trackAccess[ToontownBattleGlobals.HEAL_TRACK] == 0:
            bestQuest = 5006
        elif trackAccess[ToontownBattleGlobals.DROP_TRACK] == 0:
            bestQuest = 5007
        elif trackAccess[ToontownBattleGlobals.LURE_TRACK] == 0:
            bestQuest = 5008
        else:
            notify.warning(
                "av %s has bogus trackAccess: %s" % (av.getDoId(), trackAccess)
            )
            return fixAndCallAgain()
    else:
        if notify.getDebug():
            notify.debug(
                "questPool for reward 400 had no dynamic choice, tier: %s" % tier
            )
        bestQuest = seededRandomChoice(Tier2Reward2QuestsDict[tier][400])
    if notify.getDebug():
        notify.debug(
            "chooseTrackChoiceQuest: avId: %s trackAccess: %s tier: %s bestQuest: %s"
            % (av.getDoId(), trackAccess, tier, bestQuest)
        )
    return bestQuest


def chooseMatchingQuest(tier, validQuestPool, rewardId, npc, av):
    questsMatchingReward = Tier2Reward2QuestsDict[tier].get(rewardId, [])
    if notify.getDebug():
        notify.debug(
            "questsMatchingReward: %s tier: %s = %s"
            % (rewardId, tier, questsMatchingReward)
        )
    if (
        rewardId == 400
        and QuestDict[questsMatchingReward[0]][QuestDictNextQuestIndex] == NA
    ):
        bestQuest = chooseTrackChoiceQuest(tier, av)
        if notify.getDebug():
            notify.debug(
                "single part track choice quest: %s tier: %s avId: %s trackAccess: %s bestQuest: %s"
                % (rewardId, tier, av.getDoId(), av.getTrackAccess(), bestQuest)
            )
    else:
        validQuestsMatchingReward = PythonUtil.intersection(
            questsMatchingReward, validQuestPool
        )
        if notify.getDebug():
            notify.debug(
                "validQuestsMatchingReward: %s tier: %s = %s"
                % (rewardId, tier, validQuestsMatchingReward)
            )
        if validQuestsMatchingReward:
            bestQuest = seededRandomChoice(validQuestsMatchingReward)
        else:
            questsMatchingReward = Tier2Reward2QuestsDict[tier].get(
                AnyCashbotSuitPart, []
            )
            if notify.getDebug():
                notify.debug(
                    "questsMatchingReward: AnyCashbotSuitPart tier: %s = %s"
                    % (tier, questsMatchingReward)
                )
            validQuestsMatchingReward = PythonUtil.intersection(
                questsMatchingReward, validQuestPool
            )
            if validQuestsMatchingReward:
                if notify.getDebug():
                    notify.debug(
                        "validQuestsMatchingReward: AnyCashbotSuitPart tier: %s = %s"
                        % (tier, validQuestsMatchingReward)
                    )
                bestQuest = seededRandomChoice(validQuestsMatchingReward)
            else:
                questsMatchingReward = Tier2Reward2QuestsDict[tier].get(
                    AnyLawbotSuitPart, []
                )
                if notify.getDebug():
                    notify.debug(
                        "questsMatchingReward: AnyLawbotSuitPart tier: %s = %s"
                        % (tier, questsMatchingReward)
                    )
                validQuestsMatchingReward = PythonUtil.intersection(
                    questsMatchingReward, validQuestPool
                )
                if validQuestsMatchingReward:
                    if notify.getDebug():
                        notify.debug(
                            "validQuestsMatchingReward: AnyLawbotSuitPart tier: %s = %s"
                            % (tier, validQuestsMatchingReward)
                        )
                    bestQuest = seededRandomChoice(validQuestsMatchingReward)
                else:
                    questsMatchingReward = Tier2Reward2QuestsDict[tier].get(Any, [])
                    if notify.getDebug():
                        notify.debug(
                            "questsMatchingReward: Any tier: %s = %s"
                            % (tier, questsMatchingReward)
                        )
                    if not questsMatchingReward:
                        notify.warning("chooseMatchingQuests, no questsMatchingReward")
                        return None
                    validQuestsMatchingReward = PythonUtil.intersection(
                        questsMatchingReward, validQuestPool
                    )
                    if not validQuestsMatchingReward:
                        notify.warning(
                            "chooseMatchingQuests, no validQuestsMatchingReward"
                        )
                        return None
                    if notify.getDebug():
                        notify.debug(
                            "validQuestsMatchingReward: Any tier: %s = %s"
                            % (tier, validQuestsMatchingReward)
                        )
                    bestQuest = seededRandomChoice(validQuestsMatchingReward)
    return bestQuest


def transformReward(baseRewardId, av):
    if baseRewardId == 900:
        trackId, progress = av.getTrackProgress()
        if trackId == -1:
            notify.warning(
                "transformReward: asked to transform 900 but av is not training"
            )
            actualRewardId = baseRewardId
        else:
            actualRewardId = 900 + 1 + trackId
        return actualRewardId
    elif baseRewardId > 800 and baseRewardId < 900:
        trackId, progress = av.getTrackProgress()
        if trackId < 0:
            notify.warning(
                "transformReward: av: %s is training a track with none chosen!"
                % av.getDoId()
            )
            return 601
        else:
            actualRewardId = baseRewardId + 200 + trackId * 100
            return actualRewardId
    else:
        return baseRewardId


def chooseBestQuests(tier, currentNpc, av):
    if isLoopingFinalTier(tier):
        rewardHistory = [questDesc[3] for questDesc in av.quests]
    else:
        rewardHistory = av.getRewardHistory()[1]
    seedRandomGen(currentNpc.getNpcId(), av.getDoId(), tier, rewardHistory)
    numChoices = getNumChoices(tier)
    rewards = getNextRewards(numChoices, tier, av)
    if not rewards:
        return []
    possibleQuests = []
    possibleRewards = list(rewards)
    if Any not in possibleRewards:
        possibleRewards.append(Any)
    for rewardId in possibleRewards:
        possibleQuests.extend(Tier2Reward2QuestsDict[tier].get(rewardId, []))

    validQuestPool = filterQuests(possibleQuests, currentNpc, av)
    if not validQuestPool:
        return []
    if numChoices == 0:
        numChoices = 1
    bestQuests = []
    for i in range(numChoices):
        if len(validQuestPool) == 0:
            break
        if len(rewards) == 0:
            break
        rewardId = rewards.pop(0)
        bestQuestId = chooseMatchingQuest(
            tier, validQuestPool, rewardId, currentNpc, av
        )
        if bestQuestId is None:
            continue
        validQuestPool.remove(bestQuestId)
        bestQuestToNpcId = getQuestToNpcId(bestQuestId)
        if bestQuestToNpcId == Any:
            bestQuestToNpcId = 2003
        elif bestQuestToNpcId == Same:
            if currentNpc.getHq():
                bestQuestToNpcId = ToonHQ
            else:
                bestQuestToNpcId = currentNpc.getNpcId()
        elif bestQuestToNpcId == ToonHQ:
            bestQuestToNpcId = ToonHQ
        bestQuests.append([bestQuestId, rewardId, bestQuestToNpcId])

    for quest in bestQuests:
        quest[1] = transformReward(quest[1], av)

    return bestQuests


def questExists(id):
    return id in QuestDict


def getQuest(id):
    questEntry = QuestDict.get(id)
    if questEntry:
        questDesc = questEntry[QuestDictDescIndex]
        questClass = questDesc[0]
        return questClass(id, questDesc[1:])
    else:
        return None
    return None


def getQuestClass(id):
    questEntry = QuestDict.get(id)
    if questEntry:
        return questEntry[QuestDictDescIndex][0]
    else:
        return None
    return None


def getVisitSCStrings(npcId):
    if npcId == ToonHQ:
        strings = [
            TTLocalizer.QuestsRecoverItemQuestSeeHQSCString,
            TTLocalizer.QuestsRecoverItemQuestGoToHQSCString,
        ]
    elif npcId == ToonTailor:
        strings = [TTLocalizer.QuestsTailorQuestSCString]
    elif npcId:
        (
            npcName,
            hoodName,
            buildingArticle,
            buildingName,
            toStreet,
            streetName,
            isInPlayground,
        ) = getNpcInfo(npcId)
        strings = [TTLocalizer.QuestsVisitQuestSeeSCString % npcName]
        if isInPlayground:
            strings.append(
                TTLocalizer.QuestsRecoverItemQuestGoToPlaygroundSCString % hoodName
            )
        else:
            strings.append(
                TTLocalizer.QuestsRecoverItemQuestGoToStreetSCString
                % {"to": toStreet, "street": streetName, "hood": hoodName}
            )
        strings.extend(
            [
                TTLocalizer.QuestsRecoverItemQuestVisitBuildingSCString
                % (buildingArticle, buildingName),
                TTLocalizer.QuestsRecoverItemQuestWhereIsBuildingSCString
                % (buildingArticle, buildingName),
            ]
        )
    return strings


def getFinishToonTaskSCStrings(npcId):
    return [TTLocalizer.QuestsGenericFinishSCString] + getVisitSCStrings(npcId)


def chooseQuestDialog(id, status):
    questDialog = getQuestDialog(id).get(status)
    if questDialog == None:
        if status == QUEST:
            quest = getQuest(id)
            questDialog = quest.getDefaultQuestDialog()
        else:
            questDialog = DefaultDialog[status]
    if type(questDialog) == type(()):
        return random.choice(questDialog)
    else:
        return questDialog
    return


def chooseQuestDialogReject():
    return random.choice(DefaultReject)


def chooseQuestDialogTierNotDone():
    return random.choice(DefaultTierNotDone)


def getNpcInfo(npcId):
    npcName = NPCToons.getNPCName(npcId)
    npcZone = NPCToons.getNPCZone(npcId)
    hoodId = ZoneUtil.getCanonicalHoodId(npcZone)
    hoodName = base.cr.hoodMgr.getFullnameFromId(hoodId)
    buildingArticle = NPCToons.getBuildingArticle(npcZone)
    buildingName = NPCToons.getBuildingTitle(npcZone)
    branchId = ZoneUtil.getCanonicalBranchZone(npcZone)
    toStreet = ToontownGlobals.StreetNames[branchId][0]
    streetName = ToontownGlobals.StreetNames[branchId][-1]
    isInPlayground = ZoneUtil.isPlayground(branchId)
    return (
        npcName,
        hoodName,
        buildingArticle,
        buildingName,
        toStreet,
        streetName,
        isInPlayground,
    )


def getNpcLocationDialog(fromNpcId, toNpcId):
    if not toNpcId:
        return (None, None, None)
    fromNpcZone = None
    fromBranchId = None
    if fromNpcId:
        fromNpcZone = NPCToons.getNPCZone(fromNpcId)
        fromBranchId = ZoneUtil.getCanonicalBranchZone(fromNpcZone)
    toNpcZone = NPCToons.getNPCZone(toNpcId)
    toBranchId = ZoneUtil.getCanonicalBranchZone(toNpcZone)
    (
        toNpcName,
        toHoodName,
        toBuildingArticle,
        toBuildingName,
        toStreetTo,
        toStreetName,
        isInPlayground,
    ) = getNpcInfo(toNpcId)
    if fromBranchId == toBranchId:
        if isInPlayground:
            streetDesc = TTLocalizer.QuestsStreetLocationThisPlayground
        else:
            streetDesc = TTLocalizer.QuestsStreetLocationThisStreet
    elif isInPlayground:
        streetDesc = TTLocalizer.QuestsStreetLocationNamedPlayground % toHoodName
    else:
        streetDesc = TTLocalizer.QuestsStreetLocationNamedStreet % {
            "toStreetName": toStreetName,
            "toHoodName": toHoodName,
        }
    paragraph = TTLocalizer.QuestsLocationParagraph % {
        "building": TTLocalizer.QuestsLocationBuilding % toNpcName,
        "buildingName": toBuildingName,
        "buildingVerb": TTLocalizer.QuestsLocationBuildingVerb,
        "street": streetDesc,
    }
    return (paragraph, toBuildingName, streetDesc)


def fillInQuestNames(text, avName=None, fromNpcId=None, toNpcId=None):
    text = copy.deepcopy(text)
    if avName != None:
        text = str.replace(text, "_avName_", avName)
    if toNpcId:
        if toNpcId == ToonHQ:
            toNpcName = TTLocalizer.QuestsHQOfficerFillin
            where = TTLocalizer.QuestsHQWhereFillin
            buildingName = TTLocalizer.QuestsHQBuildingNameFillin
            streetDesc = TTLocalizer.QuestsHQLocationNameFillin
        elif toNpcId == ToonTailor:
            toNpcName = TTLocalizer.QuestsTailorFillin
            where = TTLocalizer.QuestsTailorWhereFillin
            buildingName = TTLocalizer.QuestsTailorBuildingNameFillin
            streetDesc = TTLocalizer.QuestsTailorLocationNameFillin
        else:
            toNpcName = str(NPCToons.getNPCName(toNpcId))
            where, buildingName, streetDesc = getNpcLocationDialog(fromNpcId, toNpcId)
        text = str.replace(text, "_toNpcName_", toNpcName)
        text = str.replace(text, "_where_", where)
        text = str.replace(text, "_buildingName_", buildingName)
        text = str.replace(text, "_streetDesc_", streetDesc)
    return text


def getVisitingQuest():
    return VisitQuest(VISIT_QUEST_ID)


class Reward:
    def __init__(self, id, reward):
        self.id = id
        self.reward = reward

    def getId(self):
        return self.id

    def getType(self):
        return self.__class__

    def getAmount(self):
        return None

    def sendRewardAI(self, av):
        raise "not implemented"

    def countReward(self, qrc):
        raise "not implemented"

    def getString(self):
        return "undefined"

    def getPosterString(self):
        return "base class"


class MaxHpReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getAmount(self):
        return self.reward[0]

    def sendRewardAI(self, av):
        maxHp = av.getMaxHp()
        maxHp = min(ToontownGlobals.MaxHpLimit, maxHp + self.getAmount())
        av.b_setMaxHp(maxHp)
        av.toonUp(maxHp)

    def countReward(self, qrc):
        qrc.maxHp += self.getAmount()

    def getString(self):
        return TTLocalizer.QuestsMaxHpReward % self.getAmount()

    def getPosterString(self):
        return TTLocalizer.QuestsMaxHpRewardPoster % self.getAmount()


class MoneyReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getAmount(self):
        return self.reward[0]

    def sendRewardAI(self, av):
        money = av.getMoney()
        maxMoney = av.getMaxMoney()
        av.addMoney(self.getAmount())

    def countReward(self, qrc):
        qrc.money += self.getAmount()

    def getString(self):
        amt = self.getAmount()
        if amt == 1:
            return TTLocalizer.QuestsMoneyRewardSingular
        else:
            return TTLocalizer.QuestsMoneyRewardPlural % amt

    def getPosterString(self):
        amt = self.getAmount()
        if amt == 1:
            return TTLocalizer.QuestsMoneyRewardPosterSingular
        else:
            return TTLocalizer.QuestsMoneyRewardPosterPlural % amt


class MaxMoneyReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getAmount(self):
        return self.reward[0]

    def sendRewardAI(self, av):
        av.b_setMaxMoney(self.getAmount())

    def countReward(self, qrc):
        qrc.maxMoney = self.getAmount()

    def getString(self):
        amt = self.getAmount()
        if amt == 1:
            return TTLocalizer.QuestsMaxMoneyRewardSingular
        else:
            return TTLocalizer.QuestsMaxMoneyRewardPlural % amt

    def getPosterString(self):
        amt = self.getAmount()
        if amt == 1:
            return TTLocalizer.QuestsMaxMoneyRewardPosterSingular
        else:
            return TTLocalizer.QuestsMaxMoneyRewardPosterPlural % amt


class MaxGagCarryReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getAmount(self):
        return self.reward[0]

    def getName(self):
        return self.reward[1]

    def sendRewardAI(self, av):
        av.b_setMaxCarry(self.getAmount())

    def countReward(self, qrc):
        qrc.maxCarry = self.getAmount()

    def getString(self):
        name = self.getName()
        amt = self.getAmount()
        return TTLocalizer.QuestsMaxGagCarryReward % {"name": name, "num": amt}

    def getPosterString(self):
        name = self.getName()
        amt = self.getAmount()
        return TTLocalizer.QuestsMaxGagCarryRewardPoster % {"name": name, "num": amt}


class MaxQuestCarryReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getAmount(self):
        return self.reward[0]

    def sendRewardAI(self, av):
        av.b_setQuestCarryLimit(self.getAmount())

    def countReward(self, qrc):
        qrc.questCarryLimit = self.getAmount()

    def getString(self):
        amt = self.getAmount()
        return TTLocalizer.QuestsMaxQuestCarryReward % amt

    def getPosterString(self):
        amt = self.getAmount()
        return TTLocalizer.QuestsMaxQuestCarryRewardPoster % amt


class TeleportReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getZone(self):
        return self.reward[0]

    def sendRewardAI(self, av):
        av.addTeleportAccess(self.getZone())

    def countReward(self, qrc):
        qrc.addTeleportAccess(self.getZone())

    def getString(self):
        hoodName = ToontownGlobals.hoodNameMap[self.getZone()][-1]
        return TTLocalizer.QuestsTeleportReward % hoodName

    def getPosterString(self):
        hoodName = ToontownGlobals.hoodNameMap[self.getZone()][-1]
        return TTLocalizer.QuestsTeleportRewardPoster % hoodName


TrackTrainingQuotas = {
    ToontownBattleGlobals.HEAL_TRACK: 15,
    ToontownBattleGlobals.TRAP_TRACK: 15,
    ToontownBattleGlobals.LURE_TRACK: 15,
    ToontownBattleGlobals.SOUND_TRACK: 15,
    ToontownBattleGlobals.THROW_TRACK: 15,
    ToontownBattleGlobals.SQUIRT_TRACK: 15,
    ToontownBattleGlobals.DROP_TRACK: 15,
}


class TrackTrainingReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getTrack(self):
        track = self.reward[0]
        if track == None:
            track = 0
        return track

    def sendRewardAI(self, av):
        av.b_setTrackProgress(self.getTrack(), 0)

    def countReward(self, qrc):
        qrc.trackProgressId = self.getTrack()
        qrc.trackProgress = 0

    def getString(self):
        trackName = ToontownBattleGlobals.Tracks[self.getTrack()].capitalize()
        return TTLocalizer.QuestsTrackTrainingReward % trackName

    def getPosterString(self):
        return TTLocalizer.QuestsTrackTrainingRewardPoster


class TrackProgressReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getTrack(self):
        track = self.reward[0]
        if track == None:
            track = 0
        return track

    def getProgressIndex(self):
        return self.reward[1]

    def sendRewardAI(self, av):
        av.addTrackProgress(self.getTrack(), self.getProgressIndex())

    def countReward(self, qrc):
        qrc.addTrackProgress(self.getTrack(), self.getProgressIndex())

    def getString(self):
        trackName = ToontownBattleGlobals.Tracks[self.getTrack()].capitalize()
        return TTLocalizer.QuestsTrackProgressReward % {
            "frameNum": self.getProgressIndex(),
            "trackName": trackName,
        }

    def getPosterString(self):
        trackName = ToontownBattleGlobals.Tracks[self.getTrack()].capitalize()
        return TTLocalizer.QuestsTrackProgressRewardPoster % {
            "trackName": trackName,
            "frameNum": self.getProgressIndex(),
        }


class TrackCompleteReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getTrack(self):
        track = self.reward[0]
        if track == None:
            track = 0
        return track

    def sendRewardAI(self, av):
        av.addTrackAccess(self.getTrack())
        av.clearTrackProgress()

    def countReward(self, qrc):
        qrc.addTrackAccess(self.getTrack())
        qrc.clearTrackProgress()

    def getString(self):
        trackName = ToontownBattleGlobals.Tracks[self.getTrack()].capitalize()
        return TTLocalizer.QuestsTrackCompleteReward % trackName

    def getPosterString(self):
        trackName = ToontownBattleGlobals.Tracks[self.getTrack()].capitalize()
        return TTLocalizer.QuestsTrackCompleteRewardPoster % trackName


class ClothingTicketReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def sendRewardAI(self, av):
        pass

    def countReward(self, qrc):
        pass

    def getString(self):
        return TTLocalizer.QuestsClothingTicketReward

    def getPosterString(self):
        return TTLocalizer.QuestsClothingTicketRewardPoster


class TIPClothingTicketReward(ClothingTicketReward):
    def __init__(self, id, reward):
        ClothingTicketReward.__init__(self, id, reward)

    def getString(self):
        return TTLocalizer.TIPQuestsClothingTicketReward

    def getPosterString(self):
        return TTLocalizer.TIPQuestsClothingTicketRewardPoster


class CheesyEffectReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getEffect(self):
        return self.reward[0]

    def getHoodId(self):
        return self.reward[1]

    def getDurationMinutes(self):
        return self.reward[2]

    def sendRewardAI(self, av):
        expireTime = int(time.time() / 60 + 0.5) + self.getDurationMinutes()
        av.b_setCheesyEffect(self.getEffect(), self.getHoodId(), expireTime)

    def countReward(self, qrc):
        pass

    def getString(self):
        effect = self.getEffect()
        hoodId = self.getHoodId()
        duration = self.getDurationMinutes()
        string = TTLocalizer.CheesyEffectMinutes
        if duration > 90:
            duration = int((duration + 30) / 60)
            string = TTLocalizer.CheesyEffectHours
            if duration > 36:
                duration = int((duration + 12) / 24)
                string = TTLocalizer.CheesyEffectDays
        desc = TTLocalizer.CheesyEffectDescriptions[effect][1]
        if hoodId == 0:
            whileStr = ""
        elif hoodId == 1:
            whileStr = (
                TTLocalizer.CheesyEffectExceptIn % TTLocalizer.ToonIslandCentral[-1]
            )
        else:
            hoodName = base.cr.hoodMgr.getFullnameFromId(hoodId)
            whileStr = TTLocalizer.CheesyEffectWhileYouAreIn % hoodName
        if duration:
            return string % {"time": duration, "effectName": desc, "whileIn": whileStr}
        else:
            return TTLocalizer.CheesyEffectIndefinite % {
                "effectName": desc,
                "whileIn": whileStr,
            }

    def getPosterString(self):
        effect = self.getEffect()
        desc = TTLocalizer.CheesyEffectDescriptions[effect][0]
        return TTLocalizer.QuestsCheesyEffectRewardPoster % desc


class CogSuitPartReward(Reward):
    trackNames = [
        TTLocalizer.Bossbot,
        TTLocalizer.Lawbot,
        TTLocalizer.Cashbot,
        TTLocalizer.Sellbot,
    ]

    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getCogTrack(self):
        return self.reward[0]

    def getCogPart(self):
        return self.reward[1]

    def sendRewardAI(self, av):
        dept = self.getCogTrack()
        part = self.getCogPart()
        av.giveCogPart(part, dept)

    def countReward(self, qrc):
        pass

    def getCogTrackName(self):
        index = ToontownGlobals.cogDept2index[self.getCogTrack()]
        return CogSuitPartReward.trackNames[index]

    def getCogPartName(self):
        index = ToontownGlobals.cogDept2index[self.getCogTrack()]
        return CogDisguiseGlobals.PartsQueryNames[index][self.getCogPart()]

    def getString(self):
        return TTLocalizer.QuestsCogSuitPartReward % {
            "cogTrack": self.getCogTrackName(),
            "part": self.getCogPartName(),
        }

    def getPosterString(self):
        return TTLocalizer.QuestsCogSuitPartRewardPoster % {
            "cogTrack": self.getCogTrackName(),
            "part": self.getCogPartName(),
        }


def getRewardClass(id):
    reward = RewardDict.get(id)
    if reward:
        return reward[0]
    else:
        return None
    return None


def getReward(id):
    reward = RewardDict.get(id)
    if reward:
        rewardClass = reward[0]
        return rewardClass(id, reward[1:])
    else:
        notify.warning("getReward(): id %s not found." % id)
        return None
    return None


def getNextRewards(numChoices, tier, av):
    rewardTier = list(getRewardsInTier(tier))
    optRewards = list(getOptionalRewardsInTier(tier))
    if av.getGameAccess() == OTPGlobals.AccessFull and tier == TT_TIER + 3:
        optRewards = []
    if isLoopingFinalTier(tier):
        rewardHistory = [questDesc[3] for questDesc in av.quests]
        if notify.getDebug():
            notify.debug(
                "getNextRewards: current rewards (history): %s" % rewardHistory
            )
    else:
        rewardHistory = av.getRewardHistory()[1]
        if notify.getDebug():
            notify.debug("getNextRewards: rewardHistory: %s" % rewardHistory)
    if notify.getDebug():
        notify.debug("getNextRewards: rewardTier: %s" % rewardTier)
        notify.debug("getNextRewards: numChoices: %s" % numChoices)
    for rewardId in getRewardsInTier(tier):
        if getRewardClass(rewardId) == CogSuitPartReward:
            deptStr = RewardDict.get(rewardId)[1]
            cogPart = RewardDict.get(rewardId)[2]
            dept = ToontownGlobals.cogDept2index[deptStr]
            if av.hasCogPart(cogPart, dept):
                notify.debug(
                    "getNextRewards: already has cog part: %s dept: %s"
                    % (cogPart, dept)
                )
                rewardTier.remove(rewardId)
            else:
                notify.debug(
                    "getNextRewards: keeping quest for cog part: %s dept: %s"
                    % (cogPart, dept)
                )

    for rewardId in rewardHistory:
        if rewardId in rewardTier:
            rewardTier.remove(rewardId)
        elif rewardId in optRewards:
            optRewards.remove(rewardId)
        elif rewardId in (901, 902, 903, 904, 905, 906, 907):
            genericRewardId = 900
            if genericRewardId in rewardTier:
                rewardTier.remove(genericRewardId)
        elif rewardId > 1000 and rewardId < 1699:
            index = rewardId % 100
            genericRewardId = 800 + index
            if genericRewardId in rewardTier:
                rewardTier.remove(genericRewardId)

    if numChoices == 0:
        if len(rewardTier) == 0:
            return []
        else:
            return [rewardTier[0]]
    rewardPool = rewardTier[:numChoices]
    for i in range(len(rewardPool), numChoices * 2):
        if optRewards:
            optionalReward = seededRandomChoice(optRewards)
            optRewards.remove(optionalReward)
            rewardPool.append(optionalReward)
        else:
            break

    if notify.getDebug():
        notify.debug("getNextRewards: starting reward pool: %s" % rewardPool)
    if len(rewardPool) == 0:
        if notify.getDebug():
            notify.debug("getNextRewards: no rewards left at all")
        return []
    finalRewardPool = [rewardPool.pop(0)]
    for i in range(numChoices - 1):
        if len(rewardPool) == 0:
            break
        selectedReward = seededRandomChoice(rewardPool)
        rewardPool.remove(selectedReward)
        finalRewardPool.append(selectedReward)

    if notify.getDebug():
        notify.debug("getNextRewards: final reward pool: %s" % finalRewardPool)
    return finalRewardPool


RewardDict = {
    100: (MaxHpReward, 1),
    101: (MaxHpReward, 2),
    102: (MaxHpReward, 3),
    103: (MaxHpReward, 4),
    104: (MaxHpReward, 5),
    105: (MaxHpReward, 6),
    106: (MaxHpReward, 7),
    107: (MaxHpReward, 8),
    108: (MaxHpReward, 9),
    109: (MaxHpReward, 10),
    200: (MaxGagCarryReward, 30, TTLocalizer.QuestsMediumPouch),
    201: (MaxGagCarryReward, 40, TTLocalizer.QuestsLargePouch),
    202: (MaxGagCarryReward, 50, TTLocalizer.QuestsSmallBag),
    203: (MaxGagCarryReward, 60, TTLocalizer.QuestsMediumBag),
    204: (MaxGagCarryReward, 70, TTLocalizer.QuestsLargeBag),
    205: (MaxGagCarryReward, 80, TTLocalizer.QuestsSmallBackpack),
    206: (MaxGagCarryReward, 90, TTLocalizer.QuestsMediumBackpack),
    207: (MaxGagCarryReward, 100, TTLocalizer.QuestsLargeBackpack),
    300: (TeleportReward, ToontownGlobals.ToonIslandCentral),
    301: (TeleportReward, ToontownGlobals.RainbowRise),
    302: (TeleportReward, ToontownGlobals.WitheringWoods),
    303: (TeleportReward, ToontownGlobals.OliveOasis),
    304: (TeleportReward, ToontownGlobals.CirrusCircus),
    305: (TeleportReward, ToontownGlobals.MintyMines),
    400: (TrackTrainingReward, None),
    401: (TrackTrainingReward, ToontownBattleGlobals.HEAL_TRACK),
    402: (TrackTrainingReward, ToontownBattleGlobals.TRAP_TRACK),
    403: (TrackTrainingReward, ToontownBattleGlobals.LURE_TRACK),
    404: (TrackTrainingReward, ToontownBattleGlobals.SOUND_TRACK),
    405: (TrackTrainingReward, ToontownBattleGlobals.THROW_TRACK),
    406: (TrackTrainingReward, ToontownBattleGlobals.SQUIRT_TRACK),
    407: (TrackTrainingReward, ToontownBattleGlobals.DROP_TRACK),
    500: (MaxQuestCarryReward, 2),
    501: (MaxQuestCarryReward, 3),
    502: (MaxQuestCarryReward, 4),
    600: (MoneyReward, 10),
    601: (MoneyReward, 20),
    602: (MoneyReward, 40),
    603: (MoneyReward, 60),
    604: (MoneyReward, 100),
    605: (MoneyReward, 150),
    606: (MoneyReward, 200),
    607: (MoneyReward, 250),
    608: (MoneyReward, 300),
    609: (MoneyReward, 400),
    610: (MoneyReward, 500),
    611: (MoneyReward, 600),
    612: (MoneyReward, 700),
    613: (MoneyReward, 800),
    614: (MoneyReward, 900),
    615: (MoneyReward, 1000),
    616: (MoneyReward, 1100),
    617: (MoneyReward, 1200),
    618: (MoneyReward, 1300),
    619: (MoneyReward, 1400),
    620: (MoneyReward, 1500),
    621: (MoneyReward, 1750),
    622: (MoneyReward, 2000),
    623: (MoneyReward, 2500),
    700: (MaxMoneyReward, 50),
    701: (MaxMoneyReward, 60),
    702: (MaxMoneyReward, 80),
    703: (MaxMoneyReward, 100),
    704: (MaxMoneyReward, 120),
    705: (MaxMoneyReward, 150),
    706: (MaxMoneyReward, 200),
    707: (MaxMoneyReward, 250),
    801: (TrackProgressReward, None, 1),
    802: (TrackProgressReward, None, 2),
    803: (TrackProgressReward, None, 3),
    804: (TrackProgressReward, None, 4),
    805: (TrackProgressReward, None, 5),
    806: (TrackProgressReward, None, 6),
    807: (TrackProgressReward, None, 7),
    808: (TrackProgressReward, None, 8),
    809: (TrackProgressReward, None, 9),
    810: (TrackProgressReward, None, 10),
    811: (TrackProgressReward, None, 11),
    812: (TrackProgressReward, None, 12),
    813: (TrackProgressReward, None, 13),
    814: (TrackProgressReward, None, 14),
    815: (TrackProgressReward, None, 15),
    110: (TIPClothingTicketReward,),
    1000: (ClothingTicketReward,),
    1001: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 1),
    1002: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 2),
    1003: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 3),
    1004: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 4),
    1005: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 5),
    1006: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 6),
    1007: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 7),
    1008: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 8),
    1009: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 9),
    1010: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 10),
    1011: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 11),
    1012: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 12),
    1013: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 13),
    1014: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 14),
    1015: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 15),
    1101: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 1),
    1102: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 2),
    1103: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 3),
    1104: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 4),
    1105: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 5),
    1106: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 6),
    1107: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 7),
    1108: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 8),
    1109: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 9),
    1110: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 10),
    1111: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 11),
    1112: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 12),
    1113: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 13),
    1114: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 14),
    1115: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 15),
    1201: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 1),
    1202: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 2),
    1203: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 3),
    1204: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 4),
    1205: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 5),
    1206: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 6),
    1207: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 7),
    1208: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 8),
    1209: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 9),
    1210: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 10),
    1211: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 11),
    1212: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 12),
    1213: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 13),
    1214: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 14),
    1215: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 15),
    1301: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 1),
    1302: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 2),
    1303: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 3),
    1304: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 4),
    1305: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 5),
    1306: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 6),
    1307: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 7),
    1308: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 8),
    1309: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 9),
    1310: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 10),
    1311: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 11),
    1312: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 12),
    1313: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 13),
    1314: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 14),
    1315: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 15),
    1601: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 1),
    1602: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 2),
    1603: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 3),
    1604: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 4),
    1605: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 5),
    1606: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 6),
    1607: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 7),
    1608: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 8),
    1609: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 9),
    1610: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 10),
    1611: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 11),
    1612: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 12),
    1613: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 13),
    1614: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 14),
    1615: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 15),
    900: (TrackCompleteReward, None),
    901: (TrackCompleteReward, ToontownBattleGlobals.HEAL_TRACK),
    902: (TrackCompleteReward, ToontownBattleGlobals.TRAP_TRACK),
    903: (TrackCompleteReward, ToontownBattleGlobals.LURE_TRACK),
    904: (TrackCompleteReward, ToontownBattleGlobals.SOUND_TRACK),
    905: (TrackCompleteReward, ToontownBattleGlobals.THROW_TRACK),
    906: (TrackCompleteReward, ToontownBattleGlobals.SQUIRT_TRACK),
    907: (TrackCompleteReward, ToontownBattleGlobals.DROP_TRACK),
    2205: (CheesyEffectReward, ToontownGlobals.CEBigToon, 2000, 10),
    2206: (CheesyEffectReward, ToontownGlobals.CESmallToon, 2000, 10),
    2101: (CheesyEffectReward, ToontownGlobals.CEBigHead, 1000, 10),
    2102: (CheesyEffectReward, ToontownGlobals.CESmallHead, 1000, 10),
    2105: (CheesyEffectReward, ToontownGlobals.CEBigToon, 0, 20),
    2106: (CheesyEffectReward, ToontownGlobals.CESmallToon, 0, 20),
    2501: (CheesyEffectReward, ToontownGlobals.CEBigHead, 5000, 60),
    2502: (CheesyEffectReward, ToontownGlobals.CESmallHead, 5000, 60),
    2503: (CheesyEffectReward, ToontownGlobals.CEBigLegs, 5000, 20),
    2504: (CheesyEffectReward, ToontownGlobals.CESmallLegs, 5000, 20),
    2505: (CheesyEffectReward, ToontownGlobals.CEBigToon, 0, 60),
    2506: (CheesyEffectReward, ToontownGlobals.CESmallToon, 0, 60),
    2401: (CheesyEffectReward, ToontownGlobals.CEBigHead, 1, 120),
    2402: (CheesyEffectReward, ToontownGlobals.CESmallHead, 1, 120),
    2403: (CheesyEffectReward, ToontownGlobals.CEBigLegs, 4000, 60),
    2404: (CheesyEffectReward, ToontownGlobals.CESmallLegs, 4000, 60),
    2405: (CheesyEffectReward, ToontownGlobals.CEBigToon, 0, 120),
    2406: (CheesyEffectReward, ToontownGlobals.CESmallToon, 0, 120),
    2407: (CheesyEffectReward, ToontownGlobals.CEFlatPortrait, 4000, 30),
    2408: (CheesyEffectReward, ToontownGlobals.CEFlatProfile, 4000, 30),
    2409: (CheesyEffectReward, ToontownGlobals.CETransparent, 4000, 30),
    2410: (CheesyEffectReward, ToontownGlobals.CENoColor, 4000, 30),
    2301: (CheesyEffectReward, ToontownGlobals.CEBigHead, 1, 360),
    2302: (CheesyEffectReward, ToontownGlobals.CESmallHead, 1, 360),
    2303: (CheesyEffectReward, ToontownGlobals.CEBigLegs, 1, 360),
    2304: (CheesyEffectReward, ToontownGlobals.CESmallLegs, 1, 360),
    2305: (CheesyEffectReward, ToontownGlobals.CEBigToon, 0, 1440),
    2306: (CheesyEffectReward, ToontownGlobals.CESmallToon, 0, 1440),
    2307: (CheesyEffectReward, ToontownGlobals.CEFlatPortrait, 3000, 240),
    2308: (CheesyEffectReward, ToontownGlobals.CEFlatProfile, 3000, 240),
    2309: (CheesyEffectReward, ToontownGlobals.CETransparent, 1, 120),
    2310: (CheesyEffectReward, ToontownGlobals.CENoColor, 1, 120),
    2311: (CheesyEffectReward, ToontownGlobals.CEInvisible, 3000, 120),
    2900: (CheesyEffectReward, ToontownGlobals.CENormal, 0, 0),
    2901: (CheesyEffectReward, ToontownGlobals.CEBigHead, 1, 1440),
    2902: (CheesyEffectReward, ToontownGlobals.CESmallHead, 1, 1440),
    2903: (CheesyEffectReward, ToontownGlobals.CEBigLegs, 1, 1440),
    2904: (CheesyEffectReward, ToontownGlobals.CESmallLegs, 1, 1440),
    2905: (CheesyEffectReward, ToontownGlobals.CEBigToon, 0, 1440),
    2906: (CheesyEffectReward, ToontownGlobals.CESmallToon, 0, 1440),
    2907: (CheesyEffectReward, ToontownGlobals.CEFlatPortrait, 1, 1440),
    2908: (CheesyEffectReward, ToontownGlobals.CEFlatProfile, 1, 1440),
    2909: (CheesyEffectReward, ToontownGlobals.CETransparent, 1, 1440),
    2910: (CheesyEffectReward, ToontownGlobals.CENoColor, 1, 1440),
    2911: (CheesyEffectReward, ToontownGlobals.CEInvisible, 1, 1440),
    2920: (CheesyEffectReward, ToontownGlobals.CENormal, 0, 0),
    2921: (CheesyEffectReward, ToontownGlobals.CEBigHead, 1, 2880),
    2922: (CheesyEffectReward, ToontownGlobals.CESmallHead, 1, 2880),
    2923: (CheesyEffectReward, ToontownGlobals.CEBigLegs, 1, 2880),
    2924: (CheesyEffectReward, ToontownGlobals.CESmallLegs, 1, 2880),
    2925: (CheesyEffectReward, ToontownGlobals.CEBigToon, 0, 2880),
    2926: (CheesyEffectReward, ToontownGlobals.CESmallToon, 0, 2880),
    2927: (CheesyEffectReward, ToontownGlobals.CEFlatPortrait, 1, 2880),
    2928: (CheesyEffectReward, ToontownGlobals.CEFlatProfile, 1, 2880),
    2929: (CheesyEffectReward, ToontownGlobals.CETransparent, 1, 2880),
    2930: (CheesyEffectReward, ToontownGlobals.CENoColor, 1, 2880),
    2931: (CheesyEffectReward, ToontownGlobals.CEInvisible, 1, 2880),
    2940: (CheesyEffectReward, ToontownGlobals.CENormal, 0, 0),
    2941: (CheesyEffectReward, ToontownGlobals.CEBigHead, 1, 10080),
    2942: (CheesyEffectReward, ToontownGlobals.CESmallHead, 1, 10080),
    2943: (CheesyEffectReward, ToontownGlobals.CEBigLegs, 1, 10080),
    2944: (CheesyEffectReward, ToontownGlobals.CESmallLegs, 1, 10080),
    2945: (CheesyEffectReward, ToontownGlobals.CEBigToon, 0, 10080),
    2946: (CheesyEffectReward, ToontownGlobals.CESmallToon, 0, 10080),
    2947: (CheesyEffectReward, ToontownGlobals.CEFlatPortrait, 1, 10080),
    2948: (CheesyEffectReward, ToontownGlobals.CEFlatProfile, 1, 10080),
    2949: (CheesyEffectReward, ToontownGlobals.CETransparent, 1, 10080),
    2950: (CheesyEffectReward, ToontownGlobals.CENoColor, 1, 10080),
    2951: (CheesyEffectReward, ToontownGlobals.CEInvisible, 1, 10080),
    2960: (CheesyEffectReward, ToontownGlobals.CENormal, 0, 0),
    2961: (CheesyEffectReward, ToontownGlobals.CEBigHead, 1, 43200),
    2962: (CheesyEffectReward, ToontownGlobals.CESmallHead, 1, 43200),
    2963: (CheesyEffectReward, ToontownGlobals.CEBigLegs, 1, 43200),
    2964: (CheesyEffectReward, ToontownGlobals.CESmallLegs, 1, 43200),
    2965: (CheesyEffectReward, ToontownGlobals.CEBigToon, 0, 43200),
    2966: (CheesyEffectReward, ToontownGlobals.CESmallToon, 0, 43200),
    2967: (CheesyEffectReward, ToontownGlobals.CEFlatPortrait, 1, 43200),
    2968: (CheesyEffectReward, ToontownGlobals.CEFlatProfile, 1, 43200),
    2969: (CheesyEffectReward, ToontownGlobals.CETransparent, 1, 43200),
    2970: (CheesyEffectReward, ToontownGlobals.CENoColor, 1, 43200),
    2971: (CheesyEffectReward, ToontownGlobals.CEInvisible, 1, 43200),
    4000: (CogSuitPartReward, "m", CogDisguiseGlobals.leftLegUpper),
    4001: (CogSuitPartReward, "m", CogDisguiseGlobals.leftLegLower),
    4002: (CogSuitPartReward, "m", CogDisguiseGlobals.leftLegFoot),
    4003: (CogSuitPartReward, "m", CogDisguiseGlobals.rightLegUpper),
    4004: (CogSuitPartReward, "m", CogDisguiseGlobals.rightLegLower),
    4005: (CogSuitPartReward, "m", CogDisguiseGlobals.rightLegFoot),
    4006: (CogSuitPartReward, "m", CogDisguiseGlobals.upperTorso),
    4007: (CogSuitPartReward, "m", CogDisguiseGlobals.torsoPelvis),
    4008: (CogSuitPartReward, "m", CogDisguiseGlobals.leftArmUpper),
    4009: (CogSuitPartReward, "m", CogDisguiseGlobals.leftArmLower),
    4010: (CogSuitPartReward, "m", CogDisguiseGlobals.rightArmUpper),
    4011: (CogSuitPartReward, "m", CogDisguiseGlobals.rightArmLower),
    4100: (CogSuitPartReward, "l", CogDisguiseGlobals.leftLegUpper),
    4101: (CogSuitPartReward, "l", CogDisguiseGlobals.leftLegLower),
    4102: (CogSuitPartReward, "l", CogDisguiseGlobals.leftLegFoot),
    4103: (CogSuitPartReward, "l", CogDisguiseGlobals.rightLegUpper),
    4104: (CogSuitPartReward, "l", CogDisguiseGlobals.rightLegLower),
    4105: (CogSuitPartReward, "l", CogDisguiseGlobals.rightLegFoot),
    4106: (CogSuitPartReward, "l", CogDisguiseGlobals.upperTorso),
    4107: (CogSuitPartReward, "l", CogDisguiseGlobals.torsoPelvis),
    4108: (CogSuitPartReward, "l", CogDisguiseGlobals.leftArmUpper),
    4109: (CogSuitPartReward, "l", CogDisguiseGlobals.leftArmLower),
    4110: (CogSuitPartReward, "l", CogDisguiseGlobals.leftArmHand),
    4111: (CogSuitPartReward, "l", CogDisguiseGlobals.rightArmUpper),
    4112: (CogSuitPartReward, "l", CogDisguiseGlobals.rightArmLower),
    4113: (CogSuitPartReward, "l", CogDisguiseGlobals.rightArmHand),
    4200: (CogSuitPartReward, "c", CogDisguiseGlobals.leftLegUpper),
    4201: (CogSuitPartReward, "c", CogDisguiseGlobals.leftLegLower),
    4202: (CogSuitPartReward, "c", CogDisguiseGlobals.leftLegFoot),
    4203: (CogSuitPartReward, "c", CogDisguiseGlobals.rightLegUpper),
    4204: (CogSuitPartReward, "c", CogDisguiseGlobals.rightLegLower),
    4205: (CogSuitPartReward, "c", CogDisguiseGlobals.rightLegFoot),
    4206: (CogSuitPartReward, "c", CogDisguiseGlobals.torsoLeftShoulder),
    4207: (CogSuitPartReward, "c", CogDisguiseGlobals.torsoRightShoulder),
    4208: (CogSuitPartReward, "c", CogDisguiseGlobals.torsoChest),
    4210: (CogSuitPartReward, "c", CogDisguiseGlobals.torsoPelvis),
    4211: (CogSuitPartReward, "c", CogDisguiseGlobals.leftArmUpper),
    4212: (CogSuitPartReward, "c", CogDisguiseGlobals.leftArmLower),
    4213: (CogSuitPartReward, "c", CogDisguiseGlobals.leftArmHand),
    4214: (CogSuitPartReward, "c", CogDisguiseGlobals.rightArmUpper),
    4215: (CogSuitPartReward, "c", CogDisguiseGlobals.rightArmLower),
    4216: (CogSuitPartReward, "c", CogDisguiseGlobals.rightArmHand),
}


def getNumTiers():
    return len(RequiredRewardTrackDict) - 1


def isLoopingFinalTier(tier):
    return tier == LOOPING_FINAL_TIER


def getRewardsInTier(tier):
    return RequiredRewardTrackDict.get(tier, [])


def getNumRewardsInTier(tier):
    return len(RequiredRewardTrackDict.get(tier, []))


def rewardTierExists(tier):
    return tier in RequiredRewardTrackDict


def getOptionalRewardsInTier(tier):
    return OptionalRewardTrackDict.get(tier, [])


def getRewardIdFromTrackId(trackId):
    return 401 + trackId


RequiredRewardTrackDict = {
    TT_TIER: (100,),
    TT_TIER + 1: (400,),
    TT_TIER
    + 2: (
        100,
        801,
        802,
        803,
        101,
        804,
        805,
        102,
        806,
        807,
        101,
        808,
        809,
        300,
        810,
        811,
        500,
        812,
        200,
        813,
        700,
        814,
        815,
    ),
    TT_TIER + 3: (900,),
    WW_TIER: (400,),
    WW_TIER
    + 1: (
        101,
        801,
        802,
        201,
        101,
        803,
        804,
        101,
        805,
        806,
        102,
        807,
        808,
        102,
        809,
        810,
        101,
        811,
        812,
        701,
        813,
        814,
        103,
        815,
        301,
    ),
    WW_TIER + 2: (900,),
    RR_TIER: (400,),
    RR_TIER
    + 1: (
        801,
        102,
        802,
        803,
        804,
        102,
        805,
        201,
        806,
        807,
        808,
        809,
        102,
        810,
        811,
        103,
        702,
        812,
        813,
        104,
        302,
        814,
        103,
        815,
    ),
    RR_TIER + 2: (900,),
    ELDER_TIER: (
        4000,
        4001,
        4002,
        4003,
        4004,
        4005,
        4006,
        4007,
        4008,
        4009,
        4010,
        4011,
    ),
}
OptionalRewardTrackDict = {
    TT_TIER: (),
    TT_TIER + 1: (),
    TT_TIER + 2: (1000, 601, 601, 602, 602, 2205, 2206, 2205, 2206),
    TT_TIER + 3: (1000, 601, 601, 602, 602, 2205, 2206, 2205, 2206),
    WW_TIER: (1000, 602, 602, 603, 603, 2101, 2102, 2105, 2106),
    WW_TIER + 1: (1000, 602, 602, 603, 603, 2101, 2102, 2105, 2106),
    WW_TIER + 2: (1000, 602, 602, 603, 603, 2101, 2102, 2105, 2106),
    RR_TIER: (1000, 603, 603, 604, 604, 2501, 2502, 2503, 2504, 2505, 2506),
    RR_TIER + 1: (1000, 603, 603, 604, 604, 2501, 2502, 2503, 2504, 2505, 2506),
    RR_TIER + 2: (1000, 603, 603, 604, 604, 2501, 2502, 2503, 2504, 2505, 2506),
    ELDER_TIER: (
        1000,
        1000,
        610,
        611,
        612,
        613,
        614,
        615,
        616,
        617,
        618,
        2961,
        2962,
        2963,
        2964,
        2965,
        2966,
        2967,
        2968,
        2969,
        2970,
        2971,
    ),
}


def isRewardOptional(tier, rewardId):
    return tier in OptionalRewardTrackDict and rewardId in OptionalRewardTrackDict[tier]


def getItemName(itemId):
    return ItemDict[itemId][0]


def getPluralItemName(itemId):
    return ItemDict[itemId][1]


def avatarHasTrolleyQuest(av):
    return len(av.quests) == 1 and av.quests[0][0] == TROLLEY_QUEST_ID


def avatarHasCompletedTrolleyQuest(av):
    return av.quests[0][4] > 0


def avatarHasFirstCogQuest(av):
    return len(av.quests) == 1 and av.quests[0][0] == FIRST_COG_QUEST_ID


def avatarHasCompletedFirstCogQuest(av):
    return av.quests[0][4] > 0


def avatarHasFriendQuest(av):
    return len(av.quests) == 1 and av.quests[0][0] == FRIEND_QUEST_ID


def avatarHasCompletedFriendQuest(av):
    return av.quests[0][4] > 0


def avatarHasPhoneQuest(av):
    return len(av.quests) == 1 and av.quests[0][0] == PHONE_QUEST_ID


def avatarHasCompletedPhoneQuest(av):
    return av.quests[0][4] > 0


def avatarWorkingOnRequiredRewards(av):
    tier = av.getRewardTier()
    rewardList = list(getRewardsInTier(tier))
    for i in range(len(rewardList)):
        actualRewardId = transformReward(rewardList[i], av)
        rewardList[i] = actualRewardId

    for questDesc in av.quests:
        questId = questDesc[0]
        rewardId = questDesc[3]
        if rewardId in rewardList:
            return 1
        elif rewardId == NA:
            rewardId = transformReward(getFinalRewardId(questId, fAll=1), av)
            if rewardId in rewardList:
                return 1

    return 0


def avatarHasAllRequiredRewards(av, tier):
    rewardHistory = list(av.getRewardHistory()[1])
    rewardList = getRewardsInTier(tier)
    notify.debug(
        "checking avatarHasAllRequiredRewards: history: %s, tier: %s"
        % (rewardHistory, rewardList)
    )
    for rewardId in rewardList:
        if rewardId == 900:
            found = 0
            for actualRewardId in (901, 902, 903, 904, 905, 906, 907):
                if actualRewardId in rewardHistory:
                    found = 1
                    rewardHistory.remove(actualRewardId)
                    if notify.getDebug():
                        notify.debug(
                            "avatarHasAllRequiredRewards: rewardId 900 found as: %s"
                            % actualRewardId
                        )
                    break

            if not found:
                if notify.getDebug():
                    notify.debug("avatarHasAllRequiredRewards: rewardId 900 not found")
                return 0
        else:
            actualRewardId = transformReward(rewardId, av)
            if actualRewardId in rewardHistory:
                rewardHistory.remove(actualRewardId)
            elif getRewardClass(rewardId) == CogSuitPartReward:
                deptStr = RewardDict.get(rewardId)[1]
                cogPart = RewardDict.get(rewardId)[2]
                dept = ToontownGlobals.cogDept2index[deptStr]
                if av.hasCogPart(cogPart, dept):
                    if notify.getDebug():
                        notify.debug(
                            "avatarHasAllRequiredRewards: rewardId: %s counts, avatar has cog part: %s dept: %s"
                            % (actualRewardId, cogPart, dept)
                        )
                else:
                    if notify.getDebug():
                        notify.debug(
                            "avatarHasAllRequiredRewards: CogSuitPartReward: %s not found"
                            % actualRewardId
                        )
                    return 0
            else:
                if notify.getDebug():
                    notify.debug(
                        "avatarHasAllRequiredRewards: rewardId %s not found"
                        % actualRewardId
                    )
                return 0

    if notify.getDebug():
        notify.debug(
            "avatarHasAllRequiredRewards: remaining rewards: %s" % rewardHistory
        )
        for rewardId in rewardHistory:
            if not isRewardOptional(tier, rewardId):
                notify.warning(
                    "required reward found, expected only optional: %s" % rewardId
                )

    return 1


def nextQuestList(nextQuest):
    if nextQuest == NA:
        return None
    seqTypes = (list, tuple)
    if type(nextQuest) in seqTypes:
        return nextQuest
    else:
        return (nextQuest,)
    return None


def checkReward(questId, forked=0):
    quest = QuestDict[questId]
    reward = quest[5]
    nextQuests = nextQuestList(quest[6])
    if nextQuests is None:
        validRewards = list(RewardDict.keys()) + [
            Any,
            AnyCashbotSuitPart,
            AnyLawbotSuitPart,
            OBSOLETE,
        ]
        if reward is OBSOLETE:
            print("warning: quest %s is obsolete" % questId)
        return reward
    else:
        forked = forked or len(nextQuests) > 1
        firstReward = checkReward(nextQuests[0], forked)
        for qId in nextQuests[1:]:
            thisReward = checkReward(qId, forked)

        return firstReward
    return


def assertAllQuestsValid():
    print("checking quests...")
    for questId in list(QuestDict.keys()):
        try:
            quest = getQuest(questId)
        except AssertionError as e:
            err = "invalid quest: %s" % questId
            print(err)
            raise

    for questId in list(QuestDict.keys()):
        quest = QuestDict[questId]
        tier, start, questDesc, fromNpc, toNpc, reward, nextQuest, dialog = quest
        if start:
            checkReward(questId)
