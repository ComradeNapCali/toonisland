from toontown.toonbase.TTLocalizerEnglishProperty import *
from toontown.catalog import CatalogAccessoryItemGlobals
from otp.otpbase import OTPLocalizer as OL
OL.SpeedChatStaticText = OL.SpeedChatStaticTextToontown.copy()
for key in OL.SpeedChatStaticTextCommon.keys():
    OL.SpeedChatStaticText[key] = OL.SpeedChatStaticTextCommon[key]

commitmantst = 'kptmptest - removable'
InterfaceFont = 'phase_3/models/fonts/AveriaSansLibre.ttf'
ToonFont = 'phase_3/models/fonts/AveriaSansLibre.ttf'
SuitFont = 'phase_3/models/fonts/CreteRound.ttf'
SignFont = 'phase_3/models/fonts/MickeyFont'
MinnieFont = 'phase_3/models/fonts/MinnieFont'
FancyFont = 'phase_3/models/fonts/Comedy'
NametagFonts = ('phase_3/models/fonts/AnimGothic',
 'phase_3/models/fonts/Aftershock',
 'phase_3/models/fonts/JiggeryPokery',
 'phase_3/models/fonts/Ironwork',
 'phase_3/models/fonts/HastyPudding',
 'phase_3/models/fonts/Comedy',
 'phase_3/models/fonts/Humanist',
 'phase_3/models/fonts/Portago',
 'phase_3/models/fonts/Musicals',
 'phase_3/models/fonts/Scurlock',
 'phase_3/models/fonts/Danger',
 'phase_3/models/fonts/Alie',
 'phase_3/models/fonts/OysterBar',
 'phase_3/models/fonts/RedDogSaloon')
NametagFontNames = ('Member',
 'Shivering',
 'Wonky',
 'Fancy',
 'Silly',
 'Zany',
 'Practical',
 'Nautical',
 'Whimsical',
 'Spooky',
 'Action',
 'Poetic',
 'Boardwalk',
 'Western')
NametagLabel = ' Nametag'
UnpaidNameTag = 'Basic'
GM_NAMES = ('TOON COUNCIL',
 'TOON TROOPER',
 'RESISTANCE RANGER',
 'GC')
BuildingNametagFont = 'phase_3/models/fonts/MickeyFont'
BuildingNametagShadow = None
ProductPrefix = 'TT'
Mickey = 'Mickey'
VampireMickey = 'VampireMickey'
Minnie = 'Minnie'
WitchMinnie = 'WitchMinnie'
Donald = 'Donald'
DonaldDock = 'DonaldDock'
FrankenDonald = 'FrankenDonald'
Daisy = 'Daisy'
SockHopDaisy = 'SockHopDaisy'
Goofy = 'Goofy'
SuperGoofy = 'SuperGoofy'
Pluto = 'Pluto'
WesternPluto = 'WesternPluto'
Flippy = 'Flippy'
Chip = 'Chip'
Dale = 'Dale'
JailbirdDale = 'JailbirdDale'
PoliceChip = 'PoliceChip'
lTheBrrrgh = 'Cirrus Circus'
lDaisyGardens = 'Withering Woods'
lDonaldsDock = "Rainbow Rise"
lDonaldsDreamland = "Minty Mines"
lMinniesMelodyland = "Olive Oasis"
lToonIslandCentral = 'Toon Island Central'
lToonHQ = 'Toon HQ'
lSellbotHQ = 'Sellbot HQ'
lGoofySpeedway = 'Goofy Speedway'
lOutdoorZone = "Acorn Acres"
lGolfZone = "Toon Island MiniGolf"
lPartyHood = 'Party Grounds'
GlobalStreetNames = {20000: ('to', 'on', 'Tutorial Terrace'),
 1000: ('to the', 'in the', 'Playground'),
 1100: ('to', 'on', 'Coral Court'),
 1200: ('to', 'on', 'Ocean Overpass'),
 1300: ('to', 'on', 'Plankton Path'),
 2000: ('to the', 'in the', 'Playground'),
 2100: ('to', 'on', 'Beachball Bouvelard'),
 2200: ('to', 'on', 'Aloha Avenue'),
 2300: ('to', 'on', 'Pineapple Place'),
 2400: ('to', 'on', 'Seashell Street'),
 3000: ('to the', 'in the', 'Playground'),
 3100: ('to', 'on', 'Doodle Drive'),
 3200: ('to', 'on', 'Sleet Street'),
 3300: ('to', 'on', 'Polar Place'),
 4000: ('to the', 'in the', 'Playground'),
 4100: ('to', 'on', 'Desert Drive'),
 4200: ('to', 'on', 'Tumbleweed Terrace'),
 4300: ('to', 'on', 'Cactus Court'),
 5000: ('to the', 'in the', 'Playground'),
 5100: ('to', 'on', 'Willow Way'),
 5200: ('to', 'on', 'Crow Circle'),
 5300: ('to', 'on', 'Raven Road'),
 6000: ('to the', 'in the', 'Playground'),
 8000: ('to the', 'in the', 'Playground'),
 9000: ('to the', 'in the', 'Playground'),
 9100: ('to', 'on', 'Rocky Road'),
 9200: ('to', 'on', 'Peppermint Place'),
 10000: ('to', 'in', 'Bossbot HQ Country Club'),
 10100: ('to the', 'in the', 'Bossbot HQ Lobby'),
 10200: ('to the', 'in the', 'The Clubhouse'),
 10500: ('to the', 'in the', 'The Front Three'),
 10600: ('to the', 'in the', 'The Middle Six'),
 10700: ('to the', 'in the', 'The Back Nine'),
 11000: ('to the', 'in the', 'Sellbot HQ Courtyard'),
 11100: ('to the', 'in the', 'Sellbot HQ Lobby'),
 11200: ('to the', 'in the', 'Sellbot Factory'),
 11500: ('to the', 'in the', 'Sellbot Factory'),
 11600: ('to the', 'in the', 'Sellbot Fatal Factory'),
 12000: ('to', 'in', 'Cashbot Train Yard'),
 12100: ('to the', 'in the', 'Cashbot HQ Lobby'),
 12500: ('to the', 'in the', 'Cashbot Coin Mint'),
 12600: ('to the', 'in the', 'Cashbot Dollar Mint'),
 12700: ('to the', 'in the', 'Cashbot Bullion Mint'),
 13000: ('to', 'in', 'Lawbot HQ Courtyard'),
 13100: ('to the', 'in the', 'Courthouse Lobby'),
 13200: ('to the', 'in the', "DA's Office Lobby"),
 13300: ('to the', 'in the', 'Lawbot A Office'),
 13400: ('to the', 'in the', 'Lawbot B Office'),
 13500: ('to the', 'in the', 'Lawbot C Office'),
 13600: ('to the', 'in the', 'Lawbot D Office'),
 17000: ('to the', 'in the', 'Playground'),}
RainbowRise = ('to', 'in', lDonaldsDock)
ToonIslandCentral = ('to', 'in', lToonIslandCentral)
CirrusCircus = ('to', 'in', lTheBrrrgh)
OliveOasis = ('to', 'in', lMinniesMelodyland)
WitheringWoods = ('to', 'in', lDaisyGardens)
OutdoorZone = ('to', 'in', lOutdoorZone)
CirrusCircus = ('to the', 'in the', 'Cirrus Circus')
GoofySpeedway = ('to', 'in', lGoofySpeedway)
MintyMines = ('to', 'in', lDonaldsDreamland)
BossbotHQ = ('to', 'in', 'Bossbot HQ')
SellbotHQ = ('to', 'in', 'Sellbot HQ')
CashbotHQ = ('to', 'in', 'Cashbot HQ')
LawbotHQ = ('to', 'in', 'Lawbot HQ')
Tutorial = ('to the', 'in the', 'Toon-torial')
MyEstate = ('to', 'in', 'your house')
WelcomeValley = ('to', 'in', 'Welcome Valley')
GolfZone = ('to', 'in', lGolfZone)
PartyHood = ('to the', 'in the', lPartyHood)
Factory = 'Factory'
Headquarters = 'Headquarters'
SellbotFrontEntrance = 'Front Entrance'
SellbotSideEntrance = 'Side Entrance'
SellbotFatalEntrance = 'Fatal Enterance'
Office = 'Office'
FactoryNames = {0: 'Factory Mockup',
 11500: 'Sellbot Cog Factory',
 11600: 'Sellbot Fatal Factory',
 13300: 'Lawbot Cog Office'}
FactoryTypeLeg = 'Leg'
FactoryTypeArm = 'Arm'
FactoryTypeTorso = 'Torso'
MintFloorTitle = 'Floor %s'
lCancel = 'Cancel'
lClose = 'Close'
lOK = 'OK'
lNext = 'Next'
lQuit = 'Quit'
lYes = 'Yes.'
lNo = 'No.'
sleep_auto_reply = '%s is sleeping right now.'
sleep_auto_reply_retro = '%s is sleeping right now'
lHQOfficerF = 'HQ Officer'
lHQOfficerM = 'HQ Officer'
MickeyMouse = 'Mickey Mouse'
AIStartDefaultDistrict = 'Sillyville'
Cog = 'Cog'
Cogs = 'Cogs'
ACog = 'a Cog'
TheCogs = 'The Cogs'
ASkeleton = 'a Skelecog'
Skeleton = 'Skelecog'
SkeletonP = 'Skelecogs'
Av2Cog = 'a Version 2.0 Cog'
v2Cog = 'Version 2.0 Cog'
v2CogP = 'Version 2.0 Cogs'
ASkeleton = 'a Skelecog'
Foreman = 'Factory Foreman'
ForemanP = 'Factory Foremen'
AForeman = 'a Factory Foreman'
CogVP = Cog + ' V.P.'
CogVPs = "Cog V.P.'s"
ACogVP = ACog + ' V.P.'
Supervisor = 'Mint Supervisor'
SupervisorP = 'Mint Supervisors'
ASupervisor = 'a Mint Supervisor'
CogCFO = Cog + ' C.F.O.'
CogCFOs = "Cog C.F.O.'s"
ACogCFO = ACog + ' C.F.O.'
TheFish = 'the fish'
AFish = 'a fish'
Level = 'Level'
QuestsCompleteString = 'Complete'
QuestsNotChosenString = 'Not chosen'
Period = '.'
Laff = 'Laff'
QuestInLocationString = ' %(inPhrase)s %(location)s'
QuestsDefaultGreeting = ('Hello, _avName_!',
 'Hi, _avName_!',
 'Hey there, _avName_!',
 'Say there, _avName_!',
 'Welcome, _avName_!',
 'Howdy, _avName_!',
 'How are you, _avName_?',
 'Greetings _avName_!')
QuestsDefaultIncomplete = ("How's that task coming, _avName_?",
 'Looks like you still have more work to do on that task!',
 'Keep up the good work, _avName_!',
 'Keep trying to finish that task. I know you can do it!',
 'Keep trying to complete that task, we are counting on you!',
 'Keep working on that ToonTask!')
QuestsDefaultIncompleteProgress = ('You came to the right place, but you need to finish your ToonTask first.', 'When you are finished with that ToonTask, come back here.', 'Come back when you are finished with your ToonTask.')
QuestsDefaultIncompleteWrongNPC = ('Nice work on that ToonTask. You should go visit _toNpcName_._where_', 'Looks like you are ready to finish your ToonTask. Go see _toNpcName_._where_.', 'Go see _toNpcName_ to finish your ToonTask._where_')
QuestsDefaultComplete = ('Nice work! Here is your reward…', 'Great job, _avName_! Take this reward…', 'Wonderful job, _avName_! Here is your reward…')
QuestsDefaultLeaving = ('Bye!',
 'Goodbye!',
 'So long, _avName_.',
 'See ya, _avName_!',
 'Good luck!',
 'Have fun in Toontown!',
 'See you later!')
QuestsDefaultReject = ('Hello.',
 'Can I help you?',
 'How are you?',
 'Hello there.',
 "I'm a little busy now, _avName_.",
 'Yes?',
 'Howdy, _avName_!',
 'Welcome, _avName_!',
 "Hey, _avName_! How's it going?",
 'Did you know you can open your Shticker Book by hitting F8?',
 'You can use your map to teleport back to the playground!',
 'You can make friends with other players by clicking on them.',
 'You can discover more about a ' + Cog + ' by clicking on them.',
 'Gather treasures in the playgrounds to fill your Laff meter.',
 Cog + ' buildings are dangerous places! Do not go in alone!',
 'When you lose a battle, the ' + Cogs + ' take all your gags.',
 'To get more gags, play Trolley games!',
 'You can get more Laff points by completing ToonTasks.',
 'Every ToonTask gives you a reward.',
 'Some rewards let you carry more gags.',
 'If you win a battle, you get ToonTask credit for every ' + Cog + ' defeated.',
 'If you recapture a ' + Cog + ' building, go back inside to see a special thank-you from its owner!',
 'If you press the Page Up key, you can look up!',
 'If you press the Tab key, you can see different views of your surroundings!',
 "To show True Friends what you're thinking, enter a '.' before your thought.",
 'If a ' + Cog + ' is stunned, it is more difficult for them to avoid falling objects.',
 'Each kind of ' + Cog + ' building has a distinct look.',
 'Defeating ' + Cogs + ' on the higher floors of a building will give you greater skill rewards.')
QuestsDefaultTierNotDone = ('Hello, _avName_! You must finish your current ToonTasks before getting a new one.', 'Hi there! You need to finish the ToonTasks you are working on in order to get a new one.', 'Hi, _avName_! Before I can give you a new ToonTask, you need to finish the ones you have.')
QuestsDefaultQuest = None
QuestsDefaultVisitQuestDialog = ('I heard _toNpcName_ is looking for you._where_',
 'Stop by and see _toNpcName_ when you get a chance._where_',
 'Pay a visit to _toNpcName_ next time you are over that way._where_',
 'If you get a chance, stop in and say hi to _toNpcName_._where_',
 '_toNpcName_ will give you your next ToonTask._where_')
QuestsLocationArticle = ''

def getLocalNum(num):
    return str(num)


QuestsItemNameAndNum = '%(num)s %(name)s'
QuestsCogQuestProgress = '%(progress)s of %(numCogs)s defeated'
QuestsCogQuestHeadline = 'WANTED'
QuestsCogQuestSCStringS = 'I need to defeat %(cogName)s%(cogLoc)s.'
QuestsCogQuestSCStringP = 'I need to defeat some %(cogName)s%(cogLoc)s.'
QuestsCogQuestDefeat = 'Defeat %s'
QuestsCogQuestDefeatDesc = '%(numCogs)s %(cogName)s'
QuestsCogNewNewbieQuestObjective = 'Help a new Toon defeat %s'
QuestsCogNewNewbieQuestCaption = 'Help a new Toon %d Laff or less'
QuestsCogOldNewbieQuestObjective = 'Help a Toon with %(laffPoints)d Laff or less defeat %(objective)s'
QuestsCogOldNewbieQuestCaption = 'Help a Toon %d Laff or less'
QuestsCogNewbieQuestAux = 'Defeat:'
QuestsNewbieQuestHeadline = 'APPRENTICE'
QuestsCogTrackQuestProgress = '%(progress)s of %(numCogs)s defeated'
QuestsCogTrackQuestHeadline = 'WANTED'
QuestsCogTrackQuestSCStringS = 'I need to defeat %(cogText)s%(cogLoc)s.'
QuestsCogTrackQuestSCStringP = 'I need to defeat some %(cogText)s%(cogLoc)s.'
QuestsCogTrackQuestDefeat = 'Defeat %s'
QuestsCogTrackDefeatDesc = '%(numCogs)s %(trackName)s'
QuestsCogLevelQuestProgress = '%(progress)s of %(numCogs)s defeated'
QuestsCogLevelQuestHeadline = 'WANTED'
QuestsCogLevelQuestDefeat = 'Defeat %s'
QuestsCogLevelQuestDesc = 'a Level %(level)s+ %(name)s'
QuestsCogLevelQuestDescC = '%(count)s Level %(level)s+ %(name)s'
QuestsCogLevelQuestDescI = 'some Level %(level)s+ %(name)s'
QuestsCogLevelQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsBuildingQuestFloorNumbers = ('',
 'two+',
 'three+',
 'four+',
 'five')
QuestsBuildingQuestBuilding = 'Building'
QuestsBuildingQuestBuildings = 'Buildings'
QuestsBuildingQuestHeadline = 'DEFEAT'
QuestsBuildingQuestProgressString = '%(progress)s of %(num)s defeated'
QuestsBuildingQuestString = 'Defeat %s'
QuestsBuildingQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsBuildingQuestDesc = 'a %(type)s Building'
QuestsBuildingQuestDescF = 'a %(floors)s story %(type)s Building'
QuestsBuildingQuestDescC = '%(count)s %(type)s Buildings'
QuestsBuildingQuestDescCF = '%(count)s %(floors)s story %(type)s Buildings'
QuestsBuildingQuestDescI = 'some %(type)s Buildings'
QuestsBuildingQuestDescIF = 'some %(floors)s story %(type)s Buildings'
QuestFactoryQuestFactory = 'Factory'
QuestsFactoryQuestFactories = 'Factories'
QuestsFactoryQuestHeadline = 'DEFEAT'
QuestsFactoryQuestProgressString = '%(progress)s of %(num)s defeated'
QuestsFactoryQuestString = 'Defeat %s'
QuestsFactoryQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsFactoryQuestDesc = 'a %(type)s Factory'
QuestsFactoryQuestDescC = '%(count)s %(type)s Factories'
QuestsFactoryQuestDescI = 'some %(type)s Factories'
QuestMintQuestMint = 'Mint'
QuestsMintQuestMints = 'Mints'
QuestsMintQuestHeadline = 'DEFEAT'
QuestsMintQuestProgressString = '%(progress)s of %(num)s defeated'
QuestsMintQuestString = 'Defeat %s'
QuestsMintQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsMintQuestDesc = 'a Cog Mint'
QuestsMintQuestDescC = '%(count)s Cog Mints'
QuestsMintQuestDescI = 'some Cog Mints'
QuestsRescueQuestProgress = '%(progress)s of %(numToons)s rescued'
QuestsRescueQuestHeadline = 'RESCUE'
QuestsRescueQuestSCStringS = 'I need to rescue a Toon%(toonLoc)s.'
QuestsRescueQuestSCStringP = 'I need to rescue some Toons%(toonLoc)s.'
QuestsRescueQuestRescue = 'Rescue %s'
QuestsRescueQuestRescueDesc = '%(numToons)s Toons'
QuestsRescueQuestToonS = 'a Toon'
QuestsRescueQuestToonP = 'Toons'
QuestsRescueQuestAux = 'Rescue:'
QuestsRescueNewNewbieQuestObjective = 'Help a new Toon rescue %s'
QuestsRescueOldNewbieQuestObjective = 'Help a Toon with %(laffPoints)d Laff or less rescue %(objective)s'
QuestCogPartQuestCogPart = 'Cog Suit Part'
QuestsCogPartQuestFactories = 'Factories'
QuestsCogPartQuestHeadline = 'RETRIEVE'
QuestsCogPartQuestProgressString = '%(progress)s of %(num)s retrieved'
QuestsCogPartQuestString = 'Retrieve %s'
QuestsCogPartQuestSCString = 'I need to retrieve %(objective)s%(location)s.'
QuestsCogPartQuestAux = 'Retrieve:'
QuestsCogPartQuestDesc = 'a Cog Suit Part'
QuestsCogPartQuestDescC = '%(count)s Cog Suit Parts'
QuestsCogPartQuestDescI = 'some Cog Suit Parts'
QuestsCogPartNewNewbieQuestObjective = 'Help a new Toon retrieve %s'
QuestsCogPartOldNewbieQuestObjective = 'Help a Toon with %(laffPoints)d Laff or less retrieve %(objective)s'
QuestsDeliverGagQuestProgress = '%(progress)s of %(numGags)s delivered'
QuestsDeliverGagQuestHeadline = 'DELIVER'
QuestsDeliverGagQuestToSCStringS = 'I need to deliver %(gagName)s.'
QuestsDeliverGagQuestToSCStringP = 'I need to deliver some %(gagName)s.'
QuestsDeliverGagQuestSCString = 'I need make a delivery.'
QuestsDeliverGagQuestString = 'Deliver %s'
QuestsDeliverGagQuestStringLong = 'Deliver %s to _toNpcName_.'
QuestsDeliverGagQuestInstructions = 'You can buy this gag in the Gag Shop once you earn access to it.'
QuestsDeliverItemQuestProgress = ''
QuestsDeliverItemQuestHeadline = 'DELIVER'
QuestsDeliverItemQuestSCString = 'I need to deliver %(article)s%(itemName)s.'
QuestsDeliverItemQuestString = 'Deliver %s'
QuestsDeliverItemQuestStringLong = 'Deliver %s to _toNpcName_.'
QuestsVisitQuestProgress = ''
QuestsVisitQuestHeadline = 'VISIT'
QuestsVisitQuestStringShort = 'Visit'
QuestsVisitQuestStringLong = 'Visit _toNpcName_'
QuestsVisitQuestSeeSCString = 'I need to see %s.'
QuestsRecoverItemQuestProgress = '%(progress)s of %(numItems)s recovered'
QuestsRecoverItemQuestHeadline = 'RECOVER'
QuestsRecoverItemQuestSeeHQSCString = 'I need to see an ' + lHQOfficerM + '.'
QuestsRecoverItemQuestReturnToHQSCString = 'I need to return %s to an ' + lHQOfficerM + '.'
QuestsRecoverItemQuestReturnToSCString = 'I need to return %(item)s to %(npcName)s.'
QuestsRecoverItemQuestGoToHQSCString = 'I need to go to a Toon HQ.'
QuestsRecoverItemQuestGoToPlaygroundSCString = 'I need to go to %s Playground.'
QuestsRecoverItemQuestGoToStreetSCString = 'I need to go %(to)s %(street)s in %(hood)s.'
QuestsRecoverItemQuestVisitBuildingSCString = 'I need to visit %s%s.'
QuestsRecoverItemQuestWhereIsBuildingSCString = 'Where is %s%s?'
QuestsRecoverItemQuestRecoverFromSCString = 'I need to recover %(item)s from %(holder)s%(loc)s.'
QuestsRecoverItemQuestString = 'Recover %(item)s from %(holder)s'
QuestsRecoverItemQuestHolderString = '%(level)s %(holder)d+ %(cogs)s'
QuestsTrackChoiceQuestHeadline = 'CHOOSE'
QuestsTrackChoiceQuestSCString = 'I need to choose between %(trackA)s and %(trackB)s.'
QuestsTrackChoiceQuestMaybeSCString = 'Maybe I should choose %s.'
QuestsTrackChoiceQuestString = 'Choose between %(trackA)s and %(trackB)s'
QuestsFriendQuestHeadline = 'FRIEND'
QuestsFriendQuestSCString = 'I need to make a friend.'
QuestsFriendQuestString = 'Make a friend'
QuestsMailboxQuestHeadline = 'MAIL'
QuestsMailboxQuestSCString = 'I need to check my mail.'
QuestsMailboxQuestString = 'Check your mail'
QuestsPhoneQuestHeadline = 'CLARABELLE'
QuestsPhoneQuestSCString = 'I need to call Clarabelle.'
QuestsPhoneQuestString = 'Call Clarabelle'
QuestsFriendNewbieQuestString = 'Make %d friends %d laff or less'
QuestsFriendNewbieQuestProgress = '%(progress)s of %(numFriends)s made'
QuestsFriendNewbieQuestObjective = 'Make friends with %d new Toons'
QuestsTrolleyQuestHeadline = 'TROLLEY'
QuestsTrolleyQuestSCString = 'I need to ride the trolley.'
QuestsTrolleyQuestString = 'Ride on the trolley'
QuestsTrolleyQuestStringShort = 'Ride the trolley'
QuestsMinigameNewbieQuestString = '%d Minigames'
QuestsMinigameNewbieQuestProgress = '%(progress)s of %(numMinigames)s Played'
QuestsMinigameNewbieQuestObjective = 'Play %d minigames with new Toons'
QuestsMinigameNewbieQuestSCString = 'I need to play minigames with new Toons.'
QuestsMinigameNewbieQuestCaption = 'Help a new Toon %d laff or less'
QuestsMinigameNewbieQuestAux = 'Play:'
QuestsMaxHpReward = 'Your Laff limit has been increased by %s.'
QuestsMaxHpRewardPoster = 'Reward: %s point Laff boost'
QuestsMoneyRewardSingular = 'You get 1 Jellybean.'
QuestsMoneyRewardPlural = 'You get %s Jellybeans.'
QuestsMoneyRewardPosterSingular = 'Reward: 1 Jellybean'
QuestsMoneyRewardPosterPlural = 'Reward: %s Jellybeans'
QuestsMaxMoneyRewardSingular = 'You can now carry 1 Jellybean.'
QuestsMaxMoneyRewardPlural = 'You can now carry %s Jellybeans.'
QuestsMaxMoneyRewardPosterSingular = 'Reward: Carry 1 Jellybean'
QuestsMaxMoneyRewardPosterPlural = 'Reward: Carry %s Jellybeans'
QuestsMaxGagCarryReward = 'You get a %(name)s. You can now carry %(num)s gags.'
QuestsMaxGagCarryRewardPoster = 'Reward: %(name)s (%(num)s)'
QuestsMaxQuestCarryReward = 'You can now have %s ToonTasks.'
QuestsMaxQuestCarryRewardPoster = 'Reward: Carry %s ToonTasks'
QuestsTeleportReward = 'You now have teleport access to %s.'
QuestsTeleportRewardPoster = 'Reward: Teleport access to %s'
QuestsTrackTrainingReward = 'You can now train for "%s" gags.'
QuestsTrackTrainingRewardPoster = 'Reward: Gag training'
QuestsTrackProgressReward = 'You now have frame %(frameNum)s of the %(trackName)s track animation.'
QuestsTrackProgressRewardPoster = 'Reward: "%(trackName)s" track animation frame %(frameNum)s'
QuestsTrackCompleteReward = 'You may now carry and use "%s" gags.'
QuestsTrackCompleteRewardPoster = 'Reward: Final %s track training'
QuestsClothingTicketReward = 'You can change your clothes'
QuestsClothingTicketRewardPoster = 'Reward: Clothing Ticket'
TIPQuestsClothingTicketReward = 'You can change your shirt for a TIP shirt'
TIPQuestsClothingTicketRewardPoster = 'Reward: TIP Clothing Ticket'
QuestsCheesyEffectRewardPoster = 'Reward: %s'
QuestsCogSuitPartReward = 'You now have a %(cogTrack)s %(part)s Cog Suit Part.'
QuestsCogSuitPartRewardPoster = 'Reward: %(cogTrack)s %(part)s Part'
QuestsStreetLocationThisPlayground = 'in this playground'
QuestsStreetLocationThisStreet = 'on this street'
QuestsStreetLocationNamedPlayground = 'in the %s playground'
QuestsStreetLocationNamedStreet = 'on %(toStreetName)s in %(toHoodName)s'
QuestsLocationString = '%(string)s%(location)s'
QuestsLocationBuilding = "%s's building is called"
QuestsLocationBuildingVerb = 'which is'
QuestsLocationParagraph = '\x07%(building)s "%(buildingName)s"…\x07…%(buildingVerb)s %(street)s.'
QuestsGenericFinishSCString = 'I need to finish a ToonTask.'
QuestsMediumPouch = 'Medium Pouch'
QuestsLargePouch = 'Large Pouch'
QuestsSmallBag = 'Small Bag'
QuestsMediumBag = 'Medium Bag'
QuestsLargeBag = 'Large Bag'
QuestsSmallBackpack = 'Small Backpack'
QuestsMediumBackpack = 'Medium Backpack'
QuestsLargeBackpack = 'Large Backpack'
# Toon island central quest items
QuestsItemDict = {
 1: ['Pair of Glasses', 'Pairs of Glasses', 'a '],
 2: ['Key', 'Keys', 'a '],
 3: ['Blackboard', 'Blackboards', 'a '],
 4: ['Book', 'Books', 'a '],
 5: ['Candy Bar', 'Candy Bars', 'a '],
 6: ['Encrypted Code', 'Encrypted Code', 'some '],
 7: ['Comet Pebble', 'Comet Pebbles', 'some '],
 8: ['Library Card', 'Library Cards', 'a '],
 9: ['Cog Gear', 'Cog Gears', 'some '],
 10: ['Whole Cream Pie', 'Whole Cream Pies', 'some '],
 11: ['Screwdriver', 'Screwdrivers', 'a '],
 12: ['Calculator', 'Calculators', 'a '],
 13: ['Cog Fiber', 'Cog Fibers', 'some '],
 14: ['Battery', 'Batteries', 'some '],
 15: ['Checklist', 'Checklists', 'a '],
 16: ['Scrap Metal', 'Scrap Metal', 'some '],
 17: ['Purse', 'Purses', 'some '],
 18: ['Liar Liar Pants', 'Liar Liar Pants', 'some '],
 19: ["Magic Cracker Recipe", "Magic Cracker Recipes", "a "],
 20: ['Walkie Talkie', 'Walkie Talkies', 'a '],
 21: ['Instuctors Pen', 'Instuctors Pens', 'a '],
 22: ['Octopus', 'Octopusi', 'some '],
 23: ['Orange Lizard', 'Orange Lizards', 'the '],
 24: ['Blue Turtle', 'Blue Turtles', 'the '],
 25: ['Note About The Green Frog', 'Notes About Green Frogs', 'the '],
 26: ['Green Frog', 'Green Frogs', 'the '],
 27: ['Evidence', 'Evidence', 'some '],
 28: ['Golden Spatula', 'Golden Spatulas', 'a '],
 29: ['Grape Juice', 'Grape Juices', 'some '],
 30: ['Grapes', 'Grapes', 'some '],
 31: ['Piece of Junk', 'Pieces of Junk', 'some '],
 32: ['Large Pouch', 'Large Pouches', 'a '],
 33: ['Fairy Tale Notice', 'Fairy Tale Notices', 'a '],
 34: ['Toonivari Translation Guide', 'Toonivari Translation Guides', 'a '],
 35: ['The Ring', 'Rings', 'a '],
 36: ['"The" Ring', 'Rings', 'a '],
 37: ["Angelics's Magical Wand", "Angelics's Magical Wands", "a "],
 38: ["The Lexicon Transcriber", "The Lexicon Transcibers", 'a '],
 39: ["Treasure Key", "Treasure Keys", 'a '],
 40: ["Vacation Ticket", "Vacation Tickets", 'a '],
 41: ["Key", "Keys", 'a '],
 42: ["Evidence", "Evidence", 'some '],
 43: ["Cannonball", "Cannonballs", "some "],
 44: ["Anti Invisiblity Shampoo", "Anti Invisiblity Shampoo", "bottles of "],
 45: ["Invisiblity Spray", "Invisiblity Spray", "cans of "],
 46: ["Jellybean", "Jellybeans", "50 "],
 47: ["Fishing Equipment", "Fishing Equipment", "pieces of "],
 48: ["Bait", "Bait", "some "],
 110: ['TIP Clothing Ticket', 'Clothing Tickets', 'a '],
 1000: ['Clothing Ticket', 'Clothing Tickets', 'a '],
 2001: ['Inner Tube', 'Inner Tubes', 'an '],
 2002: ['Monocle Prescription', 'Monocle Prescriptions', 'a '],
 2003: ['Eyeglass Frames', 'Eyeglass Frames', 'some '],
 2004: ['Monocle', 'Monocles', 'a '],
 2005: ['Big White Wig', 'Big White Wigs', 'a '],
 2006: ['Bushel of Ballast', 'Bushels of Ballast', 'a '],
 2007: ['Cog Gear', 'Cog Gears', 'a '],
 2008: ['Sea Chart', 'Sea Charts', 'a '],
 2009: ['Cruddy Clovis', 'Cruddy Clovi', 'a '],
 2010: ['Clean Clovis', 'Clean Clovi', 'a '],
 2011: ['Clock Spring', 'Clock Springs', 'a '],
 2012: ['Counter Weight', 'Counter Weights', 'a '],
 4001: ["Tina's Inventory", "Tina's Inventories", ''],
 4002: ["Yuki's Inventory", "Yuki's Inventories", ''],
 4003: ['Inventory Form', 'Inventory Forms', 'an '],
 4004: ["Fifi's Inventory", "Fifi's Inventories", ''],
 4005: ["Lumber Jack's Ticket", "Lumber Jack's Tickets", ''],
 4006: ["Tabitha's Ticket", "Tabitha's Tickets", ''],
 4007: ["Barry's Ticket", "Barry's Tickets", ''],
 4008: ['Cloudy Castanet', 'Cloudy Castanets', ''],
 4009: ['Blue Squid Ink', 'Blue Squid Ink', 'some '],
 4010: ['Clear Castanet', 'Clear Castanets', 'a '],
 4011: ["Leo's Lyrics", "Leo's Lyrics", ''],
 5001: ['Silk necktie', 'Silk neckties', 'a '],
 5002: ['Pinstripe Suit', 'Pinstripe Suits', 'a '],
 5003: ['Pair of Scissors', 'Pairs of Scissors', 'a '],
 5004: ['Postcard', 'Postcards', 'a '],
 5005: ['Pen', 'Pens', 'a '],
 5006: ['Inkwell', 'Inkwells', 'an '],
 5007: ['Notepad', 'Notepads', 'a '],
 5008: ['Office Lockbox', 'Office Lockboxes', 'an '],
 5009: ['Bag of Bird Seed', 'Bags of Bird Seed', 'a '],
 5010: ['Sprocket', 'Sprockets', 'a '],
 5011: ['Salad', 'Salads', 'a '],
 5012: ['Key to ' + lDaisyGardens, 'Keys to ' + lDaisyGardens, 'a '],
 5013: [lSellbotHQ + ' Blueprints', lSellbotHQ + ' HQ Blueprints', 'some '],
 5014: [lSellbotHQ + ' Memo', lSellbotHQ + ' Memos', 'a '],
 5015: [lSellbotHQ + ' Memo', lSellbotHQ + ' Memos', 'a '],
 5016: [lSellbotHQ + ' Memo', lSellbotHQ + ' Memos', 'a '],
 5017: [lSellbotHQ + ' Memo', lSellbotHQ + ' Memos', 'a '],
 3001: ['Soccer ball', 'Soccer balls', 'a '],
 3002: ['Toboggan', 'Toboggans', 'a '],
 3003: ['Ice cube', 'Ice cubes', 'an '],
 3004: ['Love letter', 'Love letters', 'a '],
 3005: ['Wiener dog', 'Wiener dogs', 'a '],
 3006: ['Engagement ring', 'Engagement rings', 'an '],
 3007: ['Sardine whiskers', 'Sardine whiskers', 'some '],
 3008: ['Calming potion', 'Calming potion', 'a '],
 3009: ['Broken tooth', 'Broken teeth', 'a '],
 3010: ['Gold tooth', 'Gold teeth', 'a '],
 3011: ['Pine cone bread', 'Pine cone breads', 'a '],
 3012: ['Lumpy cheese', 'Lumpy cheeses', 'some '],
 3013: ['Simple spoon', 'Simple spoons', 'a '],
 3014: ['Talking toad', 'Talking toad', 'a '],
 3015: ['Ice cream cone', 'Ice cream cones', 'an '],
 3016: ['Wig powder', 'Wig powders', 'some '],
 3017: ['Rubber ducky', 'Rubber duckies', 'a '],
 3018: ['Fuzzy dice', 'Fuzzy dice', 'some '],
 3019: ['Microphone', 'Microphones', 'a '],
 3020: ['Electric keyboard', 'Electric keyboards', 'an '],
 3021: ['Platform shoes', 'Platform shoes', 'some '],
 3022: ['Caviar', 'Caviar', 'some '],
 3023: ['Make-up powder', 'Make-up powders', 'some '],
 3024: ['Yarn', 'Yarn', 'some '],
 3025: ['Knitting Needle', 'Knitting Needles', 'a '],
 3026: ['Alibi', 'Alibis', 'an '],
 3027: ['External Temperature Sensor', 'External Temperature Sensors', 'an '],
 6001: ['Cashbot HQ Plans', 'Cashbot HQ Plans', 'some '],
 6002: ['Rod', 'Rods', 'a '],
 6003: ['Drive Belt', 'Drive Belts', 'a '],
 6004: ['Pair of Pincers', 'Pairs of Pincers', 'a '],
 6005: ['Reading Lamp', 'Reading Lamps', 'a '],
 6006: ['Zither', 'Zithers', 'a '],
 6007: ['Zamboni', 'Zambonis', 'a '],
 6008: ['Zebra Zabuton', 'Zebra Zabutons', 'a '],
 6009: ['Zinnias', 'Zinnias', 'some '],
 6010: ['Zydeco Records', 'Zydeco Records', 'some '],
 6011: ['Zucchini', 'Zucchinis', 'a '],
 6012: ['Zoot Suit', 'Zoot Suits', 'a '],
 7001: ['Plain Bed', 'Plain Beds', 'a '],
 7002: ['Fancy Bed', 'Fancy Beds', 'a '],
 7003: ['Blue Bedspread', 'Blue Bedspreads', 'a '],
 7004: ['Paisley Bedspread', 'Paisley Bedspreads', 'a '],
 7005: ['Pillows', 'Pillows', 'some '],
 7006: ['Hard Pillows', 'Hard Pillows', 'some '],
 7007: ['Pajamas', 'Pajamas', 'a pair of '],
 7008: ['Footie Pajamas', 'Footie Pajamas', 'a pair of '],
 7009: ['Puce Footie Pajamas', 'Puce Footie Pajamas', 'a pair of '],
 7010: ['Fuchsia Footie Pajamas', 'Fuchsia Footie Pajamas', 'a pair of '],
 7011: ['Cauliflower Coral', 'Cauliflower Coral', 'some '],
 7012: ['Slimy Kelp', 'Slimy Kelp', 'some '],
 7013: ['Pestle', 'Pestles', 'a '],
 7014: ['Jar of Wrinkle Cream', 'Jars of Wrinkle Cream', 'a ']}
QuestsHQOfficerFillin = lHQOfficerM
QuestsHQWhereFillin = ''
QuestsHQBuildingNameFillin = lToonHQ
QuestsHQLocationNameFillin = 'in any neighborhood'
QuestsTailorFillin = 'Tailor'
QuestsTailorWhereFillin = ''
QuestsTailorBuildingNameFillin = 'Clothing Store'
QuestsTailorLocationNameFillin = 'in any neighborhood'
QuestsTailorQuestSCString = 'I need to see a Tailor.'
QuestMovieQuestChoiceCancel = 'Come back later if you need a ToonTask! Bye!'
QuestMovieTrackChoiceCancel = 'Come back when you are ready to decide! Bye!'
QuestMovieQuestChoice = 'Choose a ToonTask.'
QuestMovieTrackChoice = 'Ready to decide? Choose a track, or come back later.'
GREETING = 0
QUEST = 1
INCOMPLETE = 2
INCOMPLETE_PROGRESS = 3
INCOMPLETE_WRONG_NPC = 4
COMPLETE = 5
LEAVING = 6
TheBrrrghTrackQuestDict = {GREETING: '',
 QUEST: 'Now you are ready.\x07Go out and walk the planet until you know which track you would like to '
        'choose.\x07Choose wisely, because this is your final track.\x07When you are certain, return to me.',
 INCOMPLETE_PROGRESS: 'Choose wisely.',
 INCOMPLETE_WRONG_NPC: 'Choose wisely.',
 COMPLETE: 'Very wise choice!',
 LEAVING: 'Good luck. Return to me when you have mastered your new skill.'}
QuestDialog_3225 = {QUEST: "Oh, thanks for coming, _avName_!\x07The Cogs in the neighborhood frightened away my delivery person.\x07I don't have anyone to deliver this salad to _toNpcName_!\x07Can you do it for me? Thanks so much!_where_"}
QuestDialog_2910 = {QUEST: 'Back so soon?\x07Great job on the spring.\x07The final item is a counter weight.\x07Stop by and see _toNpcName_ and bring back whatever you can get._where_'}

QuestDialogDict = {
 # ==========================
 #    Toon Island Central
 # ==========================

 # Task 1: The Grand Toontorial
 # TODO: Enable when estates get fixed
 111: {
  QUEST: 'You got the walkie talkie? Wow, thank you so much!\x07I’ll be able to call in backup from all of the districts now, thanks to you.\x07Return here when you are ready to proceed with your next quest!'},
 112: {
  QUEST: 'Thank you again for returning our walkie talkie!\x07Before we can set you up with any more tasks we need to make sure you have been trained with your Shticker Book.\x07Health and Safety, of course.\x07Let’s see…\x07Ah…\x07We can set you up with Librarian Liz for now.\x07She should be able to cover most of the book, she is the creator of the book, after all!_where_'},
 113: {
  QUEST: 'You are new here, yes?\x07Oh, I did not realize. Sorry!\x07Hmm… No one is here, so we should be fine to talk.\x07Oh yes, the book!\x07I guess I can set you up with some lessons.\x07Each page have different functions.\x07There is the Options Page which can be used to enter rather strange and unique codes as well as accessing Toon function options.\x07Default is what I prefer but, you do you.\x07Next, onto the District Section, here you are able to travel through all district areas\x07If one gets filled up, travel to another or find friends in other districts\x07Districts act as replicated areas of the island for all Toons to visit, so this place never gets over-crowded.\x07If only Disney World had Districts…\x07Next, I am sure you are aware of the Map Page.\x07The Map Page is used to navigate through the island and to discover new things, of course!\x07Teleportation can be unlocked to travel through each area or playground you find.\x07And, next, the Inventory Page is the most important part!\x07You can view if you are low on gags or how much you have here\x07as well as the ability to view how many gag points you need until you can unlock new gags.\x07Wait…\x07Tutorial Tom never told you?\x07Ah, yes.\x07New gags can be unlocked through fighting enough Cogs and earning gag points.\x07You can check how far you’ve gotten with learning your chosen Gag Track by going to the Training Tab under your Inventory Page.\x07That’s right, Gag tracks have to be earned using what we call Film, but only a certain amount can be gained from each playground.\x07Also, when you’ve defeated a boss, you can view the rewards that you’ve earned.\x07Anyways, now onto your Quest Page!\x07Here you can view every Toontask you are working on as well as the goal and reward of said task!\x07Eventually you’ll be able to carry four tasks at a time. You’ll be able to obtain Toontasks from HQ Officers and Shopkeepers alike.\x07Gag track training as said before is earned through tasks from each playground.\x07Simply finding which track you want is the hard part! But you’ll learn more about that as you quest.\x07Next is the Cog Gallery or the Rouges Gallery as I like to call it!\x07Each Cog you fight will be listed here.\x07Attack and destroy a certain amount of every Cog and you will be able to obtain an Activity Tracker.\x07The Activity Tracker is used to track how many Cog buildings there are on a street and to check how many Cogs of a specific department there are on a street.\x07Next up is the Events Page.\x07You can use this page to check what wacky activities the Toon Council has put in place, to remind you when your friends’ Birthday Party is scheduled, when your next Cattlelog is coming, and more!\x07There are other sections but, for now you don’t have them unlocked and unfortunately, I can only tell you about the certain sections that I know of.\x07For now take this book and use it well.\x07I’m sure you’ll need it against Cogs.\x07You’ll also need this Laff-O-Meter.\x07I am sure Tutorial Tom forgot all about that!\x07Wait, he didn’t?\x07Anyways, head back to the Headquarters!\x07I am sure they’ll need you back for further initiation.\x07Goodbye and good luck, %(Toonname)s!'},
 114: {
  QUEST: 'Liz gave you the whole run down.\x07Good\x07However, we have gotten reports of several Cogs invading this area.\x07If we do not have Toons running them out, they will run us out first.\x07We want you to find a friend to offer assistance to the cause.\x07Friends can be found anywhere on the island.\x07On the top right of you screen you will see a friend-maker button.\x07Simply click on the button, then click add a friend, followed by their name.\x07This works both ways so anyone can become your friend if you are so desired.\x07You can only have 100 friends at maximum, though, so choose friends wisely.\x07If you cannot find a friend feel free to just return back to HQ and we will set you up with your next task.'},
 115: {
  QUEST: 'Good to hear that you made a friend.\x07I think you’ll need them for the Cogs in the area.\x07Before any more Cogs start invading I need you to destroy some Cogs.\x07Head to the gag shop to buy more gags, it seems you are running low on them.\x07To buy gags, head to the trolley and play some games.\x07Games reward you with Jellybeans, but always use them on gags first!\x07Another tip to getting Jellybeans is by fishing.\x07After obtaining one Jellybean, you can use it to fish, earn a laff point, or even multiply your Jellybeans!\x07Also, remember that, while you may have started with 2 gags, the Toon HQ cannot keep supplying you with more.\x07Some things you need to pay for yourself!',
  COMPLETE: 'You defeated the invading Cogs, great!\x07Let’s look at the list…\x07shticker book, tick!\x07Catalog… tick again!\x07Gag training, tick!\x07Made friends, another tick!\x07Finally, the trolley.\x07Final tick!\x07Good work Toon, you’ll make a great HQ Officer yet.\x07Come and talk to me again when you are ready to start your next task.'},

 # Task 2: Decisions, Decisions
 120: {
  QUEST: 'Before we can set you free, you have one last task to do.\x07You will need to go see Mulzak.\x07He is our resident wizard, though these days he mainly focuses on producing crackers for Toontown.\x07Still delicious, though!\x07Anyway, why don’t you go and head over to him_where_'},
 121: {
  QUEST: 'Oh boy am I glad you’re here!\x07I’m supposed to let you pick your new gag track\x07But um… well\x07let me give you your options… you can pick Toon-Up or Sound gags.\x07I mean, they’re both great options.\x07Toon-Up will let you, um…\x07heal your fellow Toons in battle… while Sound will damage all the Cogs that are in the battle, you know?\x07Um… I need you to retrieve something for me first, though.\x07Use this time to decide which gag tack you’re gonna choose!\x07Those darn Lawbots stole my magic cracker recipe.\x07Will you go get it back for me? Oh man, oh man,\x07I can’t lose that recipe…'},
 400: {GREETING: '',
       QUEST: 'Oh thank you!\x07Thank you!\x07Thank you!\x07I would have my feathers if I lost these!\x07You’re a feather saver!\x07How can I ever repay you?\x07Um, what was that?\x07Oh yes! You’re supposed to choose a new gag track!\x07I um… I guess I forgot.\x07I’ve been a… been a terrible wreck since the Cogs returned.\x07I’ve never been comfortable around the Cogs, you know?\x07They’re incredibly creepy looking and they are always going on about their business plans!\x07Oh gosh, I’m rambling again.\x07Anyway, why don’t you choose your gag track?\x07Toon-Up or Sound.',
       INCOMPLETE_PROGRESS: 'Back so soon? Okay, are you ready to choose?',
       INCOMPLETE_WRONG_NPC: 'Think about your decision before choosing.',
       COMPLETE: 'Interesting choice, I guess.\x07Now before you can use those gags, you must train for them.\x07You must complete a series of ToonTasks for training.\x07Each task will give you a single frame of your gag attack animation.\x07When you collect 15 frames, you can get the Final Gag Training ToonTask that will allow you to use your new gags.\x07You can check your progress in your Shticker Book’s Inventory Page.',
       LEAVING: QuestsDefaultLeaving},

 # Task 3: Blue Goo That Sticks to You
 1039: {
  QUEST: 'Our resident glue-maker Sticky Lou has seemed to have gotten himself in another sticky situation.\x07Please go over to his store and see if you can help him fix the issue.\x07Oh, and PLEASE tell him to be more careful around his glue!\x07We can’t keep sending Toons out there every other day to free him from the stickiness._where_'},
 1040: {
  QUEST: 'Oh, look! They finally sent another Toon!\x07I look like a buffoon.\x07I was making a fresh batch of glue, ya’ see?\x07Then suddenly it fell and now it’s stuck to me!\x07Now, I’m stuck here, like a plant in soil!\x07Please try getting me some oil!\x07Now, you need to get it fast, like you’re in a race!\x07Perhaps you’ll find some oil with a Toon named Kace._where_'},
 1041: {
  QUEST: 'What?\x07Lou is stuck… again?\x07The truth is: this happens every week.\x07My top-grade oil usually helps him out though. So, I can see why he sent you.\x07I will need some time to prepare the oil. So, why don’t you take out a few of the Cogs around town while you wait?'},
 1042: {
  QUEST: 'Alright!\x07The oil is ready for Lou.\x07Please tell him to be more careful next time!\x07Luckily for you, he’s my best customer!\x07So, I’m giving you my BEST oil!\x07See you ‘round._where_'},
 1043: {
  QUEST: 'Ah, you’re back!\x07What a joyous day!\x07Oh no, what’s this?\x07It isn’t going away!\x07Okay, I don’t know what will help me out now.\x07What?\x07You ALSO don’t know how?\x07Well then, I know the perfect person to tell.\x07The Master of Irrelevance!\x07You know, the famous Irrel!_where_'},
 1044: {
  QUEST: 'Hi there, Toon!\x07What? Sticky Lou is stuck in ANOTHER pile of glue?\x07That’s nothing!\x07Just find some petroleum jelly!\x07It’s specialised for taking away stickiness. So, it’d be perfect for your situation.\x07If I were you, I’d try asking Donut Doug.\x07He keeps all sorts of weird jellies around for his donuts!_where_'},
 1045: {
  QUEST: 'What?\x07WHAT?\x07Yer gonna haf to speak up, laddie.\x07I don’t got no good hearing holes no more, ya’ see?\x07Smelly?\x07No?\x07Belly?\x07OH, jelly!\x07Sure!\x07I have plenty of types of jelly.\x07Strawberry, blueberry…\x07WHAT, PETROLEUM!?\x07Ye sure are one of the weird one’s, but sure!\x07Tis not teh first time being asked for that jelly, usually some mouse called… what was it?\x07Ah, Sticky Lou, me thinks.\x07He always comes ‘round askin’ for that.\x07I will need some time though! So, why don’t ye take down some of them robot thingers outside?'},
 1046: {
  QUEST: 'Ye did it!\x07Thank ye’ so much laddie!\x07Why don’t ye run this here jelly back ov’r to that Sticky Lou fella?_where_',
  COMPLETE: 'Petroleum Jelly, are you kidding me, Toon?\x07You say it works?\x07Do you think I look like a loon?\x07Okay, okay, I will see how it does.\x07What’s this…\x07I’m free!\x07I feel like I could buzz!\x07You’ve earned you rewards, Toon! Even if the journey was a bit iffy…\x07Now, I’ve got to go!\x07I have to get another batch of glue going!'},

 # Task 4: Cheating The Cheethah
 1047: {
  QUEST: 'We’ll need you to go see Cheetah.\x07He’s reported that he’s been having some issues with his "friends"?\x07Not sure what that means, but I know that you’ll be able to find out!\x07Good luck_where_'},
 1048: {
  QUEST: 'Ay, ay, ay whatta we got here?\x07Oh, youza Toon.\x07I heard of yah.\x07My fellow uh\x07er…. associate rivals believe I am err.. a lie-ah about business and scamming customers.\x07I need you to do some err.. talking to my friends…\x07you see my friends are Cogs.\x07Listen, I don’t do no such Toony business and I don’t fool around.\x07I need you to permanently erase my Cog friends.\x07Gettin’ some sellbots should do the trick.\x07Get rid of the competition and end this rivalry for good.'},
 1049: {
  QUEST: 'Thanks and all but, wees gotz us a new problem you see.\x07With all this Toony and Cog business in town well of course my liar liar pants got stolen!\x07I need to set them on fire and get rid of them, like get rid of the evidence and all.\x07I don’t lie!\x07It’s my…\x07uh…\x07cousin’s pants?\x07Yes, my cousin’s! Just get it back in one piece.\x07I think someone dropped it in some lake.'},
 1050: {
  QUEST: 'Listen I know you did a lot but, my aunt got her purse stolen from my friends.\x07I need youz to be the town hero and all…\x07basically get my aunt her purse back.'},
 1051: {
  QUEST: 'Ok so you did a pretty good job and all.\x07Now I need you to check in with my friends the HQ Officers,\x07they owe me a sandwich.\x07Just get it from them\x07I need it now and I’m getting hungry!\x07I’ll pay you handsomely with all I gotz.'},
 1052: {
  QUEST: 'Whats this…\x07A sandwich?\x07You got lied to my friend.\x07You see, Cheetah likes to well…\x07cheat Toons out of things.\x07He has them do all kinds of stupid errands for him and then cheats them out of the reward they were supposed to get!\x07Always the same lies; a sandwich, liar liar pants, and some sort of purse.\x07Yeah that purse wasn’t his, it was another Toon’s.\x07I’m sorry to break the news to you, but Cheetah is nothing but a liar.\x07Here, take this note.\x07I’ve written that if he continues to act this way we may have to take some action.',
  COMPLETE: 'Whoa-whoa-whoa back it up buddy-o.\x07Yeah, so what maybe the whole game was a cheat?\x07Maybe I rigged the game from the start.\x07Maybe…\x07I had a reward this whole time for you.\x07Oh wait what?\x07A note?\x07HQ Officers, always pranksters.\x07This wasn’t a joke?\x07Oh, well… I suppose I should stop.\x07As for you I guess you got in on some of the business I had in store.\x07I don’t normally do this but, I guess I’ll have to give you a reward.\x07You just have to do 50 buildings…\x07hah, just messing with you.\x07Now get outta here and keep this secret to yourself, mkay?'},

 # Task 5, Lean Mean Jellybean Machine
 # Yes its a Coach Z Evil Twin's Reference
 1053: {
  QUEST: 'Next up we have a task we think you’ll love, if you like Jellybeans that is.\x07Go see Silly Billy for your next task._where_'},
 1054: {
  QUEST: 'Howdy there, partner!\x07Now don’t get scared off if I go and say somethin’ you don’t understand.\x07That’s why they call me Silly Billy!\x07Now, I’ve heard you’re so poor that you have a tumbleweed as a pet!\x07I’m kiddin’!\x07Now, bud, let me make a deal for ya’.\x07You go collect some stuff for me that I need, an’ I’ll see about settin’ you up with a new state o’ the art Jellybean jar, eh?\x07Betcha like the idea of that!\x07To start off, I’ll need around… 5 pieces of scrap metal.\x07That should do it.\x07I’d think that those Cogs are built of some, eh?\x07Go defeat some Cogs until ya’ get what I need.'},
 1055: {
  QUEST: 'Well butter my buns and call me a biscuit!\x07Ya’ did it!\x07Now, go take these to Natta Cog at Not A Cog Place.\x07She is a pro at craftin’ all things from tiny doohickeys to… you guessed it, Jellybeans jars!\x07She will fix ya up with what I need to make this for ya!_where_'},
 1056: {
  QUEST: 'What? Silly Billy sent you?\x07Ah! Of course\x07I’ll make you a bigger Jellybean jar!\x07I will need a bit of time though, it’s quite a difficult project!\x07Why don’t you take down some Cogs for me while you wait?'},
 1057: {
  QUEST: 'Thanks, buddy! Your jar is all finished, and I went ahead and sent it over to Silly Billy just for you.\x07You should go return to him now, see ya’ round._where_',
  COMPLETE: 'Wow!\x07You’re faster than green grass through a goose!\x07Here, take your new jar as a reward!'},

 # Task 6: Something Sus-swiss-cious
 1058: {
  QUEST: 'We’ve been having some issues over at the detention center\x07It seems some of the more… unruly ones have been giving Officer Orion a run for his money.\x07Could you go over and ask him if he needs any help?._where_'},
 1059: {
  QUEST: 'Stay back! I warn you!\x07Oh, it’s just a Toon.\x07Phew, for a second I thought it was another…\x07AH!\x07Behind you!\x07Oh… nevermind.\x07It’s just a door.\x07Up to now, everything in the detention center had been running fine.\x07Then, suddenly, we got an influx of some rather rude visitors being sent into the detention center\x07which halted all progress we were making with our previous guests!\x07I suppose you could help me, though.\x07First of all, I’ll need some checklists so that I can count how many new guests we have.\x07Usually I see Telemarketers roaming around carrying some, so maybe try defeating a few of them?'},
 1060: {
  QUEST: 'Ah, good work, Toon!\x07That’ll be useful for seeing who we actually have here in the detention center.\x07Next up, I’ll need some batteries to put into the automated doors and remotes that we use here in the center.\x07You may not see them but do not fret\x07It’ll help the center run more smoothly, of course, as we can’t have our guests running around in a rampage!\x07Now, for the best batteries, I’ve heard that Yesmen have some of the best out there.\x07Try grabbing as many batteries as you can from them.'},
 1061: {
  QUEST: 'Amazing, Toon!\x07Rumor has it that these batteries can last for millenia!\x07Or atleast until the next Toon comes.\x07Anyway, we should nearly be done with the list now.\x07Next up, I believe I’ll need…\x07ah, yes\x07I’ll need a new uniform.\x07You see, my old uniform was ravaged by the rampaging guests.\x07I don’t think you’ll be able to get that from a Cog\x07though… ah, I know!\x07Go see Funny Pant\x07she always has had the best attire in Toontown!_where_'},
 1062: {
  QUEST: 'Ah!\x07Come through the door a customer has…\x07what does the customer want?\x07New uniform the customer says?\x07Yes! Can do that Funny Pant can!\x07Though there is one thing says Funny Pant…\x07Funny Pant needs fibres, yes!\x07From the Cog suits the fibres come from…\x07maybe 5 will do.'},
 1063: {
  QUEST: 'Beautiful the fibres are…\x07make a suit Funny Pant can.\x07Will take time though, says Funny Pant.\x07Defeat some Cogs on this street you should.'},
 1064: {
  QUEST: 'Back you are…\x07ready the suit is.\x07Please to help you Funny Pant is.\x07Send my regards to Officer Cheddar you must!_where_',
  COMPLETE: 'That should be all.\x07You’ve really helped an old officer out.\x07What was it that we’re keeping here?\x07Well, cheese of course!\x07The… rampage?\x07Cheese can be vicious too, you know!\x07Try asking the parmesan! Anyway, take your reward Toon, you’ve deserved it.\x07You can now eat Cheedar Cheese.\x07Oh, thats not the reward\x07Right, sorry bout that\x07Just remember, if you ever see another rogue cheese, make sure to come and tell me, mkay?'},

 # Task 7: Melodious Mathematical Mayhem
 # +1 Laff
 1065: {
  QUEST: 'For your next task I’m going to have to send you on a bit of an errand\x07You see, the HQ is a bit behind on it’s supplies\x07as…\x07well…\x07  I might have forgotten to order the supplies for the next month, and since they come from Toontown, they take a while to arrive.\x07t’s very important, you know!\x07We usually get our supply from Toontown Central\x07But I guess the next best place will have to be Factor’s School of Mathematics\x07He keeps all sorts of gear there_where_'},
 1066: {
  QUEST: 'Oh, hello!\x07So you see\x07I was chasing down a Cog that stole a fraction of my special rulers…\x07while I was out on lunch break!\x07This left me with this ruler that he dropped on the ground as the Cog ran.\x07Needless to say\x07I didn not get them all back.\x07What is that?\x07Here for building measurement tools?\x07Well, you gotta earn them\x07Though, I suppose you could start by getting my box of rulers back\x07yeah?\x07I would do it myself but I do not feel like it.\x07The Cog was a Cashbot.\x07You can tell it is a Cashbot by the money it exudes.\x07Well…\x07I do not care how you retrieve it the box of measuring supplies\x07I just care they they are not damaged in the process\x07And if you bring them back in one piece\x07I will sell you what you need for 100 Jellybeans.\x07Whats that…\x07Toon HQ sent you?\x07Ah, those will be free then.\x07Now, go before I change my mind\x07And come back with the box or else the deal is off.'},
 1067: {
  QUEST: 'Is that a box of broken rulers?!\x07Wait, you say the Toon HQ sent you and are in need of supplies?\x07Of course! That makes sense! - Visit Sticky Sue, Sticky Lous sister\x07She should be able to fix the rulers for you.\x07Take this box of broken rulers, and ask Sticky Sue to glue them together against the entropic nature of the Tooniverse\x07to make the broken chaos become order!\x07Factor: Take this box of broken rulers, and ask Sticky Sue to glue them together against the entropic nature of the Tooniverse to make the broken chaos become order!\x07After you are done over there, come back here and we can discuss the sales terms for the rulers._where_'},
 1068: {
  QUEST: 'Hello there, Toon!\x07I am sorry that I could not greet you at the door\x07but I am currently stuck!\x07But, Instead of asking you to free me, I am going to ask why do you have a box of rulers?\x07Why do you have a box of rulers?\x07Oh! Factor sent you! - You need them to be glued back together? That, I can do!\x07Promise to do me a favor when I call for it and I will get to work!\x07But while you wait\x07Can you take care of some of those nasty sellbots\x07'},
 1069: {
  QUEST: 'There, all done!\x07Go return these to Factor_where_.'},
 1070: {
  QUEST: 'Did you get the rulers fixed up?\x07Great! That will be 30 Jellybeans\x07Wait!\x07Is that a mis-aligned ruler?\x07Get this thing out of my perfect building!\x07I will collect my payment\x07in some other way.',
  COMPLETE: 'You got the rulers?\x07Toontastic!\x07Here is your reward'},

 # Task 8: Traveling around the Island
 # TP Access to TIC
 1071: {
  QUEST: 'We see the progress you’ve been making\x07and we think it’s time you unlock something special_where_'},
 1072: {
  QUEST: 'Would you like to look into one of our many houses we have on the beach side\x07Oh?\x07The HQ officers sent you?\x07That means they see you worthy enough to be tested!\x07Okay, go take down 6 level 2+ Cogs for me!'},
 1073: {
  QUEST: 'You did it!\x07Great job!\x07I hope you didn’t think that was all!\x07I have another task for you to do.\x07This time I need you to defeat 3 level 3+ Cogs.'},
 1074: {
  QUEST: 'Wow!\x07You’re getting strong!\x07Okay, one final task.\x07I need you to defeat one level 4 Cog.\x07You cannot find these here in Toon Island Central\x07Go check out the neightboring Rainbow Rise playground\x07Be safe!',
  COMPLETE: 'Toontastic!\x07Alright, I think you’ve proven you can handle yourself\x07So, here’s something that will help you out around town.\x07You can now Teleport to Toon Island Central.\x07And if you ever meet any other Toon, recommend this travel agency to them.'},

 # Task 9: Gag's O' Plenty
 # Carry 30 Gags
 1075: {
  QUEST: 'Alright, now that everything is starting to run smoothly\x07we think you deserve some more gag space.\x07Go talk to Ricky Tricky.\x07He is a master at training Toon into being worthy of more space._where_'},
 1076: {
  QUEST: 'So you seek to harness the power of holding more gags in your pocket?\x07I’m not going to lie the path is long and dark.\x07You may not make it out alive.\x07HA! You should have seen the look on your face!\x07Of course it’s not going to be dangerous!\x07We wouldn’t send a new Toon out into all of that in the first place.\x07Now, please go defeat 6 level 3+ Cogs for me'},
 1077: {
  QUEST: 'So you did it already?\x07Fine. Time for some more challenging stuff.\x07I need you to go defeat 4 VP’s, 2 CEO’s, and a level 20 Cog.\x07HA! Got you again!\x07We don’t even know where these guys are since the defeat of Toontown.\x07Go defeat like 5 Cogs,\x07Can be any time.',
  COMPLETE: 'Alright\x07Final mission I need you to fight your way back into Toontown and reclaim your old home.\x07Should be easy enough right?\x07HA! I swear you Toons are so easy to fool.\x07Here ya go!'},

 # Task 10: More Tasks, More Fun
 # Reward: Carry 2 Toontasks
 1078: {
  QUEST: 'You’re doing amazing work Toon!\x07Why don’t you go speak to Factor.\x07He can help you carry more tasks on you at once._where_'},
 1079: {
  QUEST: 'Why hello there!\x07Yes, I’m going to help you with improving your speeds.\x07It’s all common math.\x07Carry the X here\x07add the Y there\x07and UREEKA!\x07We have the exact mathematical equation for the process.\x07But…\x07I lost my calculator to the Cogs the other day!\x07Can you please go find it for me?'},
 1080: {
  QUEST: 'Thank you!\x07Now as for your reward…\x07Oh drat!\x07The calculator!\x07It’s broken!\x07Please take it to Remote Robert.\x07He knows how to fix these things_where_'},
 1081: {
  QUEST: 'Hello!\x07Oh?\x07Factor is having troubles?\x07I can fix this Lickity Split!\x07I just need my screwdriver\x07Which was taken by the Cogs.\x07Can you get it for me?'},
 1082: {
  QUEST: 'Thank you!\x07Just a one, two, three….\x07Alright! His calculator is fixed!\x07Send Factor my regards._where_',
  COMPLETE: 'My calculator!\x07Thank you!\x07Alright now, just let me do some configurations…..\x07And there we go!'},

 # Task 11: Baking Contest
 # Reward: +2 Laff (max 25)
 1083: {
  QUEST: 'Ma Putrid wants to enter a baking contest.\x07But she does not know how to bake\x07Can you help them bake some pies\x07or find a way to get them to enter._where_'},
 1084: {
  QUEST: 'I want to enter a baking contest.\x07But ailas I cannot bake. I always wanted to be in a baking contest\x07The winner gets to get a vacation to Toontown.\x07But not sure why would you would want to go there.\x07Anyways, my friend Cakeman owns a bakery\x07Maybe go see if they want to help us out.\x07Hopefully I dont get caught cheating_where_'},
 1085: {
  QUEST: 'Hello did Ma send you?\x07She called me earlier\x07Great ill start to bake the pies\x07But please defeat these 12 pesky Cogs first.\x07I need some time to bake these and a little errand might help me prepare them faster.\x07You know distractions makes practice\x07Wait thats not right…\x07Anyways, Thanks.'},
 1086: {
  QUEST: 'Thanks, but the pies are not done yet\x07they just went into the oven.\x07Can you go defeat 5 more Cogs\x07Paticually the Cashbots\x07They keep on trying to buy me out\x07And I cannot let that happen\x07I provide most of the islands throw gags.'},
 1087: {
  QUEST: 'You proved yourself\x07I would give you the pies\x07But a nasty little Cold Caller just came in and took them :(\x07Please defeat them until you find the pies.\x07I dont want Ma to fire me…'},
 1088: {
  QUEST: 'Great nice job finding the pies.\x07Bring them over to Ma pronto._where_'},
 1089: {
  QUEST: 'Hey thanks for the pies.\x07Now lets test their taste.\x07WOW these pies are GOOD.\x07WAIT…\x07These taste like Cream Pies\x07AND IM ALLERGIC TO CREAM PIES\x07Please go clarify with Cakeman to make sure the pies are okay._where_'},
 1090: {
  QUEST: 'Why are you back…\x07Oh right!\x07I feel really bad now\x07Please give this free batch of pies to Cakeman. Pronto before Ma eats more of them.\x07And please tell her im very sorry._where_',
  COMPLETE: 'YAY!\x07Your back\x07Wait you have more pies\x07Great!\x07Oh…\x07Well atleast these pies are for the baking contest\x07Hopefully I dont get caught that I cheated\x07Thank you so much for your hard work.'},

 # Task 12: Comet Conspiracy
 # Reward: Sound/TU Gags
 1091: {
  QUEST: 'Sir Comet have some problems regarding a device he is making that could stop the Cogs\x07It is powered by a comet he is discovering that is out of this world.\x07You see this comet is unlike any other thing we’ve ever seen.\x07I don’t believe it is even Toony or Coggy whatever it is, is out of this world.\x07Its giving off a rare side-effect to travelers that I cannot identify\x07Please go help him test his machine_where_.'},
 1092: {
  QUEST: 'I have some very strange problems with my comet I was researching.\x07You see this comet is unlike any other thing we’ve ever seen.\x07Like HQ probably told you\x07We don’t believe it is even Toony.\x07I have devised a machine capable of harnessing this device to use it to stop the Cogs\x07Well it has not been tested yet.\x07When I did test it well…\x07It came to such failure and I need Cog gears to fix it.\x07Defeat about 20 Cogs so I can fix the machine pronto.'},
 1093: {
  QUEST: 'Ah ok thanks for the Cog gears I really needed them.\x07Ok I’m going to try and configure this into the machine. Ahh\x07I dont know where they need to go!\x07Mind going over to HQ and asking them for some information on Cog gears.\x07Toon HQs can be found anywhere\x07including on this street._where_'},
 1094: {
  QUEST: 'I heard you need some information on how to use Cog gears.\x07We dont keep this information here because no one reads manuals.\x07However Edwin may be able to help you._where_'},
 1095: {
  QUEST: 'Manuals?\x07To what\x07Screws, bolts\x07What Cog GEARS!\x07I just threw that away the other day\x07Librarian Liz may have a spare copy however my library card was just stolen by the Cogs.\x07Specficially those stupid Name Droppers.\x07Please go recover it for me to lend to you.'},
 1096: {
  QUEST: 'Thank you!\x07Now use that library card and give it to Librarian Liz\x07She can hopefully provide you with some information on Cog gears._where_'},
 1097: {
  QUEST: 'You need resources on Cog gears!\x07Just need a copy of your library card…\x07WHAT!\x07This is not your card\x07Oh…\x07I see…\x07Well then here you go and tell Edwin Hi for me._where_'},
 1098: {
  QUEST: 'Thank you!\x07Great\x07Thank you for my library card. Go deliver the manual to Sir Comet in a instant._where_'},
 1099: {
  QUEST: 'Thanks for getting that information.\x07I was able to install the Cog gears properally\x07Now at days we don’t get much help around here anymore.\x07You look like you are a bit low on beans..\x07How about you go fishing?\x07I got a good fisherman near that pond and he’ll buy whatever you can fish up.\x07Speaking of fishing though…\x07I need you to recover a Comet Pebble from the pond.\x07They are hidden in lakes or even ponds around Rainbow Rise.\x07Just get it back in one piece.'},
 1100: {
  QUEST: 'You got the pebbles all in one piece.\x07Not bad kid.\x07But, before we go on about bravery and rewards I need to test this thing.\x07Speak to Celtic.\x07They said he was testing it or something.\x07Just ask him if it even works._where_'},
 1101: {
  QUEST: 'Oh, what’s this?\x07Something about testing?\x07Yeah I tested it and I don’t exactly know if it worked.\x07It turned on for a second and turned off.\x07Listen I got some more work later with the resistance and I haven’t had much time to test this thing.\x07If you could do my job for me and recover a encrypted code I’ll test it.'},
 1102: {
  QUEST: 'You got the code?\x07Man I am so shocked.\x07Just kidding, I had faith in you.\x07Anyway Sir Comet wants his testing results.\x07I tested it when you left and so far it didn’t work.\x07Now about the encrypted code..\x07The encrypted code was used to encrypt machines to change it in any way.\x07Problem is the resistance found it doesn’t work on Cogs.\x07Maybe not Cogs but, what if it works on Sir Comet’s machine?\x07Just go and give it to him.\x07Test it see if it works._where_'},
 1103: {
  QUEST: 'Ha, what is Celtic on about this time, an encrypted code?\x07Well, lets just try out this so-called encrypted code that can adapt the machine.\x07Hmm… it actually manipulated the surroundings of the machine to mimic its abilities.\x07I guess I doubted the code too much.\x07Wherever Celtic found this code is beyond me.\x07At least we know now that it works…\x07Wait, WHAT WAS THAT NOICE\x07This does not look good\x07IS THAT A Cog BUILDING!\x07Thats the first one here on this island.\x07Can you go back to HQ and tell them about it.\x07Toon HQs can be found anywhere\x07Including on this street'},
 1104: {
   QUEST: 'Oh?\x07A Cog BUILDING?\x07Caused by Sir Comet!\x07When I get the hands on him…\x07Sigh\x07Look the Cogs would of found our new home eventually.\x07Even if his stupid machine did not cause it\x07I hate to break it to you but that building needs to go down\x07Please go take down a Cog Building and return to Sir Comet when completed.\x07Hopefully then you will gain your reward.',
   COMPLETE: 'Well, you taken down the building\x07I almost doubted you\x07Thank you for hepling me test this machine\x07That apparently summons Cog buildings.'},

 # ==========================
 #      Withering Woods
 # ==========================

 # Task 1: Gag Training
 # Reward: +2 Laff

 2001: {QUEST: 'We have heard alot of good things about you _avName_ it is time for you to move on to Withering Woods.\x07Visit Instructor Gandling at The Withering School House._where_'},
 2002: {QUEST: "Well hello there you must be a new student!\x07Oh you are not a new student you say then what brings you here?\x07Ah yes now i know why you are here your the new toon\x07That flippy was raving about.\x07So You are here to choose your next gag track then?\x07Here in withering woods we dont give away free stuff so you will have to earn it.\x07The way you can earn it is very simple\x07a pesky Downsizer stole my instructor's pen.\x07Please recover the instructor's pen from that Downsizer and then I will allow you to choose your next gag track.\x07Hurry up i cant grade papers without my instructor's pen!"}, # Swap Downsizer for Sycophant
 2003: {QUEST: "Ah yes this pen will be very useful.\x07Or it would had been had that darn Downsizer not used up all the ink.\x07If you go fishing for some octopuses you can get more ink for me.\x07Remember octopuses can only be found in rainbow reef so you will have to go there to get some."},
 401: {GREETING: '',
       QUEST: 'Finally that will do just fine thanks for all the help today.\x07You can now choose between Lure and Drop as your next gag tracks!.\x07Take your time deciding, and come back here when you are ready to choose.',
       INCOMPLETE_PROGRESS: 'Think about your decision before choosing.',
       INCOMPLETE_WRONG_NPC: 'Think about your decision before choosing.',
       COMPLETE: 'A wise decision…',
       LEAVING: QuestsDefaultLeaving},
  
 # Task 2: Training With Oak
 # Reward: +2 Laff

 2165: {QUEST: 'Professor Oak is having a pet problem\x07So we need someone to fix it\x07Please go check up on the old man._where_'},
 2166: {QUEST: "Howdy toon are you here to help me with my problem?\x07Great i am a professor you see and and i also love to collect animals.\x07I had 3 very rare species of animals here in my lab but unfortunately\x07The cogs came in and stole all 3 of them can you help me find them?\x07Amazing the first was a Orange Lizard i saw a Two-Face take him.\x07Please Save him before they do something evil to him!"}, # Swap Two-Face for Temporizer
 2167: {QUEST: "Great job you found him but the other two are still out there somewhere\x07While you was gone i found this note it was dropped by a Number Cruncher\x07The Note Tells us the wearabouts of the next animal the Blue Turtle.\x07What are you waiting for _avName_ get a move on!"},
 2168: {QUEST: "Good Work we just got one more to go but unfortunately i have no clue\x07Where this one could be we could start with trying to find more notes\x07Go fight cogs till you find a note telling us the wearabouts of the final animal!"},
 2169: {QUEST: "Ok lets see here hmm interesting very interesting it seems the final animal\x07Was taken to a Big Wig. This is a dangerous task so tread lightly _avName_\x07I recommend finding other toons to attempt this.\x07Big Wigs can only be found in Buildings!",
        COMPLETE: "Thanks alot for recovering all my pets and as for your reward"},

  
 # Task 3: Food Fright
 # Reward: +2 Laff
 
 2170: {QUEST: "We got word that a disaster has happened over at Pizza Taco Burgers.\x07Go help him out im sure he will make it worth your while._where_"},
 2171: {QUEST: "Oh this is just terrible _avName_ thank goodness you have come to help me!\x07Have you heard of Dill Flye?\x07The famous Scientist himself was here at my shop.\x07I was so happy to serve him my famous taco burgers but there was one problem.\x07Cogs Poisoned my beef and Dill Flye got food poisoned!\x07And what's worse he blames me for it and he has threatened to sue me!\x07I tried to tell him it was the cogs and it wasn't my fault but he wouldn't believe me.\x07Maybe you can convince him that I am innocent!_where_"},
 2172: {QUEST: "Well hello there my toon friend you must have a good reason to be speaking to me?\x07Yes indeed i did threaten to sue pizza taco why does it matter to you?\x07So he sent you to me to try and get me to change my mind?\x07I will tell you what if you can get proof that the cogs did it i will change my mind.\x07Solver Sullivan at Axe-idents Happen will be a good start._where_"},
 2173: {QUEST: "Hello there _avName_ how may I assist you today?\x07So you wish to find evidence that Pizza Taco is innocent?\x07Its a good thing you came so soon because I happened to over hear some cogs planning to poison something.\x07Im sure if you fight some of the cogs you will find a journal detailing plans to commit this act."},
 2174: {QUEST: "You did it you found the evidence hurry and take it to Dill Flye!_where_"},
 2175: {QUEST: "Great you have done me and pizza taco a great favor!\x07Take this note to him saying that i apologize for the false accusations._where_"},
 2176: {QUEST: "Thanks _avName_ for all the help but we have one more problem\x07The Cogs found out that there plan was ruined and they sent a Legal Eagle after me\x07I was able to get away but he stole my special golden spatula please recover my Golden Spatula.\x07Also legal eagles can only be found in buildings good luck",
        COMPLETE: "Thank you so much _avName_\x07I cannot explain how happy you have made me"},

 # Task 4: Got any grapes?
 # Reward: +2 Laff
 
 2177: {QUEST: "Doug The Duck is going through a grape crisis\x07Can you help prevent a Graptastorphy._where_"},
 2178: {QUEST: "The Cogs stole all my Grape juice!\x07I am thirsty and all i have left here in my shop is lemonade and im totally not making a duck song reference, but i hate lemonade.\x07Please recover a case of grape juice from the cogs!"},
 2179: {QUEST: "What is this? I said recover Grapes not Grape Juice\x07Get back out there and find my grapes!"},
 2180: {QUEST: "No you REALLY must of misheard me\x07Grapes stink\x07I really just need is for you to take down a 3 Story Cog Building.",
        COMPLETE: "Fine im finally satisfied take this 2 point laff boost and get out of here before i change my mind"},

 # Task 5: House of Junky
 # Reward: Carry 40 Gags
 
 2181: {QUEST: "Mr. Dunky was having a yard sale when the cogs stole all his products\x07Go see if you can help him out if you wanna get a huge reward._where_"},
 2182: {QUEST: "Hello there _avName_, what have you come to buy?\x07Well unfortunately I have nothing left thanks to the cogs\x07I am selling my business and was having a huge sale\x07because everything has to go when a bunch of Cogs came in and stole all my items.\x07If you can help return my items i can give you an old gag pouch.\x07There was 20 of them\x07You can find them on any Cog here in Withering Woods."},
 2183: {QUEST: "Great job but we have one big problem.\x07While you were gone a money bags came in and took the gag pouch.\x07If You can find that money bags ill let you keep the gag pouch free of charge.",
        COMPLETE: "I Think you more than earned the right to keep this gag pouch!"},

 # Task 6: The Training Of A Warrior
 # Reward: +4 Laff
 
 2184: {QUEST: "Master Shifo at Fist and Palm Trees:Dojo is looking for the next great Kung Fu Master\x07Do you think you got what it takes?._where_"},
 2185: {QUEST: "Hello there toon it is a great honor to meet you i have heard great things about you\x07But as great as you are i don't think you got what it takes to be a Kung Fu Master\x07If you want to prove yourself worthy of being a black belt as well as receiving a 4 point laff boost then let me show you the ropes grasshopper.\x07First to Rise the ranks you must defeat Sellbots.\x075 of them to be exact\x07Good luck i am to be expecting your return"},
 2186: {QUEST: "Good job my student you have proven yourself worthy to wear this White Belt \x07You have made me proud but you are not done yet i am getting  old and very weak and some day i will need to pass this dojo down to a new master i would be honored for it to be you once your journeys are over but first i require that you atleast reach the black belt ranks\x07The next part of your Journey to becoming a Black Belt is Cashbots\x07 Please defeat 10 of them then return to me."},
 2187: {QUEST: "You are fastly improving _avName_ you give an old man hope\x07That this world is in good hands with younglings like you.\x07You have earned your Orange Belt\x07but why stop there you are becoming a great student next up to earn your Purple belt you will need to defeat 15 Lawbots here in Withering Woods i believe in you my student return to receive your final task when you are done."},
 2188: {QUEST: "You are ready for your final test to earn your black belt it is very simple i require that you take down one of the toughest buildings here in Withering Woods take down a 4 story\x07And then return to me for your final reward",
        COMPLETE: "You have done it _avName_ you have earned your black belt.\x07I am very proud of you have earned this 4 point laff boost\x07You shall be the next master of the Fist and Palm Tree Dojo.\x07Stay Safe my student."},

 # Task 7: Its Never Ogre
 # Reward: +3 Laff
 2189: {QUEST: "Howdy _avName_\x07Green the Ogre over at xer shop is having a problem with fairy tale creatures\x07Xe needs your help to get rid of them._where_"},
 2190: {QUEST: "You dere toon i just wanna  be alone here in mah Shop  but these fairy tale creatures\x07Wont leave my shop they say they were ran here  by some cogs if you help me get rid of these fairy tale\x07Creatures i will greatly reward ya i doubt just defeating just a bunch of cogs will  run the head honcho off \x07But its a good first start defeat cogs till you recover a journal detailing who is the cause of bringing these fairy\x07Tale creatures here._where_"},
 2191: {QUEST: "Good but we got one problem I cant read this its in some type of ancient language.\x07You will have to find a way to translate this maybe the library here in Withering woods will be a good start Librarian Lucas im sure will have what we need to translate this head over to Shhh! Library.\x07Thats where Lucas sets up shop good luck._where_"},
 2192: {QUEST: "Welcome to my library these books come in all sizes all lengths and all times. New,old,long and short we got them all so what brings you here? Ah so you need a book to learn how to translate this journal? Lets see here hmm interesting this journal is in toonivari language an ancient toon civilization they used all types of symbols for there language when it was written i have what you need or i would of had it had a Downsizer not come in and take it\x07Ill tell you what if you find that Downsizer and recover that book ill let you keep it for free hows that sound?\x07Good now hurry up and get that Downsizer before its to late"}, # Downsizer -> Control Freak
 2193: {QUEST: "Good job unfortunately i cant translate this for you right now cause im very busy\x07Im sure you or whoever needed this will be able to do it just fine see ya around!"},
 2194: {QUEST: "Thanks for all the help but i will need time to translate this im kinda struggling here\x07In the mean time go take down 1 3+ Story Cog Buildings that should give me enough time to figure this out."},
 2195: {QUEST: "Good Job Ive cracked the code it looks like the culprit of this operation is one of the most strongest cogs, Mr. Hollywood himself.\x07You must gather a group of toons and go find one.",
        COMPLETE: "You did it those fairy tale creatures have left and now i can relax here alone in mah shop here"},

 # Task 8: The Hunt for The Ring
 # Reward: +3 Laff
 2196: {QUEST: "Dangolf needs your help hunting a very powerful ring._where_"},
 2197: {QUEST: "Halt You Shall not pass!\x07Oh your not a cog so your here to help me?\x07Great\x07So There was this ring a very powerful ring if fallen into the wrong hands could be\x07Catastrophic for everyone and alas thats exactly what happened a group of corporate raiders\x07Raided my shop and i fear the worse they are taking the ring back to there boss you must stop them\x07Before it is to late _avName_!\x07Corporate Raiders can only be found in buildings"},
 2198: {QUEST: "No this isnt good this isnt the right ring we will have to look again try to find another corporate raider this is just a normal gold ring nothing special about it "},
 2199: {QUEST: "Good job hero you found it but there is a big problem it seems the cogs have drained all the power out of it and used it for something i have no idea what but i fear what they could of done\x07But anyways there is still hope for us to fix it but we will need to find someone who has powerful enough magic to do so this is where my good friend Archmage Angelic comes in you will go talk to them\x07And see if they can fix the ring Archmage Angelic is held up at Arcanium Of Archmages "},
 2200: {QUEST: "Ah so your are a mage i have plenty of spells for sale for any able body with the skill enough to cast them.\x07Oh your not a mage well then what brings you here my friend?\x07Ah Dangolf my good pal has sent you here to fix this Ring this was a very powerful artifact i could fix it\x07But The Cogs Stole my Magical Wand if you recover it from them then we can continue "},
 2201: {QUEST: "You found it great i can fix it but it will take awhile\x07In the mean while clear out a 4 story+ Cog Building while your at it"},
 2202: {QUEST: "Great its all fixed up here take it dangolf and tell him i said fair greetings!",
        COMPLETE: "You have restored the ring to its former glory\x07But I am afraid we will find out very soon what the cogs did with The Ring soon enough be careful out there my friend."},

 # Task 9: A Little Birdie Told Me
 # Reward: Carry 60 Beans
 2203: {QUEST: "Gossipping Gibby Has really been picking up the gossiping here lately she has been talking about how there is some treasure hidden somewhere\x07but she wont tell no onex\x07maybe you can convince  her to tell you where it is if you help her out._where_"},
 2204: {QUEST: "Yes indeed you are here for the treasure i can see it in your eyes\x07Old Gibby Knows yes i can give you what you want if you  can run a few errands for me\x07You see Old Gibby has this big machine but she cant open it you need to play music\x07But Gibby cannot play it requires this lexicon to be transcribed indeed the key lies with Magic Maya._where_"},
 2205: {QUEST: "Hello there _avName_ welcome to my shop how may i help you?\x07Oh Boy so you have been talking to Gossiping Gibby? Shes a mad woman i tell you \x07She is not a normal toon ill tell you that much theres a dark secret so tread lightfully\x07I will help you though since you have done a good bunch of deeds for Withering Woods\x07But i cannot help you without the ancient toonvari transcriber. You see this cube you have here is not no ordinary cube its an ancient Cube that was created by the ancient tribe of toonvari they were an ancient \x07Tribe of toons that were very smart and were very advanced for there time but one day all of them disappeared out the blue they must of done something to anger the higher ups this cube and many other\x07Artifacts of theirs is all we have left of there culture but anyways enough explaining of who the toonvari are lets get to the point\x07A Pencil Pusher took off with it\x07If you can find that Pencil Pusher and bring the machinery back to me i can then help you transcribe this lexicon"},
 2206: {QUEST: "You did it lets see here yes it worked take this back to Gibby it should work now!_where_"},
 2207: {QUEST: "Yes lets see here lets open up the machine and see whats inside.\x07What? A book just a normal book this cant be Impossibl\x07let Gibby read this book!\x07NO YOU WILL GET NO TREASURE\x07GET OUT OF MY SHOP"},
 2208: {QUEST: "Your back i heard the terrible news are you alright?\x07Its Gibby that book she read it made her go mad i think that book has some type of dark magic or curse put on it.\x07Gibby ran off somewhere screaming and shouting that she was going to takeover toon island\x07for her dark lord and the treasure is all hers i managed to pick up this note that gibby dropped telling of the location of the treasure if you hurry\x07maybe you can retrieve the treasure but you will need a key first im sure one of the cogs around here will have the key",
        COMPLETE: "You found the key great but i have more updates on Gibby. It Turns out after all that book was cursed i talked to my friends dangolf and  Archmage Angelics and we have come to the conclusion that the disappearance of the toonvari was no random occurrence they  disappeared because they angered this same dark lord that is controlling Gibby.\x07We have also founded that pretty much\x07All of the artifacts of the toonvari except the treasure have been cursed thats why the dark lord is controlling Gibby he wants the treasure for his self we have made a huge mistake helping Gibby\x07But in time we will be able to Stop her here for all your troubles take this Jellybean Jar"},

 # Task 10: Taking A Vacation In Withering Woods
 # Reward: TP Access to Withering Woods
 2209: {QUEST: "Slippery Sloppy requires your assistance _avName_._where_"}, 
 2210: {QUEST: "Hey there again my friend! So you like withering woods right you think its liveable?\x07Well most people dont think so withering woods is rated the worst place to live in toon island\x07It is very sad it hurts my heart ive lived here since i was a little boy way before most of the outsider toons came here i want to restore this place to its former glory withering woods wasnt always so withering \x07And while we cant fix the withering part we can for sure make it a place to wanna live i was planning on giving away four free tickets for a vacation here in withering woods at an amazing five star resort\x07But the cogs took them you will need to recover each one then bring them to the toons that i planned on\x07Giving them to the first ticket was taken by a Two-Face"}, 
 2211: {QUEST: "Good Job!\x07Now your destination is Pop That Corn! Popcorn Making\x07Take this ticket to King Popcorn._where_"}, 
 2212: {QUEST: "Hows it going would you like to try some of my amazing popcorn?\x07Oh you got a gift for me what is it?\x07Wonderful a free vacation to withering woods id love to tell Slippery Sloppy\x07I Will Be On My Way as soon as possible._where_"}, 
 2213: {QUEST: "Alright Good job the next Cog you will need to take out is an Head Hunter."}, 
 2214: {QUEST: "Two Down two to go\x07Alright take this to Reg at the Sandy Spitoon in Olive Oasis then return once you do._where_"}, 
 2215: {QUEST: "Welcome to the Sandy Spitoon how tough are you?\x07Your so tough that you brought me a free vacation ticket to Withering Woods?\x07Wow that is impressive anyways tell Slippery Sloppy I Accept His Offer._where_"}, 
 2216: {QUEST: "Great ok so now  we need a ticket that was stolen by an Mingler\x07Minglers can only be found in buildings good luck!"}, 
 2217: {QUEST: "Only One More to go after this one keep it up!\x07Take this to Rod Rooster at Rock-A-Doodle-Doo in Minty Mines._where_"}, 
 2218: {QUEST: "Welcome to the best shop to hear some Rock N Roll Baby! Whats this you have something for me?\x07A Vacation Trip to Withering Woods?\x07Why would i want to go there that place is almost as bad as Olive Oasis.\x07You say it will be worth my while?\x07Fine i guess ill believe you tell Slippery Sloppy that i will come stay at this resort for a vacation._where_"}, 
 2219: {QUEST: "Great ok for the last ticket it seems i have no knowledge of what cog took it\x07So just fight cogs till you find it good luck!"}, 
 2220: {QUEST: "Great you have found all the tickets now hurry and take this one to Howard Horse at The Family Friendly Stern and then you can receive your reward._where_"}, 
 2221: {QUEST: "Hows it going bro\x07Welcome to the Family Friendly Stern where the whole family can come to have fun what brings you here?\x07Great thanks for this ticket my friend i will be packing my things as soon as you leave\x07Tell Slippery Sloppy i said whats up!_where_", 
        COMPLETE: "Wow you did it _avName_\x07You have returned withering woods to its former glory our ratings have went way up since you gave away these free vacation tickets\x07I have you to thank so here"}, 
 
 # Task 11: The Withering Finale
 # Reward: Last Gag Track Frame
 2222: {QUEST: "Return to Instructor Gandling he needs you urgently._where_"},
 2223: {QUEST: "You are finally ready to earn your final track frame _avName_\x07You have done this town a great deal.\x07Ill tell you that my friend but you have also caused one big problem\x07And as you probably know it has to do with Gossipping Gibby\x07I Hate To Inform you but it seems she has gone completely insane she has gone completely mad and is now working with the cogs to try and destroy Withering Woods\x07Its up to you to stop her first\x07You will need to head over to my friend at Withering The Witcher he has a task for you that is urgently in need of completion if we are gonna stop Gibby._where_"},
 2224: {QUEST: "Howdy _avName_\x07Gandling told me alot about you.\x07Well now that you are hereheres the plan\x07Have you ever noticed that giant pumpkin in the middle of the town?\x07We call it the Grandfather Pumpkin because its as old as toon island its self\x07It dates back to when all the lands split apart due to a massive earthquake.\x07It truly is an mystical ancient phenomenon.\x07Well that is your first target its been taken over by the cogs.\x07You must relight it because its power will greatly help us in this fight against Gibby but its not gonna be that easy\x07It is heavily guarded by the strongest of cogs in Withering Woods\x07You will have to Gather a group of toons and clear it out then once you do you must relight it as its bright lights will protect us from Gibby and her Dark Lords dark magic\x07To gain access to the grandfather pumpkin you will need to recover a key to the grandfather pumpkin from the cogs"},
 2225: {QUEST: "Aw man this isnt the correct\x07You will have to recover the key from a specific cog\x07but since we have no idea which cog took it\x07we will need to find evidence on it\x07Im sure if you fight more of the cogs you can find a note that details the cogs plans to steal the key"},
 2226: {QUEST: "Yes ive put the evidence together and it seems that the real key is held by a Loan Shark\x07Defeat Loan Sharks pronto to recover that key!"},
 2227: {QUEST: "Great you recovered the real key.\x07Since its too dangerous for you to go\x07and partly because Toon Island does not have many developers\x07Im going to try to take down Gibby\x07Thank you so much toon\x07But if you could clear out some of these cog buildings, that would be a big help\x07Thank you so much.",
        COMPLETE: "You did it!\x07While you were gone I defeated Gibby and her evil magic.\x07Thank you so much for making Withering Woods not so Withering\x07How could i ever thank you.\x07Oh the gags right."},
 
 # ==========================w
 #       Rainbow Rise
 # ==========================

 # Task 1: Meeting The Captain
 # Reward: Gag Training
 3001: {QUEST: "How's it going, _avName_?\x07We heard great things about your efforts in Toon Island Central and Withering Woods.\x07Rainbow Rise could really use a toon like you.\x07Speak to Pegleg Peg at Peg's Pegged Peg Legs._where_"},
 3002: {QUEST: "Yar Matey, welcome to Rainbow Rise!\x07Ye be the one I've been hearing good things about.\x07Well, allow me to introduce myself.\x07My name is Pegleg Peg, and I am the captain of the largest ship across the seven seas\x07The Red Cloud!\x07Ye see, me and my crew were the most feared pirates across the seven seas till them darn cogs started their own crew\x07Tthey have been taking all our treasures.\x07This is where you will come in handy.\x07Yer gunna unite Rainbow Rise, and together we will be able to take down them Cogs. Well,\x07I assume ya ain't gonna work for free, so every task you complete here will be heavily rewarded.\x07And speaking of tasks, I got one for ya right now.\x07If we gonna be taking the fight to dem cogs, we are gonna need some fire powa, and I know just where we can get it from.\x07Them Corporate Raiders usually carry cannonballs on them.\x07We will need a bunch of them if we hope to take out the cogs.\x07Recover 5 cannonballs from Corporate Raiders."},
 3003: {GREETING: '',
       QUEST: "Great job, matey! You won't have to walk the plank after all.\x07You have earned your reward.\x07You may now choose to train for Toon-up or Trap.",
       INCOMPLETE_PROGRESS: 'Think about your decision before choosing.',
       INCOMPLETE_WRONG_NPC: 'Think about your decision before choosing.',
       COMPLETE: 'Eh? Thats a great choice',
       LEAVING: 'See you around Rainbow Rise matey!'},
 3004: {GREETING: '',
       QUEST: "Great job, matey! You won't have to walk the plank after all.\x07You have earned your reward.\x07You may now choose to train for Sound or Trap.",
       INCOMPLETE_PROGRESS: 'Think about your decision before choosing.',
       INCOMPLETE_WRONG_NPC: 'Think about your decision before choosing.',
       COMPLETE: 'Eh? Thats a great choice',
       LEAVING: 'See you around Rainbow Rise matey!'},

  # Task 2: Freaks in Control
  # Reward: +3 Laff Boost
  3161: {QUEST: "Report to Howard Horse at The Family Friendly Stern.\x07He is having problems with cogs hacking into his television channel\x07spreading non-toony propaganda._where_"},
  3162: {QUEST: "Hello, _avName_!\x07Good thing you made it.\x07How am I supposed to make a profit off my television channel with the cogs hacking into it\x07spreading non-toony propaganda?\x07If you can help me out, I'll reward you well.\x07I bet if you take down three 3-story Bossbot buildings, it will prevent the cogs from hacking into my channel."},
  3163: {QUEST: "That didn't seem to work.\x07Maybe if we try a 4-story Bossbot building, it will stop this nonsense."},
  3164: {QUEST: "Hmm, that didn't work either. While you were gone, I've come up with the solution.\x07We need to take out the head honcho of this operation.\x07You need to defeat a Big Cheese to stop this madness.\x07That should work.", # Swap to Control Freak when Cog Update is done.
         COMPLETE: "Purrfecto!\x07You did it!\x07Well, I am going to be a man of my word.\x07Here is a +3 Laff Boost. Remember, _avName_, keep it family-friendly."}, 

  # Task 3: You Cant Sea Me
  # Reward: +4 Laff Boost + Invisible Toon Cheesy Effect
  3165: {QUEST: "Jonathan Sea-No has sprayed himself with invisibility spray and is stuck invisible.\x07He needs your help to become visible again.\x07I'm sure he will reward you if you help him._where_"},
  3166: {QUEST: "It's a disaster, _avName_!\x07I sprayed myself with this invisibility spray because I wanted to scare my friend as a prank, but now I'm stuck like this.\x07It seems the cogs switched my temporary spray out with a permanent one, and now I'm stuck.\x07There has to be a way to reverse this.\x07I got an idea, go see my friend Baron Corbear at Rain-Below 5$ Or Less.\x07I'm sure he has a product that can help reverse this._where_"},
  3167: {QUEST: "Welcome _avName!\x07So Jonathan sent you.\x07Very well, you need a product that will help him reverse his invisibility.\x07Well, you came to the right place.\x07I have some Anti-Invisibility Shampoo, but they are currently out of stock.\x07They won't be in stock for another couple of days.\x07If you go defeat some cogs, that should kill some time."},
  3168: {QUEST: "Good job on defeating those cogs.\x07The shampoo came back in stock, but some Big Wigs came by and stole all the shampoo.\x07I guess that's how they keep their hair so perfect\x07but that's beside the point.\x07Before I give you any\x07I need you to recover all of the shampoo that they stole."},
  3169: {QUEST: "Great, you did it!\x07I knew I could trust you. Here, keep some Anti-Invisibility Shampoo.\x07It should work.\x07Take this to, Jonathan Sea-No._where_"},
  3170: {QUEST: "Thanks! It took you long enough, though.\x07Well, while I'm taking a shower, why don't you go recover my real invisibility spray so no one has to suffer this fate again?\x07You can find them on any cogs in Rainbow Rise.",
         COMPLETE: "It worked! Wow, you did me a good deed here today, _avName_! You deserve a reward."}, # add this in later -> and also an Invisibility Spray. The invisibility spray will allow you to be an invisible toon whenever you want. You can switch out your cheesy effects by opening your sticker book."}, 

  # Task 4: A Grassy Accident
  # Reward: +4 Laff Boost + Invisible Toon Cheesy Effect
  3171: {QUEST: "Report to Reef Blowers Lawn Care and speak to Bob Square.\x07He needs your help._where_"},
  3172: {QUEST: "Oh no, please no!\x07Are you a lawyer?\x07Did Nayla send you?!\x07Okay, you are not.\x07Well, can you help me?\x07You see, me and my employees run a lawn service here.\x07We cut all the toons around here's grass, and we made a mistake.\x07We accidentally cut the wrong yard\x07Nayla's yard—and now they are mad at us.\x07Can you try to talk to her and calm her down so they won't pursue legal action?_where_"},
  3173: {QUEST: "What do you want?\x07I'm not in the best of moods right now.\x07Some mediocre lawn service I didn't hire cut my grass accidentally, and now it looks bad.\x07You want me to forget about what happened?\x07Are you kidding me?\x07Go back and tell Bob Square the only way I'll forgive him is if he pays me in beans._where_"},
  3174: {QUEST: "Well, this is bad.\x07I have very few jellybeans to pay Cranky.\x07\x07I'll give you 50 jellybeans to pay Cranky back\x07because that's how much cutting the yard would have cost._where_"},
  3175: {QUEST: "50 Jellybeans?!\x07That's all he can give?\x07Is this a joke?\x07I'll tell you what, if you help me out with something,\x07I'll forgive him.\x07But you must help me out first.\x07Some cogs keep breaking into my shop and waking me up while I'm trying to sleep.\x07I haven't been able to sleep in a couple of days\x07and it's what's making me so cranky lately.\x07If you can defeat some of them, I'll forgive Bob Square."},
  3176: {QUEST: "Okay, that will be good enough.\x07Go talk to Bob Square\x07Tell him I will not be pursuing any legal actions against himand his crew._where_",
         COMPLETE: "You're a blessing in disguise.\x07Thanks a lot, _avName_!"},

  # Task 5: Swimming in the Ocean
  # Reward: Gag Pouch 50
  3177: {QUEST: "Nar Whal is having a seaside issue. Can you go SEA them _avName_._where_"},
  3178: {QUEST: "Narwhals\x07Narwhals\x07Swimming in trhe ocean causing a.....\x07oh\x07Im so sorry\x07Yeah my singing is TERRIBLE.\x07but hey you came from my singing\x07No?\x07Oh Toon HQ sent you\x07Right I might of underestimated my singing\x07Can you help me with a seaside issue.\x07You see\x07A Bunch of cogs came in here and stole all my FISHING EQUIPMENT!\x07If you help me recover it, ill reward you.\x07You can find my equipment on any cog here in Rainbow Rise (i think)"},
  3179: {QUEST: "Good job _avName\x07But i have one other teensy tiny problem\x07While you were gone, some big Two-Face came in and stole ALL MY BAIT!\x07If you can recover those, then I can help you out with a SICKER reward.\x07Get to it, lol.",
         COMPLETE: "You totally rock dudette.\x07Here have my backpack i use to store bait.\x07It could be very useful to store some gags.\x07Thank you for your help, _avName_."},


 # ==========================
 #       Cirrus Circus
 # ==========================

 # Task 1: Gag Training

 # ==========================
 #        Cirrus Circus
 # ==========================

 # Task 1: Sellbot Suit Explanation

 # ==========================
 #        Olive Oasis
 # ==========================

 # Task 1: Cashbot Suit Explanation

 # ==========================
 #          UNKNOWN
 # ==========================

 # Task 1: Lawbot Suit Explanation


 # ==========================
 #        Minty Mines
 # ==========================

 # Task 1: Bossbot Suit Explanation

}

ChatGarblerDog = ['woof', 'arf', 'rruff']
ChatGarblerCat = ['meow', 'mew', 'mau']
ChatGarblerMouse = ['squeak', 'squeaky', 'squeakity']
ChatGarblerHorse = ['neigh', 'brrr', 'whinny']
ChatGarblerRabbit = ['eek',
 'eepr',
 'eepy',
 'eeky']
ChatGarblerDuck = ['quack', 'quackity', 'quacky']
ChatGarblerMonkey = ['ooh', 'ooo', 'ahh']
ChatGarblerBear = ['growl', 'grrr', 'roar']
ChatGarblerPig = ['oink', 'oik', 'snort']
ChatGarblerDeer = ['meep', 'meepy', 'meepity']
ChatGarblerDefault = ['blah']
Bossbot = 'Bossbot'
Lawbot = 'Lawbot'
Cashbot = 'Cashbot'
Sellbot = 'Sellbot'
BossbotS = 'a Bossbot'
LawbotS = 'a Lawbot'
CashbotS = 'a Cashbot'
SellbotS = 'a Sellbot'
BossbotP = 'Bossbots'
LawbotP = 'Lawbots'
CashbotP = 'Cashbots'
SellbotP = 'Sellbots'
BossbotSkelS = 'a Bossbot Skelecog'
LawbotSkelS = 'a Lawbot Skelecog'
CashbotSkelS = 'a Cashbot Skelecog'
SellbotSkelS = 'a Sellbot Skelecog'
BossbotSkelP = 'Bossbot Skelecogs'
LawbotSkelP = 'Lawbot Skelecogs'
CashbotSkelP = 'Cashbot Skelecogs'
SellbotSkelP = 'Sellbot Skelecogs'
SkeleRevivePostFix = ' v2.0'
AvatarDetailPanelOK = lOK
AvatarDetailPanelCancel = lCancel
AvatarDetailPanelClose = lClose
AvatarDetailPanelLookup = 'Looking up details for %s.'
AvatarDetailPanelFailedLookup = 'Unable to get details for %s.'
AvatarDetailPanelPlayer = 'Player: %(player)s\nWorld: %(world)s'
AvatarDetailPanelPlayerShort = '%(player)s\nWorld: %(world)s\nLocation: %(location)s'
AvatarDetailPanelRealLife = 'Offline'
AvatarDetailPanelOnline = 'District: %(district)s\nLocation: %(location)s\nToonID: %(toonid)s'
AvatarDetailPanelOnlinePlayer = 'District: %(district)s\nLocation: %(location)s\nPlayer: %(player)s'
AvatarDetailPanelOffline = 'District: offline\nLocation: offline\nToon ID: %(toonid)s'
AvatarShowPlayer = 'Show Player'
OfflineLocation = 'Offline'
PlayerToonName = 'Toon: %(Toonname)s'
PlayerShowToon = 'Show Toon'
PlayerPanelDetail = 'Player Details'
AvatarPanelFriends = 'Friends'
AvatarPanelWhisper = 'Whisper'
AvatarPanelGoTo = 'Go To'
AvatarPanelPet = 'Show Doodle'
AvatarPanelIgnore = 'Ignore'
AvatarPanelIgnoreCant = 'Okay'
AvatarPanelStopIgnoring = 'Stop Ignoring'
AvatarPanelReport = 'Report'
AvatarPanelCogLevel = 'Level: %s'
AvatarPanelCogDetailClose = lClose
AvatarPanelDetail = 'Toon Details'
AvatarPanelGroupInvite = 'Invite'
AvatarPanelGroupRetract = 'Retract Invitation'
AvatarPanelGroupMember = 'Already In Group'
AvatarPanelGroupMemberKick = 'Remove'
ReportPanelTitle = 'Report A Player'
ReportPanelBody = 'This feature will send a complete report to a Moderator. Instead of sending a report, you might choose to do one of the following:\n\n  - Teleport to another district\n  - Use "Ignore" on the Toon\'s panel\n\nDo you really want to report %s to a Moderator?'
ReportPanelBodyFriends = 'This feature will send a complete report to a Moderator. Instead of sending a report, you might choose to do one of the following:\n\n  - Teleport to another district\n  - Break your friendship\n\nDo you really want to report %s to a Moderator?\n\n(This will also break your friendship)'
ReportPanelCategoryBody = 'You are about to report %s. A Moderator will be alerted to your complaint and will take appropriate action for anyone breaking our rules. Please choose the reason you are reporting %s:'
ReportPanelBodyPlayer = 'This feature is stilling being worked on and will be coming soon. In the meantime you can do the following:\n\n  - Go to DXD and break the friendship there.\n - Tell a parent about what happened.'
ReportPanelCategoryLanguage = 'Foul Language'
ReportPanelCategoryPii = 'Sharing/Requesting Personal Info'
ReportPanelCategoryRude = 'Rude or Mean Behavior'
ReportPanelCategoryName = 'Bad Name'
ReportPanelCategoryHacking = 'Hacking'
# Gracie's Notes: Add an option for "Other..." that allows you to type what you're reporting.
ReportPanelConfirmations = ('You are about to report that %s has used obscene, bigoted or sexually explicit language.',
 'You are about to report that %s is being unsafe by giving out or requesting a phone number, address, last name, email address, password or account name.',
 'You are about to report that %s is bullying, harassing, or using extreme behavior to disrupt the game.',
 "You are about to report that %s has created a name that does not follow this server's rules.",
 'You are about to report that %s has hacked/tampered with the game or used third party software.')
ReportPanelWarning = "We take reporting very seriously. Your report will be viewed by a Moderator who will take appropriate action for anyone breaking our rules. If your account is found to have participated in breaking the rules, or if you make false reports or abuse the 'Report a Player' system, a Moderator may take action against your account. Are you absolutely sure you want to report this player?"
ReportPanelThanks = 'Thank you! Your report has been sent to a Moderator for review. There is no need to contact us again about the issue. The moderation team will take appropriate action for a player found breaking our rules.'
ReportPanelRemovedFriend = 'We have automatically removed %s from your Toon Friends List.'
ReportPanelRemovedPlayerFriend = 'We have automatically removed %s as a Player friend so as such you will not see them as your friend in any linked products.' # …in any Digipulse-linked products :joey:
ReportPanelAlreadyReported = 'You have already reported %s during this session. A Moderator will review your previous report.'
IgnorePanelTitle = 'Ignore A Player'
IgnorePanelAddIgnore = 'Would you like to ignore %s for the rest of this session?'
IgnorePanelIgnore = 'You are now ignoring %s.'
IgnorePanelRemoveIgnore = 'Would you like to stop ignoring %s?'
IgnorePanelEndIgnore = 'You are no longer ignoring %s.'
IgnorePanelAddFriendAvatar = '%s is your friend, you cannot ignore them while you are friends.'
IgnorePanelAddFriendPlayer = '%s (%s)is your friend, you cannot ignore them while you are friends.'
PetPanelFeed = 'Feed'
PetPanelCall = 'Call'
PetPanelGoTo = 'Go To'
PetPanelOwner = 'Show Owner'
PetPanelDetail = 'Pet Details'
PetPanelScratch = 'Scratch'
PetDetailPanelTitle = 'Trick Training'
PetTrickStrings = {0: 'Jump',
 1: 'Beg',
 2: 'Play dead',
 3: 'Rollover',
 4: 'Backflip',
 5: 'Dance',
 6: 'Speak'}
PetMoodAdjectives = {'neutral': 'neutral',
 'hunger': 'hungry',
 'boredom': 'bored',
 'excitement': 'excited',
 'sadness': 'sad',
 'restlessness': 'restless',
 'playfulness': 'playful',
 'loneliness': 'lonely',
 'fatigue': 'tired',
 'confusion': 'confused',
 'anger': 'angry',
 'surprise': 'surprised',
 'affection': 'affectionate'}
SpokenMoods = {'neutral': 'neutral',
 'hunger': ["I'm tired of Jellybeans! How'bout giving me a slice of pie?", "How'bout a Red Jellybean? I'm tired of the Green ones!", "Oh, those Jellybeans were for planting?!! But I'm hungry!"],
 'boredom': ["I'm dying of boredom over here!", "You didn't think I understood you, huh?", 'Could we, like, DO something already?'],
 'excitement': ["Wow, it's you, it's you, it's you!",
                'mmm, Jellybeans, mmm!',
                'Does it GET any better than this?',
                "Happy April Toons' Week!"],
 'sadness': ["Don't go, Don't go, Don't go, Don't go, Don't go, Don't go, Don't go, Don't go, Don't go, Don't go, Don't go…", "I'll be good, I promise!", "I don't know WHY I'm sad, I just am!!!"],
 'restlessness': ["I'm sooo restless!!!"],
 'playfulness': ["Let's play, Let's play, Let's play, Let's play, Let's play, Let's play, Let's play, Let's play, Let's play…", 'Play with me or I dig up some flowers!', 'Lets run around and  around and around and around and around and around…'],
 'loneliness': ['Where have you been?', 'Wanna cuddle?', 'I want to go with you when you fight Cogs!'],
 'fatigue': ['That swim in the pond really tired me out!', 'Being a Doodle is exhausting!', 'I gotta get to Dreamland!'],
 'confusion': ['Where am I? Who are you again?', "What's a Toon-up again?", "Whoa, I'm standing between you and the Cogs! Run away!"],
 'anger': ['… and you wonder why I never give you a Toon-up?!!!', 'You always leave me behind!', 'You love your gags more than you love me!'],
 'surprise': ['Of course Doodles can talk!', 'Toons can talk?!!', 'Whoa, where did you come from?'],
 'affection': ["You're the best Toon EVER!!!!!!!!!!", 'Do you even KNOW how great you are?!?', 'I am SO lucky to be with you!!!']}
DialogQuestion = '?'
FriendsListLabel = 'Friends'
TeleportPanelOK = lOK
TeleportPanelCancel = lCancel
TeleportPanelYes = lYes
TeleportPanelNo = lNo
TeleportPanelCheckAvailability = 'Trying to go to %s.'
TeleportPanelNotAvailable = '%s is busy right now; try again later.'
TeleportPanelIgnored = '%s is ignoring you.'
TeleportPanelNotOnline = "%s isn't online right now."
TeleportPanelWentAway = '%s went away.'
TeleportPanelUnknownHood = "You don't know how to get to %s!"
TeleportPanelUnavailableHood = '%s is not available right now; try again later.'
TeleportPanelDenySelf = "You can't go to yourself!"
TeleportPanelOtherShard = "%(avName)s is in district %(shardName)s, and you're in district %(myShardName)s. Do you want to switch to %(shardName)s?"
TeleportPanelBusyShard = '%(avName)s is in a full District. Playing in a full District can severely slow down game performance. Are you sure you want to switch districts?'
BattleBldgBossTaunt = "I'm the boss."
CogdoBattleBldgBossTaunt = "I don't take meetings with Toons."
FactoryBossTaunt = "I'm the Foreman."
FactoryBossBattleTaunt = 'Let me introduce you to the Foreman.'
MintBossTaunt = "I'm the Supervisor."
MintBossBattleTaunt = 'You need to talk to the Supervisor.'
StageBossTaunt = "My Justice isn't Blind"
StageBossBattleTaunt = 'I am above the Law'
CountryClubBossTaunt = "I'm the Club President."
CountryClubBossBattleTaunt = 'You need to talk to the Club President.'
ForcedLeaveCountryClubAckMsg = 'The Club President was defeated before you could reach him. You did not recover any Stock Options.'
ToonHealJokes = [['What goes TICK-TICK-TICK-WOOF?', 'A watchdog! '],
 ['Why do male deer need braces?', "Because they have 'buck teeth'!"],
 ['Why is it hard for a ghost to tell a lie?', 'Because you can see right through him.'],
 ['What did the ballerina do when she hurt her foot?', 'She called the toe truck!'],
 ['What has one horn and gives milk?', 'A milk truck!'],
 ["Why don't witches ride their brooms when they're angry?", "They don't want to fly off the handle!"],
 ['Why did the dolphin cross the ocean?', 'To get to the other tide.'],
 ['What kind of mistakes do spooks make?', 'Boo boos.'],
 ['Why did the chicken cross the playground?', 'To get to the other slide!'],
 ['Where does a peacock go when he loses his tail?', 'A retail store.'],
 ["Why didn't the skeleton cross the road?", "He didn't have the guts."],
 ["Why wouldn't they let the butterfly into the dance?", 'Because it was a moth ball.'],
 ["What's gray and squirts jam at you?", 'A mouse eating a doughnut.'],
 ['What happened when 500 hares got loose on the main street?', 'The police had to comb the area.'],
 ["What's the difference between a fish and a piano?", "You can tune a piano, but you can't tuna fish!"],
 ['What do people do in clock factories?', 'They make faces all day.'],
 ['What do you call a blind dinosaur?', "An I-don't-think-he-saurus."],
 ['If you drop a white hat into the Red Sea, what does it become?', 'Wet.'],
 ['Why was Cinderella thrown off the basketball team?', 'She ran away from the ball.'],
 ['Why was Cinderella such a bad player?', 'She had a pumpkin for a coach.'],
 ["What two things can't you have for breakfast?", 'Lunch and dinner.'],
 ['What do you give an elephant with big feet?', 'Big shoes.'],
 ['Where do baby ghosts go during the day?', 'Day-scare centers.'],
 ['What did Snow White say to the photographer?', 'Some day my prints will come.'],
 ["What's Tarzan's favorite song?", 'Jungle bells.'],
 ["What's green and loud?", 'A froghorn.'],
 ["What's worse than raining cats and dogs?", 'Hailing taxis.'],
 ['When is the vet busiest?', "When it's raining cats and dogs."],
 ['What do you call a gorilla wearing ear-muffs?', "Anything you want, he can't hear you."],
 ['Where would you weigh a whale?', 'At a whale-weigh station.'],
 ['What travels around the world but stays in the corner?', 'A stamp.'],
 ['What do you give a pig with a sore throat?', 'Oinkment.'],
 ['What did the hat say to the scarf?', 'You hang around while I go on a head.'],
 ["What's the best parting gift?", 'A comb.'],
 ['What kind of cats like to go bowling?', 'Alley cats.'],
 ["What's wrong if you keep seeing talking animals?", "You're having Disney spells."],
 ['What did one eye say to the other?', 'Between you and me, something smells.'],
 ["What's round, white and giggles?", 'A tickled onion.'],
 ['What do you get when you cross Bambi with a ghost?', 'Bamboo.'],
 ['Why do golfers take an extra pair of socks?', 'In case they get a hole in one.'],
 ['What do you call a fly with no wings?', 'A walk.'],
 ['Who did Frankenstein take to the prom?', 'His ghoul friend.'],
 ['What lies on its back, one hundred feet in the air?', 'A sleeping centipede.'],
 ['How do you keep a bull from charging?', 'Take away his credit card.'],
 ['What do you call a chicken at the North Pole?', 'Lost.'],
 ['What do you get if you cross a cat with a dog?', 'An animal that chases itself.'],
 ['What did the digital watch say to the grandfather clock?', 'Look dad, no hands.'],
 ['Where does Ariel the mermaid go to see movies?', 'The dive-in.'],
 ['What do you call a mosquito with a tin suit?', 'A bite in shining armor.'],
 ['What do giraffes have that no other animal has?', 'Baby giraffes.'],
 ['Why did the man hit the clock?', 'Because the clock struck first.'],
 ['Why did the apple go out with a fig?', "Because it couldn't find a date."],
 ['What do you get when you cross a parrot with a monster?', 'A creature that gets a cracker whenever it asks for one.'],
 ["Why didn't the monster make the football team?", 'Because he threw like a ghoul!'],
 ['What do you get if you cross a Cocker Spaniel with a Poodle and a rooster?', 'A cockapoodledoo!'],
 ['What goes dot-dot-dash-dash-squeak?', 'Mouse code.'],
 ["Why aren't elephants allowed on beaches?", "They can't keep their trunks up."],
 ['What is at the end of everything?', 'The letter G.'],
 ['How do trains hear?', 'Through the engineers.'],
 ['What does the winner of a marathon lose?', 'His breath.'],
 ['Why did the pelican refuse to pay for his meal?', 'His bill was too big.'],
 ['What has six eyes but cannot see?', 'Three blind mice.'],
 ["What works only when it's fired?", 'A rocket.'],
 ["Why wasn't there any food left after the monster party?", 'Because everyone was a goblin!'],
 ['What bird can be heard at mealtimes?', 'A swallow.'],
 ['What goes Oh, Oh, Oh?', 'Santa walking backwards.'],
 ['What has green hair and runs through the forest?', 'Moldy locks.'],
 ['Where do ghosts pick up their mail?', 'At the ghost office.'],
 ['Why do dinosaurs have long necks?', 'Because their feet smell.'],
 ['What do mermaids have on toast?', 'Mermarlade.'],
 ['Why do elephants never forget?', 'Because nobody ever tells them anything.'],
 ["What's in the middle of a jellyfish?", 'A jellybutton.'],
 ['What do you call a very popular perfume?', 'A best-smeller.'],
 ["Why can't you play jokes on snakes?", 'Because you can never pull their legs.'],
 ['Why did the baker stop making donuts?', 'He got sick of the hole business.'],
 ['Why do mummies make excellent spies?', "They're good at keeping things under wraps."],
 ['How do you stop an elephant from going through the eye of a needle?', 'Tie a knot in its tail.'],
 ["What goes 'Ha Ha Ha Thud'?", 'Someone laughing his head off.'],
 ["My friend thinks he's a rubber band.", 'I told him to snap out of it.'],
 ["My sister thinks she's a pair of curtains.", 'I told her to pull herself together!'],
 ['Did you hear about the dentist that married the manicurist?', 'Within a month they were fighting tooth and nail.'],
 ['Why do hummingbirds hum?', "Because they don't know the words."],
 ['Why did the baby turkey bolt down his food?', 'Because he was a little gobbler.'],
 ['Where did the whale go when it was bankrupt?', 'To the loan shark.'],
 ['How does a sick sheep feel?', 'Baah-aahd.'],
 ["What's gray, weighs 10 pounds and squeaks?", 'A mouse that needs to go on a diet.'],
 ['Why did the dog chase his tail?', 'To make ends meet.'],
 ['Why do elephants wear running shoes?', 'For jogging of course.'],
 ['Why are elephants big and gray?', "Because if they were small and yellow they'd be canaries."],
 ['If athletes get tennis elbow what do astronauts get?', 'Missile toe.'],
 ['Did you hear about the man who hated Santa?', 'He suffered from Claustrophobia.'],
 ['Why did ' + Donald + ' sprinkle sugar on his pillow?', 'Because he wanted to have sweet dreams.'],
 ['Why did ' + Goofy + ' take his comb to the dentist?', 'Because it had lost all its teeth.'],
 ['Why did ' + Goofy + ' wear his shirt in the bath?', 'Because the label said wash and wear.'],
 ['Why did the dirty chicken cross the road?', 'For some fowl purpose.'],
 ["Why didn't the skeleton go to the party?", 'He had no body to go with.'],
 ['Why did the burglar take a shower?', 'To make a clean getaway.'],
 ['Why does a sheep have a woolly coat?', "Because he'd look silly in a plastic one."],
 ['Why do potatoes argue all the time?', "They can't see eye to eye."],
 ['Why did ' + Pluto + ' sleep with a banana peel?', 'So he could slip out of bed in the morning.'],
 ['Why did the mouse wear brown sneakers?', 'His white ones were in the wash.'],
 ['Why are false teeth like stars?', 'They come out at night.'],
 ['Why are Saturday and Sunday so strong?', 'Because the others are weekdays.'],
 ['Why did the archaeologist go bankrupt?', 'Because his career was in ruins.'],
 ['What do you get if you cross the Atlantic on the Titanic?', 'Very wet.'],
 ['What do you get if you cross a chicken with cement?', 'A brick-layer.'],
 ['What do you get if you cross a dog with a phone?', 'A golden receiver.'],
 ['What do you get if you cross an elephant with a shark?', 'Swimming trunks with sharp teeth.'],
 ['What did the tablecloth say to the table?', "Don't move, I've got you covered."],
 ['Did you hear about the time ' + Goofy + ' ate a candle?', 'He wanted a light snack.'],
 ['What did the balloon say to the pin?', 'Hi Buster.'],
 ['What did the big chimney say to the little chimney?', "You're too young to smoke."],
 ['What did the carpet say to the floor?', 'I got you covered.'],
 ['What did the necklace say to the hat?', "You go ahead, I'll hang around."],
 ['What goes zzub-zzub?', 'A bee flying backwards.'],
 ['How do you communicate with a fish?', 'Drop him a line.'],
 ["What do you call a dinosaur that's never late?", 'A prontosaurus.'],
 ['What do you get if you cross a bear and a skunk?', 'Winnie-the-phew.'],
 ['How do you clean a tuba?', 'With a tuba toothpaste.'],
 ['What do frogs like to sit on?', 'Toadstools.'],
 ['Why was the math book unhappy?', 'It had too many problems.'],
 ['Why was the school clock punished?', 'It tocked too much.'],
 ["What's a polygon?", 'A dead parrot.'],
 ['What needs a bath and keeps crossing the street?', 'A dirty double crosser.'],
 ['What do you get if you cross a camera with a crocodile?', 'A snap shot.'],
 ['What do you get if you cross an elephant with a canary?', 'A very messy cage.'],
 ['What do you get if you cross a jeweler with a plumber?', 'A ring around the bathtub.'],
 ['What do you get if you cross an elephant with a crow?', 'Lots of broken telephone poles.'],
 ['What do you get if you cross a plum with a tiger?', 'A purple people eater.'],
 ["What's the best way to save water?", 'Dilute it.'],
 ["What's a lazy shoe called?", 'A loafer.'],
 ["What's green, noisy and dangerous?", 'A thundering herd of cucumbers.'],
 ['What color is a shout?', 'Yellow!'],
 ['What do you call a sick duck?', 'A mallardy.'],
 ["What's worse then a giraffe with a sore throat?", "A centipede with athlete's foot."],
 ['What goes ABC…slurp…DEF…slurp?', 'Someone eating alphabet soup.'],
 ["What's green and jumps up and down?", 'Lettuce at a dance.'],
 ["What's a cow after she gives birth?", 'De-calf-inated.'],
 ['What do you get if you cross a cow and a camel?', 'Lumpy milk shakes.'],
 ["What's white with black and red spots?", 'A Dalmatian with measles.'],
 ["What's brown has four legs and a trunk?", 'A mouse coming back from vacation.'],
 ["What does a skunk do when it's angry?", 'It raises a stink.'],
 ["What's gray, weighs 200 pounds and says, Here Kitty, kitty?", 'A 200 pound mouse.'],
 ["What's the best way to catch a squirrel?", 'Climb a tree and act like a nut.'],
 ["What's the best way to catch a rabbit?", 'Hide in a bush and make a noise like lettuce.'],
 ['What do you call a spider that just got married?', 'A newly web.'],
 ['What do you call a duck that robs banks?', 'A safe quacker.'],
 ["What's furry, meows and chases mice underwater?", 'A catfish.'],
 ["What's a funny egg called?", 'A practical yolker.'],
 ["What's green on the outside and yellow inside?", 'A banana disguised as a cucumber.'],
 ['What did the elephant say to the lemon?', "Let's play squash."],
 ['What weighs 4 tons, has a trunk and is bright red?', 'An embarrassed elephant.'],
 ["What's gray, weighs 4 tons, and wears glass slippers?", 'Cinderelephant.'],
 ["What's an elephant in a fridge called?", 'A very tight squeeze.'],
 ['What did the elephant say to her naughty child?', 'Tusk! Tusk!'],
 ['What did the peanut say to the elephant?', "Nothing -- Peanuts can't talk."],
 ['What do elephants say when they bump into each other?', "Small world, isn't it?"],
 ['What did the cashier say to the register?', "I'm counting on you."],
 ['What did the flea say to the other flea?', 'Shall we walk or take the cat?'],
 ['What did the big hand say to the little hand?', 'Got a minute.'],
 ['What does the sea say to the sand?', 'Not much. It usually waves.'],
 ['What did the stocking say to the shoe?', 'See you later, I gotta run.'],
 ['What did one tonsil say to the other tonsil?', 'It must be spring, here comes a swallow.'],
 ['What did the soil say to the rain?', 'Stop, or my name is mud.'],
 ['What did the puddle say to the rain?', 'Drop in sometime.'],
 ['What did the bee say to the rose?', 'Hi, bud.'],
 ['What did the appendix say to the kidney?', "The doctor's taking me out tonight."],
 ['What did the window say to the venetian blinds?', "If it wasn't for you it'd be curtains for me."],
 ['What did the doctor say to the sick orange?', 'Are you peeling well?'],
 ['What do you get if you cross a chicken with a banjo?', 'A self-plucking chicken.'],
 ['What do you get if you cross a hyena with a bouillon cube?', 'An animal that makes a laughing stock of itself.'],
 ['What do you get if you cross a rabbit with a spider?', 'A hare net.'],
 ['What do you get if you cross a germ with a comedian?', 'Sick jokes.'],
 ['What do you get if you cross a hyena with a mynah bird?', 'An animal that laughs at its own jokes.'],
 ['What do you get if you cross a railway engine with a stick of gum?', 'A chew-chew train.'],
 ['What would you get if you crossed an elephant with a computer?', 'A big know-it-all.'],
 ['What would you get if you crossed an elephant with a skunk?', 'A big stinker.'],
 ['Why did ' + MickeyMouse + ' take a trip to outer space?', 'He wanted to find ' + Pluto + '.']]
MovieHealLaughterMisses = ('hmm',
 'heh',
 'ha',
 'harr harr')
MovieHealLaughterHits1 = ('Ha Ha Ha',
 'Hee Hee',
 'Tee Hee',
 'Ha Ha')
MovieHealLaughterHits2 = ('BWAH HAH HAH!', 'HO HO HO!', 'HA HA HA!')
MovieSOSCallHelp = '%s HELP!'
MovieSOSWhisperHelp = '%s needs help in battle!'
MovieSOSObserverHelp = 'HELP!'
MovieNPCSOSGreeting = 'Hi %s! Glad to help!'
MovieNPCSOSGoodbye = 'See you later!'
MovieNPCSOSToonsHit = 'Toons Always Hit!'
MovieNPCSOSCogsMiss = 'Cogs Always Miss!'
MovieNPCSOSRestockGags = 'Restocking %s gags!'
MovieNPCSOSHeal = 'Toon-Up'
MovieNPCSOSTrap = 'Trap'
MovieNPCSOSLure = 'Lure'
MovieNPCSOSSound = 'Sound'
MovieNPCSOSThrow = 'Throw'
MovieNPCSOSSquirt = 'Squirt'
MovieNPCSOSDrop = 'Drop'
MovieNPCSOSAll = 'All'
MoviePetSOSTrickFail = 'Sigh'
MoviePetSOSTrickSucceedBoy = 'Good boy!'
MoviePetSOSTrickSucceedGirl = 'Good girl!'
MovieSuitCancelled = 'CANCELLED\nCANCELLED\nCANCELLED'
RewardPanelToonTasks = 'ToonTasks'
RewardPanelItems = 'Items Recovered'
RewardPanelMissedItems = 'Items Not Recovered'
RewardPanelQuestLabel = 'Quest %s'
RewardPanelCongratsStrings = ['Yeah!',
 'Congratulations!',
 'Wow!',
 'Cool!',
 'Awesome!',
 'Toon-tastic!']
RewardPanelNewGag = 'New %(gagName)s gag for %(avName)s!'
RewardPanelUberGag = '%(avName)s earned the %(gagName)s gag with %(exp)s experience points!'
RewardPanelEndTrack = 'Yay! %(avName)s has reached the end of the %(gagName)s Gag Track!'
RewardPanelMeritsMaxed = 'Maxed'
RewardPanelMeritBarLabels = ['Stock Options',
 'Jury Notices',
 'Cogbucks',
 'Merits']
RewardPanelMeritAlert = 'Ready for promotion!'
RewardPanelCogPart = 'You gained a Cog disguise part!'
RewardPanelPromotion = 'Ready for promotion in %s  track!'
RewardPanelSkip = 'Skip'
CheesyEffectDescriptions = [('Normal Toon', 'you will be normal'),
 ('Big head', 'you will have a big head'),
 ('Small head', 'you will have a small head'),
 ('Big legs', 'you will have big legs'),
 ('Small legs', 'you will have small legs'),
 ('Big Toon', 'you will be a little bigger'),
 ('Small Toon', 'you will be a little smaller'),
 ('Flat portrait', 'you will be two-dimensional'),
 ('Flat profile', 'you will be two-dimensional'),
 ('Transparent', 'you will be transparent'),
 ('No color', 'you will be colorless'),
 ('Invisible Toon', 'you will be invisible')]
CheesyEffectIndefinite = 'Until you choose another effect, %(effectName)s%(whileIn)s.'
CheesyEffectMinutes = 'For the next %(time)s minutes, %(effectName)s%(whileIn)s.'
CheesyEffectHours = 'For the next %(time)s hours, %(effectName)s%(whileIn)s.'
CheesyEffectDays = 'For the next %(time)s days, %(effectName)s%(whileIn)s.'
CheesyEffectWhileYouAreIn = ' while you are in %s'
CheesyEffectExceptIn = ', except in %s'
SuitFlunky = 'Flunky'
SuitPencilPusher = 'Pencil Pusher'
SuitYesman = 'Yesman'
SuitMicromanager = 'Micro\x03manager'
SuitDownsizer = 'Downsizer'
SuitHeadHunter = 'Head Hunter'
SuitCorporateRaider = 'Corporate Raider'
SuitTheBigCheese = 'The Big Cheese'
SuitColdCaller = 'Cold Caller'
SuitTelemarketer = 'Tele\x03marketer'
SuitNameDropper = 'Name Dropper'
SuitGladHander = 'Glad Hander'
SuitMoverShaker = 'Mover & Shaker'
SuitTwoFace = 'Two-Face'
SuitTheMingler = 'The Mingler'
SuitMrHollywood = 'Mr. Hollywood'
SuitShortChange = 'Short Change'
SuitPennyPincher = 'Penny Pincher'
SuitTightwad = 'Tightwad'
SuitBeanCounter = 'Bean Counter'
SuitNumberCruncher = 'Number Cruncher'
SuitMoneyBags = 'Money Bags'
SuitLoanShark = 'Loan Shark'
SuitRobberBaron = 'Robber Baron'
SuitBottomFeeder = 'Bottom Feeder'
SuitBloodsucker = 'Blood\x03sucker'
SuitDoubleTalker = 'Double Talker'
SuitAmbulanceChaser = 'Ambulance Chaser'
SuitBackStabber = 'Back Stabber'
SuitSpinDoctor = 'Spin Doctor'
SuitLegalEagle = 'Legal Eagle'
SuitBigWig = 'Big Wig'
SuitFlunkyS = 'a Flunky'
SuitPencilPusherS = 'a Pencil Pusher'
SuitYesmanS = 'a Yesman'
SuitMicromanagerS = 'a Micromanager'
SuitDownsizerS = 'a Downsizer'
SuitHeadHunterS = 'a Head Hunter'
SuitCorporateRaiderS = 'a Corporate Raider'
SuitTheBigCheeseS = 'a The Big Cheese'
SuitColdCallerS = 'a Cold Caller'
SuitTelemarketerS = 'a Telemarketer'
SuitNameDropperS = 'a Name Dropper'
SuitGladHanderS = 'a Glad Hander'
SuitMoverShakerS = 'a Mover & Shaker'
SuitTwoFaceS = 'a Two-Face'
SuitTheMinglerS = 'a The Mingler'
SuitMrHollywoodS = 'a Mr. Hollywood'
SuitShortChangeS = 'a Short Change'
SuitPennyPincherS = 'a Penny Pincher'
SuitTightwadS = 'a Tightwad'
SuitBeanCounterS = 'a Bean Counter'
SuitNumberCruncherS = 'a Number Cruncher'
SuitMoneyBagsS = 'a Money Bags'
SuitLoanSharkS = 'a Loan Shark'
SuitRobberBaronS = 'a Robber Baron'
SuitBottomFeederS = 'a Bottom Feeder'
SuitBloodsuckerS = 'a Bloodsucker'
SuitDoubleTalkerS = 'a Double Talker'
SuitAmbulanceChaserS = 'an Ambulance Chaser'
SuitBackStabberS = 'a Back Stabber'
SuitSpinDoctorS = 'a Spin Doctor'
SuitLegalEagleS = 'a Legal Eagle'
SuitBigWigS = 'a Big Wig'
SuitFlunkyP = 'Flunkies'
SuitPencilPusherP = 'Pencil Pushers'
SuitYesmanP = 'Yesmen'
SuitMicromanagerP = 'Micromanagers'
SuitDownsizerP = 'Downsizers'
SuitHeadHunterP = 'Head Hunters'
SuitCorporateRaiderP = 'Corporate Raiders'
SuitTheBigCheeseP = 'The Big Cheeses'
SuitColdCallerP = 'Cold Callers'
SuitTelemarketerP = 'Telemarketers'
SuitNameDropperP = 'Name Droppers'
SuitGladHanderP = 'Glad Handers'
SuitMoverShakerP = 'Movers & Shakers'
SuitTwoFaceP = 'Two-Faces'
SuitTheMinglerP = 'The Minglers'
SuitMrHollywoodP = 'Mr. Hollywoods'
SuitShortChangeP = 'Short Changes'
SuitPennyPincherP = 'Penny Pinchers'
SuitTightwadP = 'Tightwads'
SuitBeanCounterP = 'Bean Counters'
SuitNumberCruncherP = 'Number Crunchers'
SuitMoneyBagsP = 'Money Bags'
SuitLoanSharkP = 'Loan Sharks'
SuitRobberBaronP = 'Robber Barons'
SuitBottomFeederP = 'Bottom Feeders'
SuitBloodsuckerP = 'Bloodsuckers'
SuitDoubleTalkerP = 'Double Talkers'
SuitAmbulanceChaserP = 'Ambulance Chasers'
SuitBackStabberP = 'Back Stabbers'
SuitSpinDoctorP = 'Spin Doctors'
SuitLegalEagleP = 'Legal Eagles'
SuitBigWigP = 'Big Wigs'
SuitFaceoffDefaultTaunts = ['Boo!']
SuitAttackDefaultTaunts = ['Take that!', 'Take a memo on this!']
SuitAttackNames = {'Audit': 'Audit!',
 'Bite': 'Bite!',
 'BounceCheck': 'Bounce Check!',
 'BrainStorm': 'Brain Storm!',
 'BuzzWord': 'Buzz Word!',
 'Calculate': 'Calculate!',
 'Canned': 'Canned!',
 'Chomp': 'Chomp!',
 'CigarSmoke': 'Cigar Smoke!',
 'ClipOnTie': 'Clip On Tie!',
 'Crunch': 'Crunch!',
 'Demotion': 'Demotion!',
 'Downsize': 'Downsize!',
 'DoubleTalk': 'Double Talk!',
 'EvictionNotice': 'Eviction Notice!',
 'EvilEye': 'Evil Eye!',
 'Filibuster': 'Filibuster!',
 'FillWithLead': 'Fill With Lead!',
 'FiveOClockShadow': "Five O'Clock Shadow!",
 'FingerWag': 'Finger Wag!',
 'Fired': 'Fired!',
 'FloodTheMarket': 'Flood The Market!',
 'FountainPen': 'Fountain Pen!',
 'FreezeAssets': 'Freeze Assets!',
 'Gavel': 'Gavel!',
 'GlowerPower': 'Glower Power!',
 'GuiltTrip': 'Guilt Trip!',
 'HalfWindsor': 'Half Windsor!',
 'HangUp': 'Hang Up!',
 'HeadShrink': 'Head Shrink!',
 'HotAir': 'Hot Air!',
 'Jargon': 'Jargon!',
 'Legalese': 'Legalese!',
 'Liquidate': 'Liquidate!',
 'MarketCrash': 'Market Crash!',
 'MumboJumbo': 'Mumbo Jumbo!',
 'ParadigmShift': 'Paradigm Shift!',
 'PeckingOrder': 'Pecking Order!',
 'PickPocket': 'Pick Pocket!',
 'PinkSlip': 'Pink Slip!',
 'PlayHardball': 'Play Hardball!',
 'PoundKey': 'Pound Key!',
 'PowerTie': 'Power Tie!',
 'PowerTrip': 'Power Trip!',
 'Quake': 'Quake!',
 'RazzleDazzle': 'Razzle Dazzle!',
 'RedTape': 'Red Tape!',
 'ReOrg': 'Re-Org!',
 'RestrainingOrder': 'Restraining Order!',
 'Rolodex': 'Rolodex!',
 'RubberStamp': 'Rubber Stamp!',
 'RubOut': 'Rub Out!',
 'Sacked': 'Sacked!',
 'SandTrap': 'Sand Trap!',
 'Schmooze': 'Schmooze!',
 'Shake': 'Shake!',
 'Shred': 'Shred!',
 'SongAndDance': 'Song And Dance!',
 'Spin': 'Spin!',
 'Synergy': 'Synergy!',
 'Tabulate': 'Tabulate!',
 'TeeOff': 'Tee Off!',
 'ThrowBook': 'Throw Book!',
 'Tremor': 'Tremor!',
 'Watercooler': 'Watercooler!',
 'Withdrawal': 'Withdrawal!',
 'WriteOff': 'Write Off!'}
SuitAttackTaunts = {'Audit': ["I believe your books don't balance.",
           "Looks like you're in the red.",
           'Let me help you with your books.',
           'Your debit column is much too high.',
           "Let's check your assets.",
           'This will put you in debt.',
           "Let's take a close look at what you owe.",
           'This should drain your account.',
           'Time for you to account for your expenses.',
           "I've found an error in your books."],
 'Bite': ['Would you like a bite?',
          'Try a bite of this!',
          "You're biting off more than you can chew.",
          'My bite is bigger than my bark.',
          'Bite down on this!',
          'Watch out, I may bite.',
          "I don't just bite when I'm cornered.",
          "I'm just gonna grab a quick bite.",
          "I haven't had a bite all day.",
          'I just want a bite. Is that too much to ask?'],
 'BounceCheck': ["Ah, too bad, you're funless.",
                 'You have a payment due.',
                 'I believe this check is yours.',
                 'You owed me for this.',
                 "I'm collecting on this debt.",
                 "This check isn't going to be tender.",
                 "You're going to be charged for this.",
                 'Check this out.',
                 'This is going to cost you.',
                 "I'd like to cash this in.",
                 "I'm just going to kick this back to you.",
                 'This is one sour note.',
                 "I'm deducting a service charge."],
 'BrainStorm': ['I forecast rain.',
                'Hope you packed your umbrella.',
                'I want to enlighten you.',
                'How about a few rain DROPS?',
                'Not so sunny now, are you Toon?',
                'Ready for a down pour?',
                "I'm going to take you by storm.",
                'I call this a lightning attack.',
                'I love to be a wet blanket.'],
 'BuzzWord': ['Pardon me if I drone on.',
              'Have you heard the latest?',
              'Can you catch on to this?',
              'See if you can hum this Toon.',
              'Let me put in a good word for you.',
              'I\'ll "B" perfectly clear.',
              'You should "B" more careful.',
              'See if you can dodge this swarm.',
              "Careful, you're about to get stung.",
              'Looks like you have a bad case of hives.'],
 'Calculate': ['These numbers do add up!',
               'Did you count on this?',
               "Add it up, you're going down.",
               'Let me help you add this up.',
               'Did you register all your expenses?',
               "According to my calculations, you won't be around much longer.",
               "Here's the grand total.",
               'Wow, your bill is adding up.',
               'Try fiddling with these numbers!',
               Cogs + ': 1 Toons: 0'],
 'Canned': ['Do you like it out of the can?',
            '"Can" you handle this?',
            "This one's fresh out of the can!",
            'Ever been attacked by canned goods before?',
            "I'd like to donate this canned good to you!",
            'Get ready to "Kick the can"!',
            'You think you "can", you think you "can".',
            "I'll throw you in the can!",
            "I'm making me a can o' Toon-a!",
            "You don't taste so good out of the can."],
 'Chomp': ['Take a look at these chompers!',
           'Chomp, chomp, chomp!',
           "Here's something to chomp on.",
           'Looking for something to chomp on?',
           "Why don't you chomp on this?",
           "I'm going to have you for dinner.",
           'I love to feed on Toons!'],
 'ClipOnTie': ['Better dress for our meeting.',
               "You can't go OUT without your tie.",
               'The best dressed ' + Cogs + ' wear them.',
               'Try this on for size.',
               'You should dress for success.',
               'No tie, no service.',
               'Do you need help putting this on?',
               'Nothing says powerful like a good tie.',
               "Let's see if this fits.",
               'This is going to choke you up.',
               "You'll want to dress up before you go OUT.",
               "I think I'll tie you up."],
 'Crunch': ["Looks like you're in a crunch.",
            "It's crunch time!",
            "I'll give you something to crunch on!",
            'Crunch on this!',
            'I pack quite a crunch.',
            'Which do you prefer, smooth or crunchy?',
            "I hope you're ready for crunch time.",
            "It sounds like you're getting crunched!",
            "I'll crunch you like a can."],
 'Demotion': ["You're moving down the corporate ladder.",
              "I'm sending you back to the Mail Room.",
              'Time to turn in your nameplate.',
              "You're going down, clown.",
              "Looks like you're stuck.",
              "You're going nowhere fast.",
              "You're in a dead end position.",
              "You won't be moving anytime soon.",
              "You're not going anywhere.",
              'This will go on your permanent record.'],
 'Downsize': ['Come on down!',
              'Do you know how to get down?',
              "Let's get down to business.",
              "What's wrong? You look down.",
              'Going down?',
              "What's goin' down? You!",
              'Why pick on people my own size?',
              "Why don't I size you up, or should I say, down?",
              'Would you like a smaller size for just a quarter more?',
              'Try this on for size!',
              'You can get this in a smaller size.',
              'This attack is one size fits all!'],
 'EvictionNotice': ["It's moving time.",
                    'Pack your bags, Toon.',
                    'Time to make some new living arrangements.',
                    'Consider yourself served.',
                    "You're behind on your lease.",
                    'This will be extremely unsettling.',
                    "You're about to be uprooted.",
                    "I'm going to send you packing.",
                    "You're out of place.",
                    'Prepare to be relocated.',
                    "You're in a hostel position."],
 'EvilEye': ["I'm giving you the evil eye.",
             'Could you eye-ball this for me?',
             "Wait. I've got something in my eye.",
             "I've got my eye on you!",
             'Could you keep an eye on this for me?',
             "I've got a real eye for evil.",
             "I'll poke you in the eye!",
             '"Eye" am as evil as they come!',
             "I'll put you in the eye of the storm!",
             "I'm rolling my eye at you."],
 'Filibuster': ["Shall I fill 'er up?",
                'This is going to take awhile.',
                'I could do this all day.',
                "I don't even need to take a breath.",
                'I keep going and going and going.',
                'I never get tired of this one.',
                'I can talk a blue streak.',
                'Mind if I bend your ear?',
                "I think I'll shoot the breeze.",
                'I can always get a word in edgewise.'],
 'FingerWag': ['I have told you a thousand times.',
               'Now see here Toon.',
               "Don't make me laugh.",
               "Don't make me come over there.",
               "I'm tired of repeating myself.",
               "I believe we've been over this.",
               'You have no respect for us ' + Cogs + '.',
               "I think it's time you pay attention.",
               'Blah, Blah, Blah, Blah, Blah.',
               "Don't make me stop this meeting.",
               'Am I going to have to separate you?',
               "We've been through this before."],
 'Fired': ['I hope you brought some marshmallows.',
           "It's going to get rather warm around here.",
           'This should take the chill out of the air.',
           "I hope you're cold blooded.",
           'Hot, hot and hotter.',
           'You better stop, drop, and roll!',
           "You're outta here.",
           'How does "well-done" sound?',
           'Can you say ouch?',
           'Hope you wore sunscreen.',
           'Do you feel a little toasty?',
           "You're going down in flames.",
           "You'll go out in a blaze.",
           "You're a flash in the pan.",
           'I think I have a bit of a flare about me.',
           "I just sparkle, don't I?",
           'Oh look, a crispy critter.',
           "You shouldn't run around half baked."],
 'FountainPen': ['This is going to leave a stain.',
                 "Let's ink this deal.",
                 'Be prepared for some permanent damage.',
                 "You're going to need a good dry cleaner.",
                 'You should change.',
                 'This fountain pen has such a nice font.',
                 "Here, I'll use my pen.",
                 'Can you read my writing?',
                 'I call this the plume of doom.',
                 "There's a blot on your performance.",
                 "Don't you hate when this happens?"],
 'FreezeAssets': ['Your assets are mine.',
                  'Do you feel a draft?',
                  "Hope you don't have plans.",
                  'This should keep you on ice.',
                  "There's a chill in the air.",
                  'Winter is coming early this year.',
                  'Are you feeling a little blue?',
                  'Let me crystallize my plan.',
                  "You're going to take this hard.",
                  'This should cause freezer burn.',
                  'I hope you like cold cuts.',
                  "I'm very cold blooded."],
 'GlowerPower': ['You looking at me?',
                 "I'm told I have very piercing eyes.",
                 'I like to stay on the cutting edge.',
                 "Jeepers, Creepers, don't you love my peepers?",
                 "Here's looking at you kid.",
                 "How's this for expressive eyes?",
                 'My eyes are my strongest feature.',
                 'The eyes have it.',
                 'Peeka-boo, I see you.',
                 'Look into my eyes…',
                 'Shall we take a peek at your future?'],
 'GuiltTrip': ["I'll lay a real guilt trip on you!",
               'Feeling guilty?',
               "It's all your fault!",
               'I always blame everything on you.',
               'Wallow in your own guilt!',
               "I'm never speaking to you again!",
               "You had better say you're sorry.",
               "I'm would forgive you in a million years!",
               'Are you ready for your trip?',
               'Call me when you get back from your trip.',
               'When do you get back from your trip?'],
 'HalfWindsor': ["This is the fanciest tie you'll ever see!",
                 'Try not to get too winded.',
                 "This isn't even half the trouble you're in.",
                 "You're lucky I don't have a whole windsor.",
                 "You can't afford this tie.",
                 "I bet you've never even SEEN a half windsor!",
                 'This tie is out of your league.',
                 "I shouldn't even waste this tie on you.",
                 "You're not even worth half of this tie!"],
 'HangUp': ["You've been disconnected.",
            'Good bye!',
            "It's time I end our connection.",
            "…and don't call back!",
            'Click!',
            'This conversation is over.',
            "I'm severing this link.",
            'I think you have a few hang ups.',
            "It appears you've got a weak link.",
            'Your time is up.',
            'I hope you receive this loud and clear.',
            'You got the wrong number.'],
 'HeadShrink': ["Looks like you're seeing a shrink.",
                'Honey, I shrunk the Toon.',
                "Hope this doesn't shrink your pride.",
                'Do you shrink in the wash?',
                'I shrink therefore I am.',
                "It's nothing to lose your head over.",
                'Are you going out of your head?',
                'Heads up! Or should I say, down.',
                'Objects may be larger than they appear.',
                'Good Toons come in small packages.'],
 'HotAir': ["We're having a heated discussion.",
            "You're experiencing a heat wave.",
            "I've reached my boiling point.",
            'This should cause some wind burn.',
            'I hate to grill you, but…',
            "Always remember, where there's smoke, there's fire.",
            "You're looking a little burned out.",
            'Another meeting up in smoke.',
            "Guess it's time to add fuel to the fire.",
            'Let me kindle a working relationship.',
            'I have some glowing remarks for you.',
            'Air Raid!!!'],
 'Jargon': ['What nonsense.',
            'See if you can make sense of this.',
            'I hope you get this loud and clear.',
            "Looks like I'm going to have to raise my voice.",
            'I insist on having my say.',
            "I'm very outspoken.",
            'I must pontificate on this subject.',
            'See, words can hurt you.',
            'Did you catch my meaning?',
            'Words, words, words, words, words.'],
 'Legalese': ['You must cease and desist.',
              'You will be defeated, legally speaking.',
              'Are you aware of the legal ramifications?',
              "You aren't above the law!",
              'There should be a law against you.',
              "There's no ex post facto with me!",
              "The opinions expressed in this attack are not those of Toon Island: Aftermath.",
              'We cannot be held responsible for damages suffered in this attack.',
              'Your results for this attack may vary.',
              'This attack is void where prohibited.',
              "You don't fit into my legal system!",
              "You can't handle the legal matters."],
 'Liquidate': ['I like to keep things fluid.',
               'Are you having some cash flow problems?',
               "I'll have to purge your assets.",
               'Time for you to go with the flow.',
               "Remember it's slippery when wet.",
               'Your numbers are running.',
               'You seem to be slipping.',
               "It's all crashing down on you.",
               "I think you're diluted.",
               "You're all washed up."],
 'MarketCrash': ["I'm going to crash your party.",
                 "You won't survive the crash.",
                 "I'm more than the market can bear.",
                 "I've got a real crash course for you!",
                 "Now I'll come crashing down.",
                 "I'm a real bull in the market.",
                 'Looks like the market is going down.',
                 'You had better get out quick!',
                 'Sell! Sell! Sell!',
                 'Shall I lead the recession?',
                 "Everybody's getting out, shouldn't you?"],
 'MumboJumbo': ['Let me make this perfectly clear.',
                "It's as simple as this.",
                "This is how we're going to do this.",
                'Let me supersize this for you.',
                'You might call this technobabble.',
                'Here are my five-dollar words.',
                'Boy, this is a mouth full.',
                'Some call me bombastic.',
                'Let me just interject this.',
                'I believe these are the right words.'],
 'ParadigmShift': ["Watch out! I'm rather shifty.",
                   'Prepare to have your paradigm shifted!',
                   "Isn't this an interesting paradigm.",
                   "You'll get shifted out of place.",
                   "I guess it's your shift now.",
                   'Your shift is up!',
                   "You've never shifted this much in your life.",
                   "I'm giving you the bad shift!",
                   'Look into my shifty eyes!'],
 'PeckingOrder': ["This one's for the birds.",
                  'Get ready for a bird bath.',
                  "Looks like you're going to hit a birdie.",
                  'Some think this attack is fowl.',
                  "You're on the bottom of the pecking order.",
                  'A bird in my hand is worth ten on your head!',
                  'Your order is up; the pecking order!',
                  "Why don't I peck on someone my own size? Nah.",
                  'Birds of a feather strike together.'],
 'PickPocket': ['Let me check your valuables.',
                "Hey, what's that over there?",
                'Like taking candy from a baby.',
                'What a steal.',
                "I'll hold this for you.",
                'Watch my hands at all times.',
                'The hand is quicker than the eye.',
                "There's nothing up my sleeve.",
                'The management is not responsible for lost items.',
                "Finder's keepers.",
                "You'll never see it coming.",
                'One for me, none for you.',
                "Don't mind if I do.",
                "You won't be needing this…"],
 'PinkSlip': ['Try not to slip up.',
              "Are you frightened? You've turned pink!",
              'This one will surely slip you up.',
              'Oops, I guess you slipped there, huh?',
              "Watch yourself, wouldn't want to slip!",
              "This one's slippery when wet.",
              "I'll just slip this one in.",
              "Don't mind if you slip by, do you?",
              "Pink isn't really your color.",
              "Here's your pink slip, you're outta here!"],
 'PlayHardball': ['So you wanna play hardball?',
                  "You don't wanna play hardball with me.",
                  'Batter up!',
                  'Hey batter, batter!',
                  "And here's the pitch…",
                  "You're going to need a relief pitcher.",
                  "I'm going to knock you out of the park.",
                  "Once you get hit, you'll run home.",
                  'This is your final inning!',
                  "You can't play with me!",
                  "I'll strike you out.",
                  "I'm throwing you a real curve ball!"],
 'PoundKey': ['Time to return some calls.',
              "I'd like to make a collect call.",
              "Ring-a-ling - it's for you!",
              "I've been wanting to drop a pound or two.",
              'I have a lot of clout.',
              'This may cause a slight pounding sensation.',
              "I'll just punch in this number.",
              'Let me call up a little surprise.',
              "I'll ring you up.",
              "O.K. Toon, it's the pound for you."],
 'PowerTie': ["I'll call later, you looked tied up.",
              'Are you ready to tie die?',
              "Ladies and gentlemen, it's a tie!",
              'You had better learn how to tie.',
              "I'll have you tongue-tied!",
              "This is the worst tie you'll ever get!",
              'Can you feel the power?',
              'My powers are far too great for you!',
              "I've got the power!",
              "By the powers vested in me, I'll tie you up."],
 'PowerTrip': ["Pack your bags, we're taking a little trip.",
               'Did you have a nice trip?',
               "Nice trip, I guess I'll see you next fall.",
               'How was your trip?',
               'Sorry to trip you up there!',
               'You look a little tripped up.',
               "Now you see who's in power!",
               'I am much more powerful than you.',
               "Who's got the power now?",
               "You can't fight the power.",
               'Power corrupts, especially in my hands!'],
 'Quake': ["Let's quake, rattle, and roll.",
           "I've got a whole lot of quakin' goin' on!",
           "I see you quakin' in your shoes.",
           "Here it comes, it's the big one!",
           "This one's off the Richter scale.",
           'Now the land will quake!',
           "Hey, what's shakin'? You!",
           'Ever been in an landquake?',
           "You're on shaky ground now!"],
 'RazzleDazzle': ['Read my lips.',
                  'How about these choppers?',
                  "Aren't I charming?",
                  "I'm going to wow you.",
                  'My dentist does excellent work.',
                  "Blinding aren't they?",
                  "Hard to believe these aren't real.",
                  "Shocking, aren't they?",
                  "I'm going to cap this off.",
                  'I floss after every meal.',
                  'Say Cheese!'],
 'RedTape': ['This should wrap things up.',
             "I'm going to tie you up for awhile.",
             "You're on a roll.",
             'See if you can cut through this.',
             'This will get sticky.',
             "Hope you're claustrophobic.",
             "I'll make sure you stick around.",
             'Let me keep you busy.',
             'Just try to unravel this.',
             'I want this meeting to stick with you.'],
 'ReOrg': ["You don't like the way I reorganized things!",
           'Perhaps a little reorganization is in order.',
           "You're not that bad, you just need to be reorganized.",
           'Do you like my organizational skills.',
           "I just thought I'd give things a new look.",
           'You need to get organized!',
           "You're looking a little disorganized.",
           'Hold on while I reorganize your thoughts.',
           "I'll just wait for you to get a little organized.",
           "You don't mind if I just reorganize a bit?"],
 'RestrainingOrder': ['You should show a little restraint.',
                      "I'm slapping you with a restraining order!",
                      "You can't come within five feet of me.",
                      'Perhaps you better keep your distance.',
                      'You should be restrained.',
                      Cogs + '! Restrain that Toon!',
                      'Try and restrain yourself.',
                      "I hope I'm being too much of a restraint on you.",
                      'See if you can lift these restraints!',
                      "I'm ordering you to restrain!",
                      "Why don't we start with basic restraining?"],
 'Rolodex': ["Your card's in here somewhere.",
             "Here's the number for a pest exterminator.",
             'I want to give you my card.',
             "I've got your number right here.",
             "I've got you covered from a-z.",
             "You'll flip over this.",
             'Take this for a spin.',
             'Watch out for paper cuts.',
             "I'll let my fingers do the knocking.",
             'Is this how I can contact you?',
             'I want to make sure we stay in touch.'],
 'RubberStamp': ['I always make a good impression.',
                 "It's important to apply firm and even pressure.",
                 'A perfect imprint every time.',
                 'I want to stamp you out.',
                 'You must be RETURNED TO SENDER.',
                 "You've been CANCELLED.",
                 'You have a PRIORITY delivery.',
                 "I'll make sure you RECEIVED my message.",
                 "You're not going anywhere - you have POSTAGE DUE.",
                 "I'll need a response ASAP."],
 'RubOut': ['And now for my disappearing act.',
            "I sense I've lost you somewhere.",
            'I decided to leave you out.',
            'I always rub out all obstacles.',
            "I'll just erase this error.",
            'I can make any nuisance disappear.',
            'I like things neat and tidy.',
            'Please try and stay animated.',
            "Now I see YOU…  now I don't.",
            'This will cause some fading.',
            "I'm going to eliminate the problem.",
            'Let me take care of your problem areas.'],
 'Sacked': ["Looks like you're getting sacked.",
            "This one's in the bag.",
            "You've been bagged.",
            'Paper or plastic?',
            'My enemies shall be sacked!',
            'I hold the Toontown record in sacks per game.',
            "You're no longer wanted around here.",
            "Your time is up around here, you're being sacked!",
            'Let me bag that for you.',
            'No defense can match my sack attack!'],
 'Schmooze': ["You'll never see this coming.",
              'This will look good on you.',
              "You've earned this.",
              "I don't mean to gush.",
              'Flattery will get me everywhere.',
              "I'm going to pile it on now.",
              'Time to lay it on thick.',
              "I'm going to get on your good side.",
              'That deserves a good slap on the back.',
              "I'm going to ring your praises.",
              'I hate to knock you off your pedestal, but…'],
 'Shake': ["You're right on the epicenter.",
           "You're standing on a fault line.",
           "It's going to be a bumpy ride.",
           'I think of this as a natural disaster.',
           "It's a disaster of seismic proportions.",
           "This one's off the Richter scale.",
           'Time to duck and cover.',
           'You seem disturbed.',
           'Ready for a jolt?',
           "I'll have you shaken, not stirred.",
           'This will shake you up.',
           'I suggest a good escape plan.'],
 'Shred': ['I need to get rid of some hazardous waste.',
           "I'm increasing my throughput.",
           "I think I'll dispose of you right now.",
           'This will get rid of the evidence.',
           "There's no way to prove it now.",
           'See if you can put this back together.',
           'This should cut you down to size.',
           "I'm going to rip that idea to shreds.",
           "We don't want this to fall into the wrong hands.",
           'Easy come, easy go.',
           "Isn't this your last shred of hope?"],
 'Spin': ['What do you say we go for a little spin?',
          'Do you use the spin cycle?',
          "This'll really make your head spin!",
          "Here's my spin on things.",
          "I'll take you for a spin.",
          'How do you like to "spin" your time?',
          "Watch it. Wouldn't want to spin out of control!",
          "Oh what a spin you're in!",
          'My attacks will make your head spin!'],
 'Synergy': ["I'm taking this to committee.",
             "Your project's been cancelled.",
             "Your budget's been cut.",
             "We're restructuring your division.",
             'I put it to a vote, and you lose.',
             'I just received the final approval.',
             'A good team can get rid of any problem.',
             "I'll get back to you on this.",
             "Let's get right to business.",
             'Consider this a Synergy crisis.'],
 'Tabulate': ["This doesn't add up.",
              'By my count, you lose.',
              "You're racking up quite a tab.",
              "I'll have you totaled in a moment.",
              'Are you ready for these numbers?',
              'Your bill is now due and payable.',
              'Time for the reckoning.',
              'I like to put things in order.',
              'And the tally is…',
              'These numbers should prove to be quite powerful.'],
 'TeeOff': ["You're not up to par.",
            'Fore!',
            "I'm getting teed off.",
            "Caddie, I'll need my driver!",
            'Just try and avoid this hazard.',
            'Swing!',
            'This is a sure hole in one.',
            "You're in my fairway.",
            'Notice my grip.',
            'Watch the birdie!',
            'Keep your eye on the ball!',
            'Mind if I play through?'],
 'Tremor': ['Did you feel that?',
            'Not afraid of a little tremor are you?',
            'A tremor is only the beginning.',
            'You look jittery.',
            "I'll shake things up a bit!",
            'Are you ready to rumble?',
            "What's wrong? You look shaken.",
            'Tremor with fear!',
            'Why are you tremoring with fear?'],
 'Watercooler': ['This ought to cool you off.',
                 "Isn't this refreshing?",
                 'I deliver.',
                 'Straight from the tap - into your lap.',
                 "What's the matter, it's just spring water.",
                 "Don't worry, it's purified.",
                 'Ah, another satisfied customer.',
                 "It's time for your daily delivery.",
                 "Hope your colors don't run.",
                 'Care for a drink?',
                 'It all comes out in the wash.',
                 "The drink's on you."],
 'Withdrawal': ["I believe you're overdrawn.",
                'I hope your balance is high enough for this.',
                'Take that, with interest.',
                'Your balance is dropping.',
                "You're going to need to make a deposit soon.",
                "You've suffered an economic collapse.",
                "I think you're in a slump.",
                'Your finances have taken a decline.',
                'I foresee a definite downturn.',
                "It's a reversal of fortune."],
 'WriteOff': ['Let me increase your losses.',
              "Let's make the best of a bad deal.",
              'Time to balance the books.',
              "This won't look good on your books.",
              "I'm looking for some dividends.",
              'You must account for your losses.',
              'You can forget about a bonus.',
              "I'll shuffle your accounts around.",
              "You're about to suffer some losses.",
              'This is going to hurt your bottom line.']}
BuildingWaitingForVictors = ('Waiting for other players…',)
ElevatorHopOff = 'Hop off'
ElevatorStayOff = "If you hop off, you'll need to wait\nfor the elevator to leave or empty."
ElevatorLeaderOff = 'Only your leader can decide when to hop off.'
ElevatorHoppedOff = 'You need to wait for the next elevator.'
ElevatorMinLaff = 'You need %s laff points to ride this elevator.'
ElevatorHopOK = 'Okay'
ElevatorGroupMember = 'Only your group leader can\n decide when to board.'
KartMinLaff = 'You need %s laff points to ride this kart'
CogsIncExt = ', Inc.'
CogsIncModifier = '%s' + CogsIncExt
CogsInc = Cogs + CogsIncExt
CogsIncRetro = Cogs.upper() + CogsIncExt
CogdominiumsExt = ' Field Office'
Cogdominiums = Cog + CogdominiumsExt
CogdominiumsRetro = Cog.upper() + CogdominiumsExt
DoorKnockKnock = 'Knock, knock.'
DoorWhosThere = "Who's there?"
DoorWhoAppendix = ' who?'
DoorNametag = 'Door'
FADoorCodes_UNLOCKED = None
FADoorCodes_TALK_TO_TOM = 'You need gags! Go talk to Tutorial Tom!'
FADoorCodes_DEFEAT_FLUNKY_HQ = 'Come back here when you have defeated the Flunky!'
FADoorCodes_TALK_TO_HQ = 'Go get your reward from HQ Harry!'
FADoorCodes_WRONG_DOOR_HQ = 'Wrong door! Take the other door to the playground!'
FADoorCodes_GO_TO_PLAYGROUND = 'Wrong way! You need to go to the playground!'
FADoorCodes_DEFEAT_FLUNKY_TOM = 'Walk up to that Flunky to battle him!'
FADoorCodes_TALK_TO_HQ_TOM = 'Go get your reward from Toon Headquarters!'
FADoorCodes_SUIT_APPROACHING = None
FADoorCodes_BUILDING_TAKEOVER = "Watch out! There's a Cog in there!"
FADoorCodes_SB_DISGUISE_INCOMPLETE = "You'll get caught going in there as a Toon! You need to complete your Sellbot Disguise first!\n\nBuild your Sellbot Disguise out of parts from the Factory."
FADoorCodes_CB_DISGUISE_INCOMPLETE = "You'll get caught going in there as a Toon! You need to complete your Cashbot Disguise first!\n\nBuild your Cashbot Disguise by doing ToonTasks in MintyMines."
FADoorCodes_LB_DISGUISE_INCOMPLETE = "You'll get caught going in there as a Toon! You need to complete your Lawbot Disguise first!\n\nBuild your Lawbot Disguise by doing the ToonTasks after MintyMines."
FADoorCodes_BB_DISGUISE_INCOMPLETE = "You'll get caught going in there as a Toon! You need to complete your Bossbot Disguise first!\n\nBuild your Bossbot Disguise by doing the ToonTasks after MintyMines."
KnockKnockContestJokes = {2100: ['Wally', "Wally's not looking, hit him with a pie!"],
 2200: {28: ['Biscuit', 'Biscuit out of here the Cogs are coming!'],
        41: ['Dewey', 'Dewey want to go defeat some more Cogs?'],
        40: ['Minnie', "Minnie people have asked that, and it's driving me crazy!"],
        27: ['Disguise', 'Disguise where the Cogs fly!']},
 2300: ['Justin', 'Justin other couple of Cog parts and off we go!'],
 3300: {10: ['Aladdin', 'Aladdin HQ wants a word with you.'],
        6: ['Weirdo', 'Weirdo all these Cogs come from?'],
        30: ['Bacon', 'Bacon a cake to throw at the Cogs.'],
        28: ['Isaiah', 'Isaiah we go ride the trolley.'],
        12: ['Juliet', "Juliet me in that Cog building with you and I'll give you a Toon-Up."]}}
KnockKnockJokes = [['Who', "Bad echo in here, isn't there?"],
 ['Dozen', 'Dozen anybody want to let me in?'],
 ['Freddie', 'Freddie or not, here I come.'],
 ['Dishes', 'Dishes your friend, let me in.'],
 ['Wooden shoe', 'Wooden shoe like to know?'], # TODO: RETRO MODE "Wooden shoe like to know."
 ['Betty', "Betty doesn't know who I am."],
 ['Kent', 'Kent you tell?'],
 ['Noah', "Noah don't know who either."],
 ["I don't know", 'Neither do I, I keep telling you that.'],
 ['Howard', 'Howard I know?'],
 ['Emma', 'Emma so glad you asked me that.'],
 ['Auto', "Auto know, but I've forgotten."],
 ['Jess', 'Jess me and my shadow.'],
 ['One', 'One-der why you keep asking that?'],
 ['Alma', 'Alma not going to tell you!'],
 ['Zoom', 'Zoom do you expect?'],
 ['Amy', "Amy fraid I've forgotten."],
 ['Arfur', 'Arfur got.'],
 ['Ewan', 'No, just me'],
 ['Cozy', "Cozy who's knocking will you?"],
 ['Sam', 'Sam person who knocked on the door last time.'],
 ['Fozzie', 'Fozzie hundredth time, my name is ' + Flippy + '.'],
 ['Deduct', Donald + ' Deduct.'],
 ['Max', 'Max no difference, just open the door.'],
 ['N.E.', 'N.E. body you like, let me in.'],
 ['Amos', 'Amos-quito bit me.'],
 ['Alma', "Alma candy's gone."],
 ['Bruce', "I Bruce very easily, don't hit me."],
 ['Colleen', "Colleen up your room, it's filthy."],
 ['Elsie', 'Elsie you later.'],
 ['Hugh', 'Hugh is going to let me in?'],
 ['Hugo', "Hugo first - I'm scared."],
 ['Ida', 'Ida know. Sorry!'],
 ['Isabel', 'Isabel on a bike really necessary?'],
 ['Joan', "Joan call us, we'll call you."],
 ['Kay', 'Kay, L, M, N, O, P.'],
 ['Justin', 'Justin time for dinner.'],
 ['Liza', 'Liza wrong to tell.'],
 ['Luke', 'Luke and see who it is.'],
 ['Mandy', "Mandy the lifeboats, we're sinking."],
 ['Max', 'Max no difference - just open the door!'],
 ['Nettie', 'Nettie as a fruitcake.'],
 ['Olivia', 'Olivia me alone!'],
 ['Oscar', 'Oscar stupid question, you get a stupid answer.'],
 ['Patsy', 'Patsy dog on the head, he likes it.'],
 ['Paul', "Paul hard, the door's stuck again."],
 ['Thea', 'Thea later, alligator.'],
 ['Tyrone', "Tyrone shoelaces, you're old enough."],
 ['Stella', 'Stella no answer at the door.'],
 ['Uriah', 'Keep Uriah on the ball.'],
 ['Dwayne', "Dwayne the bathtub. I'm drowning."],
 ['Dismay', "Dismay be a joke, but it didn't make me laugh."],
 ['Ocelot', "Ocelot of questions, don't you?"],
 ['Thermos', 'Thermos be a better knock knock joke than this.'],
 ['Sultan', 'Sultan Pepper.'],
 ['Vaughan', 'Vaughan day my prince will come.'],
 ['Donald', 'Donald come baby, cradle and all.'],
 ['Lettuce', "Lettuce in, won't you?"],
 ['Ivor', 'Ivor sore hand from knocking on your door!'],
 ['Isabel', 'Isabel broken, because I had to knock.'],
 ['Heywood, Hugh, Harry', 'Heywood Hugh Harry up and open this door.'],
 ['Juan', "Juan of this days you'll find out."],
 ['Earl', 'Earl be glad to tell you if you open this door.'],
 ['Abbot', 'Abbot time you opened this door!'],
 ['Ferdie', 'Ferdie last time, open the door!'],
 ['Don', 'Don mess around, just open the door.'],
 ['Sis', 'Sis any way to treat a friend?'],
 ['Isadore', 'Isadore open or locked?'],
 ['Harry', 'Harry up and let me in!'],
 ['Theodore', "Theodore wasn't open so I knocked-knocked."],
 ['Ken', 'Ken I come in?'],
 ['Boo', "There's no need to cry about it."],
 ['You', 'You who! Is there anybody there?'],
 ['Ice cream', "Ice cream if you don't let me in."],
 ['Sarah', "Sarah 'nother way into this building?"],
 ['Mikey', 'Mikey dropped down the drain.'],
 ['Doris', 'Doris jammed again.'],
 ['Yelp', 'Yelp me, the door is stuck.'],
 ['Scold', 'Scold outside.'],
 ['Diana', 'Diana third, can I have a drink please?'],
 ['Doris', 'Doris slammed on my finger, open it quick!'],
 ['Lettuce', 'Lettuce tell you some knock knock jokes.'],
 ['Izzy', 'Izzy come, izzy go.'],
 ['Omar', 'Omar goodness gracious - wrong door!'],
 ['Says', "Says me, that's who!"],
 ['Duck', "Just duck, they're throwing things at us."],
 ['Tank', "You're welcome."],
 ['Eyes', 'Eyes got loads more knock knock jokes for you.'],
 ['Pizza', 'Pizza cake would be great right now.'],
 ['Closure', 'Closure mouth when you eat.'],
 ['Harriet', "Harriet all my lunch, I'm starving."],
 ['Wooden', 'Wooden you like to know?'],
 ['Punch', 'Not me, please.'],
 ['Gorilla', 'Gorilla me a hamburger.'],
 ['Jupiter', "Jupiter hurry, or you'll miss the trolley."],
 ['Bertha', 'Happy Bertha to you!'],
 ['Cows', 'Cows go "moo" not "who."'],
 ['Tuna fish', "You can tune a piano, but you can't tuna fish."],
 ['Consumption', 'Consumption be done about all these knock knock jokes?'],
 ['Banana', 'Banana spilt so ice creamed.'],
 ['X', 'X-tremely pleased to meet you.'],
 ['Haydn', 'Haydn seek is fun to play.'],
 ['Rhoda', 'Rhoda boat as fast as you can.'],
 ['Quacker', "Quacker 'nother bad joke and I'm off!"],
 ['Nana', 'Nana your business.'],
 ['Ether', 'Ether bunny.'],
 ['Little old lady', "My, you're good at yodelling!"],
 ['Beets', 'Beets me, I forgot the joke.'],
 ['Hal', 'Halloo to you too!'],
 ['Sarah', 'Sarah doctor in the house?'],
 ['Aileen', 'Aileen Dover and fell down.'],
 ['Atomic', 'Atomic ache'],
 ['Agatha', 'Agatha headache. Got an aspirin?'],
 ['Stan', "Stan back, I'm going to sneeze."],
 ['Hatch', 'Bless you.'],
 ['Ida', "It's not Ida who, it's Idaho."],
 ['Zippy', 'Mrs. Zippy.'],
 ['Yukon', 'Yukon go away and come back another time.']]
# Sometimes classic characters said "MelodyLand" in TTO. It should be "Melodyland", but for retro mode it should keep the typo.
CCharChatterMelodyLand = "Melodyland" # TODO: RETRO MODE "MelodyLand"
SharedChatterGreetings = ['Hi, %!',
 'Yoo-hoo %, nice to see you.',
 "I'm glad you're here today!",
 'Well, hello there, %.']
SharedChatterComments = ["That's a great name, %.",
 'I like your name.',
 'Watch out for the ' + Cogs + '.',
 'Looks like the trolley is coming!',
 'I need to play a trolley game to get some pies!',
 'Sometimes I play trolley games just to eat the fruit pie!',
 'Whew, I just stopped a bunch of ' + Cogs + '. I need a rest!',
 'Yikes, some of those ' + Cogs + ' are big guys!',
 "You look like you're having fun.",
 "Oh boy, I'm having a good day.",
 "I like what you're wearing.",
 "I think I'll go fishing this afternoon.",
 'Have fun in my neighborhood.',
 'I hope you are enjoying your stay in Toontown!',
 "I heard it's snowing at the Brrrgh.",
 'Have you ridden the trolley today?',
 'I like to meet new people.',
 'Wow, there are lots of ' + Cogs + ' in the Brrrgh.',
 'I love to play tag. Do you?',
 'Trolley games are fun to play.',
 'I like to make people laugh.',
 "It's fun helping my friends.",
 "A-hem, are you lost? Don't forget your map is in your shticker Book.",
 'Try not to get tied up in the ' + Cogs + "' Red Tape.",
 'I hear ' + Daisy + ' has planted some new flowers in her garden.',
 'If you press the Page Up key, you can look up!',
 'If you help take over Cog buildings, you can earn a bronze star!',
 'If you press the Tab key, you can see different views of your surroundings!',
 'If you press the Ctrl key, you can jump!']
SharedChatterGoodbyes = ['I have to go now, bye!',
 "I think I'll go play a trolley game.",
 "Well, so long. I'll be seeing you, %!",
 "I'd better hurry and get to work stopping those " + Cogs + '.',
 "It's time for me to get going.",
 'Sorry, but I have to go.',
 'Good-bye.',
 'See you later, %!',
 "I think I'm going to go practice tossing cupcakes.",
 "I'm going to join a group and stop some " + Cogs + '.',
 'It was nice to see you today, %.',
 "I have a lot to do today. I'd better get busy."]
MickeyChatter = (['Welcome to ' + lToonIslandCentral + '.', 'Hi, my name is ' + Mickey + ". What's yours?"], ['Hey, have you seen ' + Donald + '?',
  "I'm going to go watch the fog roll in at " + lDonaldsDock + '.',
  'If you see my pal ' + Goofy + ', say hi to him for me.',
  'I hear ' + Daisy + ' has planted some new flowers in her garden.'], ["I'm going to " + CCharChatterMelodyLand + " to see " + Minnie + '!',
  "Gosh, I'm late for my date with " + Minnie + '!',
  "Looks like it's time for " + Pluto + "'s dinner.",
  "I think I'll go swimming at " + lDonaldsDock + '.',
  "It's time for a nap. I'm going to Dreamland."])
WinterMickeyCChatter = (["Hi, I'm Merry Mickey!",
  'Welcome to Tinseltown… I mean, Toontown!',
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %'], ['Sing your seasonal cheer at Joy Buzzers to the World and Joy is sure to return the favor!',
  'Golly, these halls sure are decked!',
  'Sing your seasonal cheer at Joy Buzzers to the World and Joy is sure to return the favor!',
  'Just look at those tree lights! What a sight!',
  'Sing your seasonal cheer at Joy Buzzers to the World and Joy is sure to return the favor!',
  'Not a creature is stirring, except this mouse!',
  'Sing your seasonal cheer at Joy Buzzers to the World and Joy is sure to return the favor!',
  'I love this time of year!',
  'Sing your seasonal cheer at Joy Buzzers to the World and Joy is sure to return the favor!',
  "I'm feeling jolly, how about you?",
  'Sing your seasonal cheer at Joy Buzzers to the World and Joy is sure to return the favor!',
  'Know any good carols?',
  'Sing your seasonal cheer at Joy Buzzers to the World and Joy is sure to return the favor!',
  'Oh boy! I love Winter Holiday!',
  'Sing your seasonal cheer at Joy Buzzers to the World and Joy is sure to return the favor!',
  "I think I'll trade my gloves for mittens!"], ['Have a happy Winter Holiday!',
  'Warm wishes to you!',
  'Shucks, sorry you have to go. So long!',
  "I'm going caroling with Minnie!"])
ValentinesMickeyChatter = (["Hi, I'm Mickey!",
  'Welcome to ValenToon Island Central!',
  "Happy ValenToon's Day!",
  "Happy ValenToon's Day, %"], ['Love is in the air! And butterflies!',
  'Those hearts are good for Laff boosts!',
  'I hope Minnie likes what I got her!',
  "The Cattlelog has lots of ValenToon's Day gifts!",
  "Throw a ValenToon's Day party!",
  'Show the Cogs you love them with a pie in the face!',
  "I'm taking Minnie out to the Kooky Cafe!",
  'Will Minnie want chocolates or flowers?'], ['I loved having you visit!', "Tell Minnie I'll pick her up soon!"])
WinterMickeyDChatter = (["Hi, I'm Merry Mickey!",
  'Welcome to Tinseltown… I mean, Toontown!',
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %'], ['Golly, these halls sure are decked!',
  'Just look at those tree lights! What a sight!',
  'Not a creature is stirring, except this mouse!',
  'I love this time of year!',
  "I'm feeling jolly, how about you?",
  'Know any good carols?',
  'Oh boy! I love Winter Holiday!',
  "I think I'll trade my gloves for mittens!"], ['Have a happy Winter Holiday!',
  'Warm wishes to you!',
  'Shucks, sorry you have to go. So long!',
  "I'm going caroling with Minnie!"])
VampireMickeyChatter = (['Welcome to ' + lToonIslandCentral + '.',
  'Hi, my name is ' + Mickey + ". What's yours?",
  'Happy Halloween!',
  'Happy Halloween, %!',
  'Welcome to Tombtown… I mean Toontown!'], ['If you think playing tricks is All Fun and Games, go see King Popcorn for a treat!',
  "It's fun to dress up for Halloween!",
  'If you think playing tricks is All Fun and Games, go see King Popcorn for a treat!',
  'Do you like my costume?',
  'If you think playing tricks is All Fun and Games, go see King Popcorn for a treat!',
  '%, watch out for Bloodsucker Cogs!',
  'If you think playing tricks is All Fun and Games, go see King Popcorn for a treat!',
  "Aren't the Halloween decorations great?",
  'If you think playing tricks is All Fun and Games, go see King Popcorn for a treat!',
  'Beware of black cats!',
  'If you think playing tricks is All Fun and Games, go see King Popcorn for a treat!',
  'Did you see the Toon with the pumpkin head?',
  'If you think playing tricks is All Fun and Games, go see King Popcorn for a treat!',
  'Boo! Did I scare you?',
  'If you think playing tricks is All Fun and Games, go see King Popcorn for a treat!',
  "Don't forget to brush your fangs!",
  'If you think playing tricks is All Fun and Games, go see King Popcorn for a treat!',
  "I'm a vampire, but not a Bloodsucker!",
  'If you think playing tricks is All Fun and Games, go see King Popcorn for a treat!',
  "I hope you're enjoying our Halloween fun!",
  'If you think playing tricks is All Fun and Games, go see King Popcorn for a treat!',
  'Vampires are really popular this year!'], ["I'm going to check out the cool Halloween decorations.",
  "I'm going to " + CCharChatterMelodyLand + " to surprise " + Minnie + '!',
  "I'm going to sneak up on another Toon! Shhh!",
  "I'm going trick-or-treating!",
  'Shhh, sneak with me.'])
FieldOfficeMickeyChatter = ['Have you heard about the new Mover & Shaker Field Offices?']
MinnieChatter = (['Welcome to Melodyland.', 'Hi, my name is ' + Minnie + ". What's yours?"], ['The hills are alive with the sound of music!',
  'You have a cool outfit, %.',
  'Hey, have you seen ' + Mickey + '?',
  'If you see my friend ' + Goofy + ', say hi to him for me.',
  'Wow, there are lots of ' + Cogs + ' near ' + Donald + "'s Dreamland.",
  "I heard it's foggy at the " + lDonaldsDock + '.',
  'Be sure and try the maze in ' + lDaisyGardens + '.',
  "I think I'll go catch some tunes.",
  'Hey %, look at that over there.',
  'I love the sound of music.',
  "I bet you didn't know Melodyland is also called TuneTown! Hee Hee!",
  'I love to play the Matching Game. Do you?',
  'I like to make people giggle.',
  'Boy, trotting around in heels all day is hard on your feet!',
  'Nice shirt, %.',
  'Is that a Jellybean on the ground?'], ["Gosh, I'm late for my date with %s!" % Mickey, "Looks like it's time for %s's dinner." % Pluto, "It's time for a nap. I'm going to Dreamland."])
WinterMinnieCChatter = (["Hi, I'm Merry Minnie!",
  'Welcome to the land of carols!',
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %!'], ["You'll get more than a Shave and a Haircut For a Song if you carol to Barbara Seville!",
  'Belt out a tune, Toon!',
  "You'll get more than a Shave and a Haircut For a Song if you carol to Barbara Seville!",
  'Show us how to croon, Toon!',
  "You'll get more than a Shave and a Haircut For a Song if you carol to Barbara Seville!",
  'Can you carry a melody here in Melodyland?',
  "You'll get more than a Shave and a Haircut For a Song if you carol to Barbara Seville!",
  'Those lamps look warm in their scarves!',
  "You'll get more than a Shave and a Haircut For a Song if you carol to Barbara Seville!",
  "The sing's the thing!",
  "You'll get more than a Shave and a Haircut For a Song if you carol to Barbara Seville!",
  "I'll always like you, for better or verse!",
  "You'll get more than a Shave and a Haircut For a Song if you carol to Barbara Seville!",
  'Everything looks better with a wreath!'], ['Have a fun Winter Holiday!', 'Happy Trails!', 'Mickey is taking me caroling!'])
WinterMinnieDChatter = (["Hi, I'm Merry Minnie!",
  'Welcome to the land of carols!',
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %!'], ['Belt out a tune, Toon!',
  'Show us how to croon, Toon!',
  'Can you carry a melody here in Melodyland?',
  'Those lamps look warm in their scarves!',
  "The sing's the thing!",
  "You can't go wrong with a song!",
  "I'll always like you, for better or verse!",
  'Everything looks better with a wreath!'], ['Have a fun Winter Holiday!', 'Happy Trails!', 'Mickey is taking me caroling!'])
ValentinesMinnieChatter = (["Hello, I'm Minnie!", "Happy ValenToon's Day!", "Happy ValenToon's Day, %"], ['I hope Mickey got me chocolates or flowers!',
  'Those hearts are good for Laff boosts!',
  'I want to go to a ValenToon Party!',
  'I hope Mickey takes me to the Kooky Cafe!',
  'Mickey is such a good ValenToon!',
  'What did you get your ValenToon?',
  "Mickey has never missed a ValenToon's Day!"], ['It was sweet having you visit!'])
WitchMinnieChatter = (['Welcome to Magicland… I mean Melodyland!',
  "Hi, my name is Magic Minnie! What's yours?",
  "Hello, I think you're enchanting!",
  'Happy Halloween!',
  'Happy Halloween, %!'], ['I hear Tabitha has treats for Really Kool Katz who can play tricks!',
  "It's a magical day, don't you think?",
  'I hear Tabitha has treats for Really Kool Katz who can play tricks!',
  'Now where did I put my spell book',
  'I hear Tabitha has treats for Really Kool Katz who can play tricks!',
  'Abra-Cadabra!',
  'I hear Tabitha has treats for Really Kool Katz who can play tricks!',
  'Toontown looks positively spooky today!',
  'I hear Tabitha has treats for Really Kool Katz who can play tricks!',
  'Are you seeing stars too?',
  'I hear Tabitha has treats for Really Kool Katz who can play tricks!',
  'Purple is really my color!',
  'I hear Tabitha has treats for Really Kool Katz who can play tricks!',
  'I hope your Halloween is bewitching!',
  'I hear Tabitha has treats for Really Kool Katz who can play tricks!',
  'Beware of musical spiders!',
  'I hear Tabitha has treats for Really Kool Katz who can play tricks!',
  'I hope you are enjoying our Halloween fun!'], ["I'm going to disappear now!", 'Time for me to vanish!', 'Mickey is taking me Trick-or-Treating!'])
FieldOfficeMinnieChatter = ['Everyone is talking about the new Mover & Shaker Field Offices!']
DaisyChatter = (['Welcome to my garden!', "Hello, I'm " + Daisy + ". What's your name?", "It's so nice to see you %!"], ['My prize winning flower is at the center of the garden maze.',
  'I just love strolling through the maze.',
  "I haven't seen " + Goofy + ' all day.',
  'I wonder where ' + Goofy + ' is.',
  'Have you seen ' + Donald + "? I can't find him anywhere.",
  'If you see my friend ' + Minnie + ', please say "Hello" to her for me.',
  'The better gardening tools you have the better plants you can grow.',
  'There are far too many ' + Cogs + ' near ' + lDonaldsDock + '.',
  'Watering your garden every day keeps your plants happy.',
  'To grow a Pink Daisy plant a yellow and red Jellybean together.',
  'Yellow daisies are easy to grow, just plant a yellow Jellybean.',
  'If you see sand under a plant it needs water or it will wilt!'], ["I'm going to Melody Land to see %s!" % Minnie,
  "I'm late for my picnic with %s!" % Donald,
  "I think I'll go swimming at " + lDonaldsDock + '.',
  "Oh, I'm a little sleepy. I think I'll go to Dreamland."])
ValentinesDaisyChatter = (["Hi, I'm Daisy!", "Happy ValenToon's Day!", "Happy ValenToon's Day, %"], ["I hope Donald doesn't get me another Amore Eel!",
  'Donald is taking me out to the Deep-see Diner!',
  'I certainly have enough roses!',
  'Those hearts are good for Laff boosts!',
  "I'd love to go to a ValenToon's Day party!",
  'This is the garden where love grows!',
  "Donald better not sleep through ValenToon's Day again!",
  'Maybe Donald and I can double-date with Mickey and Minnie!'], ["Tell Donald I'll be waiting for him!", "Have a nice ValenToon's Day!"])
WinterDaisyCChatter = (['Welcome to the only garden that grows in the winter!', 'Happy Winter Holiday!', 'Happy Winter Holiday, %!'], ['Shoshanna at Pine Needle Crafts is a real sap for songs, so why not craft her a carol?',
  'My garden needs more mistletoe!',
  'Shoshanna at Pine Needle Crafts is a real sap for songs, so why not craft her a carol?',
  'I need to plant holly for next year!',
  'Shoshanna at Pine Needle Crafts is a real sap for songs, so why not craft her a carol?',
  "I'm going to ask Goofy to build me a gingerbread house!",
  'Shoshanna at Pine Needle Crafts is a real sap for songs, so why not craft her a carol?',
  'Those lights on the lamps are lovely!',
  'Shoshanna at Pine Needle Crafts is a real sap for songs, so why not craft her a carol?',
  'That is some jolly holly!',
  'Shoshanna at Pine Needle Crafts is a real sap for songs, so why not craft her a carol?',
  'My snowman keeps melting!',
  'Shoshanna at Pine Needle Crafts is a real sap for songs, so why not craft her a carol?',
  'That duck is decked out!',
  'Shoshanna at Pine Needle Crafts is a real sap for songs, so why not craft her a carol?',
  'I grew all these lights myself!'], ['Have a jolly Winter Holiday!',
  'Happy planting!',
  'Tell Donald to stop by with presents!',
  'Donald is taking me caroling!'])
WinterDaisyDChatter = (['Welcome to the only garden that grows in the winter!', 'Happy Winter Holiday!', 'Happy Winter Holiday, %!'], ['My garden needs more mistletoe!',
  'I need to plant holly for next year!',
  "I'm going to ask Goofy to build me a gingerbread house!",
  'Those lights on the lamps are lovely!',
  'That is some jolly holly!',
  'My snowman keeps melting!',
  'That duck is decked out!',
  'I grew all these lights myself!'], ['Have a jolly Winter Holiday!',
  'Happy planting!',
  'Tell Donald to stop by with presents!',
  'Donald is taking me caroling!'])
HalloweenDaisyChatter = (['Welcome to Daisy Ghosts… I mean Gardens!', 'Happy Halloween!', 'Happy Halloween, %!'], ['Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'Wanna dance?',
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  "I'm a duck with a poodle skirt!",
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'The pirate tree needs water.',
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'Trick-or-Tree!',
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'Do you notice anything strange about the trees?',
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'I should grow some pumpkins!',
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'WHO notices something different about the lamps?',
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'Halloween really grows on me!',
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'Twig-or-Treat!',
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  "Owl bet you didn't notice the spooky lamps!",
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'I hope you are enjoying our Halloween fun!'], ['Donald is taking me Trick-or-Treating!', "I'm going to check out the fun Halloween decorations."])
FieldOfficeDaisyChatter = ['Those Mover & Shaker Field Offices are popping up like weeds!']
ChipChatter = (['Welcome to %s!' % lOutdoorZone,
  "Hello, I'm " + Chip + ". What's your name?",
  "No, I'm " + Chip + '.',
  "It's so nice to see you %!",
  'We are Chip and Dale!'], ['I like golf.', 'We have the best acorns in Toontown.', 'The golf holes with volcanoes are the most challenging for me.'], ["We're going to the " + lTheBrrrgh + ' and play with %s.' % Pluto,
  "We'll visit %s and fix him." % Donald,
  "I think I'll go swimming at " + lDonaldsDock + '.',
  "Oh, I'm a little sleepy. I think I'll go to Dreamland."])
ValentinesChipChatter = (["I'm Chip!", "Happy ValenToon's Day!", "Happy ValenToon's Day, %!"], ["What did you get me for ValenToon's Day, Dale?",
  'Those hearts are good for Laff boosts!',
  'Will you be my ValenToon, Dale?',
  "What did you get the Cogs for ValenToon's Day?",
  "I love ValenToon's Day!"], ['Come back any time!'])
WinterChipChatter = (['Happy Winter Holiday!', 'Dressed as chipmunks!', 'Happy Winter Holiday, %!'], ['Happy Winter Holiday, Dale!',
  'All this water could freeze any minute!',
  'We should switch the golf balls with snowballs!',
  'If only chipmunks knew how to sing!',
  'Did you remember to store nuts for the winter?',
  'Did you get the Cogs a present?'], ['Go nuts this Winter Holiday!', 'Have a joyful winter Holiday!'])
HalloweenChipChatter = (['Play some MiniGhoul… I mean Golf!', 'Happy Halloween!', 'Happy Halloween, %!'], ["We're nuts about Halloween!",
  "You're under arrest",
  "You can't outrun the long arm of the law",
  "I'm a Bobby!",
  'I hope you are enjoying our Halloween fun!',
  'Play golf and get a Howl-In-One.',
  'Candy corns are sweeter than acorns.',
  'I hope you are enjoying our Halloween fun!'], ['%, watch out for Bloodsucker Cogs!'])
DaleChatter = (["It's so nice to see you %!",
  "Hello, I'm " + Dale + ". What's your name?",
  "Hi I'm " + Chip + '.',
  'Welcome to %s!' % lOutdoorZone,
  'We are Chip and Dale!'], ['I like picnics.', 'Acorns are tasty, try some.', 'Those windmills can be hard too.'], ['Hihihi ' + Pluto + ' is fun to play with.',
  "Yeah, let's fix %s." % Donald,
  'A swim sounds refreshing.',
  "I'm getting tired and could use a nap."])
ValentinesDaleChatter = (["I'm Dale!", "Happy ValenToon's Day!", "Happy ValenToon's Day, %!"], ['Same thing as last year. Nothing!',
  'I miss the nuts!',
  'Will you be my ValenToon, Chip?',
  'A pie in the face',
  "Yeah, it's all right."], ['Come back any time!'])
WinterDaleChatter = (['Merry chipmunks!',
  "Hi, we're two merry elves!",
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %!'], ['Happy Winter Holiday, Chip!',
  'Better not be on the geyser when it happens!',
  'And the golf clubs with icicles!',
  'Whoever heard of singing chipmunks?',
  'I told YOU to do that!',
  'Yes, a cream pie!'], ['And bring some back for us!', 'Have a joyful Winter Holiday!'])
HalloweenDaleChatter = (['Happy Halloween, %!', 'Play some MiniGhoul… I mean Golf!', 'Happy Halloween!'], ["We're nuts about Halloween!",
  'Great, I could use a rest!',
  'But your arms are short!',
  'I thought you were a Chip!',
  'Play golf and get a Howl-In-One',
  'Candy corns are sweeter than acorns.',
  'I hope you are enjoying our Halloween fun!'], ['%, watch out for Bloodsucker Cogs!'])
GoofyChatter = (['Welcome to ' + lDaisyGardens + '.', 'Hi, my name is ' + Goofy + ". What's yours?", "Gawrsh, it's nice to see you %!"], ['Boy it sure is easy to get lost in the garden maze!',
  'Be sure and try the maze here.',
  "I haven't seen " + Daisy + ' all day.',
  'I wonder where ' + Daisy + ' is.',
  'Hey, have you seen ' + Donald + '?',
  'If you see my friend ' + Mickey + ', say hi to him for me.',
  "D'oh! I forgot to fix " + Mickey + "'s breakfast!",
  'Gawrsh there sure are a lot of ' + Cogs + ' near ' + lDonaldsDock + '.',
  'It looks like ' + Daisy + ' has planted some new flowers in her garden.',
  'At the Brrrgh branch of my Gag Shop, Hypno-Goggles are on sale for only 1 Jellybean!',
  "Goofy's Gag Shops offer the best jokes, tricks, and funnybone-ticklers in all of Toontown!",
  "At Goofy's Gag Shops, every pie in the face is guaranteed to make a laugh or you get your Jellybeans back!"], ["I'm going to Melody Land to see %s!" % Mickey,
  "Gosh, I'm late for my game with %s!" % Donald,
  "I think I'll go swimming at " + lDonaldsDock + '.',
  "It's time for a nap. I'm going to Dreamland."])
WinterGoofyChatter = (["I'm Goofy about the holidays!",
  'Welcome to Snowball Speedway!',
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %!'], ['Who needs reindeer when you have a fast kart?',
  'Gawrsh! Is it Winter Holiday already?',
  'I need my earmuffs!',
  "I haven't done any shopping yet!",
  "Don't drive your kart on ice!",
  'Seems like it was Winter Holiday only a year ago!',
  'Treat your kart to a present and spruce it up!',
  'These karts are better than any old sleigh!'], ['Have a cheery Winter Holiday!', 'Drive safe, now!', 'Watch out for flying reindeer!'])
ValentinesGoofyChatter = (["I'm Goofy about ValenToon's Day!", "Happy ValenToon's Day!", "Happy ValenToon's Day, %!"], ["Gawrsh! Is it ValenToon's Day already?",
  'I LOVE kart racing!',
  'Be sweet to each other out there!',
  'Show your sweetie a new kart!',
  'Toons love their karts!',
  'Make some new friends on the track!'], ['Drive safe, now!', 'Show some love out there!'])
GoofySpeedwayChatter = (['Welcome to ' + lGoofySpeedway + '.', 'Hi, my name is ' + Goofy + ". What's yours?", "Gawrsh, it's nice to see you %!"], ['Boy, I saw a terrific race earlier.',
  'Watch out for banana peels on the race track!',
  'Have you upgraded your kart lately?',
  'We just got in some new rims at the kart shop.',
  'Hey, have you seen ' + Donald + '?',
  'If you see my friend ' + Mickey + ', say hi to him for me.',
  "D'oh! I forgot to fix " + Mickey + "'s breakfast!",
  'Gawrsh there sure are a lot of ' + Cogs + ' near ' + lDonaldsDock + '.',
  'At the Brrrgh branch of my Gag Shop, Hypno-Goggles are on sale for only 1 Jellybean!',
  "Goofy's Gag Shops offer the best jokes, tricks, and funnybone-ticklers in all of Toontown!",
  "At Goofy's Gag Shops, every pie in the face is guaranteed to make a laugh or you get your Jellybeans back!"], ["I'm going to Melody Land to see %s!" % Mickey,
  "Gosh, I'm late for my game with %s!" % Donald,
  "I think I'll go swimming at " + lDonaldsDock + '.',
  "It's time for a nap. I'm going to Dreamland."])
SuperGoofyChatter = (['Welcome to my Super Speedway!',
  "Hi, I'm Super Goof! What's your name?",
  'Happy Halloween!',
  'Happy Halloween, %!'], ['I am feeling kind of batty today!',
  'Anybody see my cape around? Oh, there it is!',
  "Gawrsh! I don't know my own strength!",
  'Did somebody call for a superhero?',
  "Beware Cogs, I'll save Halloween!",
  "There's nothing scarier than me in a kart!",
  "I bet you don't know who I am with this mask on!",
  "It's fun to dress up for Halloween!",
  'I hope you are enjoying our Halloween fun!'], ['Gotta fly!',
  'Hi-Ho and away I go!',
  "Should I fly or drive to Rainbow Rise?",
  'Gawrsh, have a Happy Halloween!'])
DonaldChatter = (['Welcome to Dreamland.', "Hi, my name is %s. What's yours?" % Donald], ['Sometimes this place gives me the creeps.',
  'Be sure and try the maze in ' + lDaisyGardens + '.',
  "Oh boy, I'm having a good day.",
  'Hey, have you seen ' + Mickey + '?',
  'If you see my buddy ' + Goofy + ', say hi to him for me.',
  "I think I'll go fishing this afternoon.",
  'Wow, there are lots of ' + Cogs + ' at ' + lDonaldsDock + '.',
  "Hey, didn't I take you on a boat ride at " + lDonaldsDock + '?',
  "I haven't seen " + Daisy + ' all day.',
  'I hear ' + Daisy + ' has planted some new flowers in her garden.',
  'Quack.'], ["I'm going to Melody Land to see %s!" % Minnie,
  "Gosh, I'm late for my date with %s!" % Daisy,
  "I think I'll go swimming at my dock.",
  "I think I'll take my boat for a spin at my dock."])
WinterDreamlandCChatter = (["Hi, I'm Dozing Donald!",
  'Welcome to Holiday Dreamland!',
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %!'], ['Willow says that learning a little Sleep Voice Training is a real present, sing her a tune and find out why!',
  'I wish I was nestled all snug in my bed!',
  'Willow says that learning a little Sleep Voice Training is a real present, sing her a tune and find out why!',
  "I'm dreaming of a white Toontown!",
  'Willow says that learning a little Sleep Voice Training is a real present, sing her a tune and find out why!',
  'I meant to leave out milk and cookies!',
  'Willow says that learning a little Sleep Voice Training is a real present, sing her a tune and find out why!',
  'When I wake up, I better see lots of presents!',
  'Willow says that learning a little Sleep Voice Training is a real present, sing her a tune and find out why!',
  "I hope I don't sleep through the holidays!",
  'Willow says that learning a little Sleep Voice Training is a real present, sing her a tune and find out why!',
  "I love a long winter's nap!",
  'Willow says that learning a little Sleep Voice Training is a real present, sing her a tune and find out why!',
  'The trees on the streets are covered in night lights!'], ['To all, a good night!', 'Sweet dreams!', 'When I wake up I am going caroling!'])
WinterDreamlandDChatter = (["Hi, I'm Dozing Donald!",
  'Welcome to Holiday Dreamland!',
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %!'], ['I wish I was nestled all snug in my bed!',
  "I'm dreaming of a white Toontown!",
  'I meant to leave out milk and cookies!',
  'When I wake up, I better see lots of presents!',
  "I hope I don't sleep through the holidays!",
  "I love a long winter's nap!",
  'The trees on the streets are covered in night lights!'], ['To all, a good night!', 'Sweet dreams!', 'When I wake up I am going caroling!'])
HalloweenDreamlandChatter = (['Happy Halloween!', 'Happy Halloween, %!', "Hi, I'm FrankenDonald!"], ['If you can play a trick on my friend Max, then you can Relax To The Max with a treat!',
  'Am I awake or dreaming?',
  'If you can play a trick on my friend Max, then you can Relax To The Max with a treat!',
  "I'm so scared, I can't fall asleep!",
  'If you can play a trick on my friend Max, then you can Relax To The Max with a treat!',
  'So this is what Dreamland looks like!',
  'If you can play a trick on my friend Max, then you can Relax To The Max with a treat!',
  "Boy, I'm sleepy!",
  'If you can play a trick on my friend Max, then you can Relax To The Max with a treat!',
  "I hope I don't sleep through Halloween this year!",
  'If you can play a trick on my friend Max, then you can Relax To The Max with a treat!',
  'I hope you are enjoying our Halloween fun!'], ['Sleep with the lights on tonight!', 'When I wake up, I am going Trick-or-Treating!'])
ValentinesDreamlandChatter = (["Hello, I'm (yawn) Donald!", "Happy ValenToon's Day!", "Happy ValenToon's Day, %!"], ["I hope I don't sleep through ValenToon's Day!",
  "I'm dreaming of Daisy!",
  "I had a nightmare that I missed ValenToon's Day!",
  'Those hearts are good for Laff boosts!',
  "Throw a ValenToon's Day party!",
  'Show the Cogs you love them with a pie in the face!',
  "I couldn't dream of a nicer holiday than ValenToon's Day!",
  'I love sleeping!'], ['Nite-nite!', "Wake me when it's ValenToon's Day!"])
FieldOfficeDreamlandChatter = ['I dreamed about something called a Field Office…']
HalloweenDonaldChatter = (['Welcome to my Halloween harbor!',
  'Come aboard, if you have treats!',
  'Happy Halloween!',
  'Happy Halloween, %!'], ['If playing tricks is making you feel Rudderly Ridiculous, then go see Rudy for a treat!',
  "I'm dressed as a sailor!",
  'If playing tricks is making you feel Rudderly Ridiculous, then go see Rudy for a treat!',
  'Pumpkins make great lanterns!',
  'If playing tricks is making you feel Rudderly Ridiculous, then go see Rudy for a treat!',
  "I've never seen palm trees with hairy legs before!",
  'If playing tricks is making you feel Rudderly Ridiculous, then go see Rudy for a treat!',
  "Maybe I'll be a pirate next Halloween!",
  'If playing tricks is making you feel Rudderly Ridiculous, then go see Rudy for a treat!',
  'I think the best treats are starfish!',
  'If playing tricks is making you feel Rudderly Ridiculous, then go see Rudy for a treat!',
  "I'll take you Trick-or-Treating around the harbor!",
  'If playing tricks is making you feel Rudderly Ridiculous, then go see Rudy for a treat!',
  'I hope those spiders stay in the trees!',
  'If playing tricks is making you feel Rudderly Ridiculous, then go see Rudy for a treat!',
  'What do you call a ghost in the water? A BOO-y!',
  'If playing tricks is making you feel Rudderly Ridiculous, then go see Rudy for a treat!',
  'I hope you are enjoying our Halloween fun!'], ['Set sail for scares!', 'Happy haunting!', "I'm going to check out the spooky Halloween decorations."])
ValentinesDonaldChatter = (["Ahoy, I'm Donald!", "Happy ValenToon's Day!", "Happy ValenToon's Day, %!"], ["Was I supposed to take Daisy somewhere for ValenToon's Day?",
  "Just once more around the dock, then I'll get Daisy something.",
  "What would Daisy like for ValenToon's Day?",
  'Those hearts in the water are good for Laff boosts!',
  "Throw a ValenToon's Day party!",
  'Show the Cogs you love them with a pie in the face!',
  "I'll have to catch an Amore Eel for Daisy!"], ['Aloha!', 'Give the Cogs my best!'])
WinterDonaldCChatter = (["Welcome to Donald's Boat and Sleigh Dock!",
  'All aboard for the Winter Holiday cruise!',
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %!'], ['I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!',
  'How do you like my duck-orations?',
  'I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!',
  'What is snow doing on the lamp posts?',
  'I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!',
  'This water better not ice over!',
  'I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!',
  'How did they get the lights up in those trees?',
  'I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!',
  'This boat is better than a sleigh! or is it?',
  'I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!',
  "I don't need reindeer to pull this boat!",
  'I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!',
  "I'm glad I'm not a turkey this time of year!",
  'I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!',
  'My present to you? Free boat rides!',
  'I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!',
  "I hope I don't get a lump of coal again!",
  'I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!'], ['All ashore for holiday fun!', 'Remember to tip your boat driver on the way out!', 'Enjoy your holiday!'])
WinterDonaldDChatter = (["Welcome to Donald's Boat and Sleigh Dock!",
  'All aboard for the Winter Holiday cruise!',
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %!'], ['How do you like my duck-orations?',
  'What is snow doing on the lamp posts?',
  'This water better not ice over!',
  'How did they get the lights up in those trees?',
  'This boat is better than a sleigh! or is it?',
  "I don't need reindeer to pull this boat!",
  "I'm glad I'm not a turkey this time of year!",
  'My present to you? Free boat rides!',
  "I hope I don't get a lump of coal again!"], ['All ashore for holiday fun!', 'Remember to tip your boat driver on the way out!', 'Enjoy your holiday!'])
WesternPlutoChatter = (["Boo! Don't be scared, it's just me … Pluto!", 'Happy Halloween, pardner!', 'Happy Halloween, %!'], ["Frosty Fred has treats for tricks, they make him feel like there's Snowplace Like Home!",
  'I do tricks for treats!',
  "Frosty Fred has treats for tricks, they make him feel like there's Snowplace Like Home!",
  "Mickey's taking me Trick-or-Treating later!",
  "Frosty Fred has treats for tricks, they make him feel like there's Snowplace Like Home!",
  'It feels more like Winter Holiday than Halloween!',
  "Frosty Fred has treats for tricks, they make him feel like there's Snowplace Like Home!",
  "Bark! That's 'Trick-or-Treat' in dog!",
  "Frosty Fred has treats for tricks, they make him feel like there's Snowplace Like Home!",
  'I hope you are enjoying our Halloween fun!',
  "Frosty Fred has treats for tricks, they make him feel like there's Snowplace Like Home!",
  'I like to chase Black Cat Toons!',
  "Frosty Fred has treats for tricks, they make him feel like there's Snowplace Like Home!",
  "There's a snake in my boot!"], ["I'm going to go dig up a treat!", "I'm going to see if Mickey has some treats!", "I'm going to scare Donald!"])
WinterPlutoCChatter = (["Hi, I'm Pluto!",
  "Welcome to the Brrgh, where it's winter all year!",
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %'], ["Eddie could use a good tune, because Snowman's Land is a lonely place for a Yeti!",
  'I chewed on an icicle and got frost-bite!',
  "Eddie could use a good tune, because Snowman's Land is a lonely place for a Yeti!",
  'This is like living in a snow globe!',
  "Eddie could use a good tune, because Snowman's Land is a lonely place for a Yeti!",
  'I wish I was beside a warm fire!',
  "Eddie could use a good tune, because Snowman's Land is a lonely place for a Yeti!",
  'Arf! Arf! I need a scarf!',
  "Eddie could use a good tune, because Snowman's Land is a lonely place for a Yeti!",
  "At least my nose isn't red and glowing!"], ['Have a fun Winter Holiday!', 'Come back any time you want snow!', 'Mickey is taking me caroling!'])
WinterPlutoDChatter = (["Hi, I'm Pluto!",
  "Welcome to the Brrgh, where it's winter all year!",
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %'], ['I chewed on an icicle and got frost-bite!',
  'This is like living in a snow globe!',
  'I wish I was beside a warm fire!',
  'Arf! Arf! I need a scarf!',
  "At least my nose isn't red and glowing!"], ['Have a fun Winter Holiday!', 'Come back any time you want snow!', 'Mickey is taking me caroling!'])
AFMickeyChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ["Welcome to the Gardens! I'm " + Daisy + '!',
  "I'm " + Daisy + ', and I love to garden!',
  "April Toons' Week is the silliest week of the year!",
  "What, you've never seen a duck with mouse ears?",
  "Hi, I'm " + Daisy + '! Quack!',
  "It's tough quacking like a duck!",
  "I'm not feeling like myself today!",
  'Have you heard your Doodle talk yet?',
  'Gravity has taken a holiday at the Estates!'], ["Have a wacky April Toons' Week!", 'Tell Mickey I said hi!'])
AFMinnieChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ['Welcome to ' + lTheBrrrgh + "! I'm " + Pluto + '!',
  "Hi, I'm " + Pluto + "! What's your name?",
  "What, you've never seen a dog with mouse ears?",
  "I'm not feeling like myself today!",
  "Does anyone have a doggie biscuit? I'm hungry!",
  'Bark! My name is ' + Pluto + '!',
  "Isn't this silly?",
  "Don't make me chase you around!",
  "April Toons' Week is the silliest week of the year!",
  'Have you heard your Doodle talk yet?',
  'Gravity has taken a holiday at the Estates!'], ["Have a wacky April Toons' Week!", 'I have to go chase cars now! Bye!'])
AFDaisyChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ['Welcome to ' + lToonIslandCentral + "! I'm " + Mickey + ' Mouse!',
  "Hi, I'm " + Mickey + '! The happiest mouse in Toontown!',
  'If you see ' + Daisy + ', tell her ' + Mickey + ' said hi!',
  "What, you've never seen a mouse with feathers?",
  "Isn't this silly?",
  "I'm not feeling like myself today!",
  "April Toons' Week is the silliest week of the year!",
  'Have you heard your Doodle talk yet?',
  'Gravity has taken a holiday at the Estates!'], ['Bye! Tell them ' + Mickey + ' sent you!', 'If you go to ' + lDaisyGardens + ', say hi to her for me!'])
AFGoofySpeedwayChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ["Welcome to Dreamland! I'm " + Donald + '!',
  "Hello, I'm " + Donald + '! Is it nap time yet?',
  'A duck needs his beauty rest, you know!',
  "What, you've never seen a duck with dog ears?",
  'Gawrsh! I mean -- Quack!',
  'This would make a great race track … um, I mean place to nap!',
  "I'm not feeling like myself today!",
  "April Toons' Week is the silliest week of the year!",
  'Have you heard your Doodle talk yet?',
  'Gravity has taken a holiday at the Estates!'], ['If you see ' + Goofy + ', tell him ' + Donald + ' says hi!', 'Bye, and good night!'])
AFDonaldChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ["Welcome to the Speedway! I'm " + Goofy + '!',
  "I'm " + Goofy + ", and I'm dreaming I'm " + Donald + '!',
  "I've heard of sleep walking, but sleep kart driving?",
  'Gawrsh! It sure is silly being ' + Goofy + '!',
  'How can I watch the races with my eyes closed?',
  'I better grab a nap before my next race!',
  "April Toons' Week is the silliest week of the year!",
  "I'm not feeling like myself today!",
  'Have you heard your Doodle talk yet?',
  'Gravity has taken a holiday at the Estates!'], ["Have a wacky April Toons' Week!", 'I need to work on my karts! Bye!'])
AFDonaldDockChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ["Everybody gets April Toons' Week off but me!",
  "I'm the only one who has to work this week!",
  'I only get time off when I sleep!',
  'All my friends are pretending to be somebody else!',
  'Round and round in this boat, all day long!',
  'I heard Daisy is pretending to be Mickey!',
  "The silliest week of the year, and I'm missing it!",
  'Have you heard your Doodle talk yet?',
  'Gravity has taken a holiday at the Estates!'], ["Have a wacky April Toons' Week!", 'Play a joke on the Cogs for me!'])
AFPlutoChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ["Welcome to Melodyland! I'm " + Minnie + '!',
  'Hi, my name is ' + Minnie + ' Mouse!',
  "I'm as happy as a mouse can be!",
  "What, you've never seen a mouse with dog ears?",
  'I love when ' + Mickey + ' and I go for walks!',
  'What, you never heard a mouse talk before?',
  "April Toons' Week is the silliest week of the year!",
  'Have you heard your Doodle talk yet?',
  'Gravity has taken a holiday at the Estates!'], ["Have a wacky April Toons' Week!", 'If you see ' + Pluto + ', tell him ' + Minnie + ' says hi!'])
AFChipChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ["Hi, I'm " + Dale + '!',
  'How are you today, ' + Chip + '?',
  'I always thought you were ' + Dale + ', ' + Chip + '.',
  "You're sure you're " + Chip + ' and not ' + Dale + ', ' + Chip + '?',
  "April Toons' Week is the silliest week of the year!"], ['Bye from ' + Chip + ' and ' + Dale + '!'])
AFDaleChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ["Hi, I'm " + Chip + '!',
  'Very well ' + Dale + ', thanks!',
  "Nope, I'm " + Chip + ', ' + Dale + '.',
  'Yes, ' + Dale + ", I'm " + Chip + ', not ' + Dale + '.',
  'It sure is, ' + Chip + '! I mean, ' + Dale + '.'], ['Or ' + Dale + ' and ' + Chip + '!'])
CLGoofySpeedwayChatter = (['Welcome to ' + lGoofySpeedway + '.',
  'Hi, my name is ' + Goofy + ". What's yours?",
  "Gawrsh, it's nice to see you %!",
  "Hi there! Pardon my dusty clothes I've been busy fixin' that broken Leaderboard."], ['We better get this Leaderboard working soon, Grand Prix Weekend is coming up!',
  "Does anybody want to buy a slightly used kart? It's only been through the Leaderboard once!",
  'Grand Prix Weekend is coming, better get to practicing.',
  'Grand Prix Weekend will be here on Friday, May 22 through Monday, May 25!',
  "I'm gonna need a ladder to get that kart down.",
  'That Toon really wanted to get on the Leaderboard!',
  'Boy, I saw a terrific race earlier.',
  'Watch out for banana peels on the race track!',
  'Have you upgraded your kart lately?',
  'We just got in some new rims at the kart shop.',
  'Hey, have you seen ' + Donald + '?',
  'If you see my friend ' + Mickey + ', say hi to him for me.',
  "D'oh! I forgot to fix " + Mickey + "'s breakfast!",
  'Gawrsh there sure are a lot of ' + Cogs + ' near ' + lDonaldsDock + '.',
  'At the Brrrgh branch of my Gag Shop, Hypno-Goggles are on sale for only 1 Jellybean!',
  "Goofy's Gag Shops offer the best jokes, tricks, and funnybone-ticklers in all of Toontown!",
  "At Goofy's Gag Shops, every pie in the face is guaranteed to make a laugh or you get your Jellybeans back!"], ['I better go get my kart a new paint job for the upcoming Grand Prix Weekend.',
  "Gosh, I better get workin' on this broken Leaderboard!",
  "Hope I'll see y'all on Grand Prix Weekend! Goodbye!",
  "It's time for a nap. I'm going to Dreamland to dream about winnin' the Grand Prix."])
GPGoofySpeedwayChatter = (['Welcome to ' + lGoofySpeedway + '.',
  'Welcome to Grand Prix Weekend!',
  'Hi, my name is ' + Goofy + ". What's yours?",
  "Gawrsh, it's nice to see you %!"], ['Are you excited about the Grand Prix Weekend?',
  'Grand Prix Weekend really drives up those scores!',
  'Get more tickets by racing practice laps.',
  "Gawrsh, you're a fast racer!",
  'Boy, I saw a terrific race earlier.',
  'Watch out for banana peels on the race track!',
  'Have you upgraded your kart lately?',
  'We just got in some new rims at the kart shop.',
  'Hey, have you seen ' + Donald + '? He said he was gonna come watch the Grand Prix!',
  'If you see my friend ' + Mickey + ", tell him he's missing some great racing!",
  "D'oh! I forgot to fix " + Mickey + "'s breakfast!",
  'Gawrsh there sure are a lot of ' + Cogs + ' near ' + lDonaldsDock + '.',
  'At the Brrrgh branch of my Gag Shop, Hypno-Goggles are on sale for only 1 Jellybean!',
  "Goofy's Gag Shops offer the best jokes, tricks, and funnybone-ticklers in all of Toontown!",
  "At Goofy's Gag Shops, every pie in the face is guaranteed to make a laugh or you get your Jellybeans back!"], ['Good luck in the Grand Prix!',
  "I'm going to catch the next race in the Grand Prix!",
  'Gawrsh I think the next race is about to start!',
  'Gosh, I better go check on the new Leaderboard and make sure it is working right!'])
SillyPhase1Chatter = ["If you haven't seen the Silly Meter, head to Toon Hall!",
 'Toontown is getting sillier by the day!',
 "Cause silly surges in battle to boost Toontown's silly levels!",
 'Objects on the street are starting to animate!',
 'I saw a fire hydrant on Beachball Bouvelard move!']
SillyPhase2Chatter = ['Silly levels are still rising!',
 'The Silly Meter has climbed higher and gotten crazier!',
 'Someone saw a trash can moving on Crow Circle!',
 'A lot of hydrants on Beachball Bouvelard have come alive!',
 'A mailbox on Plankton Path has gone nuts!',
 'Go see the Silly Meter in Toon Hall!',
 'Keep causing those silly surges!']
SillyPhase3Chatter = ['The Cogs hated how silly Toontown was becoming!',
 'Keep a sharp eye out for Cog Invasions!',
 'Cog Invasions have caused the silly levels to drop!',
 'The Silly Meter went down after the Cog Invasions!',
 'Every street of Toontown has animated objects now!',
 'Toontown is sillier than ever!']
SillyPhase4Chatter = ['Fire hydrants make your Squirt Gags squirtier!',
 'Mail Boxes give your Throw Gags a special delivery!',
 'Those crazy Trash Cans can help boost your Toon-up!',
 'Objects on the street can help you in battle!',
 "I just know we'll get the Silly Meter back up soon!",
 'Enjoy the sillier Toontown!']
for chatter in [MickeyChatter,
 DonaldChatter,
 MinnieChatter,
 GoofyChatter]:
    chatter[0].extend(SharedChatterGreetings)
    chatter[1].extend(SharedChatterComments)
    chatter[2].extend(SharedChatterGoodbyes)

BoringTopic = 'Boring'
EmceeDialoguePhase1Topic = 'EmceeDialoguePhase1'
EmceeDialoguePhase2Topic = 'EmceeDialoguePhase2'
EmceeDialoguePhase3Topic = 'EmceeDialoguePhase3'
EmceeDialoguePhase3_5Topic = 'EmceeDialoguePhase3.5'
EmceeDialoguePhase4Topic = 'EmceeDialoguePhase4'
EmceeDialoguePhase5Topic = 'EmceeDialoguePhase5'
EmceeDialoguePhase6Topic = 'EmceeDialoguePhase6'
AprilToonsPhasePreTopTopic = 'AprilToonsPhasePreTopTopic'
AprilToonsPhaseTopTopic = 'AprilToonsPhaseTopTopic'
AprilToonsExtPhaseTopTopic = 'AprilToonsExtPhaseTopTopic'
AprilToonsPhasePostTopTopic = 'AprilToonsPhasePostTopTopic'
ToontownDialogues = {BoringTopic: {(1, 2018): ['Hello Albert', 'It looks like the sillyness levels are rising', 'Yes and dont forget April Toons!'],
               (2, 2019): ['Hello Newton', 'Yes I wonder how much the parties are contributing to all this'],
               (3, 2020): ['Why hello there Albert and Newton', 'Halloween was pretty silly too!']},
 AprilToonsPhasePreTopTopic: {(1, 2020): ['Gadzooks! The Silly Meter has come back to life!',
                                          "It's rising every day, and will reach the top soon!",
                                          'When it does, something silly is sure to happen!',
                                          'So get ready to get ridiculous!']},
 AprilToonsPhaseTopTopic: {(1, 2020): ['The Silly Meter has hit the top!',
                                       'Doodles are talking, Estates are bouncy!',
                                       "There's only one thing to say\xe2\x80\xa6",
                                       'HAPPY APRIL ToonS!']},
 AprilToonsExtPhaseTopTopic: {(1, 2020): ['The Silly Meter has hit the top!', 'Doodles are talking, Estates are bouncy!']},
 AprilToonsPhasePostTopTopic: {(1, 2020): ['April Toons is over!',
                                           "It's time for us to return to our lab.",
                                           'But when things get REALLY crazy again\xe2\x80\xa6',
                                           'The Silly Meter will return!']},
 EmceeDialoguePhase1Topic: {(1, 2020): ['Fellow Toons, this is the Silly Meter!',
                                        "It is tracking Toontown's rising silly levels…",
                                        'Which are causing objects on the street to animate!',
                                        'And YOU can help push these levels higher!',
                                        'Battle Cogs to cause Silly Surges…',
                                        'Make Toontown sillier than ever…',
                                        "And let's watch the world come alive!",
                                        "Now I'll repeat what I said, but only once more."]},
 EmceeDialoguePhase2Topic: {(1, 2020): ['Good Gag work, Toons!',
                                        "You're keeping those silly levels rising…",
                                        'And Toontown is getting sillier every day!',
                                        'Fire hydrants, trash cans, and mailboxes are springing to life…',
                                        'Making the world more animated than ever!',
                                        "You know the Cogs aren't happy about this…",
                                        'But Toons sure are!']},
 EmceeDialoguePhase3Topic: {(1, 2020): ['Gadzooks! The Silly Meter is even crazier than expected!',
                                        'Your Silly Surges are working wonders…',
                                        'And Toontown is getting more animated every day!',
                                        'Keep up the good Gag work…',
                                        'And lets see how silly we can make Toontown!',
                                        "You know the Cogs aren't happy about what's going on…",
                                        'But Toons sure are!']},
 EmceeDialoguePhase3_5Topic: {(1, 2020): ['YOU DID IT ToonS!',
                                          'You brought the streets of Toontown to life!',
                                          'You deserve a reward!',
                                          'Enter the code SILLYMETER in your Shticker Book…',
                                          '…to get a Silly Meter T-Shirt!']},
 EmceeDialoguePhase4Topic: {(1, 2020): ['Attention all Toons!',
                                        'The sudden Cog invasions have been an unhappy event.',
                                        'As a result, silly levels have rapidly fallen…',
                                        'And no new objects are coming to life.',
                                        'But those that have are very thankful…',
                                        "So perhaps they'll find a way to show their appreciation!",
                                        'Stay Tooned!']},
 EmceeDialoguePhase5Topic: {(1, 2020): ['Attention all Toons!',
                                        'The Cog invasions have been an unhappy event.',
                                        'As a result, silly levels have rapidly fallen…',
                                        'And no new objects are coming to life.',
                                        'But those that have are very thankful…',
                                        'And are showing their appreciation by helping in battle!',
                                        'We may hold off the Cogs yet, so keep up the fight!']},
 EmceeDialoguePhase6Topic: {(1, 2020): ['Congratulations Toons!',
                                        'You all succesfully held off the Cog Invasions…',
                                        'With a little help from our newly animated friends…',
                                        'And brought Toontown back to its usual silly self!',
                                        'We hope to get the Silly Meter rising again soon…',
                                        'So in the meantime, keep up the Cog fight…',
                                        'And enjoy the silliest place ever, Toontown!']}}
FriendsListPanelNewFriend = 'New Friend'
FriendsListPanelSecrets = 'True Friend'
FriendsListPanelOnlineFriends = 'ONLINE Toon\nFRIENDS'
FriendsListPanelAllFriends = 'ALL Toon\nFRIENDS'
FriendsListPanelIgnoredFriends = 'IGNORED\nToonS'
FriendsListPanelPets = 'NEARBY\nPETS'
FriendsListPanelPlayers = 'ALL PLAYER\nFRIENDS'
FriendsListPanelOnlinePlayers = 'ONLINE PLAYER\nFRIENDS'
FriendInviterClickToon = 'Click on the Toon you would like to make friends with.\n\n(You have %s friends)'
FriendInviterToon = 'Toon'
FriendInviterThatToon = 'That Toon'
FriendInviterPlayer = 'Player'
FriendInviterThatPlayer = 'That player'
FriendInviterBegin = 'What type of friend would you like to make?'
FriendInviterToonFriendInfo = 'A friend only in Toontown'
FriendInviterPlayerFriendInfo = 'A friend in another game' # Digi……pulse…………?
FriendInviterToonTooMany = 'You have too many Toon friends to add another one now. You will have to remove some Toon friends if you want to make friends with %s. You could also try making player friends them.'
FriendInviterPlayerTooMany = 'You have too many player friends to add another one now. You will have to remove some player friends if you want to make friends with %s. You could also try making Toon friends with them.'
FriendInviterToonAlready = '%s is already your Toon friend.'
FriendInviterPlayerAlready = '%s is already your player friend.'
FriendInviterStopBeingToonFriends = 'Stop being Toon friends'
FriendInviterStopBeingPlayerFriends = 'Stop being player friends'
FriendInviterEndFriendshipToon = 'Are you sure you want to stop being Toon friends with %s?'
FriendInviterEndFriendshipPlayer = 'Are you sure you want to stop being player friends with %s?'
FriendInviterRemainToon = '\n(You will still be Toon friends with %s)'
FriendInviterRemainPlayer = '\n(You will still be player friends with %s)'
DownloadForceAcknowledgeVerbList = ['painted',
 'unpacked',
 'unfolded',
 'drawn',
 'inflated',
 'built']
DownloadForceAcknowledgeMsg = 'Sorry, the %(phase)s area is still being %(verb)s, and will be ready for you in a minute.'
TeaserTop = ''
TeaserBottom = ''
TeaserDefault = ',\nyou need to become a Member.\n\nJoin us!'
TeaserOtherHoods = 'For unlimited adventures in all 6 neighborhoods'
TeaserTypeAName = 'Type in your favorite name for your Toon!'
TeaserSixToons = 'To play more than one Toon'
TeaserClothing = 'To buy items from the Cattlelog \nto customize your Toon'
TeaserCogHQ = 'To access awesome Cog HQs'
TeaserSecretChat = 'To use the True Friends Chat feature'
TeaserSpecies = 'To pick this type of Toon'
TeaserFishing = 'To fish in all 6 neighborhoods'
TeaserGolf = 'To play Toon MiniGolf'
TeaserParties = 'To plan a party'
TeaserSubscribe = 'Subscribe'
TeaserContinue = 'Return To Game'
TeaserEmotions = 'To make your Toon more expressive'
TeaserKarting = 'To access unlimited Kart Racing'
TeaserKartingAccessories = 'To customize your Kart'
TeaserGardening = 'To continue gardening at your Toon Estate'
TeaserHaveFun = 'Have more fun!'
TeaserJoinUs = 'Join us!'
TeaserPlantGags = 'To plant these gags'
TeaserPickGags = 'To pick these gags'
TeaserRestockGags = 'To restock these gags'
TeaserGetGags = 'To get these gags'
TeaserUseGags = 'To use these gags'
TeaserMinigames = TeaserOtherHoods
TeaserQuests = TeaserOtherHoods
TeaserOtherGags = TeaserOtherHoods
TeaserTricks = TeaserOtherHoods
LauncherPhaseNames = {0: 'Initialization',
 1: 'Panda',
 2: 'Engine',
 3: 'Make-A-Toon',
 3.5: 'Toontorial',
 4: 'Playground',
 5: 'Streets',
 5.5: 'Estates',
 6: 'Neighborhoods I',
 7: Cog + ' Buildings',
 8: 'Neighborhoods II',
 9: Sellbot + ' HQ',
 10: Cashbot + ' HQ',
 11: Lawbot + ' HQ',
 12: Bossbot + ' HQ',
 13: 'Parties'}
LauncherProgress = '%(name)s (%(current)s of %(total)s)'
LauncherStartingMessage = "Starting Toon Island: Aftermath… "
LauncherDownloadFile = 'Downloading update for ' + LauncherProgress + '…'
LauncherDownloadFileBytes = 'Downloading update for ' + LauncherProgress + ': %(bytes)s'
LauncherDownloadFilePercent = 'Downloading update for ' + LauncherProgress + ': %(percent)s%%'
LauncherDecompressingFile = 'Decompressing update for ' + LauncherProgress + '…'
LauncherDecompressingPercent = 'Decompressing update for ' + LauncherProgress + ': %(percent)s%%'
LauncherExtractingFile = 'Extracting update for ' + LauncherProgress + '…'
LauncherExtractingPercent = 'Extracting update for ' + LauncherProgress + ': %(percent)s%%'
LauncherPatchingFile = 'Applying update for ' + LauncherProgress + '…'
LauncherPatchingPercent = 'Applying update for ' + LauncherProgress + ': %(percent)s%%'
LauncherConnectProxyAttempt = 'Connecting to Toontown: %s (proxy: %s) attempt: %s'
LauncherConnectAttempt = 'Connecting to Toontown: %s attempt %s'
LauncherDownloadServerFileList = 'Updating Toontown…'
LauncherCreatingDownloadDb = 'Updating Toontown…'
LauncherDownloadClientFileList = 'Updating Toontown…'
LauncherFinishedDownloadDb = 'Updating Toontown… '
LauncherStartingGame = 'Starting Toon Island: Aftermath…'
LauncherRecoverFiles = 'Updating Toontown. Recovering files…'
LauncherCheckUpdates = 'Checking for updates for ' + LauncherProgress
LauncherVerifyPhase = 'Updating Toontown…'
LoadingDownloadWatcherUpdate = 'Loading %s'
AvatarChoiceMakeAToon = 'Make A\nToon'
AvatarChoicePlayThisToon = 'Play\nThis Toon'
AvatarChoiceSubscribersOnly = 'Subscribe'
AvatarChoiceDelete = 'Delete'
AvatarChoiceDeleteConfirm = 'This will delete %s forever.'
AvatarChoiceNameRejected = 'Name\nRejected'
AvatarChoiceNameApproved = 'Name\nApproved!'
AvatarChoiceNameReview = 'Under\nReview'
AvatarChoiceNameYourToon = 'Name\nYour Toon!'
AvatarChoiceDeletePasswordText = 'Careful! This will delete %s forever. To delete this Toon, enter your password.'
AvatarChoiceDeleteConfirmText = 'Careful! This will delete %(name)s forever. If you are sure you want to do this, type "%(confirm)s" and click OK.'
AvatarChoiceDeleteConfirmUserTypes = 'delete'
AvatarChoiceDeletePasswordTitle = 'Delete Toon?'
AvatarChoicePassword = 'Password'
AvatarChoiceDeletePasswordOK = lOK
AvatarChoiceDeletePasswordCancel = lCancel
AvatarChoiceDeleteWrongPassword = 'That password does not seem to match. To delete this Toon, enter your password.'
AvatarChoiceDeleteWrongConfirm = 'You did not type the right thing. To delete %(name)s, type "%(confirm)s" and click OK. Do not type the quotation marks. Click Cancel if you have changed your mind.'
AvatarChooserPickAToon = 'Pick  A  Toon  To  Play'
AvatarChooserQuit = lQuit
DateOfBirthEntryMonths = ['Jan',
 'Feb',
 'Mar',
 'Apr',
 'May',
 'Jun',
 'Jul',
 'Aug',
 'Sep',
 'Oct',
 'Nov',
 'Dec']
DateOfBirthEntryDefaultLabel = 'Date of Birth'
AchievePageTitle = 'Achievements\n(Coming Soon)'
PhotoPageTitle = 'Photo\n(Coming Soon)'
BuildingPageTitle = 'Buildings\n(Coming Soon)'
InventoryPageTitle = 'Gags'
InventoryPageDeleteTitle = 'DELETE GAGS'
InventoryPageTrackFull = 'You have maxed the %s track.'
InventoryPagePluralPoints = 'You will get a new\n%(trackName)s gag when you\nget %(numPoints)s more %(trackName)s points.'
InventoryPageSinglePoint = 'You will get a new\n%(trackName)s gag when you\nget %(numPoints)s more %(trackName)s point.'
InventoryPageNoAccess = 'You do not have access to the %s track yet.'
NPCFriendPageTitle = 'S.O.S. Toons'
PartyDateFormat = '%(mm)s %(dd)d, %(yyyy).4d'
PartyTimeFormat = '%d:%.2d %s'
PartyTimeFormatMeridiemAM = 'AM'
PartyTimeFormatMeridiemPM = 'PM'
PartyCanStart = "It's Party Time, click Start Party in your Shticker Book Hosting page!"
PartyHasStartedAcceptedInvite = '%s party has started! Click the host then "Go To Party" in the Shticker Book Invites page.'
PartyHasStartedNotAcceptedInvite = '%s party has started! You can still go to it by teleporting to the host.'
EventsPageName = 'Events'
EventsPageCalendarTabName = 'Calendar'
EventsPageCalendarTabParty = 'Party'
EventsPageToontownTimeIs = 'TOONTOWN TIME IS'
EventsPageConfirmCancel = 'If you cancel, you will get a %d%% refund. Are you sure you want to cancel your party?'
EventsPageCancelPartyResultOk = 'Your party was cancelled and you got %d Jellybeans back!'
EventsPageCancelPartyResultError = 'Sorry, your party was not cancelled.'
EventsPageCancelPartyAlreadyRefunded = 'Your party was never started. Check your mailbox for your refund!'
EventsPageTooLateToStart = 'Sorry, it is too late to start your party. You can cancel it and plan another one.'
EventsPagePublicPrivateChange = "Changing your party's privacy setting…"
EventsPagePublicPrivateNoGo = "Sorry, you can't change your party's privacy setting right now."
EventsPagePublicPrivateAlreadyStarted = "Sorry, your party has already started, so you can't change your party's privacy setting."
EventsPageHostTabName = 'Hosting'
EventsPageHostTabTitle = 'My Next Party'
EventsPageHostTabTitleNoParties = 'No Parties'
EventsPageHostTabDateTimeLabel = 'You are having a party on %s at %s Toontown Time.'
EventsPageHostingTabNoParty = 'Go to a playground\nParty Gate to plan\nyour own party!'
EventsPageHostTabPublicPrivateLabel = 'This party is:'
EventsPageHostTabToggleToPrivate = 'Private'
EventsPageHostTabToggleToPublic = 'Public'
EventsPageHostingTabGuestListTitle = 'Guests'
EventsPageHostingTabActivityListTitle = 'Activities'
EventsPageHostingTabDecorationsListTitle = 'Decorations'
EventsPageHostingTabPartiesListTitle = 'Hosts'
EventsPageHostTabCancelButton = 'Cancel Party'
EventsPageGoButton = 'Start\nParty!'
EventsPageGoBackButton = 'Party\nNow!'
EventsPageInviteGoButton = 'Go to\nParty!'
EventsPageUnknownToon = 'Unknown Toon'
EventsPageInvitedTabName = 'Invitations'
EventsPageInvitedTabTitle = 'Party Invitations'
EventsPageInvitedTabInvitationListTitle = 'Invitations'
EventsPageInvitedTabActivityListTitle = 'Activities'
EventsPageInvitedTabTime = '%s %s Toontown Time'
EventsPageNewsTabName = 'News'
EventsPageNewsTabTitle = 'News'
EventsPageNewsDownloading = 'Retrieving News…'
EventsPageNewsUnavailable = 'Chip and Dale played with the printing press. News not available.'
EventsPageNewsPaperTitle = 'TOON ISLAND TIMES'
EventsPageNewsLeftSubtitle = 'Still only 1 Jellybean'
EventsPageNewsRightSubtitle = 'Established Toon-thousand nine'
NewsPageName = 'News'
NewsPageImportError = 'Whoops! There is an issue loading the "Toon News … for the Amused!" Please check back later.'
NewsPageDownloadingNewsSubstr = 'Stay Tooned, while we bring you the latest issue of the \n"Toon News … for the Amused!"'
NewsPageDownloadingNews0 = NewsPageDownloadingNewsSubstr + ' %s%% Complete.'
NewsPageDownloadingNews1 = NewsPageDownloadingNewsSubstr + ' %s%% Complete..'
NewsPageDownloadingNews2 = NewsPageDownloadingNewsSubstr + ' %s%% Complete…'
NewsPageErrorDownloadingFile = 'Whoops! Page %s is missing from "Toon News … for the Amused!" Please check back later.'
NewsPageErrorDownloadingFileCanStillRead = 'Whoops! Page %s \nis missing from the "Toon News … for the Amused!" \nTurn the page to continue, while we work to get this page back.'
NewsPageNoIssues = 'Whoops! The "Toon News … for the Amused!" has gone missing! \nStay Tooned … while we work to bring the news back!'
IssueFrameThisWeek = 'this week'
IssueFrameLastWeek = 'last week'
IssueFrameWeeksAgo = '%d weeks ago'
SelectedInvitationInformation = '%s is having a party on %s at %s Toontown Time.'
PartyPlannerNextButton = 'Continue'
PartyPlannerPreviousButton = 'Back'
PartyPlannerWelcomeTitle = 'Toontown Party Planner'
PartyPlannerInstructions = 'Hosting your own party is a lot of fun!\nStart planning with the arrows at the bottom!'
PartyPlannerDateTitle = 'Pick A Day For Your Party'
PartyPlannerTimeTitle = 'Pick A Time For Your Party'
PartyPlannerGuestTitle = 'Choose Your Guests'
PartyPlannerEditorTitle = 'Design Your Party\nPlace Activities and Decorations'
PartyPlannerConfirmTitle = 'Choose Invitations To Send'
PartyPlannerConfirmTitleNoFriends = 'Double Check Your Party'
PartyPlannerTimeToontown = 'Toontown'
PartyPlannerTimeTime = 'Time'
PartyPlannerTimeRecap = 'Party Date and Time'
PartyPlannerPartyNow = 'As Soon As Possible'
PartyPlannerTimeToontownTime = 'Toontown Time:'
PartyPlannerTimeLocalTime = 'Party Local Time : '
PartyPlannerPublicPrivateLabel = 'This party will be:'
PartyPlannerPublicDescription = 'Any Toon\ncan come!'
PartyPlannerPrivateDescription = 'Only\nInvited Toons\ncan come!'
PartyPlannerPublic = 'Public'
PartyPlannerPrivate = 'Private'
PartyPlannerCheckAll = 'Check\nAll'
PartyPlannerUncheckAll = 'Uncheck\nAll'
PartyPlannerDateText = 'Date'
PartyPlannerTimeText = 'Time'
PartyPlannerTTTimeText = 'Toontown Time'
PartyPlannerEditorInstructionsIdle = 'Click on the Party Activity or Decoration you would like to purchase.'
PartyPlannerEditorInstructionsClickedElementActivity = 'Click Buy or Drag the Activity Icon onto the Party Grounds Map'
PartyPlannerEditorInstructionsClickedElementDecoration = 'Click Buy or Drag the Decoration onto the Party Grounds Map'
PartyPlannerEditorInstructionsDraggingActivity = 'Drag the Activity onto the Party Grounds Map.'
PartyPlannerEditorInstructionsDraggingDecoration = 'Drag the Activity onto the Party Grounds Map.'
PartyPlannerEditorInstructionsPartyGrounds = 'Click and Drag items to move them around the Party Grounds Map'
PartyPlannerEditorInstructionsTrash = 'Drag an Activity or Decoration here to remove it.'
PartyPlannerEditorInstructionsNoRoom = 'There is no room to place that activity.'
PartyPlannerEditorInstructionsRemoved = '%(removed)s removed since %(added)s was added.'
PartyPlannerBeans = 'beans'
PartyPlannerTotalCost = 'Total Cost:\n%d beans'
PartyPlannerSoldOut = 'SOLD OUT'
PartyPlannerBuy = 'BUY'
PartyPlannerPaidOnly = 'MEMBERS ONLY'
PartyPlannerPartyGrounds = 'PARTY GROUNDS MAP'
PartyPlannerOkWithGroundsLayout = 'Are you done moving your Party Activities and Decorations around the Party Grounds Map?'
PartyPlannerChooseFutureTime = 'Please choose a time in the future.'
PartyPlannerInviteButton = 'Send Invites'
PartyPlannerInviteButtonNoFriends = 'Plan Party'
PartyPlannerBirthdayTheme = 'Birthday'
PartyPlannerGenericMaleTheme = 'Star'
PartyPlannerGenericFemaleTheme = 'Flower'
PartyPlannerRacingTheme = 'Racing'
PartyPlannerValenToonsTheme = 'ValenToons'
PartyPlannerVictoryPartyTheme = 'Victory'
PartyPlannerWinterPartyTheme = 'Winter'
PartyPlannerGuestName = 'Guest Name'
PartyPlannerClosePlanner = 'Close Planner'
PartyPlannerConfirmationAllOkTitle = 'Congratulations!'
PartyPlannerConfirmationAllOkText = 'Your party has been created and your invitations sent out.\nThanks!'
PartyPlannerConfirmationAllOkTextNoFriends = 'Your party has been created!\nThanks!'
PartyPlannerConfirmationErrorTitle = 'Oops.'
PartyPlannerConfirmationValidationErrorText = 'Sorry, there seems to be a problem\nwith that party.\nPlease go back and try again.'
PartyPlannerConfirmationDatabaseErrorText = "Sorry, I couldn't record all your information.\nPlease try again later.\nDon't worry, no beans were lost."
PartyPlannerConfirmationTooManyText = 'Sorry, you are already hosting a party.\nIf you want to plan another party, please\ncancel your current party.'
PartyPlannerInvitationThemeWhatSentence = 'You are invited to my %s party! %s!'
PartyPlannerInvitationThemeWhatSentenceNoFriends = 'I am hosting a %s party! %s!'
PartyPlannerInvitationThemeWhatActivitiesBeginning = 'It will have '
PartyPlannerInvitationWhoseSentence = '%s Party'
PartyPlannerInvitationTheme = 'Theme'
PartyPlannerInvitationWhenSentence = 'It will be on %s,\nat %s Toontown Time.\nHope you can make it!'
PartyPlannerInvitationWhenSentenceNoFriends = 'It will be on %s,\nat %s Toontown Time.\nToontastic!'
PartyPlannerComingSoon = 'Coming Soon'
PartyPlannerCantBuy = "Can't Buy"
PartyPlannerGenericName = 'Party Planner'
PartyJukeboxOccupied = 'Someone else is using the jukebox. Try again later.'
PartyJukeboxNowPlaying = 'The song you chose is now playing on the jukebox!'
MusicEncntrGeneralBg = 'Encounter With Cogs'
MusicTcSzActivity = 'Toontorial Medley'
MusicTcSz = 'Strolling Along'
MusicCreateAToon = 'The New Toon in Town'
MusicTtTheme = 'The Toontown Theme'
MusicMinigameRace = 'Slow and Steady'
MusicMgPairing = 'Remember Me?'
MusicTcNbrhood = 'Toon Island Central'
MusicMgDiving = 'Treasure Lullaby'
MusicMgCannonGame = 'Fire the Cannons!'
MusicMgTwodgame = 'Running Toon'
MusicMgCogthief = 'Catch That Cog!'
MusicMgTravel = 'Traveling Music'
MusicMgTugOWar = 'Tug-of-War'
MusicMgVine = 'The Jungle Swing'
MusicMgIcegame = 'Slippery Situation'
MusicMgToontag = 'Minigame Medley'
MusicMMatchBg2 = 'Jazzy Minnie'
MusicMgTarget = "Soarin' Over Toontown"
MusicFfSafezone = 'The Cirrus Circus'
MusicDdSz = 'Waddling Way'
MusicMmNbrhood = "Olive Oasis"
MusicGzPlaygolf = "Let's Play Golf!"
MusicGsSz = 'Goofy Speedway'
MusicOzSz = "Acres of Fun"
MusicGsRaceCc = 'Downtown Driving'
MusicGsRaceSs = 'Ready, Set, Go!'
MusicGsRaceRr = 'Route 66'
MusicGzSz = 'The Putt-Putt Polka'
MusicMmSz = 'Dancing in the Streets'
MusicMmSzActivity = 'Here Comes Treble'
MusicDdNbrhood = "Rainbow Rise"
MusicGsKartshop = 'Mr. Goofywrench'
MusicDdSzActivity = 'Sea Shanty'
MusicEncntrGeneralBgIndoor = 'Building Excitement'
MusicTtElevator = 'Going Up?'
MusicEncntrToonWinningIndoor = 'Toons Unite!'
MusicEncntrGeneralSuitWinningIndoor = 'Cog-tastrophe!'
MusicTbNbrhood = 'Cirrus Circus'
MusicDlNbrhood = "Minty Mines"
MusicDlSzActivity = 'Counting Sheep'
MusicDgSz = 'Waltz of the Flowers'
MusicDlSz = 'Sleepwalking'
MusicTbSzActivity = 'Snow Problem'
MusicTbSz = 'Shiver and Shimmy'
MusicDgNbrhood = "Daisy's Garden" # Gracie's Note: Please replace this with the new playground name that replaces Daisy's Garden
MusicEncntrHallOfFame = 'The Hall of Fame'
MusicEncntrSuitHqNbrhood = 'Dollars and Cents'
MusicChqFactBg = 'Cog Factory'
MusicCoghqFinale = 'Triumph of the Toons'
MusicEncntrToonWinning = 'Cashing In!'
MusicEncntrSuitWinning = 'Selling You Short'
MusicEncntrHeadSuitTheme = 'The Big Boss'
MusicLbJurybg = 'Court is in Session'
MusicLbCourtyard = 'Balancing Act'
MusicBossbotCeoV2 = 'Head Honcho'
MusicBossbotFactoryV1 = 'Cog Waltz'
MusicBossbotCeoV1 = 'Bossing You Around'
MusicPartyOriginalTheme = 'Party Time'
MusicPartyPolkaDance = 'Party Polka'
MusicPartySwingDance = 'Party Swing'
MusicPartyWaltzDance = 'Party Waltz'
MusicPartyGenericThemeJazzy = 'Party Jazz'
MusicPartyGenericTheme = 'Party Jingle'
JukeboxAddSong = 'Add\nSong'
JukeboxReplaceSong = 'Replace\nSong'
JukeboxQueueLabel = 'Playing Next:'
JukeboxSongsLabel = 'Pick a Song:'
JukeboxClose = 'Done'
JukeboxCurrentlyPlaying = 'Currently Playing'
JukeboxCurrentlyPlayingNothing = 'Jukebox is paused.'
JukeboxCurrentSongNothing = 'Add a song to the playlist!'
PartyOverWarningNoName = 'The party has ended! Thanks for coming!'
PartyOverWarningWithName = '%s party has ended! Thanks for coming!'
PartyCountdownClockText = 'Time\n\nLeft'
PartyTitleText = '%s Party'
PartyActivityConjunction = ', and'
PartyActivityNameDict = {0: {'generic': 'Jukebox\n20 songs',
     'invite': 'a 20 song Jukebox',
     'editor': 'Jukebox - 20',
     'description': 'Listen to music with your own 20 song jukebox!'},
 1: {'generic': 'Party Cannons',
     'invite': 'Party Cannons',
     'editor': 'Cannons',
     'description': 'Fire yourself out of the cannons and into fun!'},
 2: {'generic': 'Trampoline',
     'invite': 'Trampoline',
     'editor': 'Trampoline',
     'description': 'Collect Jellybeans and bounce the highest!'},
 3: {'generic': 'Party Catch',
     'invite': 'Party Catch',
     'editor': 'Party Catch',
     'description': 'Catch fruit to win beans! Dodge those anvils!'},
 4: {'generic': 'Dance Floor\n10 moves',
     'invite': 'a 10 move Dance Floor',
     'editor': 'Dance Floor - 10',
     'description': 'Show off all 10 of your moves, Toon style!'},
 5: {'generic': 'Party Tug-of-War',
     'invite': 'Party Tug-of-War',
     'editor': 'Tug-of-War',
     'description': 'Up to 4 on 4 Toon tugging craziness!'},
 6: {'generic': 'Party Fireworks',
     'invite': 'Party Fireworks',
     'editor': 'Fireworks',
     'description': 'Launch your very own fireworks show!'},
 7: {'generic': 'Party Clock',
     'invite': 'a Party Clock',
     'editor': 'Party Clock',
     'description': 'Counts down the time left in your party.'},
 8: {'generic': 'Jukebox\n40 songs',
     'invite': 'a 40 song jukebox',
     'editor': 'Jukebox - 40',
     'description': 'Listen to music with your own 40 song jukebox!'},
 9: {'generic': 'Dance Floor\n20 moves',
     'invite': 'a 20 move Dance Floor',
     'editor': 'Dance Floor - 20',
     'description': 'Show off all 20 of your moves, Toon style!'},
 10: {'generic': 'Cog-O-War',
      'invite': 'Cog-O-War',
      'editor': 'Cog-O-War',
      'description': 'The team vs. team game of Cog splatting!'},
 11: {'generic': 'Cog Trampoline',
      'invite': 'Cog Trampoline',
      'editor': 'Cog Trampoline',
      'description': "Jump on a Cog's face!"},
 12: {'generic': 'Present Catch',
      'invite': 'Present Catch',
      'editor': 'Present Catch',
      'description': 'Catch presents to win beans! Dodge those anvils!'},
 13: {'generic': 'Holiday Trampoline',
      'invite': 'Holiday Trampoline',
      'editor': 'Holiday Trampoline',
      'description': 'Jump if you love Winter Holidays!'},
 14: {'generic': 'Holiday Cog-O-War',
      'invite': 'Holiday Cog-O-War',
      'editor': 'Holiday Cog-O-War',
      'description': 'The team vs. team game of Cog splattering!'},
 15: {'generic': 'Dance Floor\n10 moves',
      'invite': 'a 10 move ValenToons Dance Floor',
      'editor': 'Dance Floor - 10',
      'description': 'Get your ValenToon Groove On!'},
 16: {'generic': 'Dance Floor\n20 moves',
      'invite': 'a 20 move ValenToons Dance Floor',
      'editor': 'Dance Floor - 20',
      'description': 'Get your ValenToon Groove On!'},
 17: {'generic': 'Jukebox\n20 songs',
      'invite': 'a 20 song ValenToons Jukebox',
      'editor': 'Jukebox - 20',
      'description': 'Nothing sets the mood like music!'},
 18: {'generic': 'Jukebox\n40 songs',
      'invite': 'a 40 song ValenToons jukebox',
      'editor': 'Jukebox - 40',
      'description': 'Nothing sets the mood like music!'},
 19: {'generic': 'Trampoline',
      'invite': 'ValenToons Trampoline',
      'editor': 'Trampoline',
      'description': "Jump to your heart's content!"}}
PartyDecorationNameDict = {0: {'editor': 'Balloon Anvil',
     'description': 'Try to keep the fun from floating away!'},
 1: {'editor': 'Party Stage',
     'description': 'Balloons, stars, what else could you want?'},
 2: {'editor': 'Party Bow',
     'description': 'Wrap up the fun!'},
 3: {'editor': 'Cake',
     'description': 'Delicious.'},
 4: {'editor': 'Party Castle',
     'description': "A Toon's home is his castle."},
 5: {'editor': 'Gift Pile',
     'description': 'Gifts for every Toon!'},
 6: {'editor': 'Streamer Horn',
     'description': 'This horn is a hoot! Streamers!'},
 7: {'editor': 'Party Gate',
     'description': 'Multi-colored and crazy!'},
 8: {'editor': 'Noise Makers',
     'description': 'Tweeeeet!'},
 9: {'editor': 'Pinwheel',
     'description': 'Colorful twirling for everyone!'},
 10: {'editor': 'Gag Globe',
      'description': 'Gag and star globe designed by Olivea'},
 11: {'editor': 'Bean Banner',
      'description': 'A Jellybean banner designed by Cassidy'},
 12: {'editor': 'Gag Cake',
      'description': 'A Topsy Turvy gag cake designed by Felicia'},
 13: {'editor': "Cupid's Heart",
      'description': 'Ready…Aim…\nValenToons!'},
 14: {'editor': 'Candy Hearts\n Banner',
      'description': "Who doesn't love candy hearts?"},
 15: {'editor': 'Flying Heart',
      'description': 'This heart is getting carried away!'},
 16: {'editor': 'Victory Bandstand',
      'description': 'All our new friends are ready to dance!'},
 17: {'editor': 'Victory Banner',
      'description': 'Not just a normal banner!'},
 18: {'editor': 'Confetti Cannons',
      'description': 'BOOM! Confetti! Fun!'},
 19: {'editor': 'Cog & Doodle',
      'description': "Ouch! That's gotta hurt."},
 20: {'editor': 'Cog Flappy Man',
      'description': 'A Cog full of hot air, what a shock!'},
 21: {'editor': 'Cog Ice Cream',
      'description': 'A Cog looking his best.'},
 22: {'editor': 'CogCicle',
      'description': 'A Cog looking his holiday best.'},
 23: {'editor': 'Holiday Bandstand',
      'description': 'Everyone loves a Holiday Party!'},
 24: {'editor': 'Chilly Cog',
      'description': "Ouch! That's gotta hurt."},
 25: {'editor': 'Snowman',
      'description': "So cool, he's hot!"},
 26: {'editor': 'SnowDoodle',
      'description': 'His only trick is being cold!'},
 27: {'editor': 'ValenToons Anvil',
      'description': "We've got your heart on a string!"}}
ActivityLabel = 'Cost - Activity Name'
PartyDoYouWantToPlan = 'Would you like to plan a new party right now?'
PartyPlannerOnYourWay = 'Have fun planning your party!'
PartyPlannerMaybeNextTime = 'Maybe next time. Have a good day!'
PartyPlannerHostingTooMany = 'You can only host one party at a time, sorry.'
PartyPlannerOnlyPaid = 'Only paid Toons can host a party, sorry.'
PartyPlannerNpcComingSoon = 'Parties are coming soon! Try again later.'
PartyPlannerNpcMinCost = 'It costs a minimum of %d Jellybeans to plan a party.'
PartyHatPublicPartyChoose = 'Do you want to go to the 1st available public party?'
PartyGateTitle = 'Public Parties'
PartyGateGoToParty = 'Go to\nParty!'
PartyGatePartiesListTitle = 'Hosts'
PartyGatesPartiesListToons = 'Toons'
PartyGatesPartiesListActivities = 'Activities'
PartyGatesPartiesListMinLeft = 'Minutes Left'
PartyGateLeftSign = 'Come On In!'
PartyGateRightSign = 'Public Parties Here!'
PartyGatePartyUnavailable = 'Sorry. That party is no longer available.'
PartyGatePartyFull = 'Sorry. That party is full.'
PartyGateInstructions = 'Click on a host, then click on "Go to Party"'
PartyActivityWaitingForOtherPlayers = 'Waiting for other players to join the party game…'
PartyActivityPleaseWait = 'Please wait…'
DefaultPartyActivityTitle = 'Party Game Title'
DefaultPartyActivityInstructions = 'PartyGame Instructions'
PartyOnlyHostLeverPull = 'Only the host can start this activity. Sorry.'
PartyActivityDefaultJoinDeny = 'You cannot join this activity right now. Sorry.'
PartyActivityDefaultExitDeny = 'You cannot leave this activity right now. Sorry.'
PartyJellybeanRewardOK = 'OK'
PartyCatchActivityTitle = 'Party Catch Activity'
PartyCatchActivityInstructions = "Catch as many pieces of fruit as you can. Try not to 'catch' any %(badThing)s!"
PartyCatchActivityFinishPerfect = 'PERFECT GAME!'
PartyCatchActivityFinish = 'Good Game!'
PartyCatchActivityExit = 'EXIT'
PartyCatchActivityApples = 'apples'
PartyCatchActivityOranges = 'oranges'
PartyCatchActivityPears = 'pears'
PartyCatchActivityCoconuts = 'coconuts'
PartyCatchActivityWatermelons = 'watermelons'
PartyCatchActivityPineapples = 'pineapples'
PartyCatchActivityAnvils = 'anvils'
PartyCatchStarted = 'The game has started. Go play it.'
PartyCatchCannotStart = 'The game could not start right now.'
PartyCatchRewardMessage = 'Pieces of fruit caught: %s\n\nJellybeans earned: %d'
WinterPartyCatchActivityInstructions = "Catch as many presents as you can. Try not to 'catch' any %(badThing)s!"
WinterPartyCatchRewardMessage = 'Presents caught: %s\n\nJellybeans earned: %s'
PartyDanceActivityTitle = 'Party Dance Floor'
PartyDanceActivityInstructions = 'Combine 3 or more ARROW KEY patterns to do dance moves! There are 10 dance moves available. Can you find them all?'
PartyDanceActivity20Title = 'Party Dance Floor'
PartyDanceActivity20Instructions = 'Combine 3 or more ARROW KEY patterns to do dance moves! There are 20 dance moves available. Can you find them all?'
DanceAnimRight = 'Right'
DanceAnimReelNeutral = 'The Fishertoon'
DanceAnimConked = 'The Headbob'
DanceAnimHappyDance = 'The Happy Dance'
DanceAnimConfused = 'Very Dizzy'
DanceAnimWalk = 'Walking on the Moon'
DanceAnimJump = 'The Jump!'
DanceAnimFirehose = 'The Firetoon'
DanceAnimShrug = 'Who Knows?'
DanceAnimSlipForward = 'The Fall'
DanceAnimSadWalk = 'Tired'
DanceAnimWave = 'Hello Goodbye'
DanceAnimStruggle = 'The Shuffle Hop'
DanceAnimRunningJump = 'The Running Toon'
DanceAnimSlipBackward = 'The Backfall'
DanceAnimDown = 'Down'
DanceAnimUp = 'Up'
DanceAnimGoodPutt = 'The Putt'
DanceAnimVictory = 'The Victory Dance'
DanceAnimPush = 'The MimeToon'
DanceAnimAngry = "Rock n' Roll"
DanceAnimLeft = 'Left'
PartyCannonActivityTitle = 'Party Cannons'
PartyCannonActivityInstructions = 'Hit the clouds to change their color and bounce in the air! While IN THE AIR, you can USE THE ARROW KEYS to GLIDE.'
PartyCannonResults = 'You collected %d jelly beans!\n\nNumber of Clouds Hit: %d'
FireworksActivityInstructions = 'Hit the "Page Up" key to see better.'
FireworksActivityBeginning = 'Party fireworks are about to start! Enjoy the show!'
FireworksActivityEnding = 'Hope you enjoyed the show!'
PartyFireworksAlreadyActive = 'The fireworks show has already started.'
PartyFireworksAlreadyDone = 'The fireworks show is over.'
PartyTrampolineJellybeanTitle = 'Jelly Beans Trampoline'
PartyTrampolineTricksTitle = 'Tricks Trampoline'
PartyTrampolineActivityInstructions = 'Use the Control key to jump.\n\nJump when your Toon is at its lowest point on the trampoline to jump higher.'
PartyTrampolineActivityOccupied = 'Trampoline in use.'
PartyTrampolineQuitEarlyButton = 'Hop Off'
PartyTrampolineBeanResults = 'You collected %d jelly beans.'
PartyTrampolineBonusBeanResults = 'You collected %d jelly beans, plus %d more for getting the Big Bean.'
PartyTrampolineTopHeightResults = 'Your top height was %d ft.'
PartyTrampolineTimesUp = "Time's Up"
PartyTrampolineReady = 'Ready…'
PartyTrampolineGo = 'Go!'
PartyTrampolineBestHeight = 'Best Height So Far:\n%s\n%d ft'
PartyTrampolineNoHeightYet = 'How high\ncan you jump?'
PartyTrampolineGetHeight = '%d ft'
PartyTeamActivityForMorePlural = 's'
PartyTeamActivityForMore = 'Waiting for %d player%s\non each side…'
PartyTeamActivityForMoreWithBalance = 'Waiting for %d more player%s…'
PartyTeamActivityWaitingForOtherPlayers = 'Waiting for other players…'
PartyTeamActivityWaitingToStart = 'Starting in…'
PartyTeamActivityExitButton = 'Hop Off'
PartyTeamActivitySwitchTeamsButton = 'Switch\nTeams'
PartyTeamActivityWins = '%s team wins!'
PartyTeamActivityLocalAvatarTeamWins = 'Your team won!'
PartyTeamActivityGameTie = "It's a tie!"
PartyTeamActivityJoinDenied = "Sorry, you can't join %s at this time."
PartyTeamActivityExitDenied = 'Sorry, you are unable to leave %s at this time.'
PartyTeamActivitySwitchDenied = "Sorry, you cant's switch teams at this time."
PartyTeamActivityTeamFull = 'Sorry, that team is already full!'
PartyTeamActivityRewardMessage = 'You got %d Jellybeans. Good job!'
PartyCogTeams = ('Blue', 'Orange')
PartyCogRewardMessage = 'Your Score: %d\n'
PartyCogRewardBonus = '\nYou got %d additional Jellybean%s because your team won!'
PartyCogJellybeanPlural = 's'
PartyCogsignNote = 'HI-SCORE\n%s\n%d'
PartyCogTitle = 'Cog-O-War'
PartyCogInstructions = 'Throw pies at Cogs to push them away from your team. ' + "When time's up, the team with most Cogs on the other side wins!" + '\n\nThrow with the CONTROL KEY. Move with the ARROW KEYS.'
PartyCogDistance = '%d ft'
PartyCogTimeUp = "Time's up!"
PartyCogGuiScoreLabel = 'SCORE'
PartyCogGuiPowerLabel = 'POWER'
PartyCogGuiSpamWarning = 'Hold CONTROL for more power!'
PartyCogBalanceBar = 'BALANCE'
PartyTugOfWarReady = 'Ready…'
PartyTugOfWarGo = 'GO!'
PartyTugOfWarGameEnd = 'Good game!'
PartyTugOfWarTitle = 'Party Tug-of-War'
CalendarShowAll = 'Show All'
CalendarShowOnlyHolidays = 'Show Only Holidays'
CalendarShowOnlyParties = 'Show Only Parties'
CalendarEndsAt = 'Ends at '
CalendarStartedOn = 'Started on '
CalendarEndDash = 'End-'
CalendarEndOf = 'End of '
CalendarPartyGetReady = 'Get ready!'
CalendarPartyGo = 'Go party!'
CalendarPartyFinished = "It's over…"
CalendarPartyCancelled = 'Cancelled.'
CalendarPartyNeverStarted = 'Never Started.'
NPCFriendPanelRemaining = '%d Remaining'
MapPageTitle = 'Map'
MapPageBackToPlayground = 'Back to Playground'
MapPageBackToCogHQ = 'Back to Cog Headquarters'
MapPageGoHome = 'Go Home'
MapPageYouAreHere = 'You are in: %s\n%s'
MapPageYouAreAtHome = 'You are at\nyour estate'
MapPageYouAreAtSomeonesHome = 'You are at %s estate'
MapPageGoTo = 'Go To\n%s'
OptionsPageTitle = 'Options'
OptionsTabTitle = 'Options\n& Codes'
OptionsPagePurchase = 'Subscribe'
OptionsPageLogout = 'Logout'
OptionsPageExitToontown = 'Exit Toontown'
OptionsPageMusicOnLabel = 'Music is on.'
OptionsPageMusicOffLabel = 'Music is off.'
OptionsPageSFXOnLabel = 'Sound Effects are on.'
OptionsPageSFXOffLabel = 'Sound Effects are off.'
OptionsPageToonChatSoundsOnLabel = '   Type Chat Sounds are on.'
OptionsPageToonChatSoundsOffLabel = '   Type Chat Sounds are off.'
OptionsPageFriendsEnabledLabel = 'Accepting new friend requests.'
OptionsPageFriendsDisabledLabel = 'Not accepting friend requests.'
OptionsPageWhisperEnabledLabel = 'Allowing whispers from anyone.'
OptionsPageWhisperDisabledLabel = 'Allowing whispers from friends only.'
OptionsPageSpeedChatStyleLabel = 'SpeedChat Color'
OptionsPageDisplayWindowed = 'windowed'
OptionsPageDisplayEmbedded = 'In the browser'
OptionsPageSelect = 'Select'
OptionsPageToggleOn = 'Turn On'
OptionsPageToggleOff = 'Turn Off'
OptionsPageChange = 'Change'
OptionsPageDisplaySettings = 'Display: %(screensize)s, %(api)s'
OptionsPageDisplaySettingsNoApi = 'Display: %(screensize)s'
OptionsPageExitConfirm = 'Exit Toontown?'
DisplaySettingsTitle = 'Display Settings'
DisplaySettingsIntro = 'The following settings are used to configure the way Toontown is displayed on your computer. It is probably not necessary to adjust these unless you are experiencing a problem.'
DisplaySettingsIntroSimple = 'You may adjust the screen resolution to a higher value to improve the clarity of text and graphics in Toontown, but depending on your graphics card, some higher values may make the game run less smoothly or may not work at all.'
DisplaySettingsApi = 'Graphics API:'
DisplaySettingsResolution = 'Resolution:'
DisplaySettingsWindowed = 'In a window'
DisplaySettingsFullscreen = 'Full screen'
DisplaySettingsEmbedded = 'In the browser'
DisplaySettingsApply = 'Apply'
DisplaySettingsCancel = lCancel
DisplaySettingsApplyWarning = 'When you press OK, the display settings will change. If the new configuration does not display properly on your computer, the display will automatically return to its original configuration after %s seconds.'
DisplaySettingsAccept = 'Press OK to keep the new settings, or Cancel to revert. If you do not press anything, the settings will automatically revert back in %s seconds.'
DisplaySettingsRevertUser = 'Your previous display settings have been restored.'
DisplaySettingsRevertFailed = 'The selected display settings do not work on your computer. Your previous display settings have been restored.'
OptionsPageCodesTab = 'Enter Code'
CdrPageTitle = 'Enter a Code'
CdrInstructions = 'Enter your code to receive a special item in your mailbox.'
CdrResultSuccess = 'Congratulations! Check your mailbox to claim your item!'
CdrResultInvalidCode = "You've entered an invalid code. Please check the code and try again."
CdrResultExpiredCode = "We're sorry. This code has expired."
CdrResultUnknownError = "We're sorry. This code cannot be applied to your Toon."
CdrResultMailboxFull = 'Your mailbox is full. Please remove an item, then enter your code again.'
CdrResultAlreadyInMailbox = "You've already received this item. Check your mailbox to confirm."
CdrResultAlreadyInQueue = 'Your item is on its way. Check your mailbox in a few minutes to receive it.'
CdrResultAlreadyInCloset = "You've already received this item. Check your closet to confirm."
CdrResultAlreadyBeingWorn = "You've already received this item, and you are wearing it!"
CdrResultAlreadyReceived = "You've already received this item."
CdrResultTooManyFails = "We're sorry. You've tried to enter an incorrect code too many times. Please try again after some time."
CdrResultServiceUnavailable = "We're sorry. This feature is temporarily unavailable. Please try again during your next login."
TrackPageTitle = 'Gag Track Training'
TrackPageShortTitle = 'Gag Training'
TrackPageSubtitle = 'Complete ToonTasks to learn how to use new gags!'
TrackPageTraining = 'You are training to use %s gags.\nWhen you complete all 16 tasks you\nwill be able to use %s gags in battle.'
TrackPageClear = 'You are not training any Gag Tracks now.'
TrackPageFilmTitle = '%s\nTraining\nFilm'
TrackPageDone = 'FIN'
QuestPageToonTasks = 'ToonTasks'
QuestPageChoose = 'Choose'
QuestPageLocked = 'Locked'
QuestPageDestination = '%s\n%s\n%s'
QuestPageNameAndDestination = '%s\n%s\n%s\n%s'
QuestPosterHQOfficer = lHQOfficerM
QuestPosterHQBuildingName = lToonHQ
QuestPosterHQStreetName = 'Any Street'
QuestPosterHQLocationName = 'Any Neighborhood'
QuestPosterTailor = 'Tailor'
QuestPosterTailorBuildingName = 'Clothing Store'
QuestPosterTailorStreetName = 'Any Playground'
QuestPosterTailorLocationName = 'Any Neighborhood'
QuestPosterPlayground = 'In the Playground'
QuestPosterAtHome = 'At your home'
QuestPosterInHome = 'In your home'
QuestPosterOnPhone = 'On your phone'
QuestPosterEstate = 'At your estate'
QuestPosterAnywhere = 'Anywhere'
QuestPosterAuxTo = 'to:'
QuestPosterAuxFrom = 'from:'
QuestPosterAuxFor = 'for:'
QuestPosterAuxOr = 'or:'
QuestPosterAuxReturnTo = 'Return to:'
QuestPosterLocationIn = ' in '
QuestPosterLocationOn = ' in '
QuestPosterFun = 'Just for fun!'
QuestPosterFishing = 'GO FISHING'
QuestPosterComplete = 'COMPLETE'
QuestPosterConfirmDelete = 'Are you sure you want to delete this ToonTask?'
QuestPosterDeleteBtn = 'Delete'
QuestPosterDialogYes = 'Delete'
QuestPosterDialogNo = 'Cancel'
ShardPageTitle = 'Districts'
ShardPageHelpIntro = 'Each District is a copy of the Toontown world.'
ShardPageHelpWhere = '  You are currently in the "%s" District.'
ShardPageHelpWelcomeValley = '  You are currently in the "Welcome Valley" District, within "%s".'
ShardPageHelpMove = '  To move to a new District, click on its name.'
ShardPagePopulationTotal = 'Total Toontown Population:\n%d'
ShardPageScrollTitle = 'Name            Population'
ShardPageLow = 'Quiet'
ShardPageMed = 'Ideal'
ShardPageHigh = 'Full'
ShardPageChoiceReject = 'Sorry, that district is full. Please try another one.'
SuitPageTitle = 'Cog Gallery'
SuitPageMystery = DialogQuestion + DialogQuestion + DialogQuestion
SuitPageQuota = '%s of %s'
SuitPageCogRadar = '%s present'
SuitPageBuildingRadarS = '%s building'
SuitPageBuildingRadarP = '%s buildings'
DisguisePageTitle = Cog + ' Disguise'
DisguisePageMeritAlert = 'Ready for\npromotion!'
DisguisePageCogLevel = 'Level %s'
DisguisePageMeritFull = 'Full'
FishPageTitle = 'Fishing'
FishPageTitleTank = 'Fish Bucket'
FishPageTitleCollection = 'Fish Album'
FishPageTitleTrophy = 'Fishing Trophies'
FishPageWeightStr = 'Weight: '
FishPageWeightLargeS = '%d lb. '
FishPageWeightLargeP = '%d lbs. '
FishPageWeightSmallS = '%d oz.'
FishPageWeightSmallP = '%d oz.'
FishPageWeightConversion = 16
FishPageValueS = 'Value: %d Jellybean'
FishPageValueP = 'Value: %d Jellybeans'
FishPageCollectedTotal = 'Fish Species Collected: %d of %d'
FishPageRodInfo = '%s Rod\n%d - %d Pounds'
FishPageTankTab = 'Bucket'
FishPageCollectionTab = 'Album'
FishPageTrophyTab = 'Trophies'
FishPickerTotalValue = 'Bucket: %s / %s\nValue: %d Jellybeans'
UnknownFish = '???'
FishingRod = '%s Rod'
FishingRodNameDict = {0: 'Twig',
 1: 'Bamboo',
 2: 'Hardwood',
 3: 'Steel',
 4: 'Gold'}
FishTrophyNameDict = {0: 'Guppy',
 1: 'Minnow',
 2: 'Fish',
 3: 'Flying Fish',
 4: 'Shark',
 5: 'Swordfish',
 6: 'Killer Whale'}
GardenPageTitle = 'Gardening'
GardenPageTitleBasket = 'Flower Basket'
GardenPageTitleCollection = 'Flower Album'
GardenPageTitleTrophy = 'Gardening Trophies'
GardenPageTitleSpecials = 'Gardening Specials'
GardenPageBasketTab = 'Basket'
GardenPageCollectionTab = 'Album'
GardenPageTrophyTab = 'Trophies'
GardenPageSpecialsTab = 'Specials'
GardenPageCollectedTotal = 'Flower Varieties Collected: %d of %d'
GardenPageValueS = 'Value: %d Jellybean'
GardenPageValueP = 'Value: %d Jellybeans'
FlowerPickerTotalValue = 'Basket: %s / %s\nValue: %d Jellybeans'
GardenPageShovelInfo = '%s Shovel: %d / %d\n'
GardenPageWateringCanInfo = '%s Watering Can: %d / %d'
FlowerPageWeightConversion = 1
FlowerPageWeightLargeP = 'Large P'
FlowerPageWeightLargeS = 'LargeS '
FlowerPageWeightSmallP = 'SmallP '
FlowerPageWeightSmallS = 'SmallS '
FlowerPageWeightStr = 'Weight: %s'
KartPageTitle = 'Karts'
KartPageTitleCustomize = 'Kart Customizer'
KartPageTitleRecords = 'Personal Best Records'
KartPageTitleTrophy = 'Racing Trophies'
KartPageCustomizeTab = 'Customize'
KartPageRecordsTab = 'Records'
KartPageTrophyTab = 'Trophy'
KartPageTrophyDetail = 'Trophy %s : %s'
KartPageTickets = 'Tickets : '
KartPageConfirmDelete = 'Delete Accessory?'
KartShtikerDelete = 'Delete'
KartShtikerSelect = 'Select a Category'
KartShtikerNoAccessories = 'No Accessories Owned'
KartShtikerBodyColors = 'Kart Colors'
KartShtikerAccColors = 'Accessory Colors'
KartShtikerEngineBlocks = 'Hood Accessories'
KartShtikerSpoilers = 'Trunk Accessories'
KartShtikerFrontWheelWells = 'Front Wheel Accessories'
KartShtikerBackWheelWells = 'Back Wheel Accessories'
KartShtikerRims = 'Rim Accessories'
KartShtikerDecals = 'Decal Accessories'
KartShtikerBodyColor = 'Kart Color'
KartShtikerAccColor = 'Accessory Color'
KartShtikerEngineBlock = 'Hood'
KartShtikerSpoiler = 'Trunk'
KartShtikerFrontWheelWell = 'Front Wheel'
KartShtikerBackWheelWell = 'Back Wheel'
KartShtikerRim = 'Rim'
KartShtikerDecal = 'Decal'
KartShtikerDefault = 'Default %s'
KartShtikerNo = 'No %s Accessory'
QuestChoiceGuiCancel = lCancel
TrackChoiceGuiChoose = 'Choose'
TrackChoiceGuiCancel = lCancel
TrackChoiceGuiHEAL = 'Toonup lets you heal other Toons in battle.'
TrackChoiceGuiTRAP = 'Traps are powerful gags that must be used with Lure.'
TrackChoiceGuiLURE = 'Use Lure to stun Cogs or draw them into traps.'
TrackChoiceGuiSOUND = 'Sound gags affect all Cogs, but are not very powerful.'
TrackChoiceGuiDROP = 'Drop gags do lots of damage, but are not very accurate.'
EmotePageTitle = 'Expressions / Emotions'
EmotePageDance = 'You have built the following dance sequence:'
EmoteJump = 'Jump'
EmoteDance = 'Dance'
EmoteHappy = 'Happy'
EmoteSad = 'Sad'
EmoteAnnoyed = 'Annoyed'
EmoteSleep = 'Sleepy'
TIPPageTitle = 'TIP'
SuitBaseNameWithLevel = '%(name)s\n%(dept)s\nLevel %(level)s'
HealthForceAcknowledgeMessage = 'You cannot leave the playground until your Laff meter is smiling!'
InventoryTotalGags = 'Total gags\n%d / %d'
InventroyPinkSlips = '%s Pink Slips'
InventroyPinkSlip = '1 Pink Slip'
InventoryDelete = 'DELETE'
InventoryDone = 'DONE'
InventoryDeleteHelp = 'Click on a gag to DELETE it.'
InventorySkillCredit = 'Skill credit: %s'
InventorySkillCreditNone = 'Skill credit: None'
InventoryDetailAmount = '%(numItems)s / %(maxItems)s'
InventoryDetailData = 'Accuracy: %(accuracy)s\n%(damageString)s: %(damage)d%(bonus)s\n%(singleOrGroup)s'
InventoryTrackExp = '%(curExp)s / %(nextExp)s'
InventoryUberTrackExp = '%(nextExp)s to Go!'
InventoryGuestExp = 'Guest Limit'
GuestLostExp = 'Over Guest Limit'
InventoryAffectsOneCog = 'Affects: One ' + Cog
InventoryAffectsOneToon = 'Affects: One Toon'
InventoryAffectsAllToons = 'Affects: All Toons'
InventoryAffectsAllCogs = 'Affects: All ' + Cogs
InventoryHealString = 'Toon-up'
InventoryDamageString = 'Damage'
InventoryBattleMenu = 'BATTLE MENU'
InventoryRun = 'RUN'
InventorySOS = 'S.O.S'
InventoryPass = 'PASS'
InventoryFire = 'FIRE'
InventoryClickToAttack = 'Click a\ngag to\nattack'
InventoryDamageBonus = '(+%d)'
NPCForceAcknowledgeMessage = "You must ride the trolley before leaving.\n\n\n\n\n\n\n\n\nYou can find the trolley next to Goofy's Gag Shop."
NPCForceAcknowledgeMessage2 = 'You must return to Toon Headquarters before leaving.\n\n\n\n\n\n\n\n\n\nToon Headquarters is located near the center of the playground.'
NPCForceAcknowledgeMessage3 = "Remember to ride the trolley.\n\n\n\n\n\n\n\nYou can find the trolley next to Goofy's Gag Shop."
NPCForceAcknowledgeMessage4 = 'Congratulations! You found and rode the trolley!\n\n\n\n\n\n\n\n\n\nNow report back to Toon Headquarters.'
NPCForceAcknowledgeMessage5 = "Don't forget your ToonTask!\n\n\n\n\n\n\n\n\n\n\nYou can find Cogs to defeat on the other side of tunnels like this."
NPCForceAcknowledgeMessage6 = 'Great job defeating those Cogs!\n\n\n\n\n\n\n\n\nHead back to Toon Headquarters as soon as possible.'
NPCForceAcknowledgeMessage7Retro = "Don't forget to make a friend!\n\n\n\n\n\n\nClick on another player and use the New Friend button."
NPCForceAcknowledgeMessage8Retro = 'Great! You made a new friend!\n\n\n\n\n\n\n\n\nYou should go back at Toon Headquarters now.'
NPCForceAcknowledgeMessage9 = 'Good job using the phone!\n\n\n\n\n\n\n\n\nReturn to Toon Headquarters to claim your reward.'
NPCForceAcknowledgeMessage7 = "You are a cheater!\n\n\n\n\n\n\nHey! Cut it out! You might see something you're not supposed to!"
NPCForceAcknowledgeMessage8 = '\n\n\nAnd now I see\nWith eyes serene\nThe very heart\nOf the machine'
ToonSleepString = '. . . ZZZ . . .'
MovieTutorialReward1 = 'You received 1 Throw point! When you get 10, you will get a new gag!'
MovieTutorialReward2 = 'You received 1 Squirt point! When you get 10, you will get a new gag!'
MovieTutorialReward3 = "Thanks for the help, I really needed it!"
MovieTutorialReward4 = "Head over to the Toon HQ. They may need your help."
MovieTutorialReward5 = "I fear that Cog was only just the beginning."
BattleGlobalTracks = ['toon-up',
 'trap',
 'lure',
 'sound',
 'throw',
 'squirt',
 'drop']
BattleGlobalNPCTracks = ['Restock', 'Toons Hit', 'Cogs Miss']
BattleGlobalAvPropStrings = (('Feather',
  'Megaphone',
  'Lipstick',
  'Bamboo Cane',
  'Pixie Dust',
  'Juggling Balls',
  'High Dive'),
 ('Banana Peel',
  'Rake',
  'Marbles',
  'Quicksand',
  'Trapdoor',
  'TNT',
  'Railroad'),
 ('$1 bill',
  'Small Magnet',
  '$5 bill',
  'Big Magnet',
  '$10 bill',
  'Hypno-goggles',
  'Presentation'),
 ('Bike Horn',
  'Whistle',
  'Bugle',
  'Aoogah',
  'Elephant Trunk',
  'Foghorn',
  'Opera Singer'),
 ('Cupcake',
  'Fruit Pie Slice',
  'Cream Pie Slice',
  'Whole Fruit Pie',
  'Whole Cream Pie',
  'Birthday Cake',
  'Wedding Cake'),
 ('Squirting Flower',
  'Glass of Water',
  'Squirt Gun',
  'Seltzer Bottle',
  'Fire Hose',
  'Storm Cloud',
  'Geyser'),
 ('Flower Pot',
  'Sandbag',
  'Anvil',
  'Big Weight',
  'Safe',
  'Grand Piano',
  'Toontanic'))
BattleGlobalAvPropStringsSingular = (('a Feather',
  'a Megaphone',
  'a Lipstick',
  'a Bamboo Cane',
  'a Pixie Dust',
  'a set of Juggling Balls',
  'a High Dive'),
 ('a Banana Peel',
  'a Rake',
  'a set of Marbles',
  'a patch of Quicksand',
  'a Trapdoor',
  'a TNT',
  'a Railroad'),
 ('a $1 bill',
  'a Small Magnet',
  'a $5 bill',
  'a Big Magnet',
  'a $10 bill',
  'a pair of Hypno-goggles',
  'a Presentation'),
 ('a Bike Horn',
  'a Whistle',
  'a Bugle',
  'an Aoogah',
  'an Elephant Trunk',
  'a Foghorn',
  'an Opera Singer'),
 ('a Cupcake',
  'a Fruit Pie Slice',
  'a Cream Pie Slice',
  'a Whole Fruit Pie',
  'a Whole Cream Pie',
  'a Birthday Cake',
  'a Wedding Cake'),
 ('a Squirting Flower',
  'a Glass of Water',
  'a Squirt Gun',
  'a Seltzer Bottle',
  'a Fire Hose',
  'a Storm Cloud',
  'a Geyser'),
 ('a Flower Pot',
  'a Sandbag',
  'an Anvil',
  'a Big Weight',
  'a Safe',
  'a Grand Piano',
  'the Toontanic'))
BattleGlobalAvPropStringsPlural = (('Feathers',
  'Megaphones',
  'Lipsticks',
  'Bamboo Canes',
  'Pixie Dusts',
  'sets of Juggling Balls',
  'High Dives'),
 ('Banana Peels',
  'Rakes',
  'sets of Marbles',
  'patches of Quicksand',
  'Trapdoors',
  'TNTs',
  'Railroads'),
 ('$1 bills',
  'Small Magnets',
  '$5 bills',
  'Big Magnets',
  '$10 bills',
  'pairs of Hypno-goggles',
  'Presentations'),
 ('Bike Horns',
  'Whistles',
  'Bugles',
  'Aoogahs',
  'Elephant Trunks',
  'Foghorns',
  'Opera Singers'),
 ('Cupcakes',
  'Fruit Pie Slices',
  'Cream Pie Slices',
  'Whole Fruit Pies',
  'Whole Cream Pies',
  'Birthday Cakes',
  'Wedding cakes'),
 ('Squirting Flowers',
  'Glasses of Water',
  'Squirt Guns',
  'Seltzer Bottles',
  'Fire Hoses',
  'Storm Clouds',
  'Geysers'),
 ('Flower Pots',
  'Sandbags',
  'Anvils',
  'Big Weights',
  'Safes',
  'Grand Pianos',
  'Oceanliners'))
BattleGlobalAvTrackAccStrings = ('70%',
 '100%',
 '50%',
 '95%',
 '75%',
 '95%',
 '50%')
BattleGlobalLureAccLow = '50%'
BattleGlobalLureAccLow2 = '60%'
BattleGlobalLureAccMedium = '70%'
BattleGlobalLureAccHigh = '95%'
BattleGlobalLureTrackBonus = ' (+10%)'
AttackMissed = 'MISSED'
NPCCallButtonLabel = 'CALL'
LoaderLabel = 'Initializing'
HeadingToHood = '%(hood)s'
HeadingToYourEstate = 'The Estate'
HeadingToEstate = "%s's Estate"
HeadingToFriend = "%s's Friend's Estate"
HeadingToPlayground = 'The Playground'
HeadingToStreet = '%(street)s'
TownBattleRun = 'Run all the way back to the playground?'
TownBattleChooseAvatarToonTitle = 'WHICH Toon?'
TownBattleChooseAvatarCogTitle = 'WHICH ' + Cog.upper() + '?'
TownBattleChooseAvatarBack = 'BACK'
FireCogTitle = 'PINK SLIPS LEFT:%s\nFIRE WHICH Cog?'
FireCogLowTitle = 'PINK SLIPS LEFT:%s\nNOT ENOUGH SLIPS!'
TownBattleSOSNoFriends = 'No friends to call!'
TownBattleSOSWhichFriend = 'Call which friend?'
TownBattleSOSNPCFriends = 'Rescued Toons'
TownBattleSOSBack = 'BACK'
TownBattleToonSOS = 'S.O.S.'
TownBattleToonFire = 'Fire'
TownBattleUndecided = '?'
TownBattleHealthText = '%(hitPoints)s/%(maxHit)s'
TownBattleWaitTitle = 'Waiting for\nother players…'
TownSoloBattleWaitTitle = 'Please wait…'
TownBattleWaitBack = 'BACK'
TownBattleSOSPetSearchTitle = 'Searching for doodle\n%s…'
TownBattleSOSPetInfoTitle = '%s is %s'
TownBattleSOSPetInfoOK = lOK
TrolleyHFAMessage = 'You may not board the trolley until your Laff meter is smiling.'
TrolleyTFAMessage = 'You may not board the trolley until ' + Mickey + ' says so.'
TrolleyHopOff = 'Hop off'
FishingExit = 'Exit'
FishingCast = 'Cast'
FishingAutoReel = 'Auto Reel'
FishingItemFound = 'You caught:'
FishingCrankTooSlow = 'Too\nslow'
FishingCrankTooFast = 'Too\nfast'
FishingFailure = "You didn't catch anything!"
FishingFailureTooSoon = "Don't start to reel in the line until you see a nibble. Wait for your float to bob up and down rapidly!"
FishingFailureTooLate = 'Be sure to reel in the line while the fish is still nibbling!'
FishingFailureAutoReel = "The auto-reel didn't work this time. Turn the crank by hand, at just the right speed, for your best chance to catch something!"
FishingFailureTooSlow = 'You turned the crank too slowly. Some fish are faster than others. Try to keep the speed bar centered!'
FishingFailureTooFast = 'You turned the crank too quickly. Some fish are slower than others. Try to keep the speed bar centered!'
FishingOverTankLimit = 'Your fish bucket is full. Go sell your fish to the Pet Shop Clerk and come back.'
FishingBroke = 'You do not have any more Jellybeans for bait! Ride the trolley or sell fish to the Pet Shop Clerks to earn more Jellybeans.'
FishingHowToFirstTime = 'Click and drag down from the Cast button. The farther down you drag, the stronger your cast will be. Adjust your angle to hit the fish targets.\n\nTry it now!'
FishingHowToFailed = 'Click and drag down from the Cast button. The farther down you drag, the stronger your cast will be. Adjust your angle to hit the fish targets.\n\nTry it again now!'
FishingBootItem = 'An old boot'
FishingJellybeanItem = '%s Jellybeans'
FishingNewEntry = 'New Species!'
FishingNewRecord = 'New Record!'
FishPokerCashIn = 'Cash In\n%s\n%s'
FishPokerLock = 'Lock'
FishPokerUnlock = 'Unlock'
FishPoker5OfKind = '5 of a Kind'
FishPoker4OfKind = '4 of a Kind'
FishPokerFullHouse = 'Full House'
FishPoker3OfKind = '3 of a Kind'
FishPoker2Pair = '2 Pair'
FishPokerPair = 'Pair'
TutorialGreeting1 = 'Hi %s!'
TutorialGreeting2 = 'Hi %s!\nCome over here!'
TutorialGreeting3 = 'Hi %s!\nCome over here!\nUse the arrow keys!'
TutorialMickeyWelcome = 'Welcome to Toonisland!'
TutorialFlippyIntro = 'Let me introduce you to my friend %s…' % Flippy
TutorialFlippyHi = 'Hi, %s!'
TutorialQT1 = 'You can talk by using this.'
TutorialQT2 = 'You can talk by using this.\nClick it, then choose "Hi".'
TutorialChat1 = 'You can talk using either of these buttons.'
TutorialChat2 = 'The blue button lets you chat with the keyboard.'
TutorialChat3 = "Be careful! Most other players won't understand what you say you when you use the keyboard."
TutorialChat4 = 'The green button opens the %s.'
TutorialChat5 = 'Everyone can understand you if you use the %s.'
TutorialChat6 = 'Try saying "Hi".'
TutorialBodyClick1 = 'Very good!'
TutorialBodyClick2 = 'Pleased to meet you! Want to be friends?'
TutorialBodyClick3 = 'To make friends with %s, click on him…' % Flippy
TutorialHandleBodyClickSuccess = 'Good Job!'
TutorialHandleBodyClickFail = 'Not quite. Try clicking right on %s…' % Flippy
TutorialFriendsButton = "Now click the 'Friends' button under %s's picture in the right hand corner." % Flippy
TutorialHandleFriendsButton = "And then click on the 'Yes' button.."
TutorialOK = lOK
TutorialYes = lYes
TutorialNo = lNo
TutorialFriendsPrompt = 'Would you like to make friends with %s?' % Flippy
TutorialFriendsPanelMickeyChat = "%s has agreed to be your friend. Click 'Ok' to finish up." % Flippy
TutorialFriendsPanelYes = '%s said yes!' % Flippy
TutorialFriendsPanelNo = "That's not very friendly!"
TutorialFriendsPanelCongrats = 'Congratulations! You made your first friend.'
TutorialFlippyChat1 = 'Come see me when you are ready for your first ToonTask!'
TutorialFlippyChat2 = "I'll be in ToonHall!"
TutorialAllFriendsButton = 'You can view all your friends by clicking the friends button. Try it out…'
TutorialEmptyFriendsList = "Right now your list is empty because %s isn't a real player." % Flippy
TutorialCloseFriendsList = "Click the 'Close'\nbutton to make the\nlist go away"
TutorialShtickerButton = 'The button in the lower, right corner opens your Shticker Book. Try it…'
TutorialBook1 = 'The book contains lots of useful information like this map of Toontown.'
TutorialBook2 = 'You can also check the progress of your ToonTasks.'
TutorialBook3 = 'When you are done click the book button again to make it close'
TutorialLaffMeter1 = 'You will also need this…'
TutorialLaffMeter2 = "You will also need this…\nIt's your Laff meter."
TutorialLaffMeter3 = 'When ' + Cogs + ' attack you, it gets lower.'
TutorialLaffMeter4 = 'When you are in playgrounds like this one, it goes back up.'
TutorialLaffMeter5 = 'When you complete ToonTasks, you will get rewards, like increasing your Laff limit.'
TutorialLaffMeter6 = 'Be careful! If the ' + Cogs + ' defeat you, you will lose all your gags.'
TutorialLaffMeter7 = 'To get more gags, play trolley games.'
TutorialTrolley1 = 'Follow me to the trolley!'
TutorialTrolley2 = 'Hop on board!'
TutorialBye1 = 'Play some games!'
TutorialBye2 = 'Play some games!\nBuy some gags!'
TutorialBye3 = 'Go see %s when you are done!' % Flippy
TutorialForceAcknowledgeMessage = 'You are going the wrong way! Go find %s!' % Mickey
PetTutorialTitle1 = 'The Doodle Panel'
PetTutorialTitle2 = 'Doodle SpeedChat'
PetTutorialTitle3 = 'Doodle Cattlelog'
PetTutorialNext = 'Next Page'
PetTutorialPrev = 'Previous Page'
PetTutorialDone = 'Done'
PetTutorialPage1 = 'Click on a Doodle to display the Doodle panel. From here you can feed, scratch, and call the Doodle.'
PetTutorialPage2 = "Use the new 'Pets' area in the SpeedChat menu to get a Doodle to do a trick. If he does it, reward him and he'll get better!"
PetTutorialPage3 = "Purchase new Doodle tricks from Clarabelle's Cattlelog. Better tricks give better Toon-Ups!"

def getPetGuiAlign():
    from panda3d.core import TextNode
    return TextNode.ACenter


GardenTutorialTitle1 = 'Gardening'
GardenTutorialTitle2 = 'Flowers'
GardenTutorialTitle3 = 'Trees'
GardenTutorialTitle4 = 'How-to'
GardenTutorialTitle5 = 'Statues'
GardenTutorialNext = 'Next Page'
GardenTutorialPrev = 'Previous Page'
GardenTutorialDone = 'Done'
GardenTutorialPage1 = 'Toon up your Estate with a garden! You can plant flowers, grow trees, harvest super-powerful gags, and decorate with statues!'
GardenTutorialPage2 = 'Flowers are finicky and require unique Jellybean recipes. Once grown, put them in the wheelbarrow to sell them and work toward Laff boosts!'
GardenTutorialPage3 = 'Use a gag from your inventory to plant a tree. After a few days, that gag will do more damage! Remember to keep it healthy or the damage boost will go away.'
GardenTutorialPage4 = 'Walk up to these spots to plant, water, dig up or harvest your garden.'
GardenTutorialPage5 = "Statues can be purchased in Clarabelle's Cattlelog. Increase your skill to unlock the more extravagant statues!"
PlaygroundDeathAckMessage = TheCogs + ' took all your gags!\n\nYou are sad. You may not leave the playground until you are happy.'
ForcedLeaveFactoryAckMsg = 'The ' + Foreman + ' was defeated before you could reach him. You did not recover any Cog parts.'
ForcedLeaveMintAckMsg = 'The Mint Floor Supervisor was defeated before you could reach him. You did not recover any Cogbucks.'
HeadingToFactoryTitle = '%s'
ForemanConfrontedMsg = '%s is battling the ' + Foreman + '!'
MintBossConfrontedMsg = '%s is battling the Supervisor!'
StageBossConfrontedMsg = '%s is battling the Clerk!'
stageToonEnterElevator = '%s \nhas entered the elevator'
ForcedLeaveStageAckMsg = 'The Law Clerk was defeated before you could reach him. You did not recover any Jury Notices.'
MinigameWaitingForOtherPlayers = 'Waiting for other players to join…'
MinigamePleaseWait = 'Please wait…'
DefaultMinigameTitle = 'Minigame Title'
DefaultMinigameInstructions = 'Minigame Instructions'
HeadingToMinigameTitle = 'Heading to %s…'
MinigamePowerMeterLabel = 'Power Meter'
MinigamePowerMeterTooSlow = 'Too\nslow'
MinigamePowerMeterTooFast = 'Too\nfast'
MinigameTemplateTitle = 'Minigame Template'
MinigameTemplateInstructions = 'This is a template minigame. Use it to create new minigames.'
CannonGameTitle = 'Cannon Game'
CannonGameInstructions = 'Shoot your Toon into the water tower as quickly as you can. Use the mouse or the arrow keys to aim the cannon. Be quick and win a big reward for everyone!'
CannonGameReward = 'REWARD'
TwoDGameTitle = 'Toon Escape'
TwoDGameInstructions = 'Escape from the ' + Cog + ' den as soon as you can. Use arrow keys to run/jump and Ctrl to squirt a ' + Cog + '. Collect ' + Cog + ' treasures to gain even more points.'
TwoDGameElevatorExit = 'EXIT'
TugOfWarGameTitle = 'Tug-of-War'
TugOfWarInstructions = "Alternately tap the left and right arrow keys just fast enough to line up the green bar with the red line. Don't tap them too slow or too fast, or you'll end up in the water!"
TugOfWarGameGo = 'GO!'
TugOfWarGameReady = 'Ready…'
TugOfWarGameEnd = 'Good game!'
TugOfWarGameTie = 'You tied!'
TugOfWarPowerMeter = 'Power meter'
PatternGameTitle = 'Match %s' % Minnie
PatternGameInstructions = Minnie + ' will show you a dance sequence. ' + 'Try to repeat ' + Minnie + "'s dance just the way you see it using the arrow keys!"
PatternGameWatch = 'Watch these dance steps…'
PatternGameGo = 'GO!'
PatternGameRight = 'Good, %s!'
PatternGameWrong = 'Oops!'
PatternGamePerfect = 'That was perfect, %s!'
PatternGameBye = 'Thanks for playing!'
PatternGameWaitingOtherPlayers = 'Waiting for other players…'
PatternGamePleaseWait = 'Please wait…'
PatternGameFaster = 'You were\nfaster!'
PatternGameFastest = 'You were\nthe fastest!'
PatternGameYouCanDoIt = 'Come on!\nYou can do it!'
PatternGameOtherFaster = '\nwas faster!'
PatternGameOtherFastest = '\nwas the fastest!'
PatternGameGreatJob = 'Great Job!'
PatternGameRound = 'Round %s!'
PatternGameImprov = 'You did great! Now Improv!'
RaceGameTitle = 'Race Game'
RaceGameInstructions = 'Click a number. Choose wisely! You only advance if no one else picked the same number.'
RaceGameWaitingChoices = 'Waiting for other players to choose…'
RaceGameCardText = '%(name)s draws: %(reward)s'
RaceGameCardTextBeans = '%(name)s receives: %(reward)s'
RaceGameCardTextHi1 = '%(name)s is one Fabulous Toon!'
RaceGameForwardOneSpace = ' forward 1 space'
RaceGameForwardTwoSpaces = ' forward 2 spaces'
RaceGameForwardThreeSpaces = ' forward 3 spaces'
RaceGameBackOneSpace = ' back 1 space'
RaceGameBackTwoSpaces = ' back 2 spaces'
RaceGameBackThreeSpaces = ' back 3 spaces'
RaceGameOthersForwardThree = ' all others forward \n3 spaces'
RaceGameOthersBackThree = 'all others back \n3 spaces'
RaceGameInstantWinner = 'Instant Winner!'
RaceGameJellybeans2 = '2 Jellybeans'
RaceGameJellybeans4 = '4 Jellybeans'
RaceGameJellybeans10 = '10 Jellybeans!'
RingGameTitle = 'Ring Game'
RingGameInstructionsSinglePlayer = 'Try to swim through as many of the %s rings as you can. Use the arrow keys to swim.'
RingGameInstructionsMultiPlayer = 'Try to swim through the %s rings. Other players will try for the other colored rings. Use the arrow keys to swim.'
RingGameMissed = 'MISSED'
RingGameGroupPerfect = 'GROUP\nPERFECT!!'
RingGamePerfect = 'PERFECT!'
RingGameGroupBonus = 'GROUP BONUS'
ColorRed = 'Red'
ColorGreen = 'Green'
ColorOrange = 'Orange'
ColorPurple = 'Purple'
ColorWhite = 'White'
ColorBlack = 'Black'
ColorYellow = 'Yellow'
DivingGameTitle = 'Treasure Dive'
DivingInstructionsSinglePlayer = 'Treasures will appear at the bottom of the lake. Use the arrow keys to swim. Avoid the fish and get the treasures up to the boat!'
DivingInstructionsMultiPlayer = 'Treasures will appear at the bottom of the lake. Use the arrow keys to swim. Work together to get the treasures up to the boat!'
DivingGameTreasuresRetrieved = 'Treasures Retrieved'
TargetGameTitle = 'Toon Slingshot'
TargetGameInstructionsSinglePlayer = 'Land on targets to score points'
TargetGameInstructionsMultiPlayer = 'Land on targets to score points'
TargetGameBoard = 'Round %s - Keeping Best Score'
TargetGameCountdown = 'Forced launch in %s seconds'
TargetGameCountHelp = 'Pound left and right arrows for power, stop to launch'
TargetGameFlyHelp = 'Press down to open umbrella'
TargetGameFallHelp = 'Use the arrow keys to land on target'
TargetGameBounceHelp = ' Bouncing can knock you off target'
PhotoGameScoreTaken = '%s: %s\nYou: %s'
PhotoGameScoreBlank = 'Score: %s'
PhotoGameScoreOther = '\n%s'
PhotoGameScoreYou = '\nBest Bonus!'
TagGameTitle = 'Tag Game'
TagGameInstructions = 'Collect the treasures. You cannot collect treasure when you are IT!'
TagGameYouAreIt = 'You Are IT!'
TagGameSomeoneElseIsIt = '%s is IT!'
MazeGameTitle = 'Maze Game'
MazeGameInstructions = 'Collect the treasures. Try to get them all, but look out for the ' + Cogs + '!'
CatchGameTitle = 'Catching Game'
CatchGameInstructions = 'Catch as many %(fruit)s as you can. Watch out for the ' + Cogs + ", and try not to 'catch' any %(badThing)s!"
CatchGamePerfect = 'PERFECT!'
CatchGameApples = 'apples'
CatchGameOranges = 'oranges'
CatchGamePears = 'pears'
CatchGameCoconuts = 'coconuts'
CatchGameWatermelons = 'watermelons'
CatchGamePineapples = 'pineapples'
CatchGameAnvils = 'anvils'
PieTossGameTitle = 'Pie Toss Game'
PieTossGameInstructions = 'Toss pies at the targets.'
PhotoGameInstructions = 'Capture photos matching the Toons shown at the bottom. Aim the camera with the mouse, and left click to take a picture. Press Ctrl to zoom in/out, and look around with the arrow keys. Pictures with higher ratings get more points!'
PhotoGameTitle = 'Photo Fun'
PhotoGameFilm = 'FILM'
PhotoGameScore = 'Team Score: %s\n\nBest Photos: %s\n\nTotal Score: %s'
CogThiefGameTitle = Cog + ' Thief'
CogThiefGameInstructions = 'Keep the ' + Cogs + ' from stealing our gag barrels! Press the Ctrl key to throw a pie. Use the arrow keys to move. Tip: you can move diagonally.'
CogThiefBarrelsSaved = '%(num)d Barrels\nSaved!'
CogThiefBarrelSaved = '%(num)d Barrel\nSaved!'
CogThiefNoBarrelsSaved = 'No Barrels\nSaved'
CogThiefPerfect = 'PERFECT!'
MinigameRulesPanelPlay = 'PLAY'
GagShopName = "Goofy's Gag Shop"
GagShopPlayAgain = 'PLAY\nAGAIN'
GagShopBackToPlayground = 'EXIT BACK TO\nPLAYGROUND'
GagShopYouHave = 'You have %s Jellybeans to spend'
GagShopYouHaveOne = 'You have 1 Jellybean to spend'
GagShopTooManyProps = 'Sorry, you have too many props'
GagShopDoneShopping = 'DONE\nSHOPPING'
GagShopTooManyOfThatGag = 'Sorry, you have enough %s already'
GagShopInsufficientSkill = 'You do not have enough skill for that yet'
GagShopYouPurchased = 'You purchased %s'
GagShopOutOfJellybeans = 'Sorry, you are all out of Jellybeans!'
GagShopWaitingOtherPlayers = 'Waiting for other players…'
GagShopPlayerDisconnected = '%s has disconnected'
GagShopPlayerExited = '%s has exited'
GagShopPlayerPlayAgain = 'Play Again'
GagShopPlayerBuying = 'Buying'
GenderShopQuestionMickey = 'To make a boy Toon, click on me!'
GenderShopQuestionMinnie = 'To make a girl Toon, click on me!'
GenderShopFollow = 'Follow me!'
GenderShopSeeYou = 'See you later!'
GenderShopBoyButtonText = 'Boy'
GenderShopGirlButtonText = 'Girl'
BodyShopHead = 'Head'
BodyShopBody = 'Body'
BodyShopLegs = 'Legs'
ColorShopToon = 'Toon Color'
ColorShopHead = 'Head'
ColorShopBody = 'Body'
ColorShopLegs = 'Legs'
ColorShopParts = 'Multi Color'
ColorShopAll = 'Single Color'
ClothesShopShorts = 'Shorts'
ClothesShopShirt = 'Shirts'
ClothesShopBottoms = 'Bottoms'
PromptTutorial = "Congratulations!!\nYou are Toon Island's newest citizen!\n\nWould you like to continue to the Toontorial or teleport directly to Toon Island Central?"
MakeAToonSkipTutorial = 'Skip Toontorial'
MakeAToonEnterTutorial = 'Enter Toontorial'
MakeAToonDone = 'Done'
MakeAToonCancel = lCancel
MakeAToonNext = lNext
MakeAToonLast = 'Back'
CreateYourToon = 'Click the arrows to create your Toon.'
CreateYourToonTitle = 'Choose Boy or Girl'
ShapeYourToonTitle = 'Choose Your Species'
PaintYourToonTitle = 'Choose Your Color'
PickClothesTitle = 'Choose Your Clothes'
NameToonTitle = 'Choose Your Name'
CreateYourToonHead = "Click the 'head' arrows to pick different animals."
MakeAToonClickForNextScreen = 'Click the arrow below to go to the next screen.'
PickClothes = 'Click the arrows to pick clothes!'
PaintYourToon = 'Click the arrows to paint your Toon!'
MakeAToonYouCanGoBack = 'You can go back to change your body too!'
MakeAFunnyName = 'Choose a funny name for your Toon with my Pick-A-Name game!'
MustHaveAFirstOrLast1 = "Your Toon should have a first or last name, don't you think?"
MustHaveAFirstOrLast2 = "Don't you want your Toon to have a first or last name?"
ApprovalForName1 = "That's it, your Toon deserves a great name!"
ApprovalForName2 = 'Toon names are the best kind of names!'
MakeAToonLastStep = 'Last step before going to Toontown!'
PickANameYouLike = 'Pick a name you like!'
TitleCheckBox = 'Title'
FirstCheckBox = 'First'
LastCheckBox = 'Last'
RandomButton = 'Random'
ShuffleButton = 'Shuffle'
NameShopSubmitButton = 'Submit'
TypeANameButton = 'Type-A-Name'
TypeAName = "Don't like these names?\nClick here -->"
PickAName = 'Try the PickAName game!\nClick here -->'
PickANameButton = 'Pick-A-Name'
RejectNameText = 'That name is not allowed. Please try again.'
WaitingForNameSubmission = 'Submitting your name…'
PetNameMaster = 'PetNameMasterEnglish.txt'
PetNameIndexMAX = 2713
PetshopUnknownName = 'Name: ???'
PetshopDescGender = 'Gender:\t%s'
PetshopDescCost = 'Cost:\t%s Jellybeans'
PetshopDescTrait = 'Traits:\t%s'
PetshopDescStandard = 'Standard'
PetshopCancel = lCancel
PetshopSell = 'Sell Fish'
PetshopAdoptAPet = 'Adopt a Doodle'
PetshopReturnPet = 'Return your Doodle'
PetshopAdoptConfirm = 'Adopt %s for %d Jellybeans?'
PetshopGoBack = 'Go Back'
PetshopAdopt = 'Adopt'
PetshopReturnConfirm = 'Return %s?'
PetshopReturn = 'Return'
PetshopChooserTitle = "TODAY'S DOODLES"
PetshopGoHomeText = 'Would you like to go to your estate to play with your new Doodle?'
NameShopNameMaster = 'NameMasterEnglish.txt'
NameShopPay = 'Subscribe'
NameShopPlay = 'Free Trial'
NameShopOnlyPaid = 'Only paid users\nmay name their Toons.\nUntil you subscribe\nyour name will be\n'
NameShopContinueSubmission = 'Continue Submission'
NameShopChooseAnother = 'Choose Another Name'
NameShopToonCouncil = 'The Toon Council\nwill review your\nname. ' + 'Review may\ntake a few days.\nWhile you wait\nyour name will be\n '
PleaseTypeName = 'Please type your name:'
AllNewNames = 'All new names must be\napproved by the Toon Council.'
NameMessages = 'Be creative and remember:\nfollow the rules of the server.'
NameShopNameRejected = 'The name you\nsubmitted has\nbeen rejected.'
NameShopNameAccepted = 'Congratulations!\nThe name you\nsubmitted has\nbeen accepted!'
NoPunctuation = "You can't use punctuation marks in your name!"
PeriodOnlyAfterLetter = 'You can use a period in your name, but only after a letter.'
ApostropheOnlyAfterLetter = 'You can use an apostrophe in your name, but only after a letter.'
NoNumbersInTheMiddle = 'Numeric digits may not appear in the middle of a word.'
ThreeWordsOrLess = 'Your name must be three words or fewer.'
CopyrightedNames = ('mickey',
 'mickey mouse',
 'mickeymouse',
 'minnie',
 'minnie mouse',
 'minniemouse',
 'donald',
 'donald duck',
 'donaldduck',
 'pluto',
 'goofy')
NumToColor = ['White',
 'Peach',
 'Bright Red',
 'Red',
 'Maroon',
 'Sienna',
 'Brown',
 'Tan',
 'Coral',
 'Orange',
 'Yellow',
 'Cream',
 'Citrine',
 'Lime',
 'Sea Green',
 'Green',
 'Light Blue',
 'Aqua',
 'Blue',
 'Periwinkle',
 'Royal Blue',
 'Slate Blue',
 'Purple',
 'Lavender',
 'Pink',
 'Plum',
 'Black']
AnimalToSpecies = {'dog': 'Dog',
 'cat': 'Cat',
 'mouse': 'Mouse',
 'horse': 'Horse',
 'rabbit': 'Rabbit',
 'duck': 'Duck',
 'monkey': 'Monkey',
 'bear': 'Bear',
 'pig': 'Pig',
 'deer': 'Deer'}
NameTooLong = 'That name is too long. Please try again.'
ToonAlreadyExists = 'You already have a Toon named %s!'
NameAlreadyInUse = 'That name is already used!'
EmptyNameError = 'You must enter a name first.'
NameError = 'Sorry. That name will not work.'
NCTooShort = 'That name is too short.'
NCNoDigits = 'Your name cannot contain numbers.'
NCNeedLetters = 'Each word in your name must contain some letters.'
NCNeedVowels = 'Each word in your name must contain some vowels.'
NCAllCaps = 'Your name cannot be all capital letters.'
NCMixedCase = 'That name has too many capital letters.'
NCBadCharacter = "Your name cannot contain the character '%s'"
NCGeneric = 'Sorry, that name will not work.'
NCTooManyWords = 'Your name cannot be more than four words long.'
NCDashUsage = "Dashes may only be used to connect two words together (like in 'Boo-Boo')."
NCCommaEdge = 'Your name may not begin or end with a comma.'
NCCommaAfterWord = 'You may not begin a word with a comma.'
NCCommaUsage = 'That name does not use commas properly. Commas must join two words together, like in the name "Dr. Quack, MD". Commas must also be followed by a space.'
NCPeriodUsage = 'That name does not use periods properly. Periods are only allowed in words like "Mr.", "Mrs.", "J.T.", etc.'
NCApostrophes = 'That name has too many apostrophes.'
RemoveTrophy = lToonHQ + ': ' + TheCogs + ' took over one of the buildings you rescued!'
STOREOWNER_TOOKTOOLONG = 'Need more time to think?'
STOREOWNER_GOODBYE = 'See you later!'
STOREOWNER_NEEDJellybeanS = 'You need to ride the Trolley to get some Jellybeans.'
STOREOWNER_GREETING = 'Choose what you want to buy.'
STOREOWNER_BROWSING = 'You can browse, but you need a clothing ticket to buy.'
STOREOWNER_NOCLOTHINGTICKET = 'You need a clothing ticket to shop for clothes.'
STOREOWNER_NOFISH = 'Come back here to sell fish to the Pet Shop for Jellybeans.'
STOREOWNER_THANKSFISH = 'Thanks! The Pet Shop will love these. Bye!'
STOREOWNER_THANKSFISH_PETSHOP = 'These are some fine specimens! Thanks.'
STOREOWNER_PETRETURNED = "Don't worry. We'll find a good home for your Doodle."
STOREOWNER_PETADOPTED = 'Congratulations on purchasing a Doodle! You can play with your new friend at your estate.'
STOREOWNER_PETCANCELED = 'Remember, if you see a Doodle you like, make sure to adopt him before someone else does!'
STOREOWNER_NOROOM = 'Hmm…you might want to make room in your closet before you buy new clothes.\n'
STOREOWNER_CONFIRM_LOSS = 'Your closet is full. You will lose the clothes you were wearing.'
STOREOWNER_OK = lOK
STOREOWNER_CANCEL = lCancel
STOREOWNER_TROPHY = 'Wow! You collected %s of %s fish. That deserves a trophy and a Laff boost!'
SuitInvasionBegin1 = lToonHQ + ': A Cog Invasion has begun!!!'
SuitInvasionBegin2 = lToonHQ + ': %s have taken over Toontown!!!'
SuitInvasionEnd1 = lToonHQ + ': The %s Invasion has ended!!!'
SuitInvasionEnd2 = lToonHQ + ': The Toons have saved the day once again!!!'
SuitInvasionUpdate1 = lToonHQ + ': The Cog Invasion is now at %s Cogs!!!'
SuitInvasionUpdate2 = lToonHQ + ': We must defeat those %s!!!'
SuitInvasionBulletin1 = lToonHQ + ': There is a Cog Invasion in progress!!!'
SuitInvasionBulletin2 = lToonHQ + ': %s have taken over Toontown!!!'
LeaderboardTitle = 'Toon PlaToon'
QuestScriptTutorialMickey_1 = 'The island has a new citizen, Toontorial Tom! Will you fill them in on our situation?'
QuestScriptTutorialMickey_2 = 'Sure, %s!'
QuestScriptTutorialMickey_3 = 'Tutorial Tom will tell you all about the Cogs.\x07Gotta go!'
QuestScriptTutorialMickey_4 = 'Come here! (Use the arrow keys to move.)'
QuestScriptTutorialMinnie_1 = 'The island has a new citizen, Toontorial Tom! Will you fill them in on our situation?'
QuestScriptTutorialMinnie_2 = 'Sure, %s!'
QuestScriptTutorialMinnie_3 = 'Tutorial Tom will tell you all about the Cogs.\x07Gotta go!' # Please have Minnie use the front door to exit the building and make sure the Cog isn't out there until QuestScript100_28
# QuestScript.txt
QuestScript101_0 = 'Come here! (Use the arrow keys to move.)'

QuestScript100_0 = 'Hey there, welcome to the island!'
QuestScript100_1 = 'Since you are new here…'
QuestScript100_2 = "It's my job to show you around!"
QuestScript100_3 = 'Let’s begin your lessons!'
QuestScript100_4 = 'Now, the basics:'
QuestScript100_5 = 'Well, there are these uh… things!'
QuestScript100_6 = 'Yes, these things are called Cogs!'
QuestScript100_7 = 'They turn happy Toon buildings…'
QuestScript100_8 = 'Into ugly Cog buildings!'
QuestScript100_9 = 'They have four factions, one might say.'
# TODO: Here, I'd love to see the concept art from TTO for each Cog Faction pop up as Tom mentions it OR showing the Cog Sigil found on their chest when they wander. -- Gracie
QuestScript100_10 = 'The Sellbots who make money chugging out Cog parts from their factories…'
QuestScript100_11 = 'The Cashbots who monitor the cash flow in their corporation…'
QuestScript100_12 = 'There are the Lawbots who keep order amongst the Cogs…'
QuestScript100_13 = 'And then there’s the Bossbots who keep them all in line!'
QuestScript100_14 = "They pretty much like to terrorize toons with their business ways…"
QuestScript100_15 = 'Making us sad and taking all of our gags!'
QuestScript100_16 = "Luckily, we have fully installed a Laff-O-Meter for all toons, kind of like a health meter!"
QuestScript100_17 = 'It keeps us healthy and fit for cog fights, and makes it harder for us to go sad'
QuestScript100_18 = 'A happy Toon is a healthy Toon!'
QuestScript100_19 = 'Speaking of which, we have devised new weapons against them that are harmless to all Toons called Gags!' # TODO: Switch the Laff Meter showcase and the Gag showcase with one another. -- Gracie
QuestScript100_20 = 'These are the bane of the Cogs’ existence and the Gags repel them with ease!'
QuestScript100_21 = 'Now, you must be wondering what happened to the mainland, Toontown?'
QuestScript100_22 = 'Well… A while ago, these robots started showing up and wrecking havoc across town!' # TODO: Tutorial Tom's eyes should become sad here AND add the original Toontown Map between the dialog box and Toontorial Tom's hand. -- Gracie
QuestScript100_23 = "We created the Toon Resistance to fight back but we got overrun… So, we had to flee the mainland!"
QuestScript100_24 = "We came here to this island and we've been here ever since!"
QuestScript100_25 = "Now, a while back, we deployed the Toon Resistance to take back the mainland but we haven't heard back from them since."
QuestScript100_26 = 'So, we can only assume they got caught!'
QuestScript100_27 = 'And much to our dismay, a few months ago, our new home was invaded by the Cogs AGAIN!' # TODO: Tom should show that he's angry again -- Gracie
QuestScript100_28 = 'So, we returned to the fight. We believe this will be our final stand against the---' # TODO: Here, I'd like to see a cutscene showing the Flunky whirring down from the sky and landing in front of the shop instead of it just lurking there, on the sidewalk! -- Gracie
QuestScript100_29 = 'Wait… I see something back there… is it?' # Gracie's Note: Tom should turn his head to the window to see the Flunky prior to pointing his glove toward the window.
QuestScript100_30 = 'Wait… it’s a Cog!'
QuestScript100_31 = 'Take these Gags and run that robot out of town!'

QuestScript110_1 = "So, I heard from %s that you got the run down of what's happening?" # %s is supposed to be either Minnie or Mickey, depending on the gender. (If gender stays. If it doesn't, may I recommend that we replace Mickey/Minnie with Flippy or another Toon. Also, have Minnie/Mickey go out the same door your Toon goes out of when they have to fight the Flunky. -- Gracie)
QuestScript110_2 = 'That is great and all but…'
QuestScript110_3 = "I fear with the Cog's return, we aren't doing so well out here! This Toon Headquarters is understaffed and is in danger of being overrun by the Cogs!"
QuestScript110_4 = "Hey, don’t look at me like that!"
QuestScript110_5 = 'I have no one to help defend this HQ since we’re still waiting for the return of the Resistance Rangers!'
QuestScript110_6 = 'This has left all Toon Headquarter’s vulnerable to a Cog takeover!'
QuestScript110_7 = 'To rub salt in the wound, I lost my only Walkie Talkie to a pesky Cog that waltzed in here while I was at lunch!'
QuestScript110_8 = 'I need you to find it!'
QuestScript110_9 = 'When you’ve found it, return it to a HQ Officer in Toon Island Central and they’ll return it to me!'
QuestScript110_10 = 'Before that, you’ll meet Mayor Flippy Doggenbottom so that he can finish teaching you about our world!'

QuestScriptTutorialBlocker_1 = 'Why, hello there! My name is Mayor Flippy Doggenbottom'
QuestScriptTutorialBlocker_2 = 'Hello?'
QuestScriptTutorialBlocker_3 = "Oh! You don't know how to talk!"
QuestScriptTutorialBlocker_4 = 'Click on the button to say something.'
QuestScriptTutorialBlocker_5 = 'Very good!\x07Where you are going, there are many Toons to talk to.'
QuestScriptTutorialBlocker_6 = "If you want to chat with other Toons using the keyboard, there's another button you can use."
QuestScriptTutorialBlocker_7 = "It's called the Chat button. Using it, you can type in a message and send it to all the other Toons in the area!"
QuestScriptTutorialBlocker_8 = "I heard that the pesky Cogs have stolen Toontorial Terrace's only Walkie Talkie!\x07Once you've found it, remember to return it to a HQ officer and they will take it from there!"
QuestScriptTutorialBlocker_8 = 'That should be all you need to know.\x07After you’ve finished, come visit me in my office to learn more about the Gags!'
QuestScriptTutorialBlocker_9 = 'See you later!'

QuestScriptGagShop_1 = 'Welcome to the Gag Shop!'
QuestScriptGagShop_1a = 'This is where Toons come to buy gags to use against the Cogs.'
QuestScriptGagShop_3 = 'To buy gags, click on the gag buttons. Try getting some now!'
QuestScriptGagShop_4 = 'Good! You can use these gags in battle against the Cogs.'
QuestScriptGagShop_5 = "Here's a peek at the advanced throw and squirt gags…"
QuestScriptGagShop_6 = "When you're done buying your gags, click this button to return to the playground."
QuestScriptGagShop_7 = 'Normally, you can use this button to play another Trolley Game…'
QuestScriptGagShop_8 = "…but there's no time for another game right now! You're needed at the closest Toon HQ!"
QuestScript120_1 = "Good job finding the trolley!\x07By the way, have you met Banker Bob?\x07He has quite a sweet tooth.\x07Why don't you introduce yourself by taking him this candy bar as a gift."
QuestScript120_2 = 'Banker Bob is over inside the Toontown Bank in Toon Island Central!'
QuestScript121_1 = "Yum, thank you for the Candy Bar.\x07Those Cogs stole the keys to my safe. Defeat Cogs to find a stolen key.\x07When you find a key, bring it back to me.\x07If you can help me, I'll give you a reward!"
QuestScript130_1 = 'Good job finding the trolley!\x07By the way, I received a package for Professor Pete today.\x07It must be his new chalk he ordered.\x07Can you please take it to him?\x07He is over in the Toontown School House in the playground.'
QuestScript131_1 = 'Oh, thanks for the chalk.\x07What?!?\x07Those Cogs stole my blackboard while I was out. Defeat Cogs to find my stolen blackboard.\x07When you find it, bring it back to me.'
QuestScript140_1 = 'Good job finding the trolley!\x07By the way, I have this friend, Librarian Liz, who is quite a book worm.\x07I picked this book up for him last time I was over in ' + lDonaldsDock + '.\x07Could you take it over to him, he is usually in the New Toontown Continental Library.'
QuestScript141_1 = 'Oh, yes, this book almost completes my collection.\x07Let me see…\x07Uh oh…\x07Now where did I put my glasses?\x07I had them just before those Cogs took over my building.\x07Defeat Cogs to find my stolen glasses.\x07When you find them, bring them back to me for a reward.' # Btw, I'd like to see a playground event that makes these buildings be taken over by the Cogs to make sense of the story. -- Gracie.
QuestScript145_1 = 'I see you had no problem with the trolley!\x07Listen, the Cogs have stolen our blackboard eraser.\x07Go into the streets and fight Cogs until you recover the eraser.\x07To reach the streets go through one of the tunnels like this:'
QuestScript145_2 = "When you find our eraser, bring it back here.\x07Don't forget, if you need gags, ride the trolley.\x07Also, if you need to recover Laff points, collect ice cream cones in the Playground."
QuestScript150_1 = 'Great work!\x07Did you know that Toontown is WAY more fun when you have friends?'
QuestScript150_2 = 'To make friends, find another player, click on their nametag, and use the New Friend button to add them to your friends list.'
QuestScript150_3 = 'Once you have made a friend, come back here.'
QuestScript150_4 = 'Some tasks are too difficult to do alone!'
MissingKeySanityCheck = 'Ignore me'
SellbotBossName = 'Senior Vice President'
CashbotBossName = 'Chief Financial Officer.'
LawbotBossName = 'Chief Justice'
BossCogNameWithDept = '%(name)s\n%(dept)s'
BossCogPromoteDoobers = 'You are hereby promoted to full-fledged %s. Congratulations!'
BossCogDoobersAway = {'s': 'Go! And make that sale!'}
BossCogWelcomeToons = 'Welcome, new Cogs!'
BossCogPromoteToons = 'You are hereby promoted to full-fledged %s. Congratu--'
CagedToonInterruptBoss = 'Hey! Hiya! Hey over there!'
CagedToonRescueQuery = 'So, did you Toons come to rescue me?'
BossCogDiscoverToons = 'Huh? Toons! In disguise!'
BossCogAttackToons = 'Attack!!'
CagedToonDrop = ["Great job! You're wearing him down!",
 "Keep after him! He's on the run!",
 'You guys are doing great!',
 "Fantastic! You've almost got him now!"]
CagedToonPrepareBattleTwo = "Look out, he's trying to get away!\x07Help me, everyone--get up here and stop him!"
CagedToonPrepareBattleThree = "Hooray, I'm almost free!\x07Now you need to attack the V.P. Cog directly.\x07I've got a whole bunch of pies you can use!\x07Jump up and touch the bottom of my cage and I'll give you some pies.\x07Press the Delete key to throw pies once you've got them!"
BossBattleNeedMorePies = 'You need to get more pies!'
BossBattleHowToGetPies = 'Jump up to touch the cage to get pies.'
BossBattleHowToThrowPies = 'Press the Delete key to throw pies!'
CagedToonYippee = 'Yippee!'
CagedToonThankYou = "It's great to be free!\x07Thanks for all your help!\x07I am in your debt.\x07Here's my card. If you ever need a hand in battle, give a shout!\x07Just click on your S.O.S. button."
CagedToonPromotion = "\x07Say--that V.P. Cog left behind your promotion papers.\x07I'll file them for you on the way out, so you'll get your promotion!"
CagedToonLastPromotion = "\x07Wow, you've reached level %s on your Cog suit!\x07Cogs don't get promoted higher than that.\x07You can't upgrade your Cog suit anymore, but you can certainly keep rescuing Toons!"
CagedToonHPBoost = "\x07You've rescued a lot of Toons from this HQ.\x07The Toon Council has decided to give you another Laff point. Congratulations!"
CagedToonMaxed = '\x07I see that you have a level %s Cog suit. Very impressive!\x07On behalf of the Toon Council, thank you for coming back to rescue more Toons!'
CagedToonGoodbye = 'See ya!'
CagedToonBattleThree = {10: 'Nice jump, %(Toon)s. Here are some pies!',
 11: 'Hi, %(Toon)s! Have some pies!',
 12: "Hey there, %(Toon)s! You've got some pies now!",
 20: 'Hey, %(Toon)s! Jump up to my cage and get some pies to throw!',
 21: 'Hi, %(Toon)s! Use the Ctrl key to jump up and touch my cage!',
 100: 'Press the Delete key to throw a pie.',
 101: 'The blue power meter shows how high your pie will go.',
 102: 'First try to lob a pie inside his undercarriage to gum up his works.',
 103: 'Wait for the door to open, and throw a pie straight inside.',
 104: "When he's dizzy, hit him in the face or chest to knock him back!",
 105: "You'll know you've got a good hit when you see the splat in color.",
 106: 'If you hit a Toon with a pie, it gives that Toon a Laff point!'}
CagedToonBattleThreeMaxGivePies = 12
CagedToonBattleThreeMaxTouchCage = 21
CagedToonBattleThreeMaxAdvice = 106
CashbotBossHadEnough = "That's it. I've had enough of these pesky Toons!"
CashbotBossOuttaHere = "I've got a train to catch!"
ResistanceToonName = 'Mata Hairy'
ResistanceToonCongratulations = "You did it! Congratulations!\x07You're an asset to the Resistance!\x07Here's some phrases you can use in a tight spot\x07When you say one, it will cause an effect.\x07But you can only use it once, so choose that time well!"
ResistanceToonToonupInstructions = 'all the Toons near you will gain %s Laff points'
ResistanceToonToonupAllInstructions = 'all the Toons near you will gain full Laff points'
ResistanceToonMoneyInstructions = 'all the Toons near you will gain %s Jellybeans'
ResistanceToonMoneyAllInstructions = 'all the Toons near you will fill their Jellybean jars'
ResistanceToonRestockInstructions = 'all the Toons near you will restock their "%s" gags'
ResistanceToonRestockAllInstructions = 'all the Toons near you will restock all their gags'
ResistanceToonLastPromotion = "\x07Wow, you've reached level %s on your Cog suit!\x07Cogs don't get promoted higher than that.\x07You can't upgrade your Cog suit anymore, but you can certainly keep working for the Resistance!"
ResistanceToonHPBoost = "\x07You've done a lot of work for the Resistance.\x07The Toon Council has decided to give you another Laff point. Congratulations!"
ResistanceToonMaxed = '\x07I see that you have a level %s Cog suit. Very impressive!\x07On behalf of the Toon Council, thank you for coming back to rescue more Toons!'
CashbotBossCogAttack = 'Get them!!!'
ResistanceToonWelcome = 'Hey, you made it! Follow me to the main vault before the C.F.O. finds us!'
ResistanceToonTooLate = "Blast it! We're too late!"
CashbotBossDiscoverToons1 = 'Ah-HAH!'
CashbotBossDiscoverToons2 = 'I thought I smelled something a little Toony in here! Imposters!'
ResistanceToonKeepHimBusy = "Keep him busy! I'm going to set a trap!"
ResistanceToonWatchThis = 'Watch this!'
CashbotBossGetAwayFromThat = 'Hey! Get away from that!'
ResistanceToonCraneInstructions1 = 'Control a magnet by stepping up to a podium.'
ResistanceToonCraneInstructions2 = 'Use the arrow keys to move the crane, and press the Ctrl key to grab an object.'
ResistanceToonCraneInstructions3 = "Grab a safe with a magnet and knock the C.F.O.'s safe-ty helmet off."
ResistanceToonCraneInstructions4 = 'Once his helmet is gone, grab a disabled goon and hit him in the head!'
ResistanceToonGetaway = 'Eek! Gotta run!'
CashbotCraneLeave = 'Leave Crane'
CashbotCraneAdvice = 'Use the arrow keys to move the overhead crane.'
CashbotMagnetAdvice = 'Hold down the control key to pick things up.'
CashbotCraneLeaving = 'Leaving crane'
MintElevatorRejectMessage = 'You cannot enter the Mints until you have completed your %s Cog Suit.'
BossElevatorRejectMessage = 'You cannot board this elevator until you have earned a promotion.'
NotYetAvailable = 'This elevator is not yet available.'
SellbotRentalSuitMessage = "Wear this Rental Suit so you can get close enough to the VP to attack.\n\nYou won't earn merits or promotions, but you can rescue a Toon for an S.O.S. reward!"
SellbotCogsuitNoMeritsMessage = "Your Sellbot Disguise will get you in, but since you don't have enough merits, you won't earn a promotion.\n\nIf you rescue the trapped Toon, you will earn an S.O.S. Toon reward!"
SellbotCogsuitHasMeritsMessage = "It's Operation: Storm Sellbot!\n\nBring 5 or more Rental Suit Toons with you to defeat the V.P. and earn credit towards a reward!"
FurnitureTypeName = 'Furniture'
PaintingTypeName = 'Painting'
ClothingTypeName = 'Clothing'
ChatTypeName = 'SpeedChat Phrase'
EmoteTypeName = 'Acting Lessons'
BeanTypeName = 'Jellybeans'
PoleTypeName = 'Fishing Pole'
WindowViewTypeName = 'Window View'
PetTrickTypeName = 'Doodle Training'
GardenTypeName = 'Garden Supplies'
RentalTypeName = 'Rental Item'
GardenStarterTypeName = 'Gardening Kit'
NametagTypeName = 'Name tag'
AccessoryTypeName = 'Accessory'
CatalogItemTypeNames = {0: 'INVALID_ITEM',
 1: FurnitureTypeName,
 2: ChatTypeName,
 3: ClothingTypeName,
 4: EmoteTypeName,
 5: 'WALLPAPER',
 6: 'Window View',
 7: 'FLOORING',
 8: 'MOULDING',
 9: 'WAINSCOTING',
 10: PoleTypeName,
 11: PetTrickTypeName,
 12: BeanTypeName,
 13: GardenTypeName,
 14: RentalTypeName,
 15: GardenStarterTypeName,
 16: NametagTypeName,
 17: 'TOON_STATUE',
 18: 'ANIMATED FURNITURE',
 19: AccessoryTypeName}
HatStylesDescriptions = {'hbb1': 'Green Baseball Cap',
 'hbb2': 'Blue Baseball Cap',
 'hbb3': 'Orange Baseball Cap',
 'hsf1': 'Beige Safari Hat',
 'hsf2': 'Brown Safari Hat',
 'hsf3': 'Green Safari Hat',
 'hrb1': 'Pink Bow',
 'hrb2': 'Red Bow',
 'hrb3': 'Purple Bow',
 'hht1': 'Pink Heart',
 'hht2': 'Yellow Heart',
 'htp1': 'Black Top Hat',
 'htp2': 'Blue Top Hat',
 'hav1': 'Anvil Hat',
 'hfp1': 'Flower Hat',
 'hsg1': 'Sandbag Hat',
 'hwt1': 'Weight Hat',
 'hfz1': 'Fez Hat',
 'hgf1': 'Golf Hat',
 'hpt1': 'Party Hat',
 'hpt2': 'Toon Party Hat',
 'hpb1': 'Fancy Hat',
 'hcr1': 'Crown',
 'hcw1': 'Cowboy Hat',
 'hpr1': 'Pirate Hat',
 'hpp1': 'Propeller Hat',
 'hfs1': 'Fishing Hat',
 'hsb1': 'Sombrero Hat',
 'hst1': 'Straw Hat',
 'hsu1': 'Sun Hat',
 'hrb4': 'Yellow Bow',
 'hrb5': 'Checker Bow',
 'hrb6': 'Light Red Bow',
 'hrb7': 'Rainbow Bow',
 'hat1': 'Antenna Thingy',
 'hhd1': 'Beehive Hairdo',
 'hbw1': 'Bowler Hat',
 'hch1': 'Chef Hat',
 'hdt1': 'Detective Hat',
 'hft1': 'Fancy Feathers Hat',
 'hfd1': 'Fedora',
 'hmk1': "Mickey's Band Hat",
 'hft2': 'Feather Headband',
 'hhd2': 'Pompadour Hairdo',
 'hpc1': 'Princess Hat',
 'hrh1': 'Archer Hat',
 'hhm1': 'Roman Helmet',
 'hat2': 'Spider Antenna Thingy',
 'htr1': 'Tiara',
 'hhm2': 'Viking Helmet',
 'hwz1': 'Witch Hat',
 'hwz2': 'Wizard Hat',
 'hhm3': 'Conquistador Helmet',
 'hhm4': 'Firefighter Helmet',
 'hfp2': 'Anti-Cog Control Hat',
 'hhm5': 'Miner Hat',
 'hnp1': 'Napoleon Hat',
 'hpc2': 'Pilot Cap',
 'hph1': 'Cop Hat',
 'hwg1': 'Rainbow Wacky Wig',
 'hbb4': 'Yellow Baseball Cap',
 'hbb5': 'Red Baseball Cap',
 'hbb6': 'Aqua Baseball Cap',
 'hsl1': 'Sailor Hat',
 'hfr1': 'Samba Hat',
 'hby1': 'Bobby Hat',
 'hrb8': 'Pink Dots Bow',
 'hjh1': 'Jester Hat',
 'hbb7': 'Purple Baseball Cap',
 'hrb9': 'Green Checker Bow',
 'hwt2': 'Winter Hat',
 'hhw1': 'Bandana',
 'hhw2': 'Toonosaur Hat',
 'hob1': 'Jamboree Hat',
 'hbn1': 'Bird Hat by Brianna'}
GlassesStylesDescriptions = {'grd1': 'Round Glasses',
 'gmb1': 'White Mini Blinds',
 'gnr1': 'Purple Narrow Glasses',
 'gst1': 'Yellow Star Glasses',
 'g3d1': 'Movie Glasses',
 'gav1': 'Aviator',
 'gce1': 'Cateye Glasses',
 'gdk1': 'Nerd Glasses',
 'gjo1': 'Celebrity Shades',
 'gsb1': 'Scuba Mask',
 'ggl1': 'Goggles',
 'ggm1': 'Groucho Glasses',
 'ghg1': 'Heart Glasses',
 'gie1': 'Bug Eye Glasses',
 'gmt1': 'Black Secret ID Mask',
 'gmt2': 'Blue Secret ID Mask',
 'gmt3': 'Blue Carnivale Mask',
 'gmt4': 'Purple Carnivale Mask',
 'gmt5': 'Aqua Carnivale Mask',
 'gmn1': 'Monocle',
 'gmo1': 'Smooch Glasses',
 'gsr1': 'Square Frame Glasses',
 'ghw1': 'Skull Eyepatch',
 'ghw2': 'Gem Eyepatch',
 'gag1': 'Alien Eyes by Alexandra'}
BackpackStylesDescriptions = {'bpb1': 'Blue Backpack',
 'bpb2': 'Orange Backpack',
 'bpb3': 'Purple BackPack',
 'bpd1': 'Red Dot Backpack',
 'bpd2': 'Yellow Dot Backpack',
 'bwg1': 'Bat Wings',
 'bwg2': 'Bee Wings',
 'bwg3': 'DragonFly Wings',
 'bst1': 'Scuba Tank',
 'bfn1': 'Shark Fin',
 'baw1': 'White Angel Wings',
 'baw2': 'Rainbow Angel Wings',
 'bwt1': 'Toys Backpack',
 'bwg4': 'Butterfly Wings',
 'bwg5': 'Pixie Wings',
 'bwg6': 'Dragon Wings',
 'bjp1': 'Jet Pack',
 'blg1': 'Bug Backpack',
 'bsa1': 'Plush Bear Pack',
 'bwg7': 'Bird wings',
 'bsa2': 'Plush Cat Pack',
 'bsa3': 'Plush Dog Pack',
 'bap1': 'Airplane Wings',
 'bhw1': 'Pirate Sword',
 'bhw2': 'Super Toon Cape',
 'bhw3': 'Vampire Cape',
 'bhw4': 'Toonosaur Backpack',
 'bob1': 'Jamboree Pack',
 'bfg1': 'Gag Attack Pack',
 'bfl1': 'Cog Pack by Savanah'}
ShoesStylesDescriptions = {'sat1': 'Green Athletic Shoes',
 'sat2': 'Red Athletic Shoes',
 'smb1': 'Green Toon Boots',
 'scs1': 'Green Sneakers',
 'swt1': 'Wingtips',
 'smj1': 'Black Fancy Shoes',
 'sdk1': 'Boat Shoes',
 'sat3': 'Yellow Athletic Shoes',
 'scs2': 'Black Sneakers',
 'scs3': 'White Sneakers',
 'scs4': 'Pink Sneakers',
 'scb1': 'Cowboy Boots',
 'sfb1': 'Purple Boots',
 'sht1': 'Green Hi Top Sneakers',
 'smj2': 'Brown Fancy Shoes',
 'smj3': 'Red Fancy Shoes',
 'ssb1': 'Red Super Toon Boots',
 'sts1': 'Green Tennis Shoes',
 'sts2': 'Pink Tennis Shoes',
 'scs5': 'Red Sneakers',
 'smb2': 'Aqua Toon Boots',
 'smb3': 'Brown Toon Boots',
 'smb4': 'Yellow Toon Boots',
 'sfb2': 'Blue Square Boots',
 'sfb3': 'Green Hearts Boots',
 'sfb4': 'Grey Dots Boots',
 'sfb5': 'Orange Stars Boots',
 'sfb6': 'Pink Stars Boots',
 'slf1': 'Loafers',
 'smj4': 'Purple Fancy Shoes',
 'smt1': 'Motorcycle Boots',
 'sox1': 'Oxfords',
 'srb1': 'Pink Rain Boots',
 'sst1': 'Jolly Boots',
 'swb1': 'Beige Winter Boots',
 'swb2': 'Pink Winter Boots',
 'swk1': 'Work Boots',
 'scs6': 'Yellow Sneakers',
 'smb5': 'Pink Toon Boots',
 'sht2': 'Pink Hi Top Sneakers',
 'srb2': 'Red Dots Rain Boots',
 'sts3': 'Purple Tennis Shoes',
 'sts4': 'Violet Tennis Shoes',
 'sts5': 'Yellow Tennis Shoes',
 'srb3': 'Blue Rain Boots',
 'srb4': 'Yellow Rain Boots',
 'sat4': 'Black Athletic Shoes',
 'shw1': 'Pirate Shoes',
 'shw2': 'Toonosaur Feet'}
AccessoryNamePrefix = {0: 'hat unisex ',
 1: 'glasses unisex ',
 2: 'backpack unisex ',
 3: 'shoes unisex ',
 4: 'hat boy ',
 5: 'glasses boy ',
 6: 'backpack boy ',
 7: 'shoes boy ',
 8: 'hat girl ',
 9: 'glasses girl ',
 10: 'backpack girl ',
 11: 'shoes girl '}
AwardManagerAccessoryNames = {}
AccessoryTypeNames = {}
for accessoryId in list(CatalogAccessoryItemGlobals.AccessoryTypes.keys()):
    accessoryInfo = CatalogAccessoryItemGlobals.AccessoryTypes[accessoryId]
    if accessoryInfo[0] % 4 == 0:
        accessoryStyleDescription = HatStylesDescriptions
    elif accessoryInfo[0] % 4 == 1:
        accessoryStyleDescription = GlassesStylesDescriptions
    elif accessoryInfo[0] % 4 == 2:
        accessoryStyleDescription = BackpackStylesDescriptions
    else:
        accessoryStyleDescription = ShoesStylesDescriptions
    if accessoryInfo[3]:
        AwardManagerAccessoryNames[accessoryId] = AccessoryNamePrefix[accessoryInfo[0]] + accessoryStyleDescription[accessoryInfo[1]]
    AccessoryTypeNames[accessoryId] = accessoryStyleDescription[accessoryInfo[1]]

ShirtStylesDescriptions = {'bss1': 'solid',
 'bss2': 'single stripe',
 'bss3': 'collar',
 'bss4': 'double stripe',
 'bss5': 'multiple stripes',
 'bss6': 'collar w/ pocket',
 'bss7': 'hawaiian',
 'bss8': 'collar w/ 2 pockets',
 'bss9': 'bowling shirt',
 'bss10': 'vest (special)',
 'bss11': 'collar w/ ruffles',
 'bss12': 'soccer jersey (special)',
 'bss13': 'lightning bolt (special)',
 'bss14': 'jersey 19 (special)',
 'bss15': 'guayavera',
 'gss1': 'girl solid',
 'gss2': 'girl single stripe',
 'gss3': 'girl collar',
 'gss4': 'girl double stripes',
 'gss5': 'girl collar w/ pocket',
 'gss6': 'girl flower print',
 'gss7': 'girl flower trim (special)',
 'gss8': 'girl collar w/ 2 pockets',
 'gss9': 'girl denim vest (special)',
 'gss10': 'girl peasant',
 'gss11': 'girl peasant w/ mid stripe',
 'gss12': 'girl soccer jersey (special)',
 'gss13': 'girl hearts',
 'gss14': 'girl stars (special)',
 'gss15': 'girl flower',
 'c_ss1': 'yellow hooded - Series 1',
 'c_ss2': 'yellow with palm tree - Series 1',
 'c_ss3': 'purple with stars - Series 2',
 'c_bss1': 'blue stripes (boys only) - Series 1',
 'c_bss2': 'orange (boys only) - Series 1',
 'c_bss3': 'lime green with stripe (boys only) - Series 2',
 'c_bss4': 'red kimono with checkerboard (boys only) - Series 2',
 'c_gss1': 'girl blue with yellow stripes (girls only) - Series 1',
 'c_gss2': 'girl pink and beige with flower (girls only) - Series 1',
 'c_gss3': 'girl Blue and gold with wavy stripes (girls only) - Series 2',
 'c_gss4': 'girl Blue and pink with bow (girls only) - Series 2',
 'c_gss5': 'girl Aqua kimono white stripe (girls only) - UNUSED',
 'c_ss4': 'Tie dye shirt (boys and girls) - Series 3',
 'c_ss5': 'light blue with blue and white stripe (boys only) - Series 3',
 'c_ss6': 'cowboy shirt 1 : Series 4',
 'c_ss7': 'cowboy shirt 2 : Series 4',
 'c_ss8': 'cowboy shirt 3 : Series 4',
 'c_ss9': 'cowboy shirt 4 : Series 4',
 'c_ss10': 'cowboy shirt 5 : Series 4',
 'c_ss11': 'cowboy shirt 6 : Series 4',
 'hw_ss1': 'Halloween Ghost',
 'hw_ss2': 'Halloween Pumpkin',
 'hw_ss3': 'Halloween Vampire',
 'hw_ss4': 'Halloween Turtle',
 'hw_ss5': 'Halloween Bee',
 'hw_ss6': 'Halloween Pirate',
 'hw_ss7': 'Halloween SuperToon',
 'hw_ss8': 'Halloween Vampire NoCape',
 'hw_ss9': 'Halloween Dinosaur',
 'wh_ss1': 'Winter Holiday 1',
 'wh_ss2': 'Winter Holiday 2',
 'wh_ss3': 'Winter Holiday 3',
 'wh_ss4': 'Winter Holiday 4',
 'vd_ss1': 'girl Valentines day, pink with red hearts (girls)',
 'vd_ss2': 'Valentines day, red with white hearts',
 'vd_ss3': 'Valentines day, white with winged hearts (boys)',
 'vd_ss4': ' Valentines day, pink with red flamed heart',
 'vd_ss5': '2009 Valentines day, white with red cupid',
 'vd_ss6': '2009 Valentines day, blue with green and red hearts',
 'vd_ss7': '2010 Valentines day, red with white wings',
 'sd_ss1': "St Pat's Day, four leaf clover shirt",
 'sd_ss2': "St Pat's Day, pot o gold shirt",
 'sd_ss3': 'Ides of March greenToon shirt',
 'tc_ss1': 'T-Shirt Contest, Fishing Vest',
 'tc_ss2': 'T-Shirt Contest, Fish Bowl',
 'tc_ss3': 'T-Shirt Contest, Paw Print',
 'tc_ss4': 'T-Shirt Contest, Backpack',
 'tc_ss5': 'T-Shirt Contest, Lederhosen ',
 'tc_ss6': 'T-Shirt Contest, Watermelon  ',
 'tc_ss7': 'T-Shirt Contest, Race Shirt',
 'j4_ss1': 'July 4th, Flag',
 'j4_ss2': 'July 4th, Fireworks',
 'c_ss12': 'Catalog series 7, Green w/ yellow buttons',
 'c_ss13': 'Catalog series 7, Purple w/ big flower',
 'pj_ss1': 'Blue Banana Pajama shirt',
 'pj_ss2': 'Red Horn Pajama shirt',
 'pj_ss3': 'Purple Glasses Pajama shirt',
 'sa_ss1': 'Award Striped Shirt',
 'sa_ss2': 'Award Fishing Shirt 1',
 'sa_ss3': 'Award Fishing Shirt 2',
 'sa_ss4': 'Award Gardening Shirt 1',
 'sa_ss5': 'Award Gardening Shirt 2',
 'sa_ss6': 'Award Party Shirt 1',
 'sa_ss7': 'Award Party Shirt 2',
 'sa_ss8': 'Award Racing Shirt 1',
 'sa_ss9': 'Award Racing Shirt 2',
 'sa_ss10': 'Award Summer Shirt 1',
 'sa_ss11': 'Award Summer Shirt 2',
 'sa_ss12': 'Award Golf Shirt 1',
 'sa_ss13': 'Award Golf Shirt 2',
 'sa_ss14': 'Award Halloween Bee Shirt',
 'sa_ss15': 'Award Halloween SuperToon Shirt',
 'sa_ss16': 'Award Matathon Shirt 1',
 'sa_ss17': 'Award Save Building Shirt 1',
 'sa_ss18': 'Award Save Building Shirt 2',
 'sa_ss19': 'Award Toontask Shirt 1',
 'sa_ss20': 'Award Toontask Shirt 2',
 'sa_ss21': 'Award Trolley Shirt 1',
 'sa_ss22': 'Award Trolley Shirt 2',
 'sa_ss23': 'Award Winter Shirt 1',
 'sa_ss24': 'Award Halloween Skeleton Shirt',
 'sa_ss25': 'Award Halloween Spider Shirt',
 'sa_ss26': 'Award Most Cogs Defeated Shirt',
 'sa_ss27': 'Award Most V.P.s Defeated Shirt',
 'sa_ss28': 'Award Sellbot Smasher Shirt',
 'sa_ss29': 'Award Most C.J.s Defeated Shirt',
 'sa_ss30': 'Award Lawbot Smasher Shirt',
 'sa_ss31': 'Award Racing Shirt 3',
 'sa_ss32': 'Award Fishing Shirt 4',
 'sa_ss33': 'Award Golf Shirt 3',
 'sa_ss34': 'Award Most Cogs Defeated Shirt 2',
 'sa_ss35': 'Award Racing Shirt 4',
 'sa_ss36': 'Award Save Building Shirt 3',
 'sa_ss37': 'Award Trolley Shirt 3',
 'sa_ss38': 'Award Fishing Shirt 5',
 'sa_ss39': 'Award Golf Shirt 4',
 'sa_ss40': 'Award Halloween Witchy Moon Shirt',
 'sa_ss41': 'Award Winter Holiday Sled Shirt',
 'sa_ss42': 'Award Halloween Batty Moon Shirt',
 'sa_ss43': 'Award Winter Holiday Mittens Shirt',
 'sa_ss44': 'Award Fishing Shirt 6',
 'sa_ss45': 'Award Fishing Shirt 7',
 'sa_ss46': 'Award Golf Shirt 5',
 'sa_ss47': 'Award Racing Shirt 5',
 'sa_ss48': 'Award Racing Shirt 6',
 'sa_ss49': 'Award Most Cogs Defeated shirt 3',
 'sa_ss50': 'Award Most Cogs Defeated shirt 4',
 'sa_ss51': 'Award Trolley shirt 4',
 'sa_ss52': 'Award Trolley shirt 5',
 'sa_ss53': 'Award Save Building Shirt 4',
 'sa_ss54': 'Award Save Building Shirt 5',
 'sa_ss55': 'Award Anniversary',
 'sc_1': 'Scientist top 1',
 'sc_2': 'Scientist top 2',
 'sc_3': 'Scientist top 3',
 'sil_1': 'Silly Mailbox Shirt',
 'sil_2': 'Silly Trash Can Shirt',
 'sil_3': 'Loony Labs Shirt',
 'sil_4': 'Silly Hydrant Shirt',
 'sil_5': 'Sillymeter Whistle Shirt',
 'sil_6': 'Silly Cog-Crusher Shirt',
 'sil_7': 'Victory Party Shirt 1',
 'sil_8': 'Victory Party Shirt 2',
 'emb_us1': 'placeholder emblem shirt 1',
 'emb_us2': 'placeholder emblem shirt 2',
 'emb_us3': 'placeholder emblem shirt 3',
 'sb_1': 'Sellbot Icon Shirt',
 'lb_1': 'Lawbot Icon Shirt',
 'jb_1': 'Jellybean Shirt',
 'jb_2': 'Doodle Shirt',
 'ugcms': 'Get Connected Mover & Shaker'}
BottomStylesDescriptions = {'bbs1': 'plain w/ pockets',
 'bbs2': 'belt',
 'bbs3': 'cargo',
 'bbs4': 'hawaiian',
 'bbs5': 'side stripes (special)',
 'bbs6': 'soccer shorts',
 'bbs7': 'side flames (special)',
 'bbs8': 'denim',
 'vd_bs1': 'Valentines shorts',
 'vd_bs2': 'Green with red heart',
 'vd_bs3': 'Blue denim with green and red heart',
 'c_bs1': 'Orange with blue side stripes',
 'c_bs2': 'Blue with gold cuff stripes',
 'c_bs5': 'Green stripes - series 7',
 'sd_bs1': 'St. Pats leprechaun shorts',
 'sd_bs2': 'Ides of March greenToon shorts',
 'pj_bs1': 'Blue Banana Pajama pants',
 'pj_bs2': 'Red Horn Pajama pants',
 'pj_bs3': 'Purple Glasses Pajama pants',
 'wh_bs1': 'Winter Holiday Shorts Style 1',
 'wh_bs2': 'Winter Holiday Shorts Style 2',
 'wh_bs3': 'Winter Holiday Shorts Style 3',
 'wh_bs4': 'Winter Holiday Shorts Style 4',
 'hw_bs1': 'Halloween Bee Shorts male',
 'hw_bs2': 'Halloween Pirate Shorts male',
 'hw_bs5': 'Halloween SuperToon Shorts male',
 'hw_bs6': 'Halloween Vampire NoCape Shorts male',
 'hw_bs7': 'Halloween Dinosaur Shorts male',
 'sil_bs1': 'Silly Cog-Crusher Shorts',
 'gsk1': 'solid',
 'gsk2': 'polka dots (special)',
 'gsk3': 'vertical stripes',
 'gsk4': 'horizontal stripe',
 'gsk5': 'flower print',
 'gsk6': '2 pockets (special) ',
 'gsk7': 'denim skirt',
 'gsh1': 'plain w/ pockets',
 'gsh2': 'flower',
 'gsh3': 'denim shorts',
 'c_gsk1': 'blue skirt with tan border and button',
 'c_gsk2': 'purple skirt with pink and ribbon',
 'c_gsk3': 'teal skirt with yellow and star',
 'vd_gs1': 'red skirt with hearts',
 'vd_gs2': 'Pink flair skirt with polka hearts',
 'vd_gs3': 'Blue denim skirt with green and red heart',
 'c_gsk4': 'rainbow skirt - Series 3',
 'sd_gs1': 'St. Pats day shorts',
 'sd_gs2': 'Ides of March greenToon skirt',
 'c_gsk5': 'Western skirts 1',
 'c_gsk6': 'Western skirts 2',
 'c_bs3': 'Western shorts 1',
 'c_bs4': 'Western shorts 2',
 'j4_bs1': 'July 4th shorts',
 'j4_gs1': 'July 4th Skirt',
 'c_gsk7': 'Blue with flower - series 7',
 'pj_gs1': 'Blue Banana Pajama pants',
 'pj_gs2': 'Red Horn Pajama pants',
 'pj_gs3': 'Purple Glasses Pajama pants',
 'wh_gsk1': 'Winter Holiday Skirt Style 1',
 'wh_gsk2': 'Winter Holiday Skirt Style 2',
 'wh_gsk3': 'Winter Holiday Skirt Style 3',
 'wh_gsk4': 'Winter Holiday Skirt Style 4',
 'sa_bs1': 'Award Fishing Shorts',
 'sa_bs2': 'Award Gardening Shorts',
 'sa_bs3': 'Award Party Shorts',
 'sa_bs4': 'Award Racing Shorts',
 'sa_bs5': 'Award Summer Shorts',
 'sa_bs6': 'Award Golf Shorts 1',
 'sa_bs7': 'Award Halloween Bee Shorts',
 'sa_bs8': 'Award Halloween SuperToon Shorts',
 'sa_bs9': 'Award Save Building Shorts 1',
 'sa_bs10': 'Award Trolley Shorts 1',
 'sa_bs11': 'Award Halloween Spider Shorts',
 'sa_bs12': 'Award Halloween Skeleton Shorts',
 'sa_bs13': 'Award Sellbot Smasher Shorts male',
 'sa_bs14': 'Award Lawbot Smasher Shorts male',
 'sa_bs15': 'Award Racing Shorts 1',
 'sa_bs16': 'Award Golf Shorts 3',
 'sa_bs17': 'Award Racing Shorts 4',
 'sa_bs18': 'Award Golf Shorts 4',
 'sa_bs19': 'Award Golf Shorts 5',
 'sa_bs20': 'Award Racing Shorts 5',
 'sa_bs21': 'Award Racing Shorts 6',
 'sa_gs1': 'Award Fishing Skirt',
 'sa_gs2': 'Award Gardening Skirt',
 'sa_gs3': 'Award Party Skirt',
 'sa_gs4': 'Award Racing Skirt',
 'sa_gs5': 'Award Summer Skirt',
 'sa_gs6': 'Award Golf Skirt 1',
 'sa_gs7': 'Award Halloween Bee Skirt',
 'sa_gs8': 'Award Halloween SuperToon Skirt',
 'sa_gs9': 'Award Save Building Skirt 1',
 'sa_gs10': 'Award Trolley Skirt 1',
 'sa_gs11': 'Award Halloween Skeleton Skirt',
 'sa_gs12': 'Award Halloween Spider Skirt',
 'sa_gs13': 'Award Sellbot Smasher Shorts female',
 'sa_gs14': 'Award Lawbot Smasher Shorts female',
 'sa_gs15': 'Award Racing Skirt 1',
 'sa_gs16': 'Award Golf Skirt 2',
 'sa_gs17': 'Award Racing Skirt 4',
 'sa_gs18': 'Award Golf Skirt 3',
 'sa_gs19': 'Award Golf Skirt 4',
 'sa_gs20': 'Award Racing Skirt 5',
 'sa_gs21': 'Award Racing Skirt 6',
 'sc_bs1': 'Scientist bottom male 1',
 'sc_bs2': 'Scientist bottom male 2',
 'sc_bs3': 'Scientist bottom male 3',
 'sc_gs1': 'Scientist bottom female 1',
 'sc_gs2': 'Scientist bottom female 2',
 'sc_gs3': 'Scientist bottom female 3',
 'sil_bs1': 'Silly Cog-Crusher Shorts male',
 'sil_gs1': 'Silly Cog-Crusher Shorts female',
 'hw_bs3': 'Halloween Vampire Shorts male',
 'hw_gs3': 'Halloween Vampire Shorts female',
 'hw_bs4': 'Halloween Turtle Shorts male',
 'hw_gs4': 'Halloween Turtle Shorts female',
 'hw_gs1': 'Halloween Bee Shorts female',
 'hw_gs2': 'Halloween Pirate Shorts female',
 'hw_gs5': 'Halloween SuperToon Shorts female',
 'hw_gs6': 'Halloween Vampire NoCape Shorts female',
 'hw_gs7': 'Halloween Dinosaur Shorts female',
 'hw_gsk1': 'Halloween Pirate Skirt'}
AwardMgrBoy = 'boy'
AwardMgrGirl = 'girl'
AwardMgrUnisex = 'unisex'
AwardMgrShorts = 'shorts'
AwardMgrSkirt = 'skirt'
AwardMgrShirt = 'shirt'
SpecialEventMailboxStrings = {1: 'A special item from the Toon Council just for you!',
 2: "Here is your Melville's Fishing Tournament prize! Congratulations!",
 3: "Here is your Billy Budd's Fishing Tournament prize! Congratulations!",
 4: 'Here is your Acorn Acres April Invitational prize! Congratulations!',
 5: 'Here is your Acorn Acres C.U.P. Championship prize! Congratulations!',
 6: 'Here is your Gift-Giving Extravaganza prize! Congratulations!',
 7: "Here is your Top Toons New Year's Day Marathon prize! Congratulations!",
 8: 'Here is your Perfect Trolley Games Weekend prize! Congratulations!',
 9: 'Here is your Trolley Games Madness prize! Congratulations!',
 10: 'Here is your Grand Prix Weekend prize! Congratulations!',
 11: 'Here is your ToonTask Derby prize! Congratulations!',
 12: 'Here is your Save a Building Marathon prize! Congratulations!',
 13: 'Here is your Most Cogs Defeated Tournament prize! Congratulations!',
 14: 'Here is your Most V.P.s Defeated Tournament prize! Congratulations!',
 15: 'Here is your Operation: Storm Sellbot prize! Congratulations!',
 16: 'Here is your Most C.J.s Defeated Tournament prize! Congratulations!',
 17: 'Here is your Operation: Lawbots Lose prize! Congratulations!'}
RentalHours = 'Hours'
RentalOf = 'Of'
RentalCannon = 'Cannons!'
RentalGameTable = 'Game Table!'
EstateCannonGameEnd = 'The Cannon Game rental is over.'
GameTableRentalEnd = 'The Game Table rental is over.'
MessageConfirmRent = 'Begin rental? Cancel to save the rental for later'
MessageConfirmGarden = 'Are you sure you want to start a garden?'
NametagPaid = 'Citizen Name Tag'
NametagAction = 'Action Name Tag'
NametagFrilly = 'Frilly Name Tag'
FurnitureYourOldCloset = 'your old wardrobe'
FurnitureYourOldBank = 'your old bank'
FurnitureYourOldTrunk = 'your old trunk'
TrunkHatGUI = 'Hats'
TrunkGlassesGUI = 'Glasses'
TrunkBackpackGUI = 'Backpacks'
TrunkShoesGUI = 'Shoes'
ChatItemQuotes = '"%s"'
FurnitureNames = {100: 'Armchair',
 105: 'Armchair',
 110: 'Chair',
 120: 'Desk Chair',
 130: 'Log Chair',
 140: 'Lobster Chair',
 145: 'Lifejacket Chair',
 150: 'Saddle Stool',
 160: 'Native Chair',
 170: 'Cupcake Chair',
 200: 'Bed',
 205: 'Bed',
 210: 'Bed',
 220: 'Bathtub Bed',
 230: 'Leaf Bed',
 240: 'Boat Bed',
 250: 'Cactus Hammock',
 260: 'Ice Cream Bed',
 270: "Olivia Erin & Cat's Bed",
 300: 'Player Piano',
 310: 'Pipe Organ',
 400: 'Fireplace',
 410: 'Fireplace',
 420: 'Round Fireplace',
 430: 'Fireplace',
 440: 'Apple Fireplace',
 450: "Erin's Fireplace",
 460: "Erin's Lit Fireplace",
 470: 'Lit Fireplace',
 480: 'Round Lit Fireplace',
 490: 'Lit Fireplace',
 491: 'Lit Fireplace',
 492: 'Apple Lit Fireplace',
 500: 'Wardrobe',
 502: '15 item Wardrobe',
 504: '20 item Wardrobe',
 506: '25 item Wardrobe',
 508: '50 item Wardrobe',
 510: 'Wardrobe',
 512: '15 item Wardrobe',
 514: '20 item Wardrobe',
 516: '25 item Wardrobe',
 518: '50 item Wardrobe',
 600: 'Short Lamp',
 610: 'Tall Lamp',
 620: 'Table Lamp',
 625: 'Table Lamp',
 630: 'Daisy Lamp',
 640: 'Daisy Lamp',
 650: 'Jellyfish Lamp',
 660: 'Jellyfish Lamp',
 670: 'Cowboy Lamp',
 680: 'Candle',
 681: 'Lit Candle',
 700: 'Cushioned Chair',
 705: 'Cushioned Chair',
 710: 'Couch',
 715: 'Couch',
 720: 'Hay Couch',
 730: 'Shortcake Couch',
 800: 'Desk',
 810: 'Log Desk',
 900: 'Umbrella Stand',
 910: 'Coat Rack',
 920: 'Trash Can',
 930: 'Red Mushroom',
 940: 'Yellow Mushroom',
 950: 'Coat Rack',
 960: 'Barrel Stand',
 970: 'Cactus Plant',
 980: 'Teepee',
 990: "Juliette's Fan",
 1000: 'Large Rug',
 1010: 'Round Rug',
 1015: 'Round Rug',
 1020: 'Small Rug',
 1030: 'Leaf Mat',
 1040: 'Presents',
 1050: 'Sled',
 1100: 'Display Cabinet',
 1110: 'Display Cabinet',
 1120: 'Tall Bookcase',
 1130: 'Low Bookcase',
 1140: 'Sundae Chest',
 1200: 'End Table',
 1210: 'Small Table',
 1215: 'Small Table',
 1220: 'Coffee Table',
 1230: 'Coffee Table',
 1240: "Snorkeler's Table",
 1250: 'Cookie Table',
 1260: 'Bedroom Table',
 1300: '1000 Bean Bank',
 1310: '2500 Bean Bank',
 1320: '5000 Bean Bank',
 1330: '7500 Bean Bank',
 1340: '10000 Bean Bank',
 1350: '12000 Bean Bank',
 1399: 'Telephone',
 1400: 'Cezanne Toon',
 1410: 'Flowers',
 1420: 'Modern Mickey',
 1430: 'Rembrandt Toon',
 1440: 'Toonscape',
 1441: "Whistler's Horse",
 1442: 'Toon Star',
 1443: 'Not a Pie',
 1450: 'Mickey and Minnie',
 1500: 'Radio',
 1510: 'Radio',
 1520: 'Radio',
 1530: 'Television',
 1600: 'Short Vase',
 1610: 'Tall Vase',
 1620: 'Short Vase',
 1630: 'Tall Vase',
 1640: 'Short Vase',
 1650: 'Short Vase',
 1660: 'Coral Vase',
 1661: 'Shell Vase',
 1670: 'Rose Vase',
 1680: 'Rose Watercan',
 1700: 'Popcorn Cart',
 1710: 'Ladybug',
 1720: 'Fountain',
 1725: 'Washing Machine',
 1800: 'Fish Bowl',
 1810: 'Fish Bowl',
 1900: 'Swordfish',
 1910: 'Hammerhead',
 1920: 'Hanging Horns',
 1930: 'Simple Sombrero',
 1940: 'Fancy Sombrero',
 1950: 'Dream Catcher',
 1960: 'Horseshoe',
 1970: 'Bison Portrait',
 2000: 'Candy Swing Set',
 2010: 'Cake Slide',
 3000: 'Banana Split Tub',
 4000: 'Boy Trunk',
 4010: 'Girl Trunk',
 10000: 'Short Pumpkin',
 10010: 'Tall Pumpkin',
 10020: 'Winter Tree',
 10030: 'Winter Wreath'}
AwardManagerFurnitureNames = {100: 'Armchair A - Series 1',
 105: 'Armchair A - Series 7',
 110: 'Chair - Series 1',
 120: 'Desk Chair - Series 2',
 130: 'Log Chair - Series 2',
 140: 'Lobster Chair - Series 3',
 145: 'Lifejacket Chair - Series 3',
 150: 'Saddle Stool - Series 4',
 160: 'Native Chair - Series 4',
 170: 'Cupcake Chair - Series 6',
 200: "Bed Boy's bed - Initial Furniture",
 205: "Bed Boy's bed Series 7",
 210: "Bed Girl's bed - Series 1",
 220: 'Bathtub Bed',
 230: 'Leaf Bed',
 240: 'Boat Bed',
 250: 'Cactus Hammock',
 260: 'Ice Cream Bed',
 270: "Olivia Erin & Cat's Bed - Trolley Bed",
 300: 'Player Piano',
 310: 'Pipe Organ',
 400: 'Fireplace - Square Fireplace Initial Furniture',
 410: 'Fireplace - Girly Fireplace Series 1',
 420: 'Round Fireplace',
 430: 'Fireplace - bug room series 2',
 440: 'Apple Fireplace',
 450: "Erin's Fireplace - coral",
 460: "Erin's Lit Fireplace - coral",
 470: 'Lit Fireplace - square fireplace with fire',
 480: 'Round Lit Fireplace',
 490: 'Lit Fireplac - girl fireplace with firee',
 491: 'Lit Fireplace - bug room fireplace',
 492: 'Apple Lit Fireplace',
 500: 'boy Wardrobe - 10 items initial',
 502: 'boy 15 item Wardrobe',
 504: 'boy 20 item Wardrobe',
 506: 'boy 25 item Wardrobe',
 508: 'boy 50 item Wardrobe',
 510: 'girl Wardrobe -  10 items initial',
 512: 'girl 15 item Wardrobe',
 514: 'girl 20 item Wardrobe',
 516: 'girl 25 item Wardrobe',
 518: 'girl 50 item Wardrobe',
 600: 'Short Lamp',
 610: 'Tall Lamp',
 620: 'Table Lamp - Series 1',
 625: 'Table Lamp - Series 7',
 630: 'Daisy Lamp 1',
 640: 'Daisy Lamp 2',
 650: 'Jellyfish Lamp 1',
 660: 'Jellyfish Lamp 2',
 670: 'Cowboy Lamp',
 680: 'Candle',
 681: 'Lit Candle',
 700: 'Cushioned Chair - Series 1',
 705: 'Cushioned Chair - Series 7',
 710: 'Couch - series 1',
 715: 'Couch - series 7',
 720: 'Hay Couch',
 730: 'Shortcake Couch',
 800: 'Desk',
 810: 'Log Desk',
 900: 'Umbrella Stand',
 910: 'Coat Rack - series 1',
 920: 'Trash Can',
 930: 'Red Mushroom',
 940: 'Yellow Mushroom',
 950: 'Coat Rack - underwater',
 960: 'Barrel Stand',
 970: 'Cactus Plant',
 980: 'Teepee',
 990: "Juliette's Fan - gag fan",
 1000: 'Large Rug',
 1010: 'Round Rug - Series 1',
 1015: 'Round Rug - Series 7',
 1020: 'Small Rug',
 1030: 'Leaf Mat',
 1040: 'Presents',
 1050: 'Sled',
 1100: 'Display Cabinet - Red',
 1110: 'Display Cabinet - Yellow',
 1120: 'Tall Bookcase',
 1130: 'Low Bookcase',
 1140: 'Sundae Chest',
 1200: 'End Table',
 1210: 'Small Table - series 1 ',
 1215: 'Small Table - series 7',
 1220: 'Coffee Table sq',
 1230: 'Coffee Table bw',
 1240: "Snorkeler's Table",
 1250: 'Cookie Table',
 1260: 'Bedroom Table',
 1300: '1000 Bean Bank',
 1310: '2500 Bean Bank',
 1320: '5000 Bean Bank',
 1330: '7500 Bean Bank',
 1340: '10000 Bean Bank',
 1350: '12000 Bean Bank',
 1399: 'Telephone',
 1400: 'Cezanne Toon',
 1410: 'Flowers',
 1420: 'Modern Mickey',
 1430: 'Rembrandt Toon',
 1440: 'Toonscape',
 1441: "Whistler's Horse",
 1442: 'Toon Star',
 1443: 'Not a Pie',
 1450: 'Mickey and Minnie',
 1500: 'Radio A series 2',
 1510: 'Radio B series 1',
 1520: 'Radio C series 2',
 1530: 'Television',
 1600: 'Short Vase A',
 1610: 'Tall Vase A',
 1620: 'Short Vase B',
 1630: 'Tall Vase B',
 1640: 'Short Vase C',
 1650: 'Short Vase D',
 1660: 'Coral Vase',
 1661: 'Shell Vase',
 1670: 'Rose Vase',
 1680: 'Rose Watercan',
 1700: 'Popcorn Cart',
 1710: 'Ladybug',
 1720: 'Fountain',
 1725: 'Washing Machine',
 1800: 'Fish Bowl skull',
 1810: 'Fish Bowl lizard',
 1900: 'Swordfish',
 1910: 'Hammerhead',
 1920: 'Hanging Horns',
 1930: 'Simple Sombrero',
 1940: 'Fancy Sombrero',
 1950: 'Dream Catcher',
 1960: 'Horseshoe',
 1970: 'Bison Portrait',
 2000: 'Candy Swing Set',
 2010: 'Cake Slide',
 3000: 'Banana Split Tub',
 4000: 'Boy Trunk',
 4010: 'Girl Trunk',
 10000: 'Short Pumpkin',
 10010: 'Tall Pumpkin',
 10020: 'Winter Tree',
 10030: 'Winter Wreath'}
ClothingArticleNames = ('Shirt',
 'Shirt',
 'Shirt',
 'Shorts',
 'Shorts',
 'Skirt',
 'Shorts')
ClothingTypeNames = {1001: 'Ghost Shirt',
 1002: 'Pumpkin Shirt',
 1112: 'Bee Shirt',
 1113: 'Pirate Shirt',
 1114: 'Super Toon Shirt',
 1115: 'Vampire Shirt',
 1116: 'Toonosaur Shirt',
 1117: 'Bee Shorts',
 1118: 'Pirate Shorts',
 1119: 'Super Toon Shorts',
 1120: 'Vampire Shorts',
 1121: 'Toonosaur Shorts',
 1122: 'Bee Shorts',
 1123: 'Pirate Shorts',
 1124: 'Super Toon Shorts',
 1125: 'Vampire Shorts',
 1126: 'Toonosaur Shorts',
 1127: 'Pirate Skirt',
 1304: "O'Shirt",
 1305: "O'Shorts",
 1306: "O'Skirt",
 1400: "Matthew's Shirt",
 1401: "Jessica's Shirt",
 1402: "Marissa's Shirt",
 1600: 'Trap Outfit',
 1601: 'Sound Outfit',
 1602: 'Lure Outfit',
 1603: 'Trap Outfit',
 1604: 'Sound Outfit',
 1605: 'Lure Outfit',
 1606: 'Trap Outfit',
 1607: 'Sound Outfit',
 1608: 'Lure Outfit',
 1723: 'Bee Shirt',
 1724: 'SuperToon Shirt',
 1734: 'Bee Shorts',
 1735: 'SuperToon Shorts',
 1739: 'Bee Skirt',
 1740: 'SuperToon Skirt',
 1743: 'Skeleton Shirt',
 1744: 'Spider Shirt',
 1745: 'Spider Shorts',
 1746: 'Skeleton Shorts',
 1747: 'Skeleton Skirt',
 1748: 'Spider Skirt',
 1749: 'Silly Mailbox Shirt',
 1750: 'Silly Trash Can Shirt',
 1751: 'Loony Labs Shirt',
 1752: 'Silly Hydrant Shirt',
 1753: 'Silly Meter Shirt',
 1754: 'Cog-Crusher Shirt',
 1755: 'Cog-Crusher Shorts',
 1756: 'Cog-Crusher Shorts',
 1757: 'Victory Party Shirt',
 1758: 'Relaxed Victory Shirt',
 1763: 'Smashed Sellbot Shirt',
 1764: 'Most V.P.s Defeated Shirt',
 1765: 'Sellbot Smasher Shirt',
 1766: 'Sellbot Smasher Shorts',
 1767: 'Sellbot Smasher Shorts',
 1768: 'Jellybean Bank Shirt',
 1769: 'Doodle Shirt',
 1770: 'Vampire Shirt',
 1771: 'Turtle Shirt',
 1772: 'Vampire Shorts',
 1773: 'Vampire Shorts',
 1774: 'Turtle Shorts',
 1775: 'Turtle Shorts',
 1776: 'Get Connected Mover & Shaker Shirt',
 1777: 'Smashed Lawbot Shirt',
 1778: 'Most C.J.s Defeated Shirt',
 1779: 'Lawbot Smasher Shirt',
 1780: 'Lawbot Smasher Shorts',
 1781: 'Lawbot Smasher Shorts',
 1782: 'Racing Shirt 3',
 1783: 'Racing Shorts 1',
 1784: 'Racing Skirt 1',
 1801: 'Batty Moon Shirt',
 1802: 'Mittens Shirt'}
AccessoryArticleNames = ('Hat',
 'Glasses',
 'Backpack',
 'Shoes',
 'Hat',
 'Glasses',
 'Backpack',
 'Shoes',
 'Hat',
 'Glasses',
 'Backpack',
 'Shoes')
SurfaceNames = ('Wallpaper',
 'Moulding',
 'Flooring',
 'Wainscoting',
 'Border')
WallpaperNames = {1000: 'Parchment',
 1100: 'Milan',
 1200: 'Dover',
 1300: 'Victoria',
 1400: 'Newport',
 1500: 'Pastoral',
 1600: 'Harlequin',
 1700: 'Moon',
 1800: 'Stars',
 1900: 'Flowers',
 2000: 'Spring Garden',
 2100: 'Formal Garden',
 2200: 'Race Day',
 2300: 'Touchdown!',
 2400: 'Cloud 9',
 2500: 'Climbing Vine',
 2600: 'Springtime',
 2700: 'Kokeshi',
 2800: 'Posies',
 2900: 'Angel Fish',
 3000: 'Bubbles',
 3100: 'Bubbles',
 3200: 'Go Fish',
 3300: 'Stop Fish',
 3400: 'Sea Horse',
 3500: 'Sea Shells',
 3600: 'Underwater',
 3700: 'Boots',
 3800: 'Cactus',
 3900: 'Cowboy Hat',
 10100: 'Cats',
 10200: 'Bats',
 11000: 'Snowflakes',
 11100: 'Hollyleaf',
 11200: 'Snowman',
 12000: 'ValenToons',
 12100: 'ValenToons',
 12200: 'ValenToons',
 12300: 'ValenToons',
 13000: 'Shamrock',
 13100: 'Shamrock',
 13200: 'Rainbow',
 13300: 'Shamrock'}
FlooringNames = {1000: 'Hardwood Floor',
 1010: 'Carpet',
 1020: 'Diamond Tile',
 1030: 'Diamond Tile',
 1040: 'Grass',
 1050: 'Beige Bricks',
 1060: 'Red Bricks',
 1070: 'Square Tile',
 1080: 'Stone',
 1090: 'Boardwalk',
 1100: 'Dirt',
 1110: 'Wood Tile',
 1120: 'Tile',
 1130: 'Honeycomb',
 1140: 'Water',
 1150: 'Beach Tile',
 1160: 'Beach Tile',
 1170: 'Beach Tile',
 1180: 'Beach Tile',
 1190: 'Sand',
 10000: 'Ice Cube',
 10010: 'Igloo',
 11000: 'Shamrock',
 11010: 'Shamrock'}
MouldingNames = {1000: 'Knotty',
 1010: 'Painted',
 1020: 'Dental',
 1030: 'Flowers',
 1040: 'Flowers',
 1050: 'Ladybug',
 1060: 'ValenToons',
 1070: 'Beach',
 1080: 'Winter Lights 1',
 1085: 'Winter Lights 2',
 1090: 'Winter Lights 3',
 1100: "ValenToon's Cupid",
 1110: "ValenToon's Heart 1",
 1120: "ValenToon's Heart 2"}
WainscotingNames = {1000: 'Painted',
 1010: 'Wood Panel',
 1020: 'Wood',
 1030: 'ValenToons',
 1040: 'Underwater'}
WindowViewNames = {10: 'Large Garden',
 20: 'Wild Garden',
 30: 'Greek Garden',
 40: 'Cityscape',
 50: 'Wild West',
 60: 'Under the Sea',
 70: 'Tropical Island',
 80: 'Starry Night',
 90: 'Tiki Pool',
 100: 'Frozen Frontier',
 110: 'Farm Country',
 120: 'Native Camp',
 130: 'Main Street'}
SpecialEventNames = {1: 'Generic Award',
 2: "Melville's Fishing Tournament",
 3: "Billy Budd's Fishing Tournament",
 4: 'Acorn Acres April Invitational',
 5: 'Acorn Acres C.U.P. Championship',
 6: 'Gift-Giving Extravaganza',
 7: "Top Toons New Year's Day Marathon",
 8: 'Perfect Trolley Games Weekend',
 9: 'Trolley Games Madness',
 10: 'Grand Prix Weekend',
 11: 'ToonTask Derby',
 12: 'Save a Building Marathon',
 13: 'Most Cogs Defeated',
 14: 'Most V.P.s Defeated',
 15: 'Operation Storm Sellbot Event',
 16: 'Most C.J.s Defeated',
 17: 'Operation Lawbots Lose Event'}
NewCatalogNotify = 'There are new items available to order at your phone!'
NewDeliveryNotify = 'A new delivery has just arrived at your mailbox!'
CatalogNotifyFirstCatalog = 'Your first cattlelog has arrived! You may use this to order new items for yourself or for your house.'
CatalogNotifyNewCatalog = 'Your cattlelog #%s has arrived! You can go to your phone to order items from this cattlelog.'
CatalogNotifyNewCatalogNewDelivery = 'A new delivery has arrived at your mailbox! Also, your cattlelog #%s has arrived!'
CatalogNotifyNewDelivery = 'A new delivery has arrived at your mailbox!'
CatalogNotifyNewCatalogOldDelivery = 'Your cattlelog #%s has arrived, and there are still items waiting in your mailbox!'
CatalogNotifyOldDelivery = 'There are still items waiting in your mailbox for you to pick up!'
CatalogNotifyInstructions = 'Click the "Go home" button on the map page in your Shticker Book, then walk up to the phone inside your house.'
CatalogNewDeliveryButton = 'New\nDelivery!'
CatalogNewCatalogButton = 'New\nCattlelog'
CatalogSaleItem = 'Sale! '
DistributedMailboxEmpty = 'Your mailbox is empty right now. Come back here to look for deliveries after you place an order from your phone!'
DistributedMailboxWaiting = 'Your mailbox is empty right now, but the package you ordered is on its way. Check back later!'
DistributedMailboxReady = 'Your order has arrived!'
DistributedMailboxNotOwner = 'Sorry, this is not your mailbox.'
DistributedPhoneEmpty = "You can use any phone to order special items for you and your house. New items will become available to order over time.\n\nYou don't have any items available to order right now, but check back later!"
Clarabelle = 'Clarabelle'
MailboxExitButton = 'Close Mailbox'
MailboxAcceptButton = 'Take this item'
MailBoxDiscard = 'Discard this item'
MailboxAcceptInvite = 'Accept this invite'
MailBoxRejectInvite = 'Reject this invite'
MailBoxDiscardVerify = 'Are you sure you want to Discard %s?'
MailBoxRejectVerify = 'Are you sure you want to Reject %s?'
MailboxOneItem = 'Your mailbox contains 1 item.'
MailboxNumberOfItems = 'Your mailbox contains %s items.'
MailboxGettingItem = 'Taking %s from mailbox.'
MailboxGiftTag = 'Gift From: %s'
MailboxGiftTagAnonymous = 'Anonymous'
MailboxItemNext = 'Next\nItem'
MailboxItemPrev = 'Previous\nItem'
MailboxDiscard = 'Discard'
MailboxReject = 'Reject'
MailboxLeave = 'Keep'
CatalogCurrency = 'beans'
CatalogHangUp = 'Hang Up'
CatalogNew = 'NEW'
CatalogBackorder = 'BACKORDER'
CatalogLoyalty = 'SPECIAL'
CatalogEmblem = 'EMBLEM'
CatalogPagePrefix = 'Page'
CatalogGreeting = "Hello! Thanks for calling Clarabelle's Cattlelog. Can I help you?"
CatalogGoodbyeList = ['Bye now!',
 'Call back soon!',
 'Thanks for calling!',
 'Ok, bye now!',
 'Bye!']
CatalogHelpText1 = 'Turn the page to see items for sale.'
CatalogSeriesLabel = 'Series %s'
CatalogGiftFor = 'Buy Gift for:'
CatalogGiftTo = 'To: %s'
CatalogGiftToggleOn = 'Stop Gifting'
CatalogGiftToggleOff = 'Buy Gifts'
CatalogGiftToggleWait = 'Trying!…'
CatalogGiftToggleNoAck = 'Unavailable'
CatalogPurchaseItemAvailable = 'Congratulations on your new purchase! You can start using it right away.'
CatalogPurchaseGiftItemAvailable = 'Excellent! %s can start using your gift right away.'
CatalogPurchaseItemOnOrder = 'Congratulations! Your purchase will be delivered to your mailbox soon.'
CatalogPurchaseGiftItemOnOrder = 'Excellent! Your gift to %s will be delivered to their mailbox.'
CatalogAnythingElse = 'Anything else I can get you today?'
CatalogPurchaseClosetFull = 'Your closet is full. You may purchase this item anyway, but if you do you will need to delete something from your closet to make room for it when it arrives.\n\nDo you still want to purchase this item?'
CatalogPurchaseNoTrunk = 'In order to wear this item, you need to buy a trunk.\n\nDo you still want to purchase this item?'
CatalogPurchaseTrunkFull = 'Your trunk is full. If you purchase this item, you\xe2\x80\x99ll need to delete another item from your trunk to make more room.\n\nDo you still want to purchase this item?'
CatalogAcceptClosetFull = 'Your closet is full. You must go inside and delete something from your closet to make room for this item before you can take it out of your mailbox.'
CatalogAcceptNoTrunk = "You don't have a trunk. You must buy a trunk before you can take this item out of your mailbox."
CatalogAcceptTrunkFull = 'Your trunk is full. You must delete something from your trunk before you can take this item out of your mailbox.'
CatalogAcceptShirt = 'You are now wearing your new hat. The hat you were wearing before has been moved to your trunk.'
CatalogAcceptShorts = 'You are now wearing your new shorts. What you were wearing before has been moved to your closet.'
CatalogAcceptSkirt = 'You are now wearing your new skirt. What you were wearing before has been moved to your closet.'
CatalogAcceptHat = 'You are now wearing your new hat. The hat you were wearing before has been moved to your trunk.'
CatalogAcceptGlasses = 'You are now wearing your new glasses. The glasses you were wearing before have been moved to your trunk.'
CatalogAcceptBackpack = 'You are now wearing your new backpack. The backpack you were wearing before has been moved to your trunk.'
CatalogAcceptShoes = 'You are now wearing your new shoes. The shoes you were wearing before have been moved to your trunk.'
CatalogAcceptPole = "You're now ready to go catch some bigger fish with your new pole!"
CatalogAcceptPoleUnneeded = 'You already have a better pole than this one!'
CatalogAcceptChat = 'You now have a new SpeedChat!'
CatalogAcceptEmote = 'You now have a new Emotion!'
CatalogAcceptBeans = 'You received some jelly beans!'
CatalogAcceptRATBeans = 'Your Toon recruit reward has arrived!'
CatalogAcceptPartyRefund = "Your party was never started. Here's your refund!"
CatalogAcceptNametag = 'Your new name tag has arrived!'
CatalogAcceptGarden = 'Your garden supplies have arrived!'
CatalogAcceptPet = 'You now have a new Pet Trick!'
CatalogPurchaseHouseFull = 'Your house is full. You may purchase this item anyway, but if you do you will need to delete something from your house to make room for it when it arrives.\n\nDo you still want to purchase this item?'
CatalogAcceptHouseFull = 'Your house is full. You can not accept this item until you free up some room. Would you like to discard this item now?'
CatalogAcceptInAttic = 'Your new item is now in your attic. You can put it in your house by going inside and clicking on the "Move Furniture" button.'
CatalogAcceptInAtticP = 'Your new items are now in your attic. You can put them in your house by going inside and clicking on the "Move Furniture" button.'
CatalogPurchaseMailboxFull = "Your mailbox is full! You can't purchase this item until you take some items out of your mailbox to make room."
CatalogPurchaseGiftMailboxFull = "%s's mailbox is full! You can't purchase this item."
CatalogPurchaseOnOrderListFull = "You have too many items currently on order. You can't order any more items until some of the ones you have already ordered arrive."
CatalogPurchaseGiftOnOrderListFull = '%s has too many items currently on order.'
CatalogPurchaseGeneralError = 'The item could not be purchased because of some internal game error: error code %s.'
CatalogPurchaseGiftGeneralError = 'The item could not be gifted to %(friend)s because of some internal game error: error code %(error)s.'
CatalogPurchaseGiftNotAGift = 'This item could not be sent to %s because it would be an unfair advantage.'
CatalogPurchaseGiftWillNotFit = "This item could not be sent to %s because it doesn't fit them."
CatalogPurchaseGiftLimitReached = "This item could not be sent to %s because they've already have it."
CatalogPurchaseGiftNotEnoughMoney = "This item could not be sent to %s because you can't afford it."
CatalogAcceptGeneralError = 'The item could not be removed from your mailbox because of some internal game error: error code %s.'
CatalogAcceptRoomError = "You don't have any place to put this. You'll have to get rid of something."
CatalogAcceptLimitError = "You already have as many of these as you can handle. You'll have to get rid of something."
CatalogAcceptFitError = "This won't fit you!"
CatalogAcceptInvalidError = 'This item has gone out of style!'
CatalogAcceptClosetError = 'You already have a bigger closet!'
MailboxOverflowButtonDicard = 'Discard'
MailboxOverflowButtonLeave = 'Leave'
HDMoveFurnitureButton = 'Move\nFurniture'
HDStopMoveFurnitureButton = 'Done\nMoving'
HDAtticPickerLabel = 'In the attic'
HDInRoomPickerLabel = 'In the room'
HDInTrashPickerLabel = 'In the trash'
HDDeletePickerLabel = 'Delete?'
HDInAtticLabel = 'Attic'
HDInRoomLabel = 'Room'
HDInTrashLabel = 'Trash'
HDToAtticLabel = 'Send\nto attic'
HDMoveLabel = 'Move'
HDRotateCWLabel = 'Rotate Right'
HDRotateCCWLabel = 'Rotate Left'
HDReturnVerify = 'Return this item to the attic?'
HDReturnFromTrashVerify = 'Return this item to the attic from the trash?'
HDDeleteItem = 'Click OK to send this item to the trash, or Cancel to keep it.'
HDNonDeletableItem = "You can't delete items of this type!"
HDNonDeletableBank = "You can't delete your bank!"
HDNonDeletableCloset = "You can't delete your wardrobe!"
HDNonDeletablePhone = "You can't delete your phone!"
HDNonDeletableTrunk = "You can't delete your trunk!"
HDNonDeletableNotOwner = "You can't delete %s's things!"
HDHouseFull = 'Your house is full. You have to delete something else from your house or attic before you can return this item from the trash.'
HDHelpDict = {'DoneMoving': 'Finish room decorating.',
 'Attic': 'Show list of items in attic. The attic stores items that are not in your room.',
 'Room': 'Show list of items in room. Useful for finding lost items.',
 'Trash': 'Show items in trash. Oldest items are deleted after a while or when trash overflows.',
 'ZoomIn': 'Get a closer view of room.',
 'ZoomOut': 'Get a farther view of room.',
 'SendToAttic': 'Send the current furniture item to attic for storage.',
 'RotateLeft': 'Turn left.',
 'RotateRight': 'Turn right.',
 'DeleteEnter': 'Change to delete mode.',
 'DeleteExit': 'Exit delete mode.',
 'FurnitureItemPanelDelete': 'Send %s to trash.',
 'FurnitureItemPanelAttic': 'Place %s in room.',
 'FurnitureItemPanelRoom': 'Return %s to attic.',
 'FurnitureItemPanelTrash': 'Return %s to attic.'}
MessagePickerTitle = 'You have too many phrases. In order to purchase\n"%s"\n you must choose one to remove:'
MessagePickerCancel = lCancel
MessageConfirmDelete = 'Are you sure you want to remove "%s" from your SpeedChat menu?'
CatalogBuyText = 'Buy'
CatalogRentText = 'Rent'
CatalogGiftText = 'Gift'
CatalogOnOrderText = 'On Order'
CatalogPurchasedText = 'Already\nPurchased'
CatalogCurrent = 'Current'
CatalogGiftedText = 'Gifted\nTo You'
CatalogPurchasedGiftText = 'Already\nOwned'
CatalogMailboxFull = 'No Room'
CatalogNotAGift = 'Not a Gift'
CatalogNoFit = "Doesn't\nFit"
CatalogMembersOnly = 'Members\nOnly!'
CatalogSndOnText = 'Snd On'
CatalogSndOffText = 'Snd Off'
CatalogPurchasedMaxText = 'Already\nPurchased Max'
CatalogVerifyPurchase = 'Purchase %(item)s for %(price)s Jellybeans?'
CatalogVerifyPurchaseBeanSilverGold = 'Purchase %(item)s for %(price)s Jellybeans, %(silver)s silver emblems and %(gold)s gold emblems?'
CatalogVerifyPurchaseBeanGold = 'Purchase %(item)s for %(price)s Jellybeans and %(gold)s gold emblems?'
CatalogVerifyPurchaseBeanSilver = 'Purchase %(item)s for %(price)s Jellybeans and %(silver)s silver emblems?'
CatalogVerifyPurchaseSilverGold = 'Purchase %(item)s for %(silver)s silver emblems and %(gold)s gold emblems?'
CatalogVerifyPurchaseSilver = 'Purchase %(item)s for %(silver)s silver emblems?'
CatalogVerifyPurchaseGold = 'Purchase %(item)s for %(gold)s gold emblems?'
CatalogVerifyRent = 'Rent %(item)s for %(price)s Jellybeans?'
CatalogVerifyGift = 'Purchase %(item)s for %(price)s Jellybeans as a gift for %(friend)s?'
CatalogOnlyOnePurchase = 'You may only have one of these items at a time. If you purchase this one, it will replace %(old)s.\n\nAre you sure you want to purchase %(item)s for %(price)s Jellybeans?'
CatalogExitButtonText = 'Hang Up'
CatalogCurrentButtonText = 'To Current Items'
CatalogPastButtonText = 'To Past Items'
TutorialHQOfficerName = 'HQ Harry'
NPCToonNames = {20000: 'Tutorial Tom',
 999: 'Toon Tailor',
 1000: lToonHQ,
 20001: Flippy,
 2001: Flippy,
 2002: 'Banker Bob',
 2003: 'Professor Pete',
 2004: 'Tammy the Tailor',
 2005: 'Librarian Liz',
 2006: 'Clerk Clark',
 2011: 'Clerk Clara',
 2007: 'Lucas',
 2008: 'Bob',
 2009: 'Greg',
 2010: 'Randy',
 2012: 'Fisherman Freddy',
 2018: 'Duff..err..TIP Man',
 2013: 'Clerk Poppy',
 2014: 'Clerk Peppy',
 2015: 'Clerk Pappy',
 2016: 'Party Planner Pumpkin',
 2017: 'Party Planner Polly',
 2018: 'Doctor Surlee',
 2019: 'Doctor Dimm',
 2020: 'Professor Prepostera',
 2101: 'Dentist Daniel',
 2102: 'Sheriff Sherry',
 2103: 'Factor',
 2104: 'David',
 2105: 'Diego',
 2106: 'Dom',
 2107: 'Deam',
 2108: 'Canary Coalmine',
 2109: 'Dr. Bugs',
 2110: 'Bill Board',
 2111: 'Dancing Diego',
 2112: 'Dr. Tom',
 2113: 'Mulzak The Wizard',
 2114: 'Roz Berry',
 2115: 'Patty Papercut',
 2116: 'Bruiser McDougal',
 2117: 'Ma Putrid',
 2118: 'Jesse Jester',
 2119: 'Honey Haha',
 2120: 'Professor Binky',
 2121: 'Madam Chuckle',
 2122: 'Harry Ape',
 2123: 'Agent Arlo',
 2124: 'Pilot Peak',
 2125: 'King Popcorn',
 2126: 'Professor Guffaw',
 2127: 'Woody Nickel',
 2128: 'Loony Louis',
 2129: 'Frank Furter',
 2130: 'Joy Buzzer',
 2131: 'Feather Duster',
 2132: 'Daffy Don',
 2133: 'Dr. Euphoric',
 2134: 'Silent Simone',
 2135: 'Mary',
 2136: 'Sal Snicker',
 2137: 'Happy Heikyung',
 2138: 'Funny Paint',
 2139: 'Sir Comet',
 2140: 'Fisherman Billy',
 2201: 'Postmaster Pete',
 2202: 'Shirley U. Jest',
 2203: 'Lily',
 2204: 'Lucy',
 2205: 'Lydia',
 2206: 'Luna',
 2207: 'Will Wiseacre',
 2208: 'Sticky Lou',
 2209: 'Cheetah',
 2210: 'Tee Hee',
 2211: 'Donut Doug',
 2212: 'Weird Warren',
 2213: 'Remote Robert',
 2214: 'Sam Stain',
 2215: 'Sid Seltzer',
 2216: 'Nona Seeya',
 2217: 'Sharky Jones',
 2218: 'Fanny Pages',
 2219: 'Chef Knucklehead',
 2220: 'Rick Rockhead',
 2221: 'Natta Cog',
 2222: 'Shorty Fuse',
 2223: 'Sasha Sidesplitter',
 2224: 'Smokey Joe',
 2225: 'Fisherman Droopy',
 2301: 'Dr. Pulyurleg',
 2302: 'Professor Wiggle',
 2303: 'Nurse Nancy',
 2304: 'Uriel',
 2305: 'Ulysses',
 2306: 'Ula',
 2307: 'Umar',
 2308: 'Nancy Gas',
 2309: 'Sticky Sue',
 2311: 'Franz Neckvein',
 2312: 'Officer Cheddar',
 2313: 'Lucy Shirtspot',
 2314: 'Ned Slinger',
 2315: 'Irrel',
 2316: 'Cindy Sprinkles',
 2318: 'Tony Maroni',
 2319: 'Celtic',
 2320: 'Crunchy Alfredo',
 2321: 'Fisherman Punchy',
 2401: 'Hal Haggle',
 2402: 'Bo Bonkers',
 2403: 'Kace',
 2404: 'Ricky Tricky',
 2405: 'Silly Billy',
 2406: 'Dr. Patrick',
 2407: 'Cakeman',
 2408: 'Moka Duck',
 2409: 'Rhett',
 2410: 'Richard',
 2411: 'River',
 2412: 'Reyes',
 2413: 'Tony',
 2414: 'Yellow',
 2415: 'Edwin',
 2416: 'Fisherman Grins',

 1001: 'Clerk Will',
 1002: 'Clerk Bill',
 1003: lHQOfficerM,
 1004: lHQOfficerF,
 1005: lHQOfficerM,
 1006: lHQOfficerF,
 1007: 'Longjohn Leroy',
 1008: 'Fisherman Furball',
 1009: 'Clerk Barky',
 1010: 'Clerk Purr',
 1011: 'Clerk Bloop',
 1012: 'Party Planner Pickles',
 1013: 'Party Planner Patty',
 1101: 'Billy Budd',
 1102: 'Captain Carl',
 1103: 'Fishy Frank',
 1104: 'Bob Square',
 1105: 'Admiral Hook',
 1106: 'Mrs. Starch',
 1107: 'Cal Estenicks',
 1108: lHQOfficerM,
 1109: lHQOfficerF,
 1110: lHQOfficerM,
 1111: lHQOfficerF,
 1112: 'Gary Glubglub',
 1113: 'Lisa Luff',
 1114: 'Charlie Chum',
 1115: 'Sheila Squid, Atty',
 1116: 'Pegleg Peg',
 1117: 'Captain Yucks',
 1118: 'Choppy McDougal',
 1121: 'Linda Landlubber',
 1122: 'Salty Stan',
 1123: 'Baron Corbear',
 1124: 'Flappy Docksplinter',
 1125: 'Eileen Overboard',
 1126: 'Fisherman Barney',
 1201: 'Barnacle Barbara',
 1202: 'Art',
 1203: 'Ahab',
 1204: 'Rocky Shores',
 1205: lHQOfficerM,
 1206: lHQOfficerF,
 1207: lHQOfficerM,
 1208: lHQOfficerF,
 1209: 'Professor Plank',
 1210: 'Gang Wei',
 1211: 'Wynn Bag',
 1212: 'Toby Tonguestinger',
 1213: 'Dante Dolphin',
 1214: 'Gusty Kate',
 1215: 'Dinah Down',
 1216: 'Rod Reel',
 1217: 'CC Weed',
 1218: 'Pacific Tim',
 1219: 'Brian Beachead',
 1220: 'Carla Canal',
 1221: 'Blisters McKee',
 1222: 'Shep Ahoy',
 1223: 'Sid Squid',
 1224: 'Emily Eel',
 1225: 'Bonzo Bilgepump',
 1226: 'Jonathan Sea-No',
 1227: 'Coral Reef',
 1228: 'Fisherman Reed',
 1301: 'Alice',
 1302: 'Melville',
 1303: 'Claggart',
 1304: 'Svetlana',
 1305: lHQOfficerM,
 1306: lHQOfficerF,
 1307: lHQOfficerM,
 1308: lHQOfficerF,
 1309: 'Seafoam',
 1310: 'Ted Tackle',
 1311: 'Topsy Turvey',
 1312: 'Nayla',
 1313: 'Howard Horse',
 1314: 'Rusty Ralph',
 1315: 'Doctor Drift',
 1316: 'Wilma Wobble',
 1317: 'Paula Pylon',
 1318: 'Dinghy Dan',
 1319: 'Davey Drydock',
 1320: 'Ted Calm',
 1321: 'Dinah Docker',
 1322: 'Whoopie Cushion',
 1323: 'Stinky Ned',
 1324: 'Pearl Diver',
 1325: 'Ned Setter',
 1326: 'Felicia Chips',
 1327: 'Cindy Splat',
 1328: 'Fred Flounder',
 1329: 'Shelly Seaweed',
 1330: 'Porter Hole',
 1331: 'Rudy Rudder',
 1332: 'Fisherman Shane',
 3001: 'Betty Freezes',
 3002: 'Dylan',
 3003: 'Marnie',
 3004: 'Sophie',
 3005: 'Aggie',
 3006: 'Clerk Lenny',
 3007: 'Clerk Penny',
 3008: 'Warren Bundles',
 3009: 'Fisherman Frizzy',
 3010: 'Clerk Skip',
 3011: 'Clerk Dip',
 3012: 'Clerk Kipp',
 3013: 'Party Planner Pete',
 3014: 'Party Planner Penny',
 3101: 'Mr. Cow',
 3102: 'Auntie Freeze',
 3103: 'Fred',
 3104: 'Bonnie',
 3105: 'Frosty Freddy',
 3106: 'Gus Gooseburger',
 3107: 'Patty Passport',
 3108: 'Toboggan Ted',
 3109: 'Kate',
 3110: 'Chicken Boy',
 3111: 'Snooty Sinjin',
 3112: 'Lil Oldman',
 3113: 'Hysterical Harry',
 3114: 'Henry the Hazard',
 3115: 'Mary',
 3116: 'Madeline',
 3117: 'Matteo',
 3118: 'Mike',
 3119: 'Creepy Carl',
 3120: 'Mike Mittens',
 3121: 'Joe Shockit',
 3122: 'Lucy Luge',
 3123: 'Frank Lloyd Ice',
 3124: 'Lance Iceberg',
 3125: 'Colonel Crunchmouth',
 3126: 'Colestra Awl',
 3127: 'Ifalla Yufalla',
 3128: 'Sticky George',
 3129: 'Baker Bridget',
 3130: 'Sandy',
 3131: 'Lazy Lorenzo',
 3132: 'Ashy',
 3133: 'Dr. Friezeframe',
 3134: 'Lounge Lassard',
 3135: 'Soggy Nell',
 3136: 'Happy Sue',
 3137: 'Mr. Freeze',
 3138: 'Chef Bumblesoup',
 3139: 'Granny Icestockings',
 3140: 'Fisherman Lucille',
 3201: 'Aunt Arctic',
 3202: 'Shakey',
 3203: 'Walt',
 3204: 'Dr. Ivanna Cee',
 3205: 'Bumpy Noggin',
 3206: 'Vidalia VaVoom',
 3207: 'Dr. Mumbleface',
 3208: 'Grumpy Phil',
 3209: 'Giggles McGhee',
 3210: 'Simian Sam',
 3211: 'Fanny Freezes',
 3212: 'Frosty Fred',
 3213: 'Peyton',
 3214: 'Priscilla',
 3215: 'Phoenix',
 3216: 'Patriece',
 3217: 'Sweaty Pete',
 3218: 'Blue Lou',
 3219: 'Tom Tandemfrost',
 3220: 'Mr. Sneeze',
 3221: 'Nelly Snow',
 3222: 'Mindy Windburn',
 3223: 'Chappy',
 3224: 'Freida Frostbite',
 3225: 'Blake Ice',
 3226: 'Santa Paws',
 3227: 'Solar Ray',
 3228: 'Wynne Chill',
 3229: 'Hernia Belt',
 3230: 'Balding Benjy',
 3231: 'Choppy',
 3232: 'Fisherman Albert',
 3301: 'Paisley Patches',
 3302: 'Bjorn Bord',
 3303: 'Dr. Peepers',
 3304: 'Eddie the Yeti',
 3305: 'Mack Ramay',
 3306: 'Paula Behr',
 3307: 'Fisherman Fredrica',
 3308: 'Donald Frump',
 3309: 'Bootsy',
 3310: 'Professor Flake',
 3311: 'Connie Ferris',
 3312: 'March Harry',
 3313: 'Atlas',
 3314: 'August',
 3315: 'Amy',
 3316: 'Ayvery',
 3317: 'Kissy Krissy',
 3318: 'Johnny Cashmere',
 3319: 'Sam Stetson',
 3320: 'Fizzy Lizzy',
 3321: 'Pickaxe Paul',
 3322: 'Flue Lou',
 3323: 'Dallas Borealis',
 3324: 'Snaggletooth Stu',
 3325: 'Groovy Garland',
 3326: 'Blanche',
 3327: 'Chuck Roast',
 3328: 'Shady Sadie',
 3329: 'Treading Ed',
 #3400: 'Dory
 #3401: 'Dottie'
 #3402: 'Desirae'
 #3403: 'Dakota'
 4001: 'Molly Molloy',
 4002: lHQOfficerM,
 4003: lHQOfficerF,
 4004: lHQOfficerF,
 4005: lHQOfficerF,
 4006: 'Clerk Doe',
 4007: 'Clerk Ray',
 4008: 'Tailor Harmony',
 4009: 'Fisherman Fanny',
 4010: 'Clerk Chris',
 4011: 'Clerk Neil',
 4012: 'Clerk Westin Girl',
 4013: 'Party Planner Preston',
 4014: 'Party Planner Penelope',
 4101: 'Tom',
 4102: 'Fifi',
 4103: 'Dr. Fret',
 4104: lHQOfficerM,
 4105: lHQOfficerF,
 4106: lHQOfficerF,
 4107: lHQOfficerF,
 4108: 'Cleff',
 4109: 'Carlos',
 4110: 'Metra Gnome',
 4111: 'Tom Hum',
 4112: 'Fa',
 4113: 'Madam Manners',
 4114: 'Offkey Eric',
 4115: 'Barbara Seville',
 4116: 'Piccolo',
 4117: 'Mandy Lynn',
 4118: 'Attendant Abe',
 4119: 'Moe Zart',
 4120: 'Viola Padding',
 4121: 'Gee Minor',
 4122: 'Minty Bass',
 4123: 'Lightning Ted',
 4124: 'Riff Raff',
 4125: 'Melody Wavers',
 4126: 'Mel Canto',
 4127: 'Happy Feet',
 4128: 'Luciano Scoop',
 4129: 'Tootie Twostep',
 4130: 'Metal Mike',
 4131: 'Abraham Armoire',
 4132: 'Lowdown Sally',
 4133: 'Scott Poplin',
 4134: 'Disco Dave',
 4135: 'Sluggo Songbird',
 4136: 'Patty Pause',
 4137: 'Tony Deff',
 4138: 'Cliff Cleff',
 4139: 'Harmony Swell',
 4140: 'Clumsy Ned',
 4141: 'Fisherman Jed',
 4201: 'Tina',
 4202: 'Barry',
 4203: 'Lumber Jack',
 4204: lHQOfficerM,
 4205: lHQOfficerF,
 4206: lHQOfficerF,
 4207: lHQOfficerF,
 4208: 'Hedy',
 4209: 'Corny Canter',
 4211: 'Carl Concerto',
 4212: 'Detective Dirge',
 4213: 'Fran Foley',
 4214: 'Tina Toehooks',
 4215: 'Tim Tailgater',
 4216: 'Gummy Whistle',
 4217: 'Handsome Anton',
 4218: 'Wilma Wind',
 4219: 'Sid Sonata',
 4220: 'Curtis Finger',
 4221: 'Moe Madrigal',
 4222: 'John Doe',
 4223: 'Penny Prompter',
 4224: 'Jungle Jim',
 4225: 'Holly Hiss',
 4226: 'Thelma Throatreacher',
 4227: 'Quiet Francesca',
 4228: 'August Winds',
 4229: 'June Loon',
 4230: 'Julius Wheezer',
 4231: 'Steffi Squeezebox',
 4232: 'Hedly Hymn',
 4233: 'Charlie Carp',
 4234: 'Leed Guitar',
 4235: 'Fisherman Larry',
 4301: 'Yuki',
 4302: 'Anna',
 4303: 'Leo',
 4304: lHQOfficerM,
 4305: lHQOfficerF,
 4306: lHQOfficerF,
 4307: lHQOfficerF,
 4308: 'Tabitha',
 4309: 'Marshall',
 4310: 'Martha Mopp',
 4311: 'Sea Shanty',
 4312: 'Moe Saj',
 4313: 'Dumb Dolph',
 4314: 'Dana Dander',
 4315: 'Karen Clockwork',
 4316: 'Tim Tango',
 4317: 'Stubby Toe',
 4318: 'Bob Marlin',
 4319: 'Rinky Dink',
 4320: 'Cammy Coda',
 4321: 'Luke Lute',
 4322: 'Randy Rythm',
 4323: 'Reg',
 4324: 'Ellie',
 4325: 'Banker Bran',
 4326: 'Fran Fret',
 4327: 'Flim Flam',
 4328: 'Wagner',
 4329: 'Telly Prompter',
 4330: 'Quentin',
 4331: 'Mellow Costello',
 4332: 'Ziggy',
 4333: 'Harry',
 4334: 'Fast Freddie',
 4335: 'Fisherman Walden',
 5001: lHQOfficerM,
 5002: lHQOfficerM,
 5003: lHQOfficerF,
 5004: lHQOfficerF,
 5005: 'Clerk Peaches',
 5006: 'Clerk Herb',
 5007: 'Bonnie Blossom',
 5008: 'Fisherman Flora',
 5009: 'Clerk Bo Tanny',
 5010: 'Clerk Tom A. Dough',
 5011: 'Clerk Doug Wood',
 5012: 'Party Planner Pierce',
 5013: 'Party Planner Peggy',
 5101: 'Artie',
 5102: 'Susan',
 5103: 'Master Shifo',
 5104: 'Flutterby',
 5105: 'Jack',
 5106: 'Magic Maya',
 5107: 'Postman Felipe',
 5108: 'Gossipping Gibby',
 5109: lHQOfficerM,
 5110: lHQOfficerM,
 5111: lHQOfficerF,
 5112: lHQOfficerF,
 5113: 'Dr. Spud',
 5114: 'Wilt',
 5115: 'Honey Dew',
 5116: 'Vegetable Vern',
 5117: 'Petal',
 5118: 'Pop Corn',
 5119: 'Barry Medly',
 5120: 'Dill Flye',
 5121: 'Paula Peapod',
 5122: 'Leif Pyle',
 5123: 'Diane Vine',
 5124: 'Archmage Angelic',
 5125: 'Sanjay Splash',
 5126: 'Madam Mum',
 5127: 'Professor Oak',
 5128: 'Shoshanna Sap',
 5129: 'Fisherman Sally',
 5201: 'Instructor Gandling',
 5202: 'Cynthia',
 5203: 'Lisa',
 5204: 'Bert',
 5205: 'Dan D. Lion',
 5206: 'Vine Green',
 5207: 'Sofie Squirt',
 5208: 'Samantha Spade',
 5209: lHQOfficerM,
 5210: lHQOfficerM,
 5211: lHQOfficerF,
 5212: lHQOfficerF,
 5213: 'Big Galoot',
 5214: 'Itchie Bumps',
 5215: 'Tammy Tuber',
 5216: 'Stinky Jim',
 5217: 'Greg Greenethumb',
 5218: 'Rocky Raspberry',
 5219: 'Lars Bicep',
 5220: 'Lacy Underalls',
 5221: 'Pink Flamingo',
 5222: 'Whiny Wilma',
 5223: 'Mr. Dunky',
 5224: 'Uncle Bumpkin',
 5225: 'Pamela Puddle',
 5226: 'Dangolf',
 5227: 'Begonia Biddlesmore',
 5228: 'Digger Mudhands',
 5229: 'Fisherman Lily',
 5301: lHQOfficerM,
 5302: lHQOfficerM,
 5303: lHQOfficerM,
 5304: lHQOfficerM,
 5305: 'Crystal',
 5306: 'Solver Sullivan',
 5307: 'Fun Gus',
 5308: 'Naggy Nell',
 5309: 'Ro Maine',
 5310: 'Timothy',
 5311: 'Judge McIntosh',
 5312: 'Eugene',
 5313: 'Coach Zucchini',
 5314: 'Aunt Hill',
 5315: 'Librarian Lucas',
 5316: 'Uncle Spud',
 5317: 'Detective Lima',
 5318: 'Caesar',
 5319: 'Geralt',
 5320: 'Doug',
 5321: 'Pizza Taco',
 5322: 'Fisherman Rose',
 8001: 'Graham Pree',
 8002: 'Ivona Race',
 8003: 'Anita Winn',
 8004: 'Phil Errup',
 9001: "Snoozin' Susan",
 9002: 'Sleeping Tom',
 9003: 'Drowsy Dennis',
 9004: lHQOfficerF,
 9005: lHQOfficerF,
 9006: lHQOfficerM,
 9007: lHQOfficerM,
 9008: 'Clerk Jill',
 9009: 'Clerk Phil',
 9010: 'Worn Out Waylon',
 9011: 'Fisherman Freud',
 9012: 'Clerk Sarah Snuze',
 9013: 'Clerk Kat Knap',
 9014: 'Clerk R. V. Winkle',
 9015: 'Party Planner Pebbles',
 9016: 'Party Planner Pearl',
 9101: 'Ed',
 9102: 'Big Mama',
 9103: 'P.J.',
 9104: 'Sweet Slumber',
 9105: 'Professor Yawn',
 9106: 'Max',
 9107: 'Snuggles',
 9108: 'Winky Wilbur',
 9109: 'Dreamy Daphne',
 9110: 'Kathy Nip',
 9111: 'Powers Erge',
 9112: 'Lullaby Lou',
 9113: 'Jacques Clock',
 9114: 'Smudgy Mascara',
 9115: 'Babyface MacDougal',
 9116: 'Dances with Sheep',
 9117: 'Afta Hours',
 9118: 'Starry Knight',
 9119: 'Rocco',
 9120: 'Sarah Slumber',
 9121: 'Serena Shortsheeter',
 9122: 'Puffy Ayes',
 9123: 'Teddy Blair',
 9124: 'Nina Nitelight',
 9125: 'Dr. Bleary',
 9126: 'Wyda Wake',
 9127: 'Tabby Tucker',
 9128: "Hardy O'Toole",
 9129: 'Bertha Bedhog',
 9130: 'Charlie Chamberpot',
 9131: 'Susan Siesta',
 9132: lHQOfficerF,
 9133: lHQOfficerF,
 9134: lHQOfficerF,
 9135: lHQOfficerF,
 9136: 'Fisherman Taylor',
 9201: 'Bernie',
 9202: 'Orville',
 9203: 'Nat',
 9204: 'Claire de Loon',
 9205: 'Zen Glen',
 9206: 'Skinny Ginny',
 9207: 'Jane Drain',
 9208: 'Drowsy Dave',
 9209: 'Dr. Floss',
 9210: 'Master Mike',
 9211: 'Dawn',
 9212: 'Moonbeam',
 9213: 'Rooster Rick',
 9214: 'Dr. Blinky',
 9215: 'Rip',
 9216: 'Rod Rooster',
 9217: 'Lawful Linda',
 9218: 'Waltzing Matilda',
 9219: 'The Countess',
 9220: 'Grumpy Gordon',
 9221: 'Zari',
 9222: 'Cowboy George',
 9223: 'Mark the Lark',
 9224: 'Sandy Sandman',
 9225: 'Fidgety Bridget',
 9226: 'William Teller',
 9227: 'Bed Head Ted',
 9228: 'Whispering Willow',
 9229: 'Rose Petals',
 9230: 'Tex',
 9231: 'Harry Hammock',
 9232: 'Honey Moon',
 9233: lHQOfficerM,
 9234: lHQOfficerM,
 9235: lHQOfficerM,
 9236: lHQOfficerM,
 9237: 'Fisherman Jung',
 9301: 'Phil Bettur',
 9302: 'Emma Phatic',
 9303: 'GiggleMesh',
 9304: 'Anne Ville',
 9305: 'Master Shifo Erfingerz',
 9306: 'J.S. Bark',
 9307: 'Bea Sharpe',
 9308: 'Otto Toon',
 9309: 'Al Capella',
 9310: 'Des Traction',
 9311: 'Dee Version',
 9312: 'Bo Nanapeel',
 7001: 'N. Prisoned',
 7002: 'R.E. Leaseme',
 7003: 'Lemmy Owte',
 7004: 'T. Rapped',
 7005: 'Little Helphere',
 7006: 'Gimmy Ahand',
 7007: 'Dewin Tymme',
 7008: 'Ima Cagedtoon',
 7009: 'Jimmy Thelock'}
zone2TitleDict = {2513: ('Toon Hall', ''),
 2514: ('Toontown Bank', ''),
 2516: ('Toontown School House', ''),
 2518: ('Toontown Library', ''),
 2519: ('Gag Shop', ''),
 2520: (lToonHQ, ''),
 2521: ('Clothing Shop', ''),
 2522: ('Pet Shop', ''),
 2601: ('All Smiles Tooth Repair', ''),
 2602: ('', ''),
 2603: ('One-Liner Miners', ''),
 2604: ('Whats Up Doc?', ''),
 2605: ('Toontown Sign Factory', ''),
 2606: ('', ''),
 2607: ('Jumping Beans', ''),
 2610: ('Dr. Tom Foolery', ''),
 2611: ('', ''),
 2616: ("Fractions & Subtractions", ''),
 2617: ('Mulzaks Quackers', ''),
 2618: ('All That Razz', ''),
 2621: ('Paper Airplanes', ''),
 2624: ('Happy Hooligans', ''),
 2625: ('House of Bad Pies', ''),
 2626: ("Jesse's Joke Repair", ''),
 2629: ("The Laughing Place", ''),
 2632: ('Clown Class', ''),
 2633: ('Tee-Hee Tea Shop', ''),
 2638: ('Toontown Playhouse', ''),
 2639: ('Monkey Tricks', ''),
 2643: ('Around The Island: Travel Agency', ''),
 2644: ('Islanded Flights: Passport Flights', ''),
 2649: ('Pop That Corn!: Popcorn Making', ''),
 2652: ('', ''),
 2653: ('', ''),
 2654: ('Laughing Lessons', ''),
 2655: ('Funny Money Savings & Loan', ''),
 2656: ('Used Clown Cars', ''),
 2657: ("Frank's Pranks", ''),
 2659: ('Joy Buzzers to the World', ''),
 2660: ('Tickle Machines', ''),
 2661: ('Daffy Taffy', ''),
 2662: ('Dr. I.M. Euphoric', ''),
 2663: ('Toontown Cinerama', ''),
 2664: ('The Merry Mimes', ''),
 2665: ("Mary's Go Around Travel Company", ''),
 2666: ('Laughing Gas Station', ''),
 2667: ('Happy Times', ''),
 2669: ("Funny Pant's Funny Pants", ''),
 2670: ('Comet Dreamers', ''),
 2671: ('', ''),
 2701: ('', ''),
 2704: ('Movie Multiplex', ''),
 2705: ("Wiseacre's Noisemakers", ''),
 2708: ('Blue Glue', ''),
 2711: ('Toontown Post Office', ''),
 2712: ('Only Cheetahs Try Lion', ''),
 2713: ('Laughter Hours Cafe', ''),
 2714: ('Kooky CinePlex', ''),
 2716: ('Donut Give Up: Donut Shop', ''),
 2717: ('Bottled Cans', ''),
 2720: ('Remotes For Remote Island', ''),
 2725: ('', ''),
 2727: ('Seltzer Bottles and Cans', ''),
 2728: ('Vanishing Cream', ''),
 2729: ('14 Karat Goldfish', ''),
 2730: ('News for the Amused', ''),
 2731: ('', ''),
 2732: ('Spaghetti and Goofballs', ''),
 2733: ('Cast Iron Kites', ''),
 2734: ('Not a Cog Place', ''),
 2735: ('The Kaboomery', ''),
 2739: ("Sidesplitter's Mending", ''),
 2740: ('Used Firecrackers', ''),
 2741: ('', ''),
 2742: ('', ''),
 2743: ('Ragtime Dry Cleaners', ''),
 2744: ('', ''),
 2747: ('Visible Ink', ''),
 2748: ('Jest for Laughs', ''),
 2801: ('Sofa Whoopee Cushions', ''),
 2802: ('Pink Goo', ''),
 2803: ('The Karnival Kid', ''),
 2804: ('Dr. Pulyurleg, Chiropractor', ''),
 2805: ('', ''),
 2809: ('The Punch Line Gym', ''),
 2814: ('Toontown Theatre', ''),
 2818: ('The Flying Pie', ''),
 2821: ('', ''),
 2822: ('Irr-elephant Topics: Irrelevant Researches', ''),
 2823: ('Sundae Funnies Ice Cream', ''),
 2824: ('Punchline Movie Palace', ''),
 2829: ('Phony Baloney', ''),
 2830: ("Anony-Moose: Secret Service", ''),
 2831: ("Professor Wiggle's House of Giggles", ''),
 2832: ('', ''),
 2833: ('', ''),
 2834: ('Funny Bone Emergency Room', ''),
 2836: ('', ''),
 2837: ('Up To No Gouda', ''),
 2839: ('Barely Palatable Pasta', ''),
 2841: ('', ''),

# titles for: phase_5/dna/toon_island_central_2400.dna
 2901: ('Gold & Silver Pawn Shop', ''),
 2902: ('Krazy Kafe', ''),
 2903: ('Kar-Rates', ''),
 2904: ('Rickster The Trickster: Pranks', ''),
 2905: ('Bean There Done That', ''),
 2906: ("Dr. Patrick's Office", ''),
 2907: ("Cake Factory", ''),
 2908: ("Starduck's Cafe", ''),
 2909: ('', ''),
 2910: ("Tony's Toy Store", ''),
 2912: ('Banana Cream Memes', ''),
 2913: ('Astron-aughts', ''),

 1506: ('Gag Shop', ''),
 1507: ('Toon Headquarters', ''),
 1508: ('Clothing Shop', ''),
 1510: ('', ''),
 1602: ('Used Life Preservers', ''),
 1604: ('Wet Suit Dry Cleaners', ''),
 1606: ("Hook's Clock Repair", ''),
 1608: ("Luff 'N Stuff", ''),
 1609: ('Every Little Bait', ''),
 1612: ('Dime & Quarterdeck Bank', ''),
 1613: ('Squid Pro Quo, Attorneys at Law', ''),
 1614: ('Peg’s Pegged Peg Legs', ''),
 1615: ("Yacht's All, Folks!", ''),
 1616: ("Blackbeard's Beauty Parlor", ''),
 1617: ('Reef Blowers Lawn Care', ''),
 1619: ('Disembark! Tree Surgeons', ''),
 1620: ('From Fore to Aft', ''),
 1621: ('Poop Deck Gym', ''),
 1622: ('Rain-Below 5 Or Less', ''),
 1624: ('Soles Repaired While U Wait', ''),
 1626: ('Salmon Chanted Evening Formal Wear', ''),
 1627: ("Billy Budd's Big Bargain Binnacle Barn", ''),
 1628: ('Piano Tuna', ''),
 1629: ('', ''),
 1701: ('Buoys and Gulls Nursery School', ''),
 1703: ('Wok the Plank Chinese Food', ''),
 1705: ('Sails for Sale', ''),
 1706: ('Peanut Butter and Jellyfish', ''),
 1707: ('Gifts With a Porpoise', ''),
 1709: ('Windjammers and Jellies', ''),
 1710: ('Barnacle Bargains', ''),
 1711: ('Deep Sea Diner', ''),
 1712: ('Able-Bodied Gym', ''),
 1713: ("Art's Smart Chart Mart", ''),
 1714: ("Reel 'Em Inn", ''),
 1716: ('Mermaid Swimwear', ''),
 1717: ('Be More Pacific Ocean Notions', ''),
 1718: ('Run Aground Taxi Service', ''),
 1719: ("Duck's Back Water Company", ''),
 1720: ('The Reel Deal', ''),
 1721: ('All For Nautical', ''),
 1723: ("Squid's Seaweed", ''),
 1724: ("That's  a Moray!", ''),
 1725: ("Ahab's Prefab Sea Crab Center", ''),
 1726: ('Root Beer Afloats', ''),
 1727: ('Can You Sea Me?', ''),
 1728: ('Good Luck Horseshoe Crabs', ''),
 1729: ('', ''),
 1802: ('Nautical But Nice', ''),
 1804: ('Mussel Beach Gymnasium', ''),
 1805: ('Tackle Box Lunches', ''),
 1806: ('Cap Size Hat Store', ''),
 1807: ("Nayla's Den", ''),
 1808: ('Family Friendly Stern', ''),
 1809: ('Rusty Buckets', ''),
 1810: ('Anchor Management', ''),
 1811: ("What's Canoe With You?", ''),
 1813: ('Pier Pressure Plumbing', ''),
 1814: ('The Yo Ho Stop and Go', ''),
 1815: ("Ocean Commotion Fishing Equipment?", ''),
 1818: ('Seven Seas Cafe', ''),
 1819: ("Docker's Diner", ''),
 1820: ('Hook, Line, and Sinker Prank Shop', ''),
 1821: ("King NepToon's Cannery", ''),
 1823: ('The Clam Bake Diner', ''),
 1824: ('Dog Paddles', ''),
 1825: ('Wholly Mackerel! Fish Market', ''),
 1826: ("Claggart's Clever Clovis Closet", ''),
 1828: ("Alice's Ballast Palace", ''),
 1829: ('Seagull Statue Store', ''),
 1830: ('Lost and Flounder', ''),
 1831: ('Kelp Around the House', ''),
 1832: ("Melville's Massive Mizzenmast Mart", ''),
 1833: ('This Transom Man Custom Tailored Suits', ''),
 1834: ('Rudderly Ridiculous!', ''),
 1835: ('', ''),
 4503: ('Gag Shop', ''),
 4504: ('Toon Headquarters', ''),
 4506: ('Clothing Shop', ''),
 4508: ('', ''),
 4603: ("Tom-Tom's Drums", ''),
 4604: ('In Four-Four Time', ''),
 4605: ("Fifi's Fiddles", ''),
 4606: ('Casa De Castanets', ''),
 4607: ('Catchy Toon Apparel', ''),
 4609: ('Do, Rae, Me Piano Keys', ''),
 4610: ('Please Refrain', ''),
 4611: ('Tuning Forks and Spoons', ''),
 4612: ("Dr. Fret's Dentistry", ''),
 4614: ('Shave and a Haircut for a Song', ''),
 4615: ("Piccolo's Pizza", ''),
 4617: ('Happy Mandolins', ''),
 4618: ('Rests Rooms', ''),
 4619: ('More Scores', ''),
 4622: ('Chin Rest Pillows', ''),
 4623: ('Flats Sharpened', ''),
 4625: ('Tuba Toothpaste', ''),
 4626: ('Notations', ''),
 4628: ('Accidental Insurance', ''),
 4629: ("Riff's Paper Plates", ''),
 4630: ('Music Is Our Forte', ''),
 4631: ('Canto Help You', ''),
 4632: ('Dance Around the Clock Shop', ''),
 4635: ('Tenor Times', ''),
 4637: ('For Good Measure', ''),
 4638: ('Hard Rock Shop', ''),
 4639: ('Four Score Antiques', ''),
 4641: ('Blues News', ''),
 4642: ('Ragtime Dry Cleaners', ''),
 4645: ('Club 88', ''),
 4646: ('', ''),
 4648: ('Carry a Toon Movers', ''),
 4649: ('', ''),
 4652: ('Full Stop Shop', ''),
 4653: ('', ''),
 4654: ('Pitch Perfect Roofing', ''),
 4655: ("The Treble Chef's Cooking School", ''),
 4656: ('', ''),
 4657: ('Barbershop Quartet', ''),
 4658: ('Plummeting Pianos', ''),
 4659: ('', ''),
 4701: ('The Schmaltzy Waltz School of Dance', ''),
 4702: ('Timbre! Equipment for the Singing Lumberjack', ''),
 4703: ('I Can Handel It!', ''),
 4704: ("Tina's Concertina Concerts", ''),
 4705: ('Zither Here Nor There', ''),
 4707: ("Doppler's Sound Effects Studio", ''),
 4709: ('On Ballet! Climbing Supplies', ''),
 4710: ('Hurry Up, Slow Polka! School of Driving', ''),
 4712: ('C-Flat Tire Repair', ''),
 4713: ('B-Sharp Fine Menswear', ''),
 4716: ('Four-Part Harmonicas', ''),
 4717: ('Sonata Your Fault! Discount Auto Insurance', ''),
 4718: ('Chopin Blocks and Other Kitchen Supplies', ''),
 4719: ('Madrigal Motor Homes', ''),
 4720: ('Name That Toon', ''),
 4722: ('Overture Understudies', ''),
 4723: ('Haydn Go Seek Playground Supplies', ''),
 4724: ('White Noise for Girls and Boys', ''),
 4725: ('The Baritone Barber', ''),
 4727: ('Vocal Chords Braided', ''),
 4728: ("Sing Solo We Can't Hear You", ''),
 4729: ('Double Reed Bookstore', ''),
 4730: ('Lousy Lyrics', ''),
 4731: ('Toon Tunes', ''),
 4732: ('Etude Brute? Theatre Company', ''),
 4733: ('', ''),
 4734: ('', ''),
 4735: ('Accordions, If You Want In, Just Bellow!', ''),
 4736: ('Her and Hymn Wedding Planners', ''),
 4737: ('Harp Tarps', ''),
 4738: ('Canticle Your Fancy Gift Shop', ''),
 4739: ('', ''),
 4801: ("Marshall's Stacks", ''),
 4803: ('What a Mezzo! Maid Service', ''),
 4804: ('Mixolydian Scales', ''),
 4807: ('Relax the Bach', ''),
 4809: ("I Can't Understanza!", ''),
 4812: ('', ''),
 4817: ('The Ternary Pet Shop', ''),
 4819: ("Yuki's Ukeleles", ''),
 4820: ('', ''),
 4821: ("Anna's Cruises", ''),
 4827: ('Common Time Watches', ''),
 4828: ("Schumann's Shoes for Men", ''),
 4829: ("Pachelbel's Canonballs", ''),
 4835: ('Ursatz for Kool Katz', ''),
 4836: ('Reggae Regalia', ''),
 4838: ('Kazoology School of Music', ''),
 4840: ('Coda Pop Musical Beverages', ''),
 4841: ('Lyre, Lyre, Pants on Fire!', ''),
 4842: ('The Syncopation Corporation', ''),
 4843: ('', ''),
 4844: ('Sandy Spitoon', ''),
 4845: ("Ellie's Elegant Elegies", ''),
 4848: ('Lotsa Lute Savings & Loan', ''),
 4849: ('', ''),
 4850: ('The Borrowed Chord Pawn Shop', ''),
 4852: ('Flowery Flute Fleeces', ''),
 4853: ("Leo's Fenders", ''),
 4854: ("Wagner's Vocational Violin Videos", ''),
 4855: ('The Teli-Caster Network', ''),
 4856: ('', ''),
 4862: ("Quentin's Quintessen\x03tial Quadrilles", ''),
 4867: ("Mr. Costello's Yellow Cellos", ''),
 4868: ('', ''),
 4870: ("Ziggy's Zoo of Zigeuner\x03musik", ''),
 4871: ("Harry's House of Harmonious Humbuckers", ''),
 4872: ("Fast Freddie's Fretless Fingerboards", ''),
 4873: ('', ''),
 5501: ('Gag Shop', ''),
 5502: (lToonHQ, ''),
 5503: ('Clothing Shop', ''),
 5505: ('', ''),
 5601: ('Eye of the Potato Optometry', ''),
 5602: ("Artie Choke's Neckties", ''),
 5603: ('Lettuce Alone', ''),
 5604: ('Cantaloupe Bridal Shop', ''),
 5605: ('Vege-tables and Chairs', ''),
 5606: ('Petals', ''),
 5607: ('Compost Office', ''),
 5608: ('Mom and Pop Corn', ''),
 5609: ('Berried Treasure', ''),
 5610: ("Black-eyed Susan's Boxing Lessons", ''),
 5611: ("The Withering Laboratory", ''),
 5613: ("Maya's Wacky Wonders", ''),
 5615: ("Fist and Palm Trees: Dojo", ''),
 5616: ('Little Birdy Told Me: Gossip Spreader', ''),
 5617: ("Flutterby's Butterflies", ''),
 5618: ("Peas and Q's", ''),
 5619: ("Jack's Beanstalks", ''),
 5620: ('Rake It Inn', ''),
 5621: ('Grape Expectations', ''),
 5622: ('Arcanium of Archmages', ''),
 5623: ('Bubble Bird Baths', ''),
 5624: ("Mum's the Word", ''),
 5625: ('Geome-tree!: Math Tutoring', ''),
 5626: ('Pine Needle Crafts', ''),
 5627: ('', ''),
 5701: ('From Start to Spinach', ''),
 5702: ("Withering Woods School House", ''),
 5703: ("Photo Cynthia's Camera Shop", ''),
 5704: ('Lisa Lemon Used Cars', ''),
 5705: ('Poison Oak Furniture', ''),
 5706: ('14 Carrot Jewelers', ''),
 5707: ('Musical Fruit', ''),
 5708: ("We'd Be Gone Travel Agency", ''),
 5709: ('Astroturf Mowers', ''),
 5710: ('Tuft Guy Gym', ''),
 5711: ('Garden Hosiery', ''),
 5712: ('Silly Statues', ''),
 5713: ('Trowels and Tribulations', ''),
 5714: ("Mr Dunky's House Of Junky", ''),
 5715: ('Over The Hills: Travel Agency', ''),
 5716: ('Take It or Leaf It Pawn Shop', ''),
 5717: ('The Squirting Flower', ''),
 5718: ('The Dandy Lion Exotic Pets', ''),
 5719: ('Trellis the Truth! Private Investi\x03gators', ''),
 5720: ('Vine and Dandy Menswear', ''),
 5721: ('Bewithered The Woods', ''),
 5725: ('Barley, Hops, and Malt Shop', ''),
 5726: ("Bert's Dirt", ''),
 5727: ('Gopher Broke Savings & Loan', ''),
 5728: ('', ''),
 5802: (lToonHQ, ''),
 5804: ('Just Vase It', ''),
 5805: ('Axe-idents Happen', ''),
 5809: ('Fungi Clown School', ''),
 5810: ('Honeydew This', ''),
 5811: ('The Withering Ogre?', ''),
 5815: ('Grass Roots', ''),
 5817: ('Apples and Oranges', ''),
 5819: ('Green Bean Jeans', ''),
 5821: ('Squash and Stretch Gym', ''),
 5826: ('Ant Farming Supplies', ''),
 5827: ('Shhh! Library.', ''),
 5828: ('Couch Potato Furniture', ''),
 5830: ('Spill the Beans', ''),
 5833: ('The Salad Bar', ''),
 5835: ('Withering The Witcher', ''),
 5836: ("Got Any Grapes?", ''),
 5837: ('Pizza Taco Burgers', ''),
 9501: ('Lullaby Library', ''),
 9503: ('The Snooze Bar', ''),
 9504: ('Gag Shop', ''),
 9505: (lToonHQ, ''),
 9506: ('Clothing Shop', ''),
 9508: ('', ''),
 9601: ('Snuggle Inn', ''),
 9602: ('Forty Winks for the Price of Twenty', ''),
 9604: ("Ed's Red Bed Spreads", ''),
 9605: ('Cloud Nine Design', ''),
 9607: ("Big Mama's Bahama Pajamas", ''),
 9608: ('Cat Nip for Cat Naps', ''),
 9609: ('Deep Sleep for Cheap', ''),
 9613: ('Clock Cleaners', ''),
 9616: ('Lights Out Electric Co.', ''),
 9617: ('Crib Notes - Music to Sleep By', ''),
 9619: ('Relax to the Max', ''),
 9620: ("PJ's Taxi Service", ''),
 9622: ('Sleepy Time Pieces', ''),
 9625: ('Curl Up Beauty Parlor', ''),
 9626: ('Bed Time Stories', ''),
 9627: ('The Sleepy Teepee', ''),
 9628: ('Call It a Day Calendars', ''),
 9629: ('Silver Lining Jewelers', ''),
 9630: ('Rock to Sleep Quarry', ''),
 9631: ('Down Time Watch Repair', ''),
 9633: ('The Dreamland Screening Room', ''),
 9634: ('Mind Over Mattress', ''),
 9636: ('Insomniac Insurance', ''),
 9639: ('House of Hibernation', ''),
 9640: ('Nightstand Furniture Company', ''),
 9642: ('Sawing Wood Slumber Lumber', ''),
 9643: ('Shut-Eye Optometry', ''),
 9644: ('Pillow Fights Nightly', ''),
 9645: ('The All Tucked Inn', ''),
 9647: ('Make Your Bed! Hardware Store', ''),
 9649: ('Snore or Less', ''),
 9650: ('Crack of Dawn Repairs', ''),
 9651: ('For Richer or Snorer', ''),
 9652: ('', ''),
 9703: ('Fly By Night Travel Agency', ''),
 9704: ('Night Owl Pet Shop', ''),
 9705: ('Asleep At The Wheel Car Repair', ''),
 9706: ('Tooth Fairy Dentistry', ''),
 9707: ("Dawn's Yawn & Garden Center", ''),
 9708: ('Bed Of Roses Florist', ''),
 9709: ('Pipe Dream Plumbers', ''),
 9710: ('REM Optometry', ''),
 9711: ('Wake-Up Call Phone Company', ''),
 9712: ("Counting Sheep - So You Don't Have To!", ''),
 9713: ('Wynken, Blynken & Nod, Attorneys at Law', ''),
 9714: ('Dreamboat Marine Supply', ''),
 9715: ('First Security Blanket Bank', ''),
 9716: ('Wet Blanket Party Planners', ''),
 9717: ("Baker's Dozin' Doughnuts", ''),
 9718: ("Sandman's Sandwiches", ''),
 9719: ('Armadillo Pillow Company', ''),
 9720: ('Talking In Your Sleep Voice Training', ''),
 9721: ('Snug As A Bug Rug Dealer', ''),
 9722: ('Dream On Talent Agency', ''),
 9725: ("Rock a Doodle Doo", ''),
 9727: ('You Snooze, You Lose', ''),
 9736: ('Dream Jobs Employment Agency', ''),
 9737: ("Waltzing Matilda's Dance School", ''),
 9738: ('House of Zzzzzs', ''),
 9740: ('Hit The Sack Fencing School', ''),
 9741: ("Don't Let The Bed Bugs Bite Exterminators", ''),
 9744: ("Rip Van Winkle's Wrinkle Cream", ''),
 9752: ('Midnight Oil & Gas Company', ''),
 9753: ("Moonbeam's Ice Creams", ''),
 9754: ('Sleepless in the Saddle All Night Pony Rides', ''),
 9755: ('Bedknobs & Broomsticks Movie House', ''),
 9756: ('', ''),
 9759: ('Sleeping Beauty Parlor', ''),
 3507: ('Gag Shop', ''),
 3508: (lToonHQ, ''),
 3509: ('Clothing Shop', ''),
 3511: ('', ''),
 3601: ('Northern Lights Electric Company', ''),
 3602: ("Nor'easter Bonnets", ''),
 3605: ('', ''),
 3607: ('The Blizzard Wizard', ''),
 3608: ('Nothing to Luge', ''),
 3610: ("Mike's Massive Mukluk Mart", ''),
 3611: ("Mr. Cow's Snow Plows", ''),
 3612: ('Igloo Design', ''),
 3613: ('Ice Cycle Bikes', ''),
 3614: ('Snowflakes Cereal Company', ''),
 3615: ('Fried Baked Alaskas', ''),
 3617: ('Cold Air Balloon Rides', ''),
 3618: ('Snow Big Deal! Crisis Management', ''),
 3620: ('Skiing Clinic', ''),
 3621: ('The Melting Ice Cream Bar', ''),
 3622: ('', ''),
 3623: ('The Mostly Toasty Bread Company', ''),
 3624: ('Subzero Sandwich Shop', ''),
 3625: ("Auntie Freeze's Radiator Supply", ''),
 3627: ('St. Bernard Kennel Club', ''),
 3629: ('Pea Soup Cafe', ''),
 3630: ('Icy London, Icy France Travel Agency', ''),
 3634: ('Easy Chair Lifts', ''),
 3635: ('Used Firewood', ''),
 3636: ('Affordable Goosebumps', ''),
 3637: ("Kate's Skates", ''),
 3638: ('Toboggan or Not Toboggan', ''),
 3641: ("Fred's Red Sled Beds", ''),
 3642: ('Eye of the Storm Optics', ''),
 3643: ('Snowball Hall', ''),
 3644: ('Melted Ice Cubes', ''),
 3647: ('The Sanguine Penguin Tuxedo Shop', ''),
 3648: ('Instant Ice', ''),
 3649: ('Hambrrrgers', ''),
 3650: ('Antarctic Antiques', ''),
 3651: ("Frosty Freddy's Frozen Frankfurters", ''),
 3653: ('Ice House Jewelry', ''),
 3654: ('', ''),
 3702: ('Winter Storage', ''),
 3703: ('', ''),
 3705: ('Icicles Built for Two', ''),
 3706: ("Shiverin' Shakes Malt Shop", ''),
 3707: ('Snowplace Like Home', ''),
 3708: ("Pluto's Place", ''),
 3710: ('Dropping Degrees Diner', ''),
 3711: ('', ''),
 3712: ('Go With the Floe', ''),
 3713: ('Chattering Teeth, Subzero Dentist', ''),
 3715: ("Aunt Arctic's Soup Shop", ''),
 3716: ('Road Salt and Pepper', ''),
 3717: ('Juneau What I Mean?', ''),
 3718: ('Designer Inner Tubes', ''),
 3719: ('Ice Cube on a Stick', ''),
 3721: ("Noggin's Toboggan Bargains", ''),
 3722: ('Snow Bunny Ski Shop', ''),
 3723: ("Shakey's Snow Globes", ''),
 3724: ('The Chattering Chronicle', ''),
 3725: ('You Sleigh Me', ''),
 3726: ('Solar Powered Blankets', ''),
 3728: ('Lowbrow Snowplows', ''),
 3729: ('', ''),
 3730: ('Snowmen Bought & Sold', ''),
 3731: ('Portable Fireplaces', ''),
 3732: ('The Frozen Nose', ''),
 3734: ('Icy Fine, Do You? Optometry', ''),
 3735: ('Polar Ice Caps', ''),
 3736: ('Diced Ice at a Nice Price', ''),
 3737: ('Downhill Diner', ''),
 3738: ("Heat-Get It While It's Hot", ''),
 3739: ('', ''),
 3801: ('Toon HQ', ''),
 3806: ('Alpine Chow Line', ''),
 3807: ('Used Groundhog Shadows', ''),
 3808: ('The Sweater Lodge', ''),
 3809: ('Ice Saw It Too', ''),
 3810: ('A Better Built Quilt', ''),
 3811: ('Your Snow Angel', ''),
 3812: ('Mittens for Kittens', ''),
 3813: ("Snowshoes You Can't Refuse", ''),
 3814: ('Malt in Your Mouth Soda Fountain', ''),
 3815: ('The Toupee Chalet', ''),
 3816: ('Just So Mistletoe', ''),
 3817: ('Winter Wonderland Walking Club', ''),
 3818: ('The Shovel Hovel', ''),
 3819: ('Clean Sweep Chimney Service', ''),
 3820: ('Snow Whitening', ''),
 3821: ('Hibernation Vacations', ''),
 3823: ('Precipitation Foundation', ''),
 3824: ('Open Fire Chestnut Roasting', ''),
 3825: ('Cool Cat Hats', ''),
 3826: ('Oh My Galoshes!', ''),
 3827: ('Choral Wreaths', ''),
 3828: ("Snowman's Land", ''),
 3829: ('Pinecone Zone', ''),
 3830: ('Wait and See Goggle Defogging', '')}
ClosetTimeoutMessage = 'Sorry, you ran out\n of time.'
ClosetNotOwnerMessage = "This isn't your closet, but you may try on the clothes."
ClosetPopupOK = lOK
ClosetPopupCancel = lCancel
ClosetDiscardButton = 'Remove'
ClosetAreYouSureMessage = 'You have deleted some clothes. Do you really want to delete them?'
ClosetYes = lYes
ClosetNo = lNo
ClosetVerifyDelete = 'Really delete %s?'
ClosetShirt = 'this shirt'
ClosetShorts = 'these shorts'
ClosetSkirt = 'this skirt'
ClosetDeleteShirt = 'Delete\nshirt'
ClosetDeleteShorts = 'Delete\nshorts'
ClosetDeleteSkirt = 'Delete\nskirt'
TrunkNotOwnerMessage = "This isn't your trunk, but you may try on the accessories."
TrunkNotPaidMessage = 'Only Paid Members can wear accessories, but you may try them on.'
TrunkAreYouSureMessage = 'You have deleted some accessories. Do you really want to delete them?'
TrunkHat = 'this hat'
TrunkGlasses = 'these glasses'
TrunkBackpack = 'this backpack'
TrunkShoes = 'these shoes'
TrunkDeleteHat = 'Delete\nhat'
TrunkDeleteGlasses = 'Delete\nglasses'
TrunkDeleteBackpack = 'Delete\nbackpack'
TrunkDeleteShoes = 'Delete\nshoes'
EstateOwnerLeftMessage = "Sorry, the owner of this estate left. You'll be sent to the playground in %s seconds"
EstatePopupOK = lOK
EstateTeleportFailed = "Couldn't go home. Try again!"
EstateTeleportFailedNotFriends = "Sorry, %s is in a Toon's estate that you are not friends with."
EstateTargetGameStart = 'The Toon-up Target game has started!'
EstateTargetGameInst = "The more you hit the red target, the more you'll get Tooned up."
EstateTargetGameEnd = 'The Toon-up Target game is now over…'
AvatarsHouse = '%s\n House'
BankGuiCancel = lCancel
BankGuiOk = lOK
DistributedBankNoOwner = 'Sorry, this is not your bank.'
DistributedBankNotOwner = 'Sorry, this is not your bank.'
FishGuiCancel = lCancel
FishGuiOk = 'Sell All'
FishTankValue = 'Hi, %(name)s! You have %(num)s fish in your bucket worth a total of %(value)s Jellybeans. Do you want to sell them all?'
FlowerGuiCancel = lCancel
FlowerGuiOk = 'Sell All'
FlowerBasketValue = '%(name)s, you have %(num)s flowers in your basket worth a total of %(value)s Jellybeans. Do you want to sell them all?'

def GetPossesive(name):
    if name[-1:] == 's':
        possesive = name + "'"
    else:
        possesive = name + "'s"
    return possesive


PetTrait2descriptions = {'hungerThreshold': ('Always Hungry',
                     'Often Hungry',
                     'Sometimes Hungry',
                     'Rarely Hungry'),
 'boredomThreshold': ('Always Bored',
                      'Often Bored',
                      'Sometimes Bored',
                      'Rarely Bored'),
 'angerThreshold': ('Always Grumpy',
                    'Often Grumpy',
                    'Sometimes Grumpy',
                    'Rarely Grumpy'),
 'forgetfulness': ('Always Forgets',
                   'Often Forgets',
                   'Sometimes Forgets',
                   'Rarely Forgets'),
 'excitementThreshold': ('Very Calm',
                         'Pretty Calm',
                         'Pretty Excitable',
                         'Very Excitable'),
 'sadnessThreshold': ('Always Sad',
                      'Often Sad',
                      'Sometimes Sad',
                      'Rarely Sad'),
 'restlessnessThreshold': ('Always Restless',
                           'Often Restless',
                           'Sometimes Restless',
                           'Rarely Restless'),
 'playfulnessThreshold': ('Rarely Playful',
                          'Sometimes Playful',
                          'Often Playful',
                          'Always Playful'),
 'lonelinessThreshold': ('Always Lonely',
                         'Often Lonely',
                         'Sometimes Lonely',
                         'Rarely Lonely'),
 'fatigueThreshold': ('Always Tired',
                      'Often Tired',
                      'Sometimes Tired',
                      'Rarely Tired'),
 'confusionThreshold': ('Always Confused',
                        'Often Confused',
                        'Sometimes Confused',
                        'Rarely Confused'),
 'surpriseThreshold': ('Always Surprised',
                       'Often Surprised',
                       'Sometimes Surprised',
                       'Rarely Surprised'),
 'affectionThreshold': ('Rarely Affectionate',
                        'Sometimes Affectionate',
                        'Often Affectionate',
                        'Always Affectionate')}
FireworksInstructions = lToonHQ + ': Hit the "Page Up" key to see the show!'
startFireworksResponse = "Usage: startFireworksShow ['num']\n                                         'num' = %s - New Years\n                                         %s - Party Summer \n                                         %s - 4th of July"
FireworksJuly4Beginning = lToonHQ + ': Welcome to summer fireworks! Enjoy the show!'
FireworksJuly4Ending = lToonHQ + ': Hope you enjoyed the show! Have a great summer!'
FireworksNewYearsEveBeginning = lToonHQ + ': Happy New Year! Enjoy the fireworks show!'
FireworksNewYearsEveEnding = lToonHQ + ': Hope you enjoyed the show! Happy New Year!'
FireworksComboBeginning = lToonHQ + ': Enjoy lots of Laffs with Toon fireworks!'
FireworksComboEnding = lToonHQ + ': Thank you, Toons! Hope you enjoyed the show!'
BlockerTitle = 'LOADING TOON ISLAND: AFTERMATH'
BlockerLoadingTexts = ['Scrubbing pie tins',
 'Baking pie crusts',
 'Heating pie filling',
 'Loading Doodle chow',
 'Stringing Jungle Vines',
 'Uncaging those spiders who crawl down jungle vines',
 'Planting squirting flower seeds',
 'Stretching trampolines',
 'Herding pigs',
 "Tweaking 'SPLAT' sounds",
 'Cleaning Hypno-glasses',
 'Unbottling ink for Toon News',
 'Clipping TNT fuses',
 "Setting up 'Under Construction' sign in Acorn Acres",
 'Waking Donald Duck',
 'Teaching new moves to dancing fire hydrants',
 'Binding Shticker Books',
 'Analyzing quacks',
 'Harvesting Jellybean pods',
 'Emptying fish buckets',
 'Corralling trashcan trash',
 'Spreading Cog grease',
 'Polishing kart trophies',
 'Balancing scale for weighing 1 Ton weights',
 'Practicing Victory Dances',
 'Preparing wackiness',
 "Giving Mickey Mouse the 'five minutes' sign",
 'Testing white gloves',
 'Bending underwater rings',
 'Spooling red tape',
 'Freezing Brrrgh ice',
 'Tuning falling pianos']
TIP_NONE = 0
TIP_GENERAL = 1
TIP_STREET = 2
TIP_MINIGAME = 3
TIP_COGHQ = 4
TIP_ESTATE = 5
TIP_KARTING = 6
TIP_GOLF = 7
TipTitle = 'Toon TIP:'
TipDict = {TIP_NONE: ('',),
 TIP_GENERAL: ('Quickly check your ToonTask progress by holding down the "End" key.',
               'Quickly check your Gag page by holding down the "Home" key.',
               'Open your Friends List by pressing the "F7" key.',
               'Open or close your Shticker Book by pressing the "F8" key.',
               'You can look up by pressing the "Page Up" key and look down by pressing the "Page Down" key.',
               'Press the "Control" key to jump.',
               'Press the "F9" key to take a screenshot, which will be saved in your Toontown folder on your computer.',
               'You can change your screen resolution, adjust audio, and control other options on the Options Page in the Shticker Book.',
               "Try on your friend's clothing at the closet in their house.",
               'You can go to your house using the "Go Home" button on your map.',
               'Every time you turn in a completed ToonTask your Laff points are automatically refilled.',
               'You can browse the selection at Clothing Stores even without a clothing ticket.',
               'Rewards for some ToonTasks allow you to carry more gags and Jellybeans.',
               'You can have up to 50 friends on your Friends List.',
               'Some ToonTask rewards let you teleport to playgrounds in Toontown by using the Map Page in the Shticker Book.',
               'Increase your Laff points in the Playgrounds by collecting treasures like stars and ice cream cones.',
               'To heal quickly after a battle, go to your estate and play with your Doodle.',
               'Change to different views of your Toon by pressing the Tab Key.',
               'Sometimes you can find several different ToonTasks offered for the same reward. Shop around!',
               'Finding friends with similar ToonTasks is a fun way to progress through the game.',
               'You never need to save your Toontown progress. The Toontown servers continually save all the necessary information.',
               'You can whisper to other Toons either by clicking on them or by selecting them from your Friends List.',
               'Some SpeedChat phrases play emotion animations on your Toon.',
               'If the area you are in is crowded, try changing Districts. Go to the District Page in the Shticker Book and select a different one.',
               'If you actively rescue buildings you will get a bronze, silver, or gold star above your Toon.',
               'If you rescue enough buildings to get a star above your head you may find your name on the blackboard in a Toon HQ.',
               'Rescued buildings are sometimes recaptured by the Cogs. The only way to keep your star is to go out and rescue more buildings!',
               'The names of your True Friends will appear in Blue.',
               'See if you can collect all the fish in Toontown!',
               'Different ponds hold different fish. Try them all!',
               'When your fishing bucket is full sell your fish to the Fishermen in the Playgrounds.',
               'You can sell your fish to the Fishermen or inside Pet Shops.',
               'Stronger fishing rods catch heavier fish but cost more Jellybeans to use.',
               'You can purchase stronger fishing rods in the Cattlelog.',
               'Heavier fish are worth more Jellybeans to the Pet Shop.',
               'Rare fish are worth more Jellybeans to the Pet Shop.',
               'You can sometimes find bags of Jellybeans while fishing.',
               'Some ToonTasks require fishing items out of the ponds.',
               'Fishing ponds in the Playgrounds have different fish than ponds on the streets.',
               'Some fish are really rare. Keep fishing until you collect them all!',
               'The pond at your estate has fish that can only be found there.',
               'For every 10 species you catch, you will get a fishing trophy!',
               'You can see what fish you have collected in your Shticker Book.',
               'Some fishing trophies reward you with a Laff boost.',
               'Fishing is a good way to earn more Jellybeans.',
               'Adopt a Doodle at the Pet Shop!',
               'Pet Shops get new Doodles to sell every day.',
               'Visit the Pet Shops every day to see what new Doodles they have.',
               'Different neighborhoods have different Doodles offered for adoption.',
               "Show off your stylin' ride and turbo-boost your Laff limit at Goofy Speedway.",
               'Enter Goofy Speedway through the tire-shaped tunnel in Toon Island Central Playground.',
               'Earn Laff points at Goofy Speedway.',
               'Goofy Speedway has six different race tracks. '),
 TIP_STREET: ('There are four types of Cogs: Lawbots, Cashbots, Sellbots, and Bossbots.',
              'Each Gag Track has different amounts of accuracy and damage.',
              'Sound gags will affect all Cogs but will wake up any lured Cogs.',
              'Defeating Cogs in strategic order can greatly increase your chances of winning battles.',
              'The Toon-Up Gag Track lets you heal other Toons in battle.',
              'Gag experience points are doubled during a Cog Invasion!',
              'Multiple Toons can team up and use the same Gag Track in battle to get bonus Cog damage.',
              'In battle, gags are used in order from top to bottom as displayed on the Gag Menu.',
              'The row of circular lights over Cog Building elevators show how many floors will be inside.',
              'Click on a Cog to see more details.',
              'Using high level gags against low level Cogs will not earn any experience points.',
              'A gag that will earn experience has a blue background on the Gag Menu in battle.',
              'Gag experience is multiplied when used inside Cog Buildings. Higher floors have higher multipliers.',
              'When a Cog is defeated, each Toon in that round will get credit for the Cog when the battle is over.',
              'Each street in Toontown has different Cog levels and types.',
              'Sidewalks are safe from Cogs.',
              'On the streets, side doors tell knock-knock jokes when approached.',
              'Some ToonTasks train you for new Gag Tracks. You only get to choose six of the seven Gag Tracks, so choose carefully!',
              'Traps are only useful if you or your friends coordinate using Lure in battle.',
              'Higher level Lures are less likely to miss.',
              'Lower level gags have a lower accuracy against high level Cogs.',
              'Cogs cannot attack once they have been lured in battle.',
              'When you and your friends defeat a Cog building you are rewarded with portraits inside the rescued Toon Building.',
              'Using a Toon-Up gag on a Toon with a full Laff meter will not earn Toon-Up experience.',
              'Cogs will be briefly stunned when hit by any gag. This increases the chance that other gags in the same round will hit.',
              'Drop gags have low chance of hitting, but accuracy is increased when Cogs are first hit by another gag in the same round.',
              'When you\'ve defeated enough Cogs, use the "Cog Radar" by clicking the Cog icons on the Cog Gallery page in your Shticker Book.',
              'During a battle, you can tell which Cog your teammates are attacking by looking at the dashes (-) and Xs.',
              'During a battle, Cogs have a light on them that displays their health; green is healthy, red is nearly destroyed.',
              'A maximum of four Toons can battle at once.',
              'On the street, Cogs are more likely to join a fight against multiple Toons than just one Toon.',
              'The two most difficult Cogs of each type are only found in buildings.',
              'Drop gags never work against lured Cogs.',
              'Cogs tend to attack the Toon that has done them the most damage.',
              'Sound gags do not get bonus damage against lured Cogs.',
              'If you wait too long to attack a lured Cog, it will wake up. Higher level lures last longer.',
              'There are fishing ponds on every street in Toontown. Some streets have unique fish.'),
 TIP_MINIGAME: ('After you fill up your Jellybean jar, any Jellybeans you get from Trolley Games automatically spill over into your bank.',
                'You can use the arrow keys instead of the mouse in the "Match Minnie" Trolley Game.',
                'In the Cannon Game you can use the arrow keys to move your cannon and press the "Control" key to fire.',
                'In the Ring Game, bonus points are awarded when the entire group successfully swims through its rings.',
                'A perfect game of Match Minnie will double your points.',
                'In the Tug-of-War you are awarded more Jellybeans if you play against a tougher Cog.',
                'Trolley Game difficulty varies by neighborhood; ' + lToonIslandCentral + ' has the easiest and ' + lDonaldsDreamland + ' has the hardest.',
                'Certain Trolley Games can only be played in a group.'),
 TIP_COGHQ: ('You must complete your Sellbot Disguise before visiting the V.P.',
             'You must complete your Cashbot Disguise before visiting the C.F.O.',
             'You must complete your Lawbot Disguise before visiting the Chief Justice.',
             'You can jump on Cog Goons to temporarily disable them.',
             'Collect Cog Merits by defeating Sellbot Cogs in battle.',
             'Collect Cogbucks by defeating Cashbot Cogs in battle.',
             'Collect Jury Notices by defeating Lawbot Cogs in battle.',
             'Collect Stock Options by defeating Bossbot Cogs in battle.',
             'You get more Merits, Cogbucks, Jury Notices, or Stock Options from higher level Cogs.',
             'When you collect enough Cog Merits to earn a promotion, go see the Sellbot V.P.!',
             'When you collect enough Cogbucks to earn a promotion, go see the Cashbot C.F.O.!',
             'When you collect enough Jury Notices to earn a promotion, go see the Lawbot Chief Justice!',
             'When you collect enough Stock Options to earn a promotion, go see the Bossbot C.E.O.!',
             'You can talk like a Cog when you are wearing your Cog Disguise.',
             'Up to eight Toons can join together to fight the Sellbot V.P.',
             'Up to eight Toons can join together to fight the Cashbot C.F.O.',
             'Up to eight Toons can join together to fight the Lawbot Chief Justice.',
             'Up to eight Toons can join together to fight the Bossbot C.E.O.',
             'Inside Cog Headquarters follow stairs leading up to find your way.',
             'Each time you battle through a Sellbot HQ factory, you will gain one part of your Sellbot Cog Disguise.',
             'You can check the progress of your Cog Disguise in your Shticker Book.',
             'You can check your promotion progress on your Disguise Page in your Shticker Book.',
             'Make sure you have full gags and a full Laff Meter before going to Cog Headquarters.',
             'As you get promoted, your Cog disguise updates.',
             'You must defeat the ' + Foreman + ' to recover a Sellbot Cog Disguise part.',
             "Earn Cashbot disguise suit parts as rewards for completing ToonTasks in MintyMines.",
             'Cashbots manufacture and distribute their currency, Cogbucks, in three Mints - Coin, Dollar and Bullion.',
             'Wait until the C.F.O. is dizzy to throw a safe, or he will use it as a helmet! Hit the helmet with another safe to knock it off.',
             'Earn Lawbot disguise suit parts as rewards for completing ToonTasks for Professor Flake.',
             "It pays to be puzzled: the virtual Cogs in Lawbot HQ won't reward you with Jury Notices."),
 TIP_ESTATE: ('Doodles can understand some SpeedChat phrases. Try them!',
              'Use the "Pet" SpeedChat menu to ask your Doodle to do tricks.',
              "You can teach Doodles tricks with training lessons from Clarabelle's Cattlelog.",
              'Reward your Doodle for doing tricks.',
              "If you visit a friend's estate, your Doodle will come too.",
              'Feed your Doodle a Jellybean when it is hungry.',
              'Click on a Doodle to get a menu where you can Feed, Scratch, and Call him.',
              'Doodles love company. Invite your friends over to play!',
              'All Doodles have unique personalities.',
              'You can return your Doodle and adopt a new one at the Pet Shops.',
              'When a Doodle performs a trick, the Toons around it heal.',
              'Doodles become better at tricks with practice. Keep at it!',
              'More advanced Doodle tricks heal Toons faster.',
              'Experienced Doodles can perform more tricks before getting tired.',
              'You can see a list of nearby Doodles in your Friends List.',
              "Purchase furniture from Clarabelle's Cattlelog to decorate your house.",
              'The bank inside your house holds extra Jellybeans.',
              'The closet inside your house holds extra clothes.',
              "Go to your friend's house and try on his clothes.",
              "Purchase better fishing rods from Clarabelle's Cattlelog.",
              'Call Clarabelle using the phone inside your house.',
              'Clarabelle sells a larger closet that holds more clothing.',
              'Make room in your closet before using a Clothing Ticket.',
              'Clarabelle sells everything you need to decorate your house.',
              'Check your mailbox for deliveries after ordering from Clarabelle.',
              "Clothing from Clarabelle's Cattlelog takes one hour to be delivered.",
              "Wallpaper and flooring from Clarabelle's Cattlelog take one hour to be delivered.",
              "Furniture from Clarabelle's Cattlelog takes a full day to be delivered.",
              'Store extra furniture in your attic.',
              'You will get a notice from Clarabelle when a new Cattlelog is ready.',
              'You will get a notice from Clarabelle when a Cattlelog delivery arrives.',
              'New Cattlelogs are delivered each week.',
              'Look for limited-edition holiday items in the Cattlelog.',
              'Move unwanted furniture to the trash can.',
              'Some fish, like the Holey Mackerel, are more commonly found in Toon Estates.',
              'You can invite your friends to your Estate using SpeedChat.',
              'Did you know the color of your house matches the color of your Pick-A-Toon panel?'),
 TIP_KARTING: ("Buy a Roadster, TUV, or Cruiser kart in Goofy's Auto Shop.",
               "Customize your kart with decals, rims and more in Goofy's Auto Shop.",
               'Earn tickets by kart racing at Goofy Speedway.',
               "Tickets are the only currency accepted at Goofy's Auto Shop.",
               'Tickets are required as deposits to race.',
               'A special page in the Shticker Book allows you to customize your kart.',
               'A special page in the Shticker Book allows you to view records on each track.',
               'A special page in the Shticker Book allows you to display trophies.',
               'Screwball Stadium is the easiest track at Goofy Speedway.',
               'Airborne Acres has the most hills and jumps of any track at Goofy Speedway.',
               'Blizzard Boulevard is the most challenging track at Goofy Speedway.'),
 TIP_GOLF: ('Press the Tab key to see a top view of the golf course.', 'Press the Up Arrow key to point yourself towards the golf hole.', 'Swinging the club is just like throwing a pie.')}
FishGenusNames = {0: 'Balloon Fish',
 2: 'Cat Fish',
 4: 'Clown Fish',
 6: 'Frozen Fish',
 8: 'Star Fish',
 10: 'Holey Mackerel',
 12: 'Dog Fish',
 14: 'Amore Eel',
 16: 'Nurse Shark',
 18: 'King Crab',
 20: 'Moon Fish',
 22: 'Sea Horse',
 24: 'Pool Shark',
 26: 'Bear Acuda',
 28: 'Cutthroat Trout',
 30: 'Piano Tuna',
 32: 'Peanut Butter & Jellyfish',
 34: 'Devil Ray'}
FishSpeciesNames = {0: ('Balloon Fish',
     'Hot Air Balloon Fish',
     'Weather Balloon Fish',
     'Water Balloon Fish',
     'Red Balloon Fish'),
 2: ('Cat Fish',
     'Siamese Cat Fish',
     'Alley Cat Fish',
     'Tabby Cat Fish',
     'Tom Cat Fish'),
 4: ('Clown Fish',
     'Sad Clown Fish',
     'Party Clown Fish',
     'Circus Clown Fish'),
 6: ('Frozen Fish',),
 8: ('Star Fish',
     'Five Star Fish',
     'Rock Star Fish',
     'Shining Star Fish',
     'All Star Fish'),
 10: ('Holey Mackerel',),
 12: ('Dog Fish',
      'Bull Dog Fish',
      'Hot Dog Fish',
      'Dalmatian Dog Fish',
      'Puppy Dog Fish'),
 14: ('Amore Eel', 'Electric Amore Eel'),
 16: ('Nurse Shark', 'Clara Nurse Shark', 'Florence Nurse Shark'),
 18: ('King Crab', 'Alaskan King Crab', 'Old King Crab'),
 20: ('Moon Fish',
      'Full Moon Fish',
      'Half Moon Fish',
      'New Moon Fish',
      'Crescent Moon Fish',
      'Harvest Moon Fish'),
 22: ('Sea Horse',
      'Rocking Sea Horse',
      'Clydesdale Sea Horse',
      'Arabian Sea Horse'),
 24: ('Pool Shark',
      'Kiddie Pool Shark',
      'Swimming Pool Shark',
      'Olympic Pool Shark'),
 26: ('Brown Bear Acuda',
      'Black Bear Acuda',
      'Koala Bear Acuda',
      'Honey Bear Acuda',
      'Polar Bear Acuda',
      'Panda Bear Acuda',
      'Kodiac Bear Acuda',
      'Grizzly Bear Acuda'),
 28: ('Cutthroat Trout', 'Captain Cutthroat Trout', 'Scurvy Cutthroat Trout'),
 30: ('Piano Tuna',
      'Grand Piano Tuna',
      'Baby Grand Piano Tuna',
      'Upright Piano Tuna',
      'Player Piano Tuna'),
 32: ('Peanut Butter & Jellyfish',
      'Grape PB&J Fish',
      'Crunchy PB&J Fish',
      'Strawberry PB&J Fish',
      'Concord Grape PB&J Fish'),
 34: ('Devil Ray',)}
CogPartNames = ('Upper Left Leg',
 'Lower Left Leg',
 'Left Foot',
 'Upper Right Leg',
 'Lower Right Leg',
 'Right Foot',
 'Left Shoulder',
 'Right Shoulder',
 'Chest',
 'Health Meter',
 'Pelvis',
 'Upper Left Arm',
 'Lower Left Arm',
 'Left Hand',
 'Upper Right Arm',
 'Lower Right Arm',
 'Right Hand')
CogPartNamesSimple = ('Upper Torso',)
SellbotLegFactorySpecMainEntrance = 'Front Entrance'
SellbotLegFactorySpecLobby = 'Lobby'
SellbotLegFactorySpecLobbyHallway = 'Lobby Hallway'
SellbotLegFactorySpecGearRoom = 'Gear Room'
SellbotLegFactorySpecBoilerRoom = 'Boiler Room'
SellbotLegFactorySpecEastCatwalk = 'East Catwalk'
SellbotLegFactorySpecPaintMixer = 'Paint Mixer'
SellbotLegFactorySpecPaintMixerStorageRoom = 'Paint Mixer Storage Room'
SellbotLegFactorySpecWestSiloCatwalk = 'West Silo Catwalk'
SellbotLegFactorySpecPipeRoom = 'Pipe Room'
SellbotLegFactorySpecDuctRoom = 'Duct Room'
SellbotLegFactorySpecSideEntrance = 'Side Entrance'
SellbotLegFactorySpecStomperAlley = 'Stomper Alley'
SellbotLegFactorySpecLavaRoomFoyer = 'Lava Room Foyer'
SellbotLegFactorySpecLavaRoom = 'Lava Room'
SellbotLegFactorySpecLavaStorageRoom = 'Lava Storage Room'
SellbotLegFactorySpecWestCatwalk = 'West Catwalk'
SellbotLegFactorySpecOilRoom = 'Oil Room'
SellbotLegFactorySpecLookout = 'Lookout'
SellbotLegFactorySpecWarehouse = 'Warehouse'
SellbotLegFactorySpecOilRoomHallway = 'Oil Room Hallway'
SellbotLegFactorySpecEastSiloControlRoom = 'East Silo Control Room'
SellbotLegFactorySpecWestSiloControlRoom = 'West Silo Control Room'
SellbotLegFactorySpecCenterSiloControlRoom = 'Center Silo Control Room'
SellbotLegFactorySpecEastSilo = 'East Silo'
SellbotLegFactorySpecWestSilo = 'West Silo'
SellbotLegFactorySpecCenterSilo = 'Center Silo'
SellbotLegFactorySpecEastSiloCatwalk = 'East Silo Catwalk'
SellbotLegFactorySpecWestElevatorShaft = 'West Elevator Shaft'
SellbotLegFactorySpecEastElevatorShaft = 'East Elevator Shaft'
SellbotLegFactorySpecFatalFact1 = 'East Wing Warehouse'
SellbotLegFactoryFatalLavaRoom = 'East Wing Parkour Challenge'
SellbotLegFactoryFatalFact2 = 'East Wing Parkour Battle'
SellbotLegFactoryFatalLavaRoom2 = 'East Wing Gear Challenge'
SellbotLegFactoryFatalFact3 = 'East Wing Gear Battle'
SellbotLegFactorySpecFatalFactoryEastCatWalk = 'East Wing Catwalk'
FishBingoBingo = 'BINGO!'
FishBingoVictory = 'VICTORY!!'
FishBingoJackpot = 'JACKPOT!'
FishBingoGameOver = 'GAME OVER'
FishBingoIntermission = 'Intermission\nEnds In:'
FishBingoNextGame = 'Next Game\nStarts In:'
FishBingoTypeNormal = 'Classic'
FishBingoTypeCorners = 'Four Corners'
FishBingoTypeDiagonal = 'Diagonals'
FishBingoTypeThreeway = 'Three Way'
FishBingoTypeBlockout = 'BLOCKOUT!'
FishBingoStart = "It's time for Fish Bingo! Go to any available pier to play!"
FishBingoOngoing = 'Welcome! Fish Bingo is currently in progress.'
FishBingoEnd = 'Hope you had fun playing Fish Bingo.'
FishBingoHelpMain = 'Welcome to Toontown Fish Bingo! Everyone at the pond works together to fill the card before time runs out.'
FishBingoHelpFlash = 'When you catch a fish, click on one of the flashing squares to mark the card.'
FishBingoHelpNormal = 'This is a Classic Bingo card. Mark any row down, across or diagonally to win.'
FishBingoHelpDiagonals = 'Mark both of the diagonals to win.'
FishBingoHelpCorners = 'An easy Corners card. Mark all four corners to win.'
FishBingoHelpThreeway = "Three-way. Mark both diagonals and the middle row to win. This one isn't easy!"
FishBingoHelpBingo = 'Bingo!'
FishBingoHelpBlockout = 'Blockout!. Mark the entire card to win. You are competing against all the other ponds for a huge jackpot!'
FishBingoOfferToSellFish = 'Your fish bucket is full. Would you like to sell your fish?'
FishBingoJackpotWin = 'Win %s Jellybeans!'
ResistanceToonupMenu = 'Toon-up'
ResistanceToonupItem = '%s Toon-up'
ResistanceToonupItemMax = 'Max'
ResistanceToonupChat = 'Toons of the World, Toon-up!'
ResistanceRestockMenu = 'Gag-up'
ResistanceRestockItem = 'Gag-up %s'
ResistanceRestockItemAll = 'All'
ResistanceRestockChat = 'Toons of the World, Gag-up!'
ResistanceMoneyMenu = 'Jellybeans'
ResistanceMoneyItem = '%s Jellybeans'
ResistanceMoneyChat = 'Toons of the World, Spend Wisely!'
ResistanceEmote1 = NPCToonNames[9228] + ': Welcome to the Resistance!'
ResistanceEmote2 = NPCToonNames[9228] + ': Use your new emote to identify yourself to other members.'
ResistanceEmote3 = NPCToonNames[9228] + ': Good luck!'
KartUIExit = 'Leave Kart'
KartShop_Cancel = lCancel
KartShop_BuyKart = 'Buy Kart'
KartShop_BuyAccessories = 'Buy Accessories'
KartShop_BuyAccessory = 'Buy Accessory'
KartShop_Cost = 'Cost: %d Tickets'
KartShop_ConfirmBuy = 'Buy the %s for %d Tickets?'
KartShop_NoAvailableAcc = 'No available accessories of this type'
KartShop_FullTrunk = 'Your trunk is full.'
KartShop_ConfirmReturnKart = 'Are you sure you want to return your current Kart?'
KartShop_ConfirmBoughtTitle = 'Congratulations!'
KartShop_NotEnoughTickets = 'Not Enough Tickets!'
KartView_Rotate = 'Rotate'
KartView_Right = 'Right'
KartView_Left = 'Left'
StartingBlock_NotEnoughTickets = "You don't have enough tickets! Try a practice race instead."
StartingBlock_NoBoard = 'Boarding has ended for this race. Please wait for the next race to begin.'
StartingBlock_NoKart = 'You need a kart first! Try asking one of the clerks in the Kart Shop.'
StartingBlock_Occupied = 'This block is currently occupied! Please try another spot.'
StartingBlock_TrackClosed = 'Sorry, this track is closed for remodeling.'
StartingBlock_EnterPractice = 'Would you like to enter a practice race?'
StartingBlock_EnterNonPractice = 'Would you like to enter a %s race for %s tickets?'
StartingBlock_EnterShowPad = 'Would you like to park your car here?'
StartingBlock_KickSoloRacer = 'Toon Battle and Grand Prix races require two or more racers.'
StartingBlock_Loading = 'Going to the Race!'
LeaderBoard_Time = 'Time'
LeaderBoard_Name = 'Racer Name'
LeaderBoard_Daily = 'Daily Scores'
LeaderBoard_Weekly = 'Weekly Scores'
LeaderBoard_AllTime = 'All Time Best Scores'
RecordPeriodStrings = [LeaderBoard_Daily, LeaderBoard_Weekly, LeaderBoard_AllTime]
KartRace_RaceNames = ['Practice', 'Toon Battle', 'Grand Prix']
from toontown.racing import RaceGlobals
KartRace_Go = 'Go!'
KartRace_Reverse = ' Rev'
KartRace_TrackNames = {RaceGlobals.RT_Speedway_1: 'Screwball Stadium',
 RaceGlobals.RT_Speedway_1_rev: 'Screwball Stadium' + KartRace_Reverse,
 RaceGlobals.RT_Rural_1: 'Rustic Raceway',
 RaceGlobals.RT_Rural_1_rev: 'Rustic Raceway' + KartRace_Reverse,
 RaceGlobals.RT_Urban_1: 'City Circuit',
 RaceGlobals.RT_Urban_1_rev: 'City Circuit' + KartRace_Reverse,
 RaceGlobals.RT_Speedway_2: 'Corkscrew Coliseum',
 RaceGlobals.RT_Speedway_2_rev: 'Corkscrew Coliseum' + KartRace_Reverse,
 RaceGlobals.RT_Rural_2: 'Airborne Acres',
 RaceGlobals.RT_Rural_2_rev: 'Airborne Acres' + KartRace_Reverse,
 RaceGlobals.RT_Urban_2: 'Blizzard Boulevard',
 RaceGlobals.RT_Urban_2_rev: 'Blizzard Boulevard' + KartRace_Reverse}
KartRace_Unraced = 'N/A'
KartDNA_KartNames = {0: 'Cruiser',
 1: 'Roadster',
 2: 'Toon Utility Vehicle'}
KartDNA_AccNames = {1000: 'Air Cleaner',
 1001: 'Four Barrel',
 1002: 'Flying Eagle',
 1003: 'Steer Horns',
 1004: 'Straight Six',
 1005: 'Small Scoop',
 1006: 'Single Overhead',
 1007: 'Medium Scoop',
 1008: 'Single Barrel',
 1009: 'Flugle Horn',
 1010: 'Striped Scoop',
 2000: 'Space Wing',
 2001: 'Patched Spare',
 2002: 'Roll Cage',
 2003: 'Single Fin',
 2004: 'Double-decker Wing',
 2005: 'Single Wing',
 2006: 'Standard Spare',
 2007: 'Single Fin',
 2008: 'sp9',
 2009: 'sp10',
 3000: 'Dueling Horns',
 3001: "Freddie's Fenders",
 3002: 'Cobalt Running Boards',
 3003: 'Cobra Sidepipes',
 3004: 'Straight Sidepipes',
 3005: 'Scalloped Fenders',
 3006: 'Carbon Running Boards',
 3007: 'Wood Running Boards',
 3008: 'fw9',
 3009: 'fw10',
 4000: 'Curly Tailpipes',
 4001: 'Splash Fenders',
 4002: 'Dual Exhaust',
 4003: 'Plain Dual Fins',
 4004: 'Plain Mudflaps',
 4005: 'Quad Exhaust',
 4006: 'Dual Flares',
 4007: 'Mega Exhaust',
 4008: 'Striped Dual Fins',
 4009: 'Bubble Duals Fins',
 4010: 'Striped Mudflaps',
 4011: 'Mickey Mudflaps',
 4012: 'Scalloped Mudflaps',
 5000: 'Turbo',
 5001: 'Moon',
 5002: 'Patched',
 5003: 'Three Spoke',
 5004: 'Paint Lid',
 5005: 'Heart',
 5006: 'Mickey',
 5007: 'Five Bolt',
 5008: 'Daisy',
 5009: 'Basketball',
 5010: 'Hypno',
 5011: 'Tribal',
 5012: 'Gemstone',
 5013: 'Five Spoke',
 5014: 'Knockoff',
 6000: 'Number Five',
 6001: 'Splatter',
 6002: 'Checkerboard',
 6003: 'Flames',
 6004: 'Hearts',
 6005: 'Bubbles',
 6006: 'Tiger',
 6007: 'Flowers',
 6008: 'Lightning',
 6009: 'Angel',
 7000: 'Chartreuse',
 7001: 'Peach',
 7002: 'Bright Red',
 7003: 'Red',
 7004: 'Maroon',
 7005: 'Sienna',
 7006: 'Brown',
 7007: 'Tan',
 7008: 'Coral',
 7009: 'Orange',
 7010: 'Yellow',
 7011: 'Cream',
 7012: 'Citrine',
 7013: 'Lime',
 7014: 'Sea Green',
 7015: 'Green',
 7016: 'Light Blue',
 7017: 'Aqua',
 7018: 'Blue',
 7019: 'Periwinkle',
 7020: 'Royal Blue',
 7021: 'Slate Blue',
 7022: 'Purple',
 7023: 'Lavender',
 7024: 'Pink',
 7025: 'Plum',
 7026: 'Black'}
RaceHoodSpeedway = 'Speedway'
RaceHoodRural = 'Rural'
RaceHoodUrban = 'Urban'
RaceTypeCircuit = 'Tournament'
RaceQualified = 'qualified'
RaceSwept = 'swept'
RaceWon = 'won'
Race = 'race'
Races = 'races'
Total = 'total'
GrandTouring = 'Grand Touring'

def getTrackGenreString(genreId):
    genreStrings = ['Speedway', 'Country', 'City']
    return genreStrings[genreId].lower()


def getTunnelSignName(trackId, padId):
    if trackId == 2 and padId == 0:
        return 'tunne1l_citysign'
    elif trackId == 1 and padId == 0:
        return 'tunnel_countrysign1'
    else:
        genreId = RaceGlobals.getTrackGenre(trackId)
        return 'tunnel%s_%ssign' % (padId + 1, RaceGlobals.getTrackGenreString(genreId))


KartTrophyDescriptions = [str(RaceGlobals.QualifiedRaces[0]) + ' ' + RaceHoodSpeedway + ' ' + Race + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[1]) + ' ' + RaceHoodSpeedway + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[2]) + ' ' + RaceHoodSpeedway + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[0]) + ' ' + RaceHoodRural + ' ' + Race + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[1]) + ' ' + RaceHoodRural + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[2]) + ' ' + RaceHoodRural + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[0]) + ' ' + RaceHoodUrban + ' ' + Race + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[1]) + ' ' + RaceHoodUrban + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[2]) + ' ' + RaceHoodUrban + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.TotalQualifiedRaces) + ' ' + Total + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.WonRaces[0]) + ' ' + RaceHoodSpeedway + ' ' + Race + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[1]) + ' ' + RaceHoodSpeedway + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[2]) + ' ' + RaceHoodSpeedway + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[0]) + ' ' + RaceHoodRural + ' ' + Race + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[1]) + ' ' + RaceHoodRural + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[2]) + ' ' + RaceHoodRural + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[0]) + ' ' + RaceHoodUrban + ' ' + Race + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[1]) + ' ' + RaceHoodUrban + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[2]) + ' ' + RaceHoodUrban + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.TotalWonRaces) + ' ' + Total + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonCircuitRaces[0]) + ' ' + RaceTypeCircuit + ' ' + Race + ' ' + RaceQualified,
 str(RaceGlobals.WonCircuitRaces[1]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.WonCircuitRaces[2]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.WonCircuitRaces[0]) + ' ' + RaceTypeCircuit + ' ' + Race + ' ' + RaceWon,
 str(RaceGlobals.WonCircuitRaces[1]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonCircuitRaces[2]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.SweptCircuitRaces[0]) + ' ' + RaceTypeCircuit + ' ' + Race + ' ' + RaceSwept,
 str(RaceGlobals.SweptCircuitRaces[1]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceSwept,
 str(RaceGlobals.SweptCircuitRaces[2]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceSwept,
 GrandTouring,
 str(RaceGlobals.TrophiesPerCup) + ' Kart Racing trophies won! Laff point boost!',
 str(RaceGlobals.TrophiesPerCup * 2) + ' Kart Racing trophies won! Laff point boost!',
 str(RaceGlobals.TrophiesPerCup * 3) + ' Kart Racing trophies won! Laff point boost!']
KartRace_TitleInfo = 'Get Ready to Race'
KartRace_SSInfo = 'Welcome to Screwball Stadium!\nPut the pedal to the metal and hang on tight!\n'
KartRace_CoCoInfo = 'Welcome to Corkscrew Coliseum!\nUse the banked turns to keep your speed up!\n'
KartRace_RRInfo = 'Welcome to Rustic Raceway!\nPlease be kind to the fauna and stay on the track!\n'
KartRace_AAInfo = 'Welcome to Airborne Acres!\nHold onto your hats! It looks bumpy up ahead…\n'
KartRace_CCInfo = 'Welcome to City Circuit!\nWatch out for pedestrians as you speed through downtown!\n'
KartRace_BBInfo = 'Welcome to Blizzard Boulevard!\nWatch your speed. There might be ice out there.\n'
KartRace_GeneralInfo = 'Use Control to throw gags you pick up on the track, and the arrow keys to control your kart.'
KartRace_TrackInfo = {RaceGlobals.RT_Speedway_1: KartRace_SSInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Speedway_1_rev: KartRace_SSInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Speedway_2: KartRace_CoCoInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Speedway_2_rev: KartRace_CoCoInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Rural_1: KartRace_RRInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Rural_1_rev: KartRace_RRInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Rural_2: KartRace_AAInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Rural_2_rev: KartRace_AAInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Urban_1: KartRace_CCInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Urban_1_rev: KartRace_CCInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Urban_2: KartRace_BBInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Urban_2_rev: KartRace_BBInfo + KartRace_GeneralInfo}
KartRecordStrings = {RaceGlobals.Daily: 'daily',
 RaceGlobals.Weekly: 'weekly',
 RaceGlobals.AllTime: 'all time'}
KartRace_FirstSuffix = 'st'
KartRace_SecondSuffix = '    nd'
KartRace_ThirdSuffix = '  rd'
KartRace_FourthSuffix = '   th'
KartRace_WrongWay = 'Wrong\nWay!'
KartRace_LapText = 'Lap %s'
KartRace_FinalLapText = 'Final Lap!'
KartRace_Exit = 'Exit Race'
KartRace_NextRace = 'Next Race'
KartRace_Leave = 'Leave Race'
KartRace_Qualified = 'Qualified!'
KartRace_Record = 'Record!'
KartRace_RecordString = 'You have set a new %s record for %s! Your bonus is %s tickets.'
KartRace_Tickets = 'Tickets'
KartRace_Exclamations = '!'
KartRace_Deposit = 'Deposit'
KartRace_Winnings = 'Winnings'
KartRace_Bonus = 'Bonus'
KartRace_RaceTotal = 'Race Total'
KartRace_CircuitTotal = 'Circuit Total'
KartRace_Trophies = 'Trophies'
KartRace_Zero = '0'
KartRace_Colon = ':'
KartRace_TicketPhrase = '%s ' + KartRace_Tickets
KartRace_DepositPhrase = KartRace_Deposit + KartRace_Colon + '\n'
KartRace_QualifyPhrase = 'Qualify:\n'
KartRace_RaceTimeout = 'You timed out of that race. Your tickets have been refunded. Keep trying!'
KartRace_RaceTimeoutNoRefund = 'You timed out of that race. Your tickets have not been refunded because the Grand Prix had already started. Keep trying!'
KartRace_RacerTooSlow = 'You took too long to finish the race. Your tickets have not been refunded. Keep trying!'
KartRace_PhotoFinish = 'Photo Finish!'
KartRace_CircuitPoints = 'Circuit Points'
CircuitRaceStart = 'The Toontown Grand Prix at Goofy Speedway is about to begin! To win, collect the most points in three consecutive races!'
CircuitRaceOngoing = 'Welcome! The Toontown Grand Prix is currently in progress.'
CircuitRaceEnd = "That's all for today's Toontown Grand Prix at Goofy Speedway. See you next week!"
TrickOrTreatMsg = 'You have already\nfound this treat!'
WinterCarolingMsg = 'You have already been caroling here!'
LawbotBossTempIntro0 = "Hmmm what's on the docket today?"
LawbotBossTempIntro1 = 'Aha, we have a Toon on trial!'
LawbotBossTempIntro2 = "The prosecution's case is strong."
LawbotBossTempIntro3 = 'And here are the public defenders.'
LawbotBossTempIntro4 = "Wait a minute… You're Toons!"
LawbotBossTempJury1 = 'Jury selection will now commence.'
LawbotBossHowToGetEvidence = 'Touch the witness stand to get evidence.'
LawbotBossTrialChat1 = 'Court is now in session'
LawbotBossHowToThrowPies = 'Press the Delete key to throw the evidence\n at the lawyers or into the scale!'
LawbotBossNeedMoreEvidence = 'You need to get more evidence!'
LawbotBossDefenseWins1 = 'Impossible! The defense won?'
LawbotBossDefenseWins2 = 'No. I declare a mistrial! A new one will be scheduled.'
LawbotBossDefenseWins3 = "Hrrmpphh. I'll be in my chambers."
LawbotBossProsecutionWins = 'I find in favor of the plaintiff'
LawbotBossReward = 'I award a promotion and the ability to summon Cogs'
LawbotBossLeaveCannon = 'Leave cannon'
LawbotBossPassExam = 'Bah, so you passed the bar exam.'
LawbotBossTaunts = ['%s, I find you in contempt of court!',
 'Objection sustained!',
 'Strike that from the record.',
 'Your appeal has been rejected. I sentence you to sadness!',
 'Order in the court!']
LawbotBossAreaAttackTaunt = "You're all in contempt of court!"
WitnessToonName = 'Bumpy Bumblebehr'
WitnessToonPrepareBattleTwo = "Oh no! They're putting only Cogs on the jury!\x07Quick, use the cannons and shoot some Toon jurors into the jury chairs.\x07We need %d to get a balanced scale."
WitnessToonNoJuror = 'Oh oh, no Toon jurors. This will be a tough trial.'
WitnessToonOneJuror = 'Cool! There is 1 Toon in the jury!'
WitnessToonSomeJurors = 'Cool! There are %d Toons in the jury!'
WitnessToonAllJurors = 'Awesome! All the jurors are Toons!'
WitnessToonPrepareBattleThree = 'Hurry, touch the witness stand to get evidence.\x07Press the Delete key to throw the evidence at the lawyers, or at the defense pan.'
WitnessToonCongratulations = "You did it! Thank you for a spectacular defense!\x07Here, take these papers the Chief Justice left behind.\x07With it you'll be able to summon Cogs from your Cog Gallery page."
WitnessToonLastPromotion = "\x07Wow, you've reached level %s on your Cog Suit!\x07Cogs don't get promoted higher than that.\x07You can't upgrade your Cog Suit anymore, but you can certainly keep working for the Resistance!"
WitnessToonHPBoost = "\x07You've done a lot of work for the Resistance.\x07The Toon Council has decided to give you another Laff point. Congratulations!"
WitnessToonMaxed = '\x07I see that you have a level %s Cog Suit. Very impressive!\x07On behalf of the Toon Council, thank you for coming back to defend more Toons!'
WitnessToonBonus = 'Wonderful! All the lawyers are stunned. Your evidence weight is %s times heavier for %s seconds'
WitnessToonJuryWeightBonusSingular = {6: 'This is a tough case. You seated %d Toon juror, so your evidence has a bonus weight of %d.',
 7: 'This is a very tough case. You seated %d Toon juror, so your evidence has a bonus weight of %d.',
 8: 'This is the toughest case. You seated %d Toon juror, so your evidence has a bonus weight of %d.'}
WitnessToonJuryWeightBonusPlural = {6: 'This is a tough case. You seated %d Toon jurors, so your evidence has a bonus weight of %d.',
 7: 'This is a very tough case. You seated %d Toon jurors, so your evidence has a bonus weight of %d.',
 8: 'This is the toughest case. You seated %d Toon jurors, so your evidence has a bonus weight of %d.'}
IssueSummons = 'Summon'
SummonDlgTitle = 'Issue a Cog Summons'
SummonDlgButton1 = 'Summon a Cog'
SummonDlgButton2 = 'Summon a Cog Building'
SummonDlgButton3 = 'Summon a Cog Invasion'
SummonDlgSingleConf = 'Would you like to issue a summons to a %s?'
SummonDlgBuildingConf = 'Would you like to summon a %s to a nearby Toon building?'
SummonDlgInvasionConf = 'Would you like to summon a %s invasion?'
SummonDlgNumLeft = 'You have %s left.'
SummonDlgDelivering = 'Delivering Summons…'
SummonDlgSingleSuccess = 'You have successfully summoned the Cog.'
SummonDlgSingleBadLoc = "Sorry, Cogs aren't allowed here. Try somewhere else."
SummonDlgBldgSuccess = 'You have successfully summoned the Cogs. %s has agreed to let them temporarily take over %s!'
SummonDlgBldgSuccess2 = 'You have successfully summoned the Cogs. A Shopkeeper has agreed to let them temporarily take over their building!'
SummonDlgBldgBadLoc = 'Sorry, there are no Toon buildings nearby for the Cogs to take over.'
SummonDlgInvasionSuccess = "You have successfully summoned the Cogs. It's an invasion!"
SummonDlgInvasionBusy = 'A %s cannot be found now. Try again when the Cog invasion is over.'
SummonDlgInvasionFail = 'Sorry, the Cog invasion has failed.'
SummonDlgShopkeeper = 'The Shopkeeper '
PolarPlaceEffect1 = NPCToonNames[3306] + ': Welcome to Polar Place!'
PolarPlaceEffect2 = NPCToonNames[3306] + ': Try this on for size.'
PolarPlaceEffect3 = NPCToonNames[3306] + ': Your new look will only work in ' + lTheBrrrgh + '.'
GreenToonEffectMsg = NPCToonNames[5312] + ': You look Toontastic in green!'
LaserGameMine = 'Skull Finder!'
LaserGameRoll = 'Matching'
LaserGameAvoid = 'Avoid the Skulls'
LaserGameDrag = 'Drag three of a color in a row'
LaserGameDefault = 'Unknown Game'
PinballHiScore = 'High Score:     %s\n'
PinballHiScoreAbbrev = '…'
PinballYourBestScore = 'Your Best Score:\n'
PinballScore = 'Score:            %d x %d = '
PinballScoreHolder = '%s\n'
GagTreeFeather = 'Feather Gag Tree'
GagTreeJugglingBalls = 'Juggling Balls Gag Tree'
StatuaryFountain = 'Fountain'
StatuaryDonald = 'Donald Statue'
StatuaryMinnie = 'Minnie Statue'
StatuaryMickey1 = 'Mickey Statue'
StatuaryMickey2 = 'Mickey Fountain'
StatuaryToon = 'Toon Statue'
StatuaryToonWave = 'Toon Wave Statue'
StatuaryToonVictory = 'Toon Victory Statue'
StatuaryToonCrossedArms = 'Toon Authority Statue'
StatuaryToonThinking = 'Toon Embrace Statue'
StatuaryMeltingSnowman = 'Melting Snowman'
StatuaryMeltingSnowDoodle = 'Melting SnowDoodle'
StatuaryGardenAccelerator = 'Insta-Grow Fertilizer'
AnimatedStatuaryFlappyCog = 'Flappy Cog'
FlowerColorStrings = ['Red',
 'Orange',
 'Violet',
 'Blue',
 'Pink',
 'Yellow',
 'White',
 'Green']
FlowerSpeciesNames = {49: 'Daisy',
 50: 'Tulip',
 51: 'Carnation',
 52: 'Lily',
 53: 'Daffodil',
 54: 'Pansy',
 55: 'Petunia',
 56: 'Rose'}
FlowerFunnyNames = {49: ('School Daisy',
      'Lazy Daisy',
      'Midsummer Daisy',
      'Freshasa Daisy',
      'Whoopsie Daisy',
      'Upsy Daisy',
      'Crazy Daisy',
      'Hazy Dazy'),
 50: ('Onelip', 'Twolip', 'Threelip'),
 51: ('What-in Carnation',
      'Instant Carnation',
      'Hybrid Carnation',
      'Side Carnation',
      'Model Carnation'),
 52: ('Lily-of-the-Alley',
      'Lily Pad',
      'Tiger Lily',
      'Livered Lily',
      'Chili Lily',
      'Silly Lily',
      'Indubitab Lily',
      'Dilly Lilly'),
 53: ('Laff-o-dil',
      'Daffy Dill',
      'Giraff-o-dil',
      'Time and a half-o-dil'),
 54: ('Dandy Pansy',
      'Chim Pansy',
      'Potsen Pansy',
      'Marzi Pansy',
      'Smarty Pansy'),
 55: ('Car Petunia', 'Platoonia'),
 56: ("Summer's Last Rose",
      'Corn Rose',
      'Tinted Rose',
      'Stinking Rose',
      'Istilla Rose')}
FlowerVarietyNameFormat = '%s %s'
FlowerUnknown = '????'
FloweringNewEntry = 'New Entry'
ShovelNameDict = {0: 'Tin',
 1: 'Bronze',
 2: 'Silver',
 3: 'Gold'}
WateringCanNameDict = {0: 'Small',
 1: 'Medium',
 2: 'Large',
 3: 'Huge'}
GardeningPlant = 'Plant'
GardeningWater = 'Water'
GardeningRemove = 'Remove'
GardeningPick = 'Pick'
GardeningFull = 'Full'
GardeningSkill = 'Skill'
GardeningWaterSkill = 'Water Skill'
GardeningShovelSkill = 'Shovel Skill'
GardeningNoSkill = 'No Skill Up'
GardeningPlantFlower = 'Plant\nFlower'
GardeningPlantTree = 'Plant\nTree'
GardeningPlantItem = 'Plant\nItem'
PlantingGuiOk = 'Plant'
PlantingGuiCancel = 'Cancel'
PlantingGuiReset = 'Reset'
GardeningChooseBeans = 'Choose the Jellybeans you want to plant.'
GardeningChooseBeansItem = 'Choose the Jellybeans / item you want to plant.'
GardeningChooseToonStatue = 'Choose the Toon you want to create a statue of.'
GardenShovelLevelUp = "Congratulations you've earned a %(shovel)s! You've mastered the %(oldbeans)d bean flower! To progress you should pick %(newbeans)d bean flowers."
GardenShovelSkillLevelUp = "Congratulations! You've mastered the %(oldbeans)d bean flower! To progress you should pick %(newbeans)d bean flowers."
GardenShovelSkillMaxed = "Amazing! You've maxed out your shovel skill!"
GardenWateringCanLevelUp = "Congratulations you've earned a new watering can!"
GardenMiniGameWon = "Congratulations you've watered the plant!"
ShovelTin = 'Tin Shovel'
ShovelSteel = 'Bronze Shovel'
ShovelSilver = 'Silver Shovel'
ShovelGold = 'Gold Shovel'
WateringCanSmall = 'Small Watering Can'
WateringCanMedium = 'Medium Watering Can'
WateringCanLarge = 'Large Watering Can'
WateringCanHuge = 'Huge Watering Can'
BeanColorWords = ('red',
 'green',
 'orange',
 'violet',
 'blue',
 'pink',
 'yellow',
 'cyan',
 'silver')
PlantItWith = ' Plant with %s.'
MakeSureWatered = ' Make sure all your plants are watered first.'
UseFromSpecialsTab = ' Use from the specials tab of the garden page.'
UseSpecial = 'Use Special'
UseSpecialBadLocation = 'You can only use that in your garden.'
UseSpecialSuccess = 'Success! Your watered plants just grew.'
ConfirmWiltedFlower = '%(plant)s is wilted. Are you sure you want to remove it? It will not go into your flower basket, nor will you get an increase in skill.'
ConfirmUnbloomingFlower = '%(plant)s is not blooming. Are you sure you want to remove it? It will not go into your flower basket, nor will you get an increase in skill.'
ConfirmNoSkillupFlower = 'Are you sure you want to pick the %(plant)s? It will go into your flower basket, but you will NOT get an increase in skill.'
ConfirmSkillupFlower = 'Are you sure you want to pick the %(plant)s? It will go into your flower basket. You will also get an increase in skill.'
ConfirmMaxedSkillFlower = "Are you sure you want to pick the %(plant)s? It will go into your flower basket. You will NOT get an increase in skill since you've maximized it already."
ConfirmBasketFull = 'Your flower basket is full. Sell some flowers first.'
ConfirmRemoveTree = 'Are you sure you want to remove the %(tree)s?'
ConfirmWontBeAbleToHarvest = " If you remove this tree, you won't be able to harvest gags from the higher level trees."
ConfirmRemoveStatuary = 'Are you sure you want to permanently delete the %(item)s?'
ResultPlantedSomething = 'Congratulations! You just planted a %s.'
ResultPlantedSomethingAn = 'Congratulations! You just planted an %s.'
ResultPlantedNothing = "That didn't work. Please try a different combination of Jellybeans."
GardenGagTree = ' Gag Tree'
GardenUberGag = 'Uber Gag'

def getRecipeBeanText(beanTuple):
    retval = ''
    if not beanTuple:
        return retval
    allTheSame = True
    for index in range(len(beanTuple)):
        if index + 1 < len(beanTuple):
            if not beanTuple[index] == beanTuple[index + 1]:
                allTheSame = False
                break

    if allTheSame:
        if len(beanTuple) > 1:
            retval = '%d %s Jellybeans' % (len(beanTuple), BeanColorWords[beanTuple[0]])
        else:
            retval = 'a %s Jellybean' % BeanColorWords[beanTuple[0]]
    else:
        retval += 'a'
        maxBeans = len(beanTuple)
        for index in range(maxBeans):
            if index == maxBeans - 1:
                retval += ' and %s Jellybean' % BeanColorWords[beanTuple[index]]
            elif index == 0:
                retval += ' %s' % BeanColorWords[beanTuple[index]]
            else:
                retval += ', %s' % BeanColorWords[beanTuple[index]]

    return retval


GardenTextMagicBeans = 'Magic Beans'
GardenTextMagicBeansB = 'Some Other Beans'
GardenSpecialDiscription = 'This text should explain how to use a certain garden special'
GardenSpecialDiscriptionB = 'This text should explain how to use a certain garden special, in yo face foo!'
GardenTrophyAwarded = 'Wow! You collected %s of %s flowers. That deserves a trophy and a Laff boost!'
GardenTrophyNameDict = {0: 'Wheelbarrow',
 1: 'Shovels',
 2: 'Flower',
 3: 'Watering Can',
 4: 'Shark',
 5: 'Swordfish',
 6: 'Killer Whale'}
SkillTooLow = 'Skill\nToo Low'
NoGarden = 'No\nGarden'

def isVowelStart(str):
    retval = False
    if str and len(str) > 0:
        vowels = ['A',
         'E',
         'I',
         'O',
         'U']
        firstLetter = str.upper()[0:1]
        if firstLetter in vowels:
            retval = True
    return retval


def getResultPlantedSomethingSentence(flowerName):
    if isVowelStart(flowerName):
        retval = ResultPlantedSomethingAn % flowerName
    else:
        retval = ResultPlantedSomething % flowerName
    return retval


TravelGameTitle = 'Trolley Tracks'
TravelGameInstructions = 'Click up or down to set your number of votes. Click the vote button to cast it. Reach your secret goal to get bonus beans. Earn more votes by doing well in the other games.'
TravelGameRemainingVotes = 'Remaining Votes:'
TravelGameUse = 'Use'
TravelGameVotesWithPeriod = 'votes.'
TravelGameVotesToGo = 'votes to go'
TravelGameVoteToGo = 'vote to go'
TravelGameUp = 'UP.'
TravelGameDown = 'DOWN.'
TravelGameVoteWithExclamation = 'Vote!'
TravelGameWaitingChoices = 'Waiting for other players to vote…'
TravelGameDirections = ['UP', 'DOWN']
TravelGameTotals = 'Totals '
TravelGameReasonVotes = 'The trolley is moving %(dir)s, winning by %(numVotes)d votes.'
TravelGameReasonVotesPlural = 'The trolley is moving %(dir)s, winning by %(numVotes)d votes.'
TravelGameReasonVotesSingular = 'The trolley is moving %(dir)s, winning by %(numVotes)d vote.'
TravelGameReasonPlace = '%(name)s breaks the tie. The trolley is moving %(dir)s.'
TravelGameReasonRandom = 'The trolley is randomly moving %(dir)s.'
TravelGameOneToonVote = '%(name)s used %(numVotes)s votes to go %(dir)s\n'
TravelGameBonusBeans = '%(numBeans)d Beans'
TravelGamePlaying = 'Up next, the %(game)s trolley game.'
TravelGameGotBonus = '%(name)s got a bonus of %(numBeans)s Jellybeans!'
TravelGameNoOneGotBonus = 'No one reached their secret goal. Everyone gets 1 Jellybean.'
TravelGameConvertingVotesToBeans = 'Converting some votes to Jellybeans…'
TravelGameGoingBackToShop = "Only 1 player left. Going to Goofy's Gag Shop."
PairingGameTitle = 'Toon Memory Game'
PairingGameInstructions = 'Press Delete to open a card. Match 2 cards to score a point. Make a match with the bonus glow and earn an extra point. Earn more points by keeping the flips low.'
PairingGameInstructionsMulti = 'Press Delete to open a card. Press Control to signal another player to open a card. Match 2 cards to score a point. Make a match with the bonus glow and earn an extra point. Earn more points by keeping the flips low.'
PairingGamePerfect = 'PERFECT!!'
PairingGameFlips = 'Flips:'
PairingGamePoints = 'Points:'
TrolleyHolidayStart = 'Trolley Tracks is about to begin! Board any trolley with 2 or more Toons to play.'
TrolleyHolidayOngoing = 'Welcome! Trolley Tracks is currently in progress.'
TrolleyHolidayEnd = "That's all for today's Trolley Tracks. See you next week!"
TrolleyWeekendStart = 'Trolley Tracks Weekend is about to begin! Board any trolley with 2 or more Toons to play.'
TrolleyWeekendEnd = "That's all for Trolley Tracks Weekend."
VineGameTitle = 'Jungle Vines'
VineGameInstructions = 'Get to the rightmost vine in time. Press Up or Down to climb the vine. Press Left or Right to change facing and jump. The lower you are on the vine, the faster you jump off. Collect the bananas if you can, but avoid the bats and spiders.'
ValentinesDayStart = "Happy ValenToon's Day!"
ValentinesDayEnd = "That's all for ValenToon's Day!"
GolfCourseNames = {0: 'Walk In The Par',
 1: 'Hole Some Fun',
 2: 'The Hole Kit And Caboodle'}
GolfHoleNames = {0: 'Whole In Won',
 1: 'No Putts About It',
 2: 'Down The Hatch',
 3: 'Seeing Green',
 4: 'Hot Links',
 5: 'Peanut Putter',
 6: 'Swing-A-Long',
 7: 'Afternoon Tee',
 8: 'Hole In Fun',
 9: 'Rock And Roll In',
 10: 'Bogey Nights',
 11: 'Tea Off Time',
 12: 'Holey Mackerel!',
 13: 'One Little Birdie',
 14: 'At The Drive In',
 15: 'Swing Time',
 16: 'Hole On The Range',
 17: 'Second Wind',
 18: 'Whole In Won-2',
 19: 'No Putts About It-2',
 20: 'Down The Hatch-2',
 21: 'Seeing Green-2',
 22: 'Hot Links-2',
 23: 'Peanut Putter-2',
 24: 'Swing-A-Long-2',
 25: 'Afternoon Tee-2',
 26: 'Hole In Fun-2',
 27: 'Rock And Roll In-2',
 28: 'Bogey Nights-2',
 29: 'Tea Off Time-2',
 30: 'Holey Mackerel!-2',
 31: 'One Little Birdie-2',
 32: 'At The Drive In-2',
 33: 'Swing Time-2',
 34: 'Hole On The Range-2',
 35: 'Second Wind-2'}
GolfHoleInOne = 'Hole In One'
GolfCondor = 'Condor'
GolfAlbatross = 'Albatross'
GolfEagle = 'Eagle'
GolfBirdie = 'Birdie'
GolfPar = 'Par'
GolfBogey = 'Bogey'
GolfDoubleBogey = 'Double Bogey'
GolfTripleBogey = 'Triple Bogey'
GolfShotDesc = {-4: GolfCondor,
 -3: GolfAlbatross,
 -2: GolfEagle,
 -1: GolfBirdie,
 0: GolfPar,
 1: GolfBogey,
 2: GolfDoubleBogey,
 3: GolfTripleBogey}
from toontown.golf import GolfGlobals
CoursesCompleted = 'Courses Completed'
CoursesUnderPar = 'Courses Under Par'
HoleInOneShots = 'Hole In One Shots'
EagleOrBetterShots = 'Eagle Or Better Shots'
BirdieOrBetterShots = 'Birdie Or Better Shots'
ParOrBetterShots = 'Par Or Better Shots'
MultiPlayerCoursesCompleted = 'Multiplayer Courses Completed'
TwoPlayerWins = 'Two Player Wins'
ThreePlayerWins = 'Three Player Wins'
FourPlayerWins = 'Four Player Wins'
CourseZeroWins = GolfCourseNames[0] + ' Wins'
CourseOneWins = GolfCourseNames[1] + ' Wins'
CourseTwoWins = GolfCourseNames[2] + ' Wins'
GolfHistoryDescriptions = [CoursesCompleted,
 CoursesUnderPar,
 HoleInOneShots,
 EagleOrBetterShots,
 BirdieOrBetterShots,
 ParOrBetterShots,
 MultiPlayerCoursesCompleted,
 CourseZeroWins,
 CourseOneWins,
 CourseTwoWins]
GolfTrophyDescriptions = [str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesCompleted][0]) + ' ' + CoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesCompleted][1]) + ' ' + CoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesCompleted][2]) + ' ' + CoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesUnderPar][0]) + ' ' + CoursesUnderPar,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesUnderPar][1]) + ' ' + CoursesUnderPar,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesUnderPar][2]) + ' ' + CoursesUnderPar,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.HoleInOneShots][0]) + ' ' + HoleInOneShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.HoleInOneShots][1]) + ' ' + HoleInOneShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.HoleInOneShots][2]) + ' ' + HoleInOneShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.EagleOrBetterShots][0]) + ' ' + EagleOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.EagleOrBetterShots][1]) + ' ' + EagleOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.EagleOrBetterShots][2]) + ' ' + EagleOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.BirdieOrBetterShots][0]) + ' ' + BirdieOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.BirdieOrBetterShots][1]) + ' ' + BirdieOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.BirdieOrBetterShots][2]) + ' ' + BirdieOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.ParOrBetterShots][0]) + ' ' + ParOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.ParOrBetterShots][1]) + ' ' + ParOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.ParOrBetterShots][2]) + ' ' + ParOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.MultiPlayerCoursesCompleted][0]) + ' ' + MultiPlayerCoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.MultiPlayerCoursesCompleted][1]) + ' ' + MultiPlayerCoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.MultiPlayerCoursesCompleted][2]) + ' ' + MultiPlayerCoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseZeroWins][0]) + ' ' + CourseZeroWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseZeroWins][1]) + ' ' + CourseZeroWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseZeroWins][2]) + ' ' + CourseZeroWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseOneWins][0]) + ' ' + CourseOneWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseOneWins][1]) + ' ' + CourseOneWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseOneWins][2]) + ' ' + CourseOneWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseTwoWins][0]) + ' ' + CourseTwoWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseTwoWins][1]) + ' ' + CourseTwoWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseTwoWins][2]) + ' ' + CourseTwoWins]
GolfCupDescriptions = [str(GolfGlobals.TrophiesPerCup) + ' Trophies won', str(GolfGlobals.TrophiesPerCup * 2) + ' Trophies won', str(GolfGlobals.TrophiesPerCup * 3) + ' Trophies won']
GolfAvReceivesHoleBest = '%(name)s scored a new hole best at %(hole)s!'
GolfAvReceivesCourseBest = '%(name)s scored a new course best at %(course)s!'
GolfAvReceivesCup = '%(name)s receives the %(cup)s cup!! Laff point boost!'
GolfAvReceivesTrophy = '%(name)s receives the %(award)s trophy!!'
GolfRanking = 'Ranking: \n'
GolfPowerBarText = '%(power)s%%'
GolfChooseTeeInstructions = 'Press Left or Right to change tee spot.\nPress Control to select.'
GolfWarningMustSwing = 'Warning: You must press Control on your next swing.'
GolfAimInstructions = 'Press Left or Right to aim.\nPress and hold Control to swing.'
GolferExited = '%s has left the golf course.'
GolfPowerReminder = 'Hold Down Control Longer to\nHit the Ball Further'
GolfPar = 'Par'
GolfHole = 'Hole'
GolfTotal = 'Total'
GolfExitCourse = 'Exit Course'
GolfUnknownPlayer = '???'
GolfPageTitle = 'Golf'
GolfPageTitleCustomize = 'Golf Customizer'
GolfPageTitleRecords = 'Personal Best Records'
GolfPageTitleTrophy = 'Golfing Trophies'
GolfPageCustomizeTab = 'Customize'
GolfPageRecordsTab = 'Records'
GolfPageTrophyTab = 'Trophy'
GolfPageTickets = 'Tickets : '
GolfPageConfirmDelete = 'Delete Accessory?'
GolfTrophyTextDisplay = 'Trophy %(number)s : %(desc)s'
GolfCupTextDisplay = 'Cup %(number)s : %(desc)s'
GolfCurrentHistory = 'Current %(historyDesc)s : %(num)s'
GolfTieBreakWinner = '%(name)s wins the random tie breaker!'
GolfSeconds = ' -  %(time).2f seconds'
GolfTimeTieBreakWinner = '%(name)s wins the total aiming time tie breaker!!!'
RoamingTrialerWeekendStart = 'Tour Toontown is starting! Free players may now enter any neighborhood!'
RoamingTrialerWeekendOngoing = 'Welcome to Tour Toontown! Free players may now enter any neighborhood!'
RoamingTrialerWeekendEnd = "That's all for Tour Toontown."
MoreXpHolidayStart = 'Good news! Exclusive Test Toon double gag experience time has started.'
MoreXpHolidayOngoing = 'Welcome! Exclusive Test Toon double gag experience time is currently ongoing.'
MoreXpHolidayEnd = 'Exclusive Test Toon double gag experience time has ended. Thanks for helping us Test things!'
JellybeanDayHolidayStart = "It's Jellybean Day! Get Double Jellybean rewards at Parties!"
JellybeanDayHolidayEnd = "That's all for Jellybean Day. See you next year."
PartyRewardDoubledJellybean = 'Double Jellybeans!'
GrandPrixWeekendHolidayStart = "It's Grand Prix Weekend at Goofy Speedway! Free and paid players collect the most points in three consecutive races."
GrandPrixWeekendHolidayEnd = "That's all for Grand Prix Weekend. See you next year."
KartRace_DoubleTickets = 'Double Tickets'
SellbotNerfHolidayStart = 'Operation: Storm Sellbot is happening now! Battle the VP today!'
SellbotNerfHolidayEnd = 'Operation: Storm Sellbot has ended. Great work, Toons!'
JellybeanTrolleyHolidayStart = 'Double Bean Days for Trolley Games have begun!'
JellybeanTrolleyHolidayEnd = 'Double Bean Days for Trolley Games have ended!'
JellybeanFishingHolidayStart = 'Double Bean Days for Fishing have begun!'
JellybeanFishingHolidayEnd = 'Double Bean Days for Fishing have ended!'
JellybeanPartiesHolidayStart = "It's Jellybean Week! Get Double Jellybean rewards!"
JellybeanPartiesHolidayEnd = "That's all for Jellybean Week. See you next year."
JellybeanMonthHolidayStart = 'Celebrate Toontown with double beans, Cattlelog items and silly surprises!'
BankUpgradeHolidayStart = 'Something Toontastic happened to your Jellybean Bank!'
HalloweenPropsHolidayStart = "It's Halloween in Toontown!"
HalloweenPropsHolidayEnd = 'Halloween has ended. Boo!'
SpookyPropsHolidayStart = 'Silly Meter spins Toontown into spooky mode!'
BlackCatHolidayStart = 'Create a Black Cat - Today only!'
BlackCatHolidayEnd = 'Black Cat day has ended!'
SpookyBlackCatHolidayStart = 'Friday 13th means a Black Cat blast!'
TopToonsMarathonStart = "The Top Toons New Year's Day Marathon has begun!"
TopToonsMarathonEnd = "The Top Toons New Year's Day Marathon has ended."
WinterDecorationsStart = "It's Winter Holiday time in Toontown!"
WinterDecorationsEnd = 'Winter Holiday is over - Happy New Year!'
WackyWinterDecorationsStart = 'Brrr! Silly Meter goes from silly to chilly!'
WinterCarolingStart = 'Caroling has come to Toontown. Sing for your Snowman Head - see the Blog for details!'
ExpandedClosetsStart = 'Attention Toons: For a limited time, Members can purchase the new 50 item Closet from the Cattlelog for the low price of 50 Jellybeans!'
KartingTicketsHolidayStart = 'Get double tickets from Practice races at Goofy Speedway today!'
IdesOfMarchStart = 'Toons go GREEN!'
LogoutForced = 'You have done something wrong\n and are being logged out automatically,\n additionally your account may be frozen.\n Try going on a walk outside, it is fun.'
CountryClubToonEnterElevator = '%s \nhas jumped in the golf kart.'
CountryClubBossConfrontedMsg = '%s is battling the Club President!'
ElevatorBlockedRoom = 'All challenges must be defeated first.'
MolesLeft = 'Moles Left: %d'
MolesInstruction = 'Mole Stomp!\nJump on the red moles!'
MolesFinished = 'Mole Stomp successful!'
MolesPityWin = 'Stomp Failed! But the moles left.'
MolesRestarted = 'Stomp Failed! Restarting…'
BustACogInstruction = 'Remove the Cog ball!'
BustACogExit = 'Exit for Now'
BustACogHowto = 'How to Play'
BustACogFailure = 'Out of Time!'
BustACogSuccess = 'Success!'
GolfGreenGameScoreString = 'Puzzles Left: %s'
GolfGreenGamePlayerScore = 'Solved %s'
GolfGreenGameBonusGag = 'You won %s!'
GolfGreenGameGotHelp = '%s solved a Puzzle!'
GolfGreenGameDirections = 'Shoot balls using the the mouse\n\n\nMatching three of a color causes the balls to fall\n\n\nRemove all Cog balls from the board'
enterHedgeMaze = 'Race through the Hedge Maze\n for a laff bonus!'
toonFinishedHedgeMaze = '%s \n  finished in %s place!'
hedgeMazePlaces = ['first',
 'second',
 'third',
 'Fourth']
mazeLabel = 'Maze Race!'
BoardingPartyReadme = 'Boarding Group?'
BoardingGroupHide = 'Hide'
BoardingGroupShow = 'Show Boarding Group'
BoardingPartyInform = 'Create an elevator Boarding Group by clicking on another Toon and Inviting them.\nIn this area Boarding Groups cannot have more than %s Toons.'
BoardingPartyTitle = 'Boarding Group'
QuitBoardingPartyLeader = 'Disband'
QuitBoardingPartyNonLeader = 'Leave'
QuitBoardingPartyConfirm = 'Are you sure you want to quit this Boarding Group?'
BoardcodeMissing = 'Something went wrong; try again later.'
BoardcodeMinLaffLeader = 'Your group cannot board because you have less than %s laff points.'
BoardcodeMinLaffNonLeaderSingular = 'Your group cannot board because %s has less than %s laff points.'
BoardcodeMinLaffNonLeaderPlural = 'Your group cannot board because %s have less than %s laff points.'
BoardcodePromotionLeader = 'Your group cannot board because you do not have enough promotion merits.'
BoardcodePromotionNonLeaderSingular = 'Your group cannot board because %s does not have enough promotion merits.'
BoardcodePromotionNonLeaderPlural = 'Your group cannot board because %s do not have enough promotion merits.'
BoardcodeSpace = 'Your group cannot board because there is not enough space.'
BoardcodeBattleLeader = 'Your group cannot board because you are in battle.'
BoardcodeBattleNonLeaderSingular = 'Your group cannot board because %s is in battle.'
BoardcodeBattleNonLeaderPlural = 'Your group cannot board because %s are in battle.'
BoardingInviteMinLaffInviter = 'You need %s Laff Points before being a member of this Boarding Group.'
BoardingInviteMinLaffInvitee = '%s needs %s Laff Points before being a member of this Boarding Group.'
BoardingInvitePromotionInviter = 'You need to earn a promotion before being a member of this Boarding Group.'
BoardingInvitePromotionInvitee = '%s needs to earn a promotion before being a member of this Boarding Group.'
BoardingInviteNotPaidInvitee = '%s needs to be a paid Member to be a part of your Boarding Group.'
BoardingInviteeInDiffGroup = '%s is already in a different Boarding Group.'
BoardingInviteeInKickOutList = '%s had been removed by your leader. Only the leader can re-invite removed members.'
BoardingInviteePendingIvite = '%s has a pending invite; try again later.'
BoardingInviteeInElevator = '%s is currently busy; try again later.'
BoardingInviteGroupFull = 'Your Boarding Group is already full.'
BoardingAlreadyInGroup = 'You cannot accept this invitation because you are part of another Boarding Group.'
BoardingGroupAlreadyFull = 'You cannot accept this invitation because the group is already full.'
BoardingKickOutConfirm = 'Are you sure you want to remove %s?'
BoardingPendingInvite = 'You need to deal with the\n pending invitation first.'
BoardingCannotLeaveZone = 'You cannot leave this area because you are part of a Boarding Group.'
BoardingInviteeMessage = '%s would like you to join their Boarding Group.'
BoardingInvitingMessage = 'Inviting %s to your Boarding Group.'
BoardingInvitationRejected = '%s has rejected to join your Boarding Group.'
BoardingMessageKickedOut = 'You have been removed from the Boarding Group.'
BoardingMessageInvited = '%s has invited %s to the Boarding Group.'
BoardingMessageLeftGroup = '%s has left the Boarding Group.'
BoardingMessageGroupDissolved = 'Your Boarding Group was disbanded by the group leader.'
BoardingMessageGroupDisbandedGeneric = 'Your Boarding Group was disbanded.'
BoardingMessageInvitationFailed = '%s tried to invite you to their Boarding Group.'
BoardingMessageGroupFull = '%s tried to accept your invitation but your group was full.'
BoardingGo = 'GO'
BoardingCancelGo = 'Click Again to\nCancel Go'
And = 'and'
BoardingGoingTo = 'Going To:'
BoardingTimeWarning = 'Boarding the elevator in '
BoardingMore = 'more'
BoardingGoShow = 'Going to\n%s in '
BoardingGoPreShow = 'Confirming…'
BossbotBossName = 'C.E.O.'
BossbotRTWelcome = 'You Toons will need different disguises.'
BossbotRTRemoveSuit = 'First take off your Cog suits…'
BossbotRTFightWaiter = 'and then fight these waiters.'
BossbotRTWearWaiter = "Good Job! Now put on the waiters' clothes."
BossbotBossPreTwo1 = "What's taking so long? "
BossbotBossPreTwo2 = 'Get cracking and serve my banquet!'
BossbotRTServeFood1 = 'Hehe, serve the food I place on these conveyor belts.'
BossbotRTServeFood2 = 'If you serve a Cog three times in a row it will explode.'
BossbotResistanceToonName = "Good ol' Gil Giggles"
BossbotPhase3Speech1 = "What's happening here?!"
BossbotPhase3Speech2 = 'These waiters are Toons!'
BossbotPhase3Speech3 = 'Get them!!!'
BossbotPhase4Speech1 = 'Hrrmmpph. When I need a job done right…'
BossbotPhase4Speech2 = "I'll do it myself."
BossbotRTPhase4Speech1 = 'Good Job! Now squirt the C.E.O. with the water on the tables…'
BossbotRTPhase4Speech2 = 'or use golf balls to slow him down.'
BossbotPitcherLeave = 'Leave Bottle'
BossbotPitcherLeaving = 'Leaving Bottle'
BossbotPitcherAdvice = 'Use the left and right keys to rotate.\nHold down Ctrl increase power.\nRelease Ctrl to fire.'
BossbotGolfSpotLeave = 'Leave Golf Ball'
BossbotGolfSpotLeaving = 'Leaving Golf Ball'
BossbotGolfSpotAdvice = 'Use the left and right keys to rotate.\nCtrl to fire.'
BossbotRewardSpeech1 = "No! The Chairman won't like this."
BossbotRewardSpeech2 = 'Arrrggghhh!!!!'
BossbotRTCongratulations = "You did it! You've demoted the C.E.O.!\x07Here, take these pink slips the C.E.O. left behind.\x07With it you'll be able to fire Cogs in a battle."
BossbotRTLastPromotion = "\x07Wow, you've reached level %s on your Cog Suit!\x07Cogs don't get promoted higher than that.\x07You can't upgrade your Cog Suit anymore, but you can certainly keep working for the Resistance!"
BossbotRTHPBoost = "\x07You've done a lot of work for the Resistance.\x07The Toon Council has decided to give you another Laff point. Congratulations!"
BossbotRTMaxed = '\x07I see that you have a level %s Cog Suit. Very impressive!\x07On behalf of the Toon Council, thank you for coming back to defend more Toons!'
GolfAreaAttackTaunt = 'Fore!'
OvertimeAttackTaunts = ["It's time to reorganize.", "Now let's downsize."]
ElevatorBossBotBoss = 'C.E.O Battle'
ElevatorBossBotCourse0 = 'The Front Three'
ElevatorBossBotCourse1 = 'The Middle Six'
ElevatorBossBotCourse2 = 'The Back Nine'
ElevatorCashBotBoss = 'C.F.O Battle'
ElevatorCashBotMint0 = 'Coin Mint'
ElevatorCashBotMint1 = 'Dollar Mint'
ElevatorCashBotMint2 = 'Bullion Mint'
ElevatorSellBotBoss = 'Senior V.P Battle'
ElevatorSellBotFactory0 = 'Front Entrance'
ElevatorSellBotFactory1 = 'Side Entrance'
ElevatorSellBotFactory2 = 'Fatal Entrance'
ElevatorLawBotBoss = 'Chief Justice Battle'
ElevatorLawBotCourse0 = 'Office A'
ElevatorLawBotCourse1 = 'Office B'
ElevatorLawBotCourse2 = 'Office C'
ElevatorLawBotCourse3 = 'Office D'
DaysToGo = 'Wait\n%s Days'
IceGameTitle = 'Ice Slide'
IceGameInstructions = 'Get as close to the center by the end of the second round. Use arrow keys to change direction and force. Press Ctrl to launch your Toon. Hit barrels for extra points and avoid the TNT!'
IceGameInstructionsNoTnt = 'Get as close to the center by the end of the second round. Use arrow keys to change direction and force. Press Ctrl to launch your Toon. Hit barrels for extra points.'
IceGameWaitingForPlayersToFinishMove = 'Waiting for other players…'
IceGameWaitingForAISync = 'Waiting for other players…'
IceGameInfo = 'Match %(curMatch)d/%(numMatch)d, Round %(curRound)d/%(numRound)d'
IceGameControlKeyWarning = 'Remember to press the Ctrl key!'
PicnicTableJoinButton = 'Join'
PicnicTableObserveButton = 'Observe'
PicnicTableCancelButton = 'Cancel'
PicnicTableTutorial = 'How To Play'
PicnicTableMenuTutorial = 'What game do you want to learn?'
PicnicTableMenuSelect = 'What game do you want to play?'
ChineseCheckersGetUpButton = 'Get Up'
ChineseCheckersStartButton = 'Start Game'
ChineseCheckersQuitButton = 'Quit Game'
ChineseCheckersIts = "It's "
ChineseCheckersYourTurn = 'Your Turn'
ChineseCheckersGreenTurn = "Green's Turn"
ChineseCheckersYellowTurn = "Yellow's Turn"
ChineseCheckersPurpleTurn = "Purple's Turn"
ChineseCheckersBlueTurn = "Blue's Turn"
ChineseCheckersPinkTurn = "Pink's Turn"
ChineseCheckersRedTurn = "Red's Turn"
ChineseCheckersColorG = 'You are Green'
ChineseCheckersColorY = 'You are Yellow'
ChineseCheckersColorP = 'You are Purple'
ChineseCheckersColorB = 'You are Blue'
ChineseCheckersColorPink = 'You are Pink'
ChineseCheckersColorR = 'You are Red'
ChineseCheckersColorO = 'You are Observing'
ChineseCheckersYouWon = 'You just won a game of Chinese Checkers!'
ChineseCheckers = 'Chinese Checkers.'
ChineseCheckersGameOf = ' has just won a game of '
ChineseTutorialTitle1 = 'Objective'
ChineseTutorialTitle2 = 'How to Play'
ChineseTutorialPrev = 'Previous Page'
ChineseTutorialNext = 'Next Page'
ChineseTutorialDone = 'Done'
ChinesePage1 = 'The goal of Chinese Checkers is to be the first  player to move all of your marbles from the bottom triangle across the board and into the triangle at the top. The first player to do so wins!'
ChinesePage2 = 'Players take turns moving any marble of their own color. A marble can move into an adjacent hole or it can hop over other marbles. Hops must go over a marble and end in an empty hole. It is possible to chain hops together for longer moves!'
CheckersPage1 = 'The goal of Checkers is to leave the opponent without any possible moves. To do this you can either capture all of his peices or block them in such that he has no available moves.'
CheckersPage2 = 'Players take turns moving any peice of their own color. A peice can move one square diagonal and forward. A peice can only move into a square that is not occupied by another peice. Kings follow the same rules but are allowed to move backwards.'
CheckersPage3 = 'To capture an opponents peice your peice must jump over it diagonally into the vacant square beyond it. If you have any jump moves during a turn, you must do one of them. You can chain jump moves together as long as it is with the same peice.'
CheckersPage4 = 'A peice becomes a king when it reaches the last row on the board. A peice that has just become a king cannot continue jumping until the next turn. Additionally, kings are allowed to move all directions and are allowed to change directions while jumping.'
CheckersGetUpButton = 'Get Up'
CheckersStartButton = 'Start Game'
CheckersQuitButton = 'Quit Game'
CheckersIts = "It's "
CheckersYourTurn = 'Your Turn'
CheckersWhiteTurn = "White's Turn"
CheckersBlackTurn = "Black's Turn"
CheckersColorWhite = 'You are White'
CheckersColorBlack = 'You are Black'
CheckersObserver = 'You are Observing'
RegularCheckers = 'Checkers.'
RegularCheckersGameOf = ' has just won a game of '
RegularCheckersYouWon = 'You just won a game of Checkers!'
MailNotifyNewItems = "You've got mail!"
MailNewMailButton = 'Mail'
MailSimpleMail = 'Note'
MailFromTag = 'Note From: %s'
AwardNotifyNewItems = 'You have a new award in your mailbox!'
AwardNotifyOldItems = 'There are still awards waiting in your mailbox for you to pick up!'
InviteInvitation = 'the invitation'
InviteAcceptInvalidError = 'The invitation is no longer valid.'
InviteAcceptPartyInvalid = 'That party has been cancelled.'
InviteAcceptAllOk = 'The host has been informed of your reply.'
InviteRejectAllOk = 'The host has been informed that you declined the invitation.'
Months = {1: 'JANUARY',
 2: 'FEBRUARY',
 3: 'MARCH',
 4: 'APRIL',
 5: 'MAY',
 6: 'JUNE',
 7: 'JULY',
 8: 'AUGUST',
 9: 'SEPTEMBER',
 10: 'OCTOBER',
 11: 'NOVEMBER',
 12: 'DECEMBER'}
DayNames = ('Monday',
 'Tuesday',
 'Wednesday',
 'Thursday',
 'Friday',
 'Saturday',
 'Sunday')
DayNamesAbbrev = ('MON',
 'TUE',
 'WED',
 'THU',
 'FRI',
 'SAT',
 'SUN')
HolidayNamesInCalendar = {1: ('Summer Fireworks', 'Celebrate Summer with a fireworks show every hour in each playground!'),
 2: ('New Year Fireworks', 'Happy New Year! Enjoy a fireworks show every hour in each playground!'),
 3: ('Bloodsucker Invasion', 'Help defend Toontown from the Bloodsucker invasion!'),
 4: ('Winter Holiday', 'Celebrate the Winter Holiday with Toontastic decorations, party and Cattlelog items, and more!'),
 5: ('Skelecog Invasion', 'Stop the Skelecogs from invading Toontown!'),
 6: ('Mr. Hollywood Invasion', 'Stop the Mr. Hollywood Cogs from invading Toontown!'),
 7: ('Fish Bingo', 'Fish Bingo Wednesday! Everyone at the pond works together to complete the card before time runs out.'),
 8: ('Toon Species Election', 'Vote on the new Toon species! Will it be Goat? Will it be Pig?'),
 9: ('Black Cat Day', 'Happy Halloween! Create a Toontastic Black Cat Toon - Today Only!'),
 13: ('Trick or Treat', 'Happy Halloween! Trick or treat throughout Toontown to get a nifty Halloween pumpkin head reward!'),
 14: ('Grand Prix', 'Grand Prix Monday at Goofy Speedway! To win, collect the most points in three consecutive races!'),
 16: ('Grand Prix Weekend', 'Free and Paid players compete in circuit races at Goofy Speedway!'),
 17: ('Trolley Tracks', 'Trolley Tracks Thursday! Board any Trolley with two or more Toons to play.'),
 19: ('Silly Saturdays', 'Saturdays are silly with Fish Bingo and Grand Prix throughout the day!'),
 24: ('Ides of March', 'Beware the Ides of March! Stop the Backstabber Cogs from invading Toontown!'),
 26: ('Halloween Decor', 'Celebrate Halloween as spooky trees and streetlights transform Toontown!'),
 28: ('Winter Invasion', 'The sellbots are on the loose spreading their cold sales tactics!'),
 29: ("April Toons' Week", "Celebrate April Toons' Week - a holiday built by Toons for Toons!"),
 33: ('Sellbot Surprise 1', 'Sellbot Surprise! Stop the Cold Caller Cogs from invading Toontown!'),
 34: ('Sellbot Surprise 2', 'Sellbot Surprise! Stop the Name Dropper Cogs from invading Toontown!'),
 35: ('Sellbot Surprise 3', 'Sellbot Surprise! Stop the Gladhander Cogs from invading Toontown!'),
 36: ('Sellbot Surprise 4', 'Sellbot Surprise! Stop the Mover & Shaker Cogs from invading Toontown!'),
 37: ('A Cashbot Conundrum 1', 'A Cashbot Conundrum. Stop the Short Change Cogs from invading Toontown!'),
 38: ('A Cashbot Conundrum 2', 'A Cashbot Conundrum. Stop the Penny Pincher Cogs from invading Toontown!'),
 39: ('A Cashbot Conundrum 3', 'A Cashbot Conundrum. Stop the Bean Counter Cogs from invading Toontown!'),
 40: ('A Cashbot Conundrum 4', 'A Cashbot Conundrum. Stop the Number Cruncher Cogs from invading Toontown!'),
 41: ('The Lawbot Gambit 1', 'The Lawbot Gambit. Stop the Bottomfeeder Cogs from invading Toontown!'),
 42: ('The Lawbot Gambit 2', 'The Lawbot Gambit. Stop the Double Talker Cogs from invading Toontown!'),
 43: ('The Lawbot Gambit 3', 'The Lawbot Gambit. Stop the Ambulance Chaser Cogs from invading Toontown!'),
 44: ('The Lawbot Gambit 4', 'The Lawbot Gambit. Stop the Backstabber Cogs from invading Toontown!'),
 45: ('The Trouble With Bossbots 1', 'The Trouble with Bossbots. Stop the Flunky Cogs from invading Toontown!'),
 46: ('The Trouble With Bossbots 2', 'The Trouble with Bossbots. Stop the Pencil Pusher Cogs from invading Toontown!'),
 47: ('The Trouble With Bossbots 3', 'The Trouble with Bossbots. Stop the Micromanager Cogs from invading Toontown!'),
 48: ('The Trouble With Bossbots 4', 'The Trouble with Bossbots. Stop the Downsizer Cogs from invading Toontown!'),
 49: ('Jellybean Day', 'Celebrate Jellybean Day with double Jellybean rewards at parties!'),
 53: ('Cold Caller Invasion', 'Stop the Cold Caller Cogs from invading Toontown!'),
 54: ('Bean Counter Invasion', 'Stop the Bean Counter Cogs from invading Toontown!'),
 55: ('Double Talker Invasion', 'Stop the Double Talker Cogs from invading Toontown!'),
 56: ('Downsizer Invasion', 'Stop the Downsizer Cogs from invading Toontown!'),
 57: ('Caroling', 'Sing for your Snowman Head! See the Blog for details!'),
 59: ("ValenToon's Day", "Celebrate ValenToon's Day from Feb 09 to Feb 16!"),
 72: ('Yes Men Invasion', 'Stop the Yes Men Cogs from invading Toontown!'),
 73: ('Tightwad Invasion', 'Stop the Tightwad Cogs from invading Toontown!'),
 74: ('Telemarketers Invasion', 'Stop the Telemarketer Cogs from invading Toontown!'),
 75: ('Head Hunter Invasion', 'Stop the Head Hunter Cogs from invading Toontown!'),
 76: ('Spin Doctor Invasion', 'Stop the Spin Doctor Cogs from invading Toontown!'),
 77: ('Moneybags Invasion', 'Stop the Moneybags from invading Toontown!'),
 78: ('Two-faces Invasion', 'Stop the Two-faces from invading Toontown!'),
 79: ('Mingler Invasion', 'Stop the Mingler Cogs from invading Toontown!'),
 80: ('Loan Shark Invasion', 'Stop the Loanshark Cogs from invading Toontown!'),
 81: ('Corporate Raider Invasion', 'Stop the Corporate Raider Cogs from invading Toontown!'),
 82: ('Robber Baron Invasion', 'Stop the Robber Baron Cogs from invading Toontown!'),
 83: ('Legal Eagle Invasion', 'Stop the Legal Eagle Cogs from invading Toontown!'),
 84: ('Big Wig Invasion', 'Stop the Big Wig Cogs from invading Toontown!'),
 85: ('Big Cheese Invasion', 'Stop the Big Cheese from invading Toontown!'),
 86: ('Down Sizer Invasion', 'Stop the Down Sizer Cogs from invading Toontown!'),
 87: ('Mover And Shaker Invasion', 'Stop the Mover and Shaker Cogs from invading Toontown!'),
 88: ('Double Talker Invasion', 'Stop the Double Talkers Cogs from invading Toontown!'),
 89: ('Penny Pincher Invasion', 'Stop the Penny Pinchers Cogs from invading Toontown!'),
 90: ('Name Dropper Invasion', 'Stop the Name Dropper Cogs from invading Toontown!'),
 91: ('Ambulance Chaser Invasion', 'Stop the Ambulance Chaser Cogs from invading Toontown!'),
 92: ('Micro Manager Invasion', 'Stop the Micro Manager Cogs from invading Toontown!'),
 93: ('Number Cruncher Invasion', 'Stop the Number Cruncher Cogs from invading Toontown!'),
 95: ('Victory Parties', 'Celebrate our historic triumph against the Cogs!'),
 96: ('Operation: Storm Sellbot', "Sellbot HQ is open to everyone. Let's go fight the VP!"),
 97: ('Double Bean Days - Trolley Games', ''),
 98: ('Double Bean Days - Fishing', ''),
 99: ('Jellybean Week', 'Celebrate Jellybean Week with double Jellybean rewards!'),
 101: ("Top Toons New Year's Day Marathon", "Chances to win every hour! See the What's New Blog for details!"),
 105: ('Toons go GREEN!', 'Toons make a green scene at Green Bean Jeans on Raven Road in Withering Woods!')}
UnknownHoliday = 'Unknown Holiday %d'
HolidayFormat = '%b %d '
TimeZone = 'US/Pacific'
CogdoMemoGuiTitle = 'Memos:'
CogdoMemoNames = 'Barrel-Destruction Memos'
CogdoStomperName = 'Stomp-O-Matic'
CogdoBarrelRoomTitle = 'Stomper Room'
CogdoBarrelIntroMovieDialogue = 'Good work! You\'ve halted the %s and are now able to collect some of the stolen Laff Barrels, but make sure to hurry before the Cogs come!' % CogdoStomperName
BoardroomGameTitle = 'Boardroom Hijinks'
BoardroomGameInstructions = 'The Cogs are having a meeting to decide what to do with stolen gags. Slide on through and grab as many gag-destruction memos as you can!'
CogdoCraneGameTitle = 'Vend-A-Stomper'
CogdoCraneGameInstructions = 'The Cogs are using a coin-operated machine to destroy laff barrels. Use the cranes to pick up and throw money bags, in order to prevent barrel destruction!'
CogdoMazeGameTitle = 'Mover & Shaker\nField Office'
CogdoMazeGameInstructions = 'The big Mover & Shaker Cogs have the code to open the door. Defeat them with your water balloons in order to get it!'
CogdoMazeIntroMovieDialogue = (("This is the Toon Resistance! The Movers & Shakers\nhave our Jokes, and they've locked the exit!",), ('Grab water balloons at coolers, and throw them at Cogs!\nSmall Cogs drop Jokes, BIG Cogs open the exit.',), ('The more Jokes you rescue, the bigger your Toon-Up\nat the end. Good luck!',))
CogdoMazeGameDoorOpens = 'THE EXIT IS OPEN FOR 60 SECONDS!\nGET THERE FAST FOR A BIGGER Toon-UP'
CogdoMazeGameLocalToonFoundExit = "The exit will open when\nyou've busted all four BIG Cogs!"
CogdoMazeGameWaitingForToons = 'Waiting for other Toons…'
CogdoMazeGameTimeOut = 'Oh no, time ran out! You lost your jokes.'
CogdoMazeGameTimeAlert = 'Hurry up! 60 seconds to go!'
CogdoMazeGameBossGuiTitle = 'BIG Cogs:'
CogdoMazeFindHint = 'Find a Water Cooler'
CogdoMazeThrowHint = "Press 'Ctrl' to throw your water balloon"
CogdoMazeSquashHint = 'Falling objects pop your balloon'
CogdoMazeBossHint = 'Big Cogs take TWO hits to defeat'
CogdoMazeMinionHint = 'Smaller Cogs drop jokes'
CogdoFlyingGameTitle = 'Legal Eagle Offices'
CogdoFlyingGameInstructions = "Fly through the Legal Eagles' lair. Watch out for obstacles and Cogs along the way, and don't forget to refuel your helicopter!"
CogdoFlyingIntroMovieDialogue = (("You won't ruffle our feathers, Toons! We're destroying barrels of your Laff, and you cannot stop us!", "A flock of Toons! We're crushing barrels of your Laff in our %s, and there's nothing you can do about it!" % CogdoStomperName, "You can't egg us on, Toons! We're powering our offices with your Laff, and you're powerless to stop us!"), ('This is the Toon Resistance! A little bird told me you can use propellers to fly around, grab Barrel Destruction Memos, and keep Laff from being destroyed! Good luck, Toons!', 'Attention Toons! Wing it with a propeller and collect Barrel Destruction Memos to keep our Laff from being stomped! Toon Resistance out!', 'Toon Resistance here! Cause a flap by finding propellers, flying to the Barrel Destruction Memos, and keeping our Laff from being smashed! Have fun!'), ("Squawk! I'm a Silver Sprocket Award winner, I don't need this!", 'Do your best, Toons! You will find us to be quite talon-ted!', "We'll teach you to obey the pecking order, Toons!"))
CogdoFlyingGameWaiting = 'Waiting for other Toons%s'
CogdoFlyingGameFuelLabel = 'Fuel'
CogdoFlyingGameLegalEagleTargeting = 'A Legal Eagle has noticed you!'
CogdoFlyingGameLegalEagleAttacking = 'Incoming Eagle!'
CogdoFlyingGamePickUpAPropeller = 'You need a propeller to fly!'
CogdoFlyingGamePressShiftToFly = "Press 'Shift' to fly up!"
CogdoFlyingGameYouAreInvincible = 'Red Tape protects you!'
CogdoFlyingGameTimeIsRunningOut = 'Time is running out!'
CogdoFlyingGameMinimapIntro = 'This meter shows your progress!\nX marks the finish line.'
CogdoFlyingGameMemoIntro = 'Memos prevent Laff Barrels in\nthe Stomper Room from being destroyed!'
CogdoFlyingGameOutOfTime = 'Oh No! You ran out of time!'
CogdoFlyingGameYouMadeIt = 'You made it on time!'
CogdoFlyingGameYouMadeIt = 'Good work, you made it on time!'
CogdoFlyingGameTakingMemos = 'The legal eagles took all your memos!'
CogdoElevatorRewardLaff = 'Great job, Toons!\nYou get a Toon-Up from the jokes you saved!'
CogdoExecutiveSuiteTitle = 'Executive Suite'
CogdoExecutiveSuiteIntroMessage = "Oh no, they've got the shop keeper!\nDefeat the Cogs and free the captive."
CogdoExecutiveSuiteToonThankYou = 'Thanks for the rescue!\nIf you need help in a fight, use these S.O.S. cards to call my friend %s.'
CogdoExecutiveSuiteToonThankYouLawbot = 'Thanks for the rescue!\nThe Lawbots have left behind some sprocket awards that you can use to buy new things in your cattlelog!'
CogdoExecutiveSuiteToonThankYouSummon = 'Thanks for the rescue!\nThe Lawbots have left behind some summons that you can use to summon a %s!'
CogdoExecutiveSuiteToonBye = 'Bye!'
SillySurgeTerms = {1: 'Amusing Ascent!',
 2: 'Silly Surge!',
 3: 'Ridiculous Rise!',
 4: 'Giggle Growth!',
 5: 'Funny Fueling!',
 6: 'Batty Boost!',
 7: 'Crazy Climb!',
 8: 'Jolly Jump!',
 9: 'Loony Lift!',
 10: 'Hilarity Hike!',
 11: 'Insanity Increase!',
 12: 'Cracked-Uptick!'}
InteractivePropTrackBonusTerms = {0: 'Super Toon-Up!',
 1: '',
 2: '',
 3: '',
 4: 'Super Throw!',
 5: 'Super Squirt!',
 6: ''}
PlayingCardUnknown = 'Card Name is unknown'

TeleportGUITitle = 'Teleport'
TeleportGUITeleport = 'Go!'

InventoryRoundsString = 'Rounds'

BattleGlobalCogLuredText = 'Lured %s Rounds'
BossCogDoStunned = 'Stunned!'

OptionsPageFpsEnabledLabel = 'FPS meter is on.'
OptionsPageFpsDisabledLabel = 'FPS meter is off.'

GagShopNotEnoughJellybeans = 'You do not have enough Jellybeans for that gag'

AvatarPanelCogHealth = 'HP: %s/%s'

InventoryMaxed = 'Maxed'

IntroPresents = 'Introducing the toontastic world of...'
IntroDisclaimer = 'The Toon Island Crew Presents...'
IntroPowered = "Powered By:"
IntroExitButton = 'Exit'
IntroYesButton = 'Yes'
IntroNoButton = 'No'
ClickToStartLabel = '\x01shadow\x01Click to begin your journey!\x02'
CreatedBy = "By Nayla and the Toon Island Crew"