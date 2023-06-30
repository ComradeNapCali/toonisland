from toontown.coghq.SpecImports import *

GlobalEntities = {
    1000: {
        "type": "levelMgr",
        "name": "LevelMgr",
        "comment": "",
        "parentEntId": 0,
        "cogLevel": 0,
        "farPlaneDistance": 1500,
        "modelFilename": "phase_10/models/cashbotHQ/ZONE04a",
        "wantDoors": 1,
    },
    1001: {
        "type": "editMgr",
        "name": "EditMgr",
        "parentEntId": 0,
        "insertEntity": None,
        "removeEntity": None,
        "requestNewEntity": None,
        "requestSave": None,
    },
    0: {
        "type": "zone",
        "name": "UberZone",
        "comment": "",
        "parentEntId": 0,
        "scale": 1,
        "description": "",
        "visibility": [],
    },
    10001: {
        "type": "battleBlocker",
        "name": "exitBlocker",
        "comment": "",
        "parentEntId": 0,
        "pos": Point3(0.0, 76.2264404297, 0.0),
        "hpr": Vec3(0.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "cellId": 0,
        "radius": 10.0,
    },
    10021: {
        "type": "battleBlocker",
        "name": "middleBlocker",
        "comment": "",
        "parentEntId": 0,
        "pos": Point3(9.79564476013, 7.17855405807, 0.0),
        "hpr": Vec3(90.0, 0.0, 0.0),
        "scale": Vec3(1.61347305775, 0.225867271423, 1.99822974205),
        "cellId": 1,
        "radius": 10.0,
    },
    10061: {
        "type": "battleBlocker",
        "name": "frontBlocker",
        "comment": "",
        "parentEntId": 0,
        "pos": Point3(-45.6075019836, -22.7538051605, 0.0),
        "hpr": Vec3(45.0, 0.0, 0.0),
        "scale": Vec3(1.61347305775, 0.225867271423, 1.99822974205),
        "cellId": 2,
        "radius": 10.0,
    },
    10025: {
        "type": "mintProductPallet",
        "name": "<unnamed>",
        "comment": "",
        "parentEntId": 10024,
        "pos": Point3(0.0, 7.96000003815, 0.0),
        "hpr": Vec3(0.0, 0.0, 0.0),
        "scale": 1,
        "mintId": 12500,
    },
    10031: {
        "type": "mintProductPallet",
        "name": "<unnamed>",
        "comment": "",
        "parentEntId": 10024,
        "pos": Point3(-32.7900009155, -5.48999977112, 0.0),
        "hpr": Vec3(0.0, 0.0, 0.0),
        "scale": 1,
        "mintId": 12500,
    },
    10032: {
        "type": "mintProductPallet",
        "name": "<unnamed>",
        "comment": "",
        "parentEntId": 10028,
        "pos": Point3(-25.0, 9.05000019073, 0.0),
        "hpr": Vec3(0.0, 0.0, 0.0),
        "scale": 1,
        "mintId": 12500,
    },
    10033: {
        "type": "mintProductPallet",
        "name": "<unnamed>",
        "comment": "",
        "parentEntId": 10028,
        "pos": Point3(26.8400001526, 0.0, 0.0),
        "hpr": Vec3(0.0, 0.0, 0.0),
        "scale": 1,
        "mintId": 12500,
    },
    10003: {
        "type": "mintShelf",
        "name": "bookshelf",
        "comment": "",
        "parentEntId": 10002,
        "pos": Point3(-60.8400001526, 0.0, 0.0),
        "hpr": Vec3(0.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10004: {
        "type": "mintShelf",
        "name": "copy of bookshelf",
        "comment": "",
        "parentEntId": 10003,
        "pos": Point3(0.180000007153, 6.85808324814, 0.0),
        "hpr": Point3(180.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10005: {
        "type": "mintShelf",
        "name": "bookshelf",
        "comment": "",
        "parentEntId": 10002,
        "pos": Point3(-47.4124145508, 0.0, 0.0),
        "hpr": Vec3(0.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10006: {
        "type": "mintShelf",
        "name": "copy of bookshelf",
        "comment": "",
        "parentEntId": 10005,
        "pos": Point3(0.180000007153, 6.85808324814, 0.0),
        "hpr": Point3(180.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10007: {
        "type": "mintShelf",
        "name": "bookshelf",
        "comment": "",
        "parentEntId": 10002,
        "pos": Point3(-33.9436340332, 0.0, 0.0),
        "hpr": Vec3(0.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10008: {
        "type": "mintShelf",
        "name": "copy of bookshelf",
        "comment": "",
        "parentEntId": 10007,
        "pos": Point3(0.180000007153, 6.85808324814, 0.0),
        "hpr": Point3(180.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10009: {
        "type": "mintShelf",
        "name": "bookshelf",
        "comment": "",
        "parentEntId": 10002,
        "pos": Point3(-20.4898967743, 0.0, 0.0),
        "hpr": Vec3(0.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10010: {
        "type": "mintShelf",
        "name": "copy of bookshelf",
        "comment": "",
        "parentEntId": 10009,
        "pos": Point3(0.180000007153, 6.85808324814, 0.0),
        "hpr": Point3(180.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10011: {
        "type": "mintShelf",
        "name": "bookshelf",
        "comment": "",
        "parentEntId": 10002,
        "pos": Point3(60.7196426392, 0.0, 0.0),
        "hpr": Vec3(0.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10012: {
        "type": "mintShelf",
        "name": "copy of bookshelf",
        "comment": "",
        "parentEntId": 10011,
        "pos": Point3(0.180000007153, 6.85808324814, 0.0),
        "hpr": Point3(180.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10013: {
        "type": "mintShelf",
        "name": "bookshelf",
        "comment": "",
        "parentEntId": 10002,
        "pos": Point3(33.2060928345, 0.0, 0.0),
        "hpr": Vec3(0.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10014: {
        "type": "mintShelf",
        "name": "copy of bookshelf",
        "comment": "",
        "parentEntId": 10013,
        "pos": Point3(0.180000007153, 6.85808324814, 0.0),
        "hpr": Point3(180.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10015: {
        "type": "mintShelf",
        "name": "bookshelf",
        "comment": "",
        "parentEntId": 10002,
        "pos": Point3(19.7813663483, 0.0, 0.0),
        "hpr": Vec3(0.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10016: {
        "type": "mintShelf",
        "name": "copy of bookshelf",
        "comment": "",
        "parentEntId": 10015,
        "pos": Point3(0.180000007153, 6.85808324814, 0.0),
        "hpr": Point3(180.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10017: {
        "type": "mintShelf",
        "name": "bookshelf",
        "comment": "",
        "parentEntId": 10002,
        "pos": Point3(-7.05515527725, 0.0, 0.0),
        "hpr": Vec3(0.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10018: {
        "type": "mintShelf",
        "name": "copy of bookshelf",
        "comment": "",
        "parentEntId": 10017,
        "pos": Point3(0.180000007153, 6.85808324814, 0.0),
        "hpr": Point3(180.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10019: {
        "type": "mintShelf",
        "name": "bookshelf",
        "comment": "",
        "parentEntId": 10002,
        "pos": Point3(6.35370635986, 0.0, 0.0),
        "hpr": Vec3(0.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10020: {
        "type": "mintShelf",
        "name": "copy of bookshelf",
        "comment": "",
        "parentEntId": 10019,
        "pos": Point3(0.180000007153, 6.85808324814, 0.0),
        "hpr": Point3(180.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10042: {
        "type": "mintShelf",
        "name": "bookshelf",
        "comment": "",
        "parentEntId": 10041,
        "pos": Point3(-7.05515527725, 0.0, 0.0),
        "hpr": Vec3(0.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10043: {
        "type": "mintShelf",
        "name": "bookshelf",
        "comment": "",
        "parentEntId": 10041,
        "pos": Point3(-60.8400001526, 0.0, 0.0),
        "hpr": Vec3(0.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10044: {
        "type": "mintShelf",
        "name": "bookshelf",
        "comment": "",
        "parentEntId": 10041,
        "pos": Point3(6.35370635986, 0.0, 0.0),
        "hpr": Vec3(0.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10045: {
        "type": "mintShelf",
        "name": "bookshelf",
        "comment": "",
        "parentEntId": 10041,
        "pos": Point3(-47.4124145508, 0.0, 0.0),
        "hpr": Vec3(0.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10046: {
        "type": "mintShelf",
        "name": "bookshelf",
        "comment": "",
        "parentEntId": 10041,
        "pos": Point3(-33.9436340332, 0.0, 0.0),
        "hpr": Vec3(0.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10047: {
        "type": "mintShelf",
        "name": "bookshelf",
        "comment": "",
        "parentEntId": 10041,
        "pos": Point3(-20.4898967743, 0.0, 0.0),
        "hpr": Vec3(0.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10048: {
        "type": "mintShelf",
        "name": "bookshelf",
        "comment": "",
        "parentEntId": 10041,
        "pos": Point3(60.7196426392, 0.0, 0.0),
        "hpr": Vec3(0.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10049: {
        "type": "mintShelf",
        "name": "bookshelf",
        "comment": "",
        "parentEntId": 10041,
        "pos": Point3(33.2060928345, 0.0, 0.0),
        "hpr": Vec3(0.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10050: {
        "type": "mintShelf",
        "name": "bookshelf",
        "comment": "",
        "parentEntId": 10041,
        "pos": Point3(19.7813663483, 0.0, 0.0),
        "hpr": Vec3(0.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10051: {
        "type": "mintShelf",
        "name": "copy of bookshelf",
        "comment": "",
        "parentEntId": 10042,
        "pos": Point3(0.180000007153, 6.85808324814, 0.0),
        "hpr": Point3(180.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10052: {
        "type": "mintShelf",
        "name": "copy of bookshelf",
        "comment": "",
        "parentEntId": 10043,
        "pos": Point3(0.180000007153, 6.85808324814, 0.0),
        "hpr": Point3(180.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10053: {
        "type": "mintShelf",
        "name": "copy of bookshelf",
        "comment": "",
        "parentEntId": 10044,
        "pos": Point3(0.180000007153, 6.85808324814, 0.0),
        "hpr": Point3(180.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10054: {
        "type": "mintShelf",
        "name": "copy of bookshelf",
        "comment": "",
        "parentEntId": 10045,
        "pos": Point3(0.180000007153, 6.85808324814, 0.0),
        "hpr": Point3(180.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10055: {
        "type": "mintShelf",
        "name": "copy of bookshelf",
        "comment": "",
        "parentEntId": 10046,
        "pos": Point3(0.180000007153, 6.85808324814, 0.0),
        "hpr": Point3(180.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10056: {
        "type": "mintShelf",
        "name": "copy of bookshelf",
        "comment": "",
        "parentEntId": 10047,
        "pos": Point3(0.180000007153, 6.85808324814, 0.0),
        "hpr": Point3(180.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10057: {
        "type": "mintShelf",
        "name": "copy of bookshelf",
        "comment": "",
        "parentEntId": 10048,
        "pos": Point3(0.180000007153, 6.85808324814, 0.0),
        "hpr": Point3(180.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10058: {
        "type": "mintShelf",
        "name": "copy of bookshelf",
        "comment": "",
        "parentEntId": 10049,
        "pos": Point3(0.180000007153, 6.85808324814, 0.0),
        "hpr": Point3(180.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10059: {
        "type": "mintShelf",
        "name": "copy of bookshelf",
        "comment": "",
        "parentEntId": 10050,
        "pos": Point3(0.180000007153, 6.85808324814, 0.0),
        "hpr": Point3(180.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
        "mintId": 12500,
    },
    10000: {
        "type": "nodepath",
        "name": "cogs",
        "comment": "",
        "parentEntId": 0,
        "pos": Point3(0.0, 58.7970542908, 0.0),
        "hpr": Point3(0.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
    },
    10002: {
        "type": "nodepath",
        "name": "backWall",
        "comment": "",
        "parentEntId": 0,
        "pos": Point3(0.0, 22.0885009766, 0.0),
        "hpr": Vec3(0.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
    },
    10022: {
        "type": "nodepath",
        "name": "middleCogs",
        "comment": "",
        "parentEntId": 0,
        "pos": Point3(0.0, 7.5760216713, 0.0),
        "hpr": Vec3(270.0, 0.0, 0.0),
        "scale": Point3(1.0, 1.0, 1.0),
    },
    10023: {
        "type": "nodepath",
        "name": "props",
        "comment": "",
        "parentEntId": 0,
        "pos": Point3(0.0, 0.0, 0.0),
        "hpr": Vec3(0.0, 0.0, 0.0),
        "scale": 1,
    },
    10024: {
        "type": "nodepath",
        "name": "frontMoney",
        "comment": "",
        "parentEntId": 10023,
        "pos": Point3(22.4126205444, -39.3388214111, 0.0),
        "hpr": Vec3(0.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
    },
    10028: {
        "type": "nodepath",
        "name": "backMoney",
        "comment": "",
        "parentEntId": 10023,
        "pos": Point3(0.0, 48.498249054, 0.0),
        "hpr": Vec3(0.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
    },
    10041: {
        "type": "nodepath",
        "name": "backWall",
        "comment": "",
        "parentEntId": 0,
        "pos": Point3(0.0, -6.69597911835, 0.0),
        "hpr": Vec3(180.0, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
    },
    10060: {
        "type": "nodepath",
        "name": "frontCogs",
        "comment": "",
        "parentEntId": 0,
        "pos": Point3(-28.8658733368, -31.173248291, 0.0),
        "hpr": Vec3(51.3401908875, 0.0, 0.0),
        "scale": Vec3(1.0, 1.0, 1.0),
    },
}
Scenario0 = {}
levelSpec = {"globalEntities": GlobalEntities, "scenarios": [Scenario0]}
