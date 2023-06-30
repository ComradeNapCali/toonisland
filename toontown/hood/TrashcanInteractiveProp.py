from direct.actor import Actor
from direct.directnotify import DirectNotifyGlobal
from toontown.hood import InteractiveAnimatedProp
from toontown.hood import GenericAnimatedProp
from toontown.toonbase import ToontownGlobals, ToontownBattleGlobals, TTLocalizer


class TrashcanInteractiveProp(InteractiveAnimatedProp.InteractiveAnimatedProp):
    notify = DirectNotifyGlobal.directNotify.newCategory("TrashcanInteractiveProp")
    BattleCheerText = TTLocalizer.InteractivePropTrackBonusTerms[
        ToontownBattleGlobals.HEAL_TRACK
    ]
    ZoneToIdles = {
        ToontownGlobals.ToonIslandCentral: (
            ("tt_a_ara_ttc_trashcan_idleTake2", 1, 1, None, 3, 10),
            ("tt_a_ara_ttc_trashcan_idleHiccup0", 1, 1, None, 3, 10),
            ("tt_a_ara_ttc_trashcan_idleLook1", 1, 1, None, 3, 10),
            ("tt_a_ara_ttc_trashcan_idleAwesome3", 1, 1, None, 3, 10),
        ),
        ToontownGlobals.RainbowRise: (
            (
                "tt_a_ara_dod_trashcan_idleBounce2",
                3,
                10,
                "tt_a_ara_dod_trashcan_idle0settle",
                3,
                10,
            ),
            ("tt_a_ara_dod_trashcan_idle0", 1, 1, None, 3, 10),
            ("tt_a_ara_dod_trashcan_idle1", 1, 1, None, 3, 10),
            ("tt_a_ara_dod_trashcan_idleAwesome3", 1, 1, None, 3, 10),
        ),
        ToontownGlobals.WitheringWoods: (
            ("tt_a_ara_dga_trashcan_idleTake2", 1, 1, None, 3, 10),
            ("tt_a_ara_dga_trashcan_idleHiccup0", 1, 1, None, 3, 10),
            ("tt_a_ara_dga_trashcan_idleLook1", 1, 1, None, 3, 10),
            ("tt_a_ara_dga_trashcan_idleAwesome3", 1, 1, None, 3, 10),
        ),
        ToontownGlobals.OliveOasis: (
            (
                "tt_a_ara_mml_trashcan_idleBounce0",
                3,
                10,
                "tt_a_ara_mml_trashcan_idle0settle",
                3,
                10,
            ),
            ("tt_a_ara_mml_trashcan_idleLook1", 1, 1, None, 3, 10),
            ("tt_a_ara_mml_trashcan_idleHelicopter2", 1, 1, None, 3, 10),
            ("tt_a_ara_mml_trashcan_idleAwesome3", 1, 1, None, 3, 10),
        ),
        ToontownGlobals.CirrusCircus: (
            ("tt_a_ara_tbr_trashcan_idleShiver1", 1, 1, None, 3, 10),
            ("tt_a_ara_tbr_trashcan_idleSneeze2", 1, 1, None, 3, 10),
            ("tt_a_ara_tbr_trashcan_idle0", 1, 1, None, 3, 10),
            ("tt_a_ara_tbr_trashcan_idleAwesome3", 1, 1, None, 3, 10),
        ),
        ToontownGlobals.MintyMines: (
            ("tt_a_ara_ddl_trashcan_idleSleep0", 3, 10, None, 0, 0),
            ("tt_a_ara_ddl_trashcan_idleShake2", 1, 1, None, 0, 0),
            ("tt_a_ara_ddl_trashcan_idleSnore1", 1, 1, None, 0, 0),
            ("tt_a_ara_ddl_trashcan_idleAwesome3", 1, 1, None, 0, 0),
        ),
    }
    ZoneToIdleIntoFightAnims = {
        ToontownGlobals.ToonIslandCentral: "tt_a_ara_ttc_trashcan_idleIntoFight",
        ToontownGlobals.RainbowRise: "tt_a_ara_dod_trashcan_idleIntoFight",
        ToontownGlobals.WitheringWoods: "tt_a_ara_dga_trashcan_idleIntoFight",
        ToontownGlobals.OliveOasis: "tt_a_ara_mml_trashcan_idleIntoFight",
        ToontownGlobals.CirrusCircus: "tt_a_ara_tbr_trashcan_idleIntoFight",
        ToontownGlobals.MintyMines: "tt_a_ara_ddl_trashcan_idleIntoFight",
    }
    ZoneToVictoryAnims = {
        ToontownGlobals.ToonIslandCentral: "tt_a_ara_ttc_trashcan_victoryDance",
        ToontownGlobals.RainbowRise: "tt_a_ara_dod_trashcan_victoryDance",
        ToontownGlobals.WitheringWoods: "tt_a_ara_dga_trashcan_victoryDance",
        ToontownGlobals.OliveOasis: "tt_a_ara_mml_trashcan_victoryDance",
        ToontownGlobals.CirrusCircus: "tt_a_ara_tbr_trashcan_victoryDance",
        ToontownGlobals.MintyMines: "tt_a_ara_ddl_trashcan_victoryDance",
    }
    ZoneToSadAnims = {
        ToontownGlobals.ToonIslandCentral: "tt_a_ara_ttc_trashcan_fightSad",
        ToontownGlobals.RainbowRise: "tt_a_ara_dod_trashcan_fightSad",
        ToontownGlobals.WitheringWoods: "tt_a_ara_dga_trashcan_fightSad",
        ToontownGlobals.OliveOasis: "tt_a_ara_mml_trashcan_fightSad",
        ToontownGlobals.CirrusCircus: "tt_a_ara_tbr_trashcan_fightSad",
        ToontownGlobals.MintyMines: "tt_a_ara_ddl_trashcan_fightSad",
    }
    ZoneToFightAnims = {
        ToontownGlobals.ToonIslandCentral: (
            "tt_a_ara_ttc_trashcan_fightBoost",
            "tt_a_ara_ttc_trashcan_fightCheer",
            "tt_a_ara_ttc_trashcan_fightIdle",
        ),
        ToontownGlobals.RainbowRise: (
            "tt_a_ara_dod_trashcan_fightBoost",
            "tt_a_ara_dod_trashcan_fightCheer",
            "tt_a_ara_dod_trashcan_fightIdle",
        ),
        ToontownGlobals.WitheringWoods: (
            "tt_a_ara_dga_trashcan_fightBoost",
            "tt_a_ara_dga_trashcan_fightCheer",
            "tt_a_ara_dga_trashcan_fightIdle",
        ),
        ToontownGlobals.OliveOasis: (
            "tt_a_ara_mml_trashcan_fightBoost",
            "tt_a_ara_mml_trashcan_fightCheer0",
            "tt_a_ara_mml_trashcan_fightCheer1",
            "tt_a_ara_mml_trashcan_fightIdle",
        ),
        ToontownGlobals.CirrusCircus: (
            "tt_a_ara_tbr_trashcan_fightBoost",
            "tt_a_ara_tbr_trashcan_fightCheer",
            "tt_a_ara_tbr_trashcan_fightIdle",
        ),
        ToontownGlobals.MintyMines: (
            "tt_a_ara_ddl_trashcan_fightBoost",
            "tt_a_ara_ddl_trashcan_fightCheer",
            "tt_a_ara_ddl_trashcan_fightIdle",
        ),
    }
    IdlePauseTime = base.config.GetFloat("prop-idle-pause-time", 0.0)

    def __init__(self, node):
        InteractiveAnimatedProp.InteractiveAnimatedProp.__init__(
            self, node, ToontownGlobals.TRASHCANS_BUFF_BATTLES
        )
