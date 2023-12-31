from toontown.toonbase import ToontownGlobals
OFF = 0
MOVING = 1
StepTime = 5.0
MinimumHunger = 1.0
NUM_TARGETS_INDEX = 0
POS_START_INDEX = 1
POS_END_INDEX = 4
RADIUS_INDEX = 4
WATER_LEVEL_INDEX = 5
__targetInfoDict = {ToontownGlobals.ToonIslandCentral: (2,
                                   -81,
                                   31,
                                   -4.8,
                                   14,
                                   -1.4),
 ToontownGlobals.BeachballBoulevard: (2,
                               20,
                               -664,
                               -1.4,
                               14,
                               -1.4 - 0.438),
 ToontownGlobals.AlohaAvenue: (2,
                             -234,
                             175,
                             -1.4,
                             14,
                             -1.4 - 0.462),
 ToontownGlobals.PineapplePlace: (2,
                                  529,
                                  -70,
                                  -1.4,
                                  13,
                                  -1.4 - 0.486),
 ToontownGlobals.SeashellStreet: (3,
                                  -154,
                                  239,
                                  -1.4,
                                  13,
                                  -1.4 - 0.486),
 ToontownGlobals.RainbowRise: (2,
                               -17,
                               130,
                               1.73,
                               15,
                               1.73 - 3.615),
 ToontownGlobals.CoralCourt: (2,
                                     381,
                                     -350,
                                     -2,
                                     14,
                                     -2 - 0.482),
 ToontownGlobals.OceanOverpass: (2,
                                 -395,
                                 -226,
                                 -2,
                                 14,
                                 -2 - 0.482),
 ToontownGlobals.PlanktonPath: (2,
                                  350,
                                  100,
                                  -2,
                                  14,
                                  -2 - 0.482),
 ToontownGlobals.WitheringWoods: (2,
                                50,
                                47,
                                -1.48,
                                13,
                                -1.48 - 0.345),
 ToontownGlobals.WillowWay: (2,
                             149,
                             44,
                             -1.43,
                             13,
                             -1.43 - 0.618),
 ToontownGlobals.CrowCircle: (2,
                               176,
                               100,
                               -1.43,
                               13,
                               -1.43 - 0.618),
 ToontownGlobals.RavenRoad: (2,
                             134,
                             -70.5,
                             -1.5,
                             13,
                             -1.5 - 0.377),
 ToontownGlobals.OliveOasis: (2,
                                     -0.2,
                                     -20.2,
                                     -14.65,
                                     14,
                                     -14.65 - -12),
 ToontownGlobals.DesertDrive: (2,
                              -580,
                              -90,
                              -0.87,
                              14,
                              -0.87 - 1.844),
 ToontownGlobals.TumbleweedTerrace: (2,
                                     -214,
                                     250,
                                     -0.87,
                                     14,
                                     -0.87 - 1.844),
 ToontownGlobals.CactusCourt: (2,
                                715,
                                -15,
                                -0.87,
                                14,
                                -0.87 - 1.844),
 ToontownGlobals.CirrusCircus: (2,
                             -58,
                             -26,
                             1.7,
                             10,
                             -0.8),
 ToontownGlobals.DoodleDrive: (2,
                             460,
                             29,
                             -2,
                             13,
                             -2 - 0.4),
 ToontownGlobals.SleetStreet: (2,
                               340,
                               480,
                               -2,
                               13,
                               -2 - 0.4),
 ToontownGlobals.PolarPlace: (2,
                              45.5,
                              90.86,
                              -2,
                              13,
                              -2 - 0.4),
 ToontownGlobals.MintyMines: (2,
                                    159,
                                    0.2,
                                    -17.1,
                                    14,
                                    -17.1 - -14.6),
 ToontownGlobals.RoackyRoad: (2,
                               118,
                               -185,
                               -2.1,
                               14,
                               -2.1 - 0.378),
 ToontownGlobals.PeppermintPlace: (2,
                               241,
                               -348,
                               -2.1,
                               14,
                               -2.1 - 0.378),
 ToontownGlobals.MyEstate: (3,
                            30,
                            -126,
                            -0.3,
                            16,
                            -0.83)}

def getNumTargets(zone):
    info = __targetInfoDict.get(zone)
    if info:
        return info[NUM_TARGETS_INDEX]
    else:
        return 2


def getTargetCenter(zone):
    info = __targetInfoDict.get(zone)
    if info:
        return info[POS_START_INDEX:POS_END_INDEX]
    else:
        return (0, 0, 0)


def getTargetRadius(zone):
    info = __targetInfoDict.get(zone)
    if info:
        return info[RADIUS_INDEX]
    else:
        return 10


def getWaterLevel(zone):
    info = __targetInfoDict.get(zone)
    if info:
        return info[WATER_LEVEL_INDEX]
    else:
        return 0
