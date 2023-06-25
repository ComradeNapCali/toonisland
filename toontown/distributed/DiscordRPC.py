#from ctypes import * # Used to interact with DLL
from direct.task import Task # Used to manage the Callback timer
from dependencies.pypresence import Presence
import time

client_id = '571705676858916874'
try:
    RPC = Presence(client_id)
    RPC.connect()
except:
    pass

class DiscordRPC:

    zone2imgdesc = { # A dict of ZoneID -> An image and a description
        1000: ["barnacle-boatyard", "In Rainbow Reef"],
        1100: ["barnacle-boatyard", "On Coral Court"],
        1200: ["barnacle-boatyard", "On Ocean Overpass"],
        1300: ["barnacle-boatyard", "On Plankton Path"],
        
        2000: ["toontown-central", "In Toon Island Central"],
        2100: ["toontown-central", "On Beach Ball Boulevard"],
        2200: ["toontown-central", "On Aloha Avenue"],
        2300: ["toontown-central", "On Pineapple Place"],
        2400: ["toontown-central", "On Seashell Street"],
        
        3000: ["winter-wonderland", "In Cirrus Circus"],
        3100: ["winter-wonderland", "On Balloon Boulevard"],
        3200: ["winter-wonderland", "On Horizon Hill"],
        3300: ["winter-wonderland", "On Stratus Strait"],
        
        4000: ["musical-melodyland", "In Olive Oasis"],
        4100: ["musical-melodyland", "On Desert Drive"],
        4200: ["musical-melodyland", "On Sandy Station"],
        4300: ["musical-melodyland", "On Palm Tree Place"],
        
        5000: ["daffodil-gardens", "In Withering Woods"],
        5100: ["daffodil-gardens", "On Willow Way"],
        5200: ["daffodil-gardens", "On Crow Circle"],
        5300: ["daffodil-gardens", "On Raven Road"],
        
        6000: ["acorn-acres", "At Acorn Acres"],
        
        8000: ["toontown-speedway", "In Toontown Speedway"],

        9000: ["drowzy-dreamland", "In Minty Mines"],
        9100: ["drowzy-dreamland", "On Candy Close"],
        9200: ["drowzy-dreamland", "On Peppermint Place"],
        
        10000: ["bossbot-hq", "In Bossbot HQ"],
        10100: ["bossbot-hq", "In The CEO Lobby"],
        10500: ["bossbot-hq", "In The Front Three"],
        10600: ["bossbot-hq", "In The Middle Six"],
        10700: ["bossbot-hq", "In The Back Nine"],

        11000: ["sellbot-hq","At Sellbot HQ"],
        11100: ["sellbot-hq", "In The VP Lobby"],
        11200: ["sellbot-hq", "In The Sellbot Factory"],
        11500: ["sellbot-hq", "In The Sellbot Factory"],
        11600: ["sellbot-hq", "In The Sellbot Fatal Factory"],
        
        12000: ["cashbot-hq", "At Cashbot HQ"],
        12100: ["cashbot-hq", "In The CFO Lobby"],
        12500: ["cashbot-hq", "In The Cashbot Coin Mint"],
        12600: ["cashbot-hq", "In The Cashbot Dollar Mint"],
        12700: ["cashbot-hq", "In The Cashbot Bullion Mint"],

        13000: ["lawbot-hq", "At Lawbot HQ"],
        13100: ["lawbot-hq","In The CJ Lobby"],
        13200: ["lawbot-hq","In The DA Office Lobby"],
        13300: ["lawbot-hq", "In The Lawbot Office A"],
        13400: ["lawbot-hq", "In The Lawbot Office B"],
        13500: ["lawbot-hq", "In The Lawbot Office C"],
        13600: ["lawbot-hq", "In The Lawbot Office D"],

        14000: ["tutorial", "In The Toontorial"],

        16000: ["estate", "At A Toon Estate"],

        17000: ["minigames", "In The Minigames Area"],

        18000: ["party", "At A Toon Party"]
   }
    
    def __init__(self):
        RPC.update()

    def stopBoarding(self):  #Boarding groups :D
        RPC.update(state="")

    def AllowBoarding(self, size):
        RPC.update(state="In A Boarding Group", party_size=[1-size])

    def setBoarding(self, size): # Sets how many members are in a boarding group
        RPC.update(party_size=size)

    def AvChoice(self): # Call in pick-a-toon
        RPC.update(state="Picking A Toon", large_image="logo")

    def Launching(self): # Call When loading game - toontownstart
        RPC.update(large_image="logo", state="Launching Game")

    def Making(self): # Call in make-a-toon
        RPC.update(large_image="logo", state="Making A Toon")

    def setZone(self,Zone): # Set image and text based on the zone
        if not isinstance(Zone, int):
            return
        Zone -= Zone % 100
        data = self.zone2imgdesc.get(Zone,None)
        if data:
            RPC.update(large_image=data[0], state=data[1], small_image="globe", small_text=currentDistrict, details=toonName)
        else:
            print("Error: Zone Not Found!")

    def setDistrict(self, district): # Set the image text the district name
        global currentDistrict 
        currentDistrict = district
    
    def setAv(self, name):
        global toonName
        toonName = name

    def AFK(self): # if toon falls asleep
        RPC.update(large_image="logo", state="Making A Toon")