from ast import Try
from dataclasses import field
from pynput import keyboard
from pynput.keyboard import Key, Controller
#from functions import *
from threading import *
import sys, time, pywinauto, win32gui, os, tkinter, datetime
from tkinter import *
from tkinter import scrolledtext

numMags = 1
secIDListA = ['Greenill', 'Bluefull', 'Pinkal', 'Oran', 'Whitill']
secIDListB = ['Viridia', 'Skyly', 'Purplenum', 'Redria', 'Yellowboze']
secIDListAll = ['Viridia', 'Greenill', 'Skyly', 'Bluefull', 'Purplenum', 'Pinkal', 'Redria', 'Oran', 'Yellowboze', 'Whitill']
characterList = ['HUmar', 'HUnewearl', 'HUcast', 'HUcaseal', 'RAmar', 'RAmarl', 'RAcast', 'RAcaseal', 'FOmar', 'FOmarl', 'FOnewm', 'FOnewearl']
thirdEvoMagList = ['Andhaka', 'Apsaras', 'Bana', 'Bhirava', 'Durga', 'Garuda', 'Ila', 'Kabanda', 'Kaitabha', 'Kama', 'Kumara', 'Madhu', 'Marica', 'Naga', 'Nandin', 'Naraka', 'Ravana', 'Ribhava', 'Sita', 'Soma', 'Ushasu', 'Varaha', 'Yaksa']

magFeedingTables = {"Mag": 0,
    "Kalki": 1, "Varuna": 1, "Vritra": 1,
    "Ashvinau": 2, "Namuci": 2, "Marutah":2, "Rudra": 2, "Sumba": 2,
    "Mitra": 3, "Tapas": 3, "Surya": 3,
    "Vayu": 4, "Apsaras": 4, "Bhirava": 4, "Kaitabha": 4, "Kama": 4, "Kumara": 4, "Ushasu": 4, "Varaha": 4,
    "Durga": 5, "Garuda": 5, "Ila": 5, "Nandin": 5, "Ribhava": 5, "Sita": 5, "Soma": 5, "Yaksa": 5, "Deva": 5, "Rukmin": 5, "Sato": 5,
    "Andhaka": 6, "Bana": 6, "Kabanda": 6, "Madhu": 6, "Marica": 6, "Naga": 6, "Naraka": 6, "Ravana":6, "Bhima": 6, "Pushan": 6, "Rati": 6,
    "Cell Mag": 7, "Diwari": 7, "Nidra": 7, "Savitri": 7}
itemTbl0 = {'Monomate': [0.05, 0.4, 0.05, 0.0, 50],
     'Dimate': [0.1, 0.45, 0.05, 0.0, 300],
     'Trimate': [0.15, 0.5, 0.1, 0.0, 2000],
     'Monofluid': [0.05, 0.0, 0.05, 0.4, 100],
     'Difluid': [0.1, 0.0, 0.05, 0.45, 500],
     'Trifluid': [0.15, 0.0, 0.1, 0.5, 3600],
     'Antidote': [0.05, 0.1, 0.4, 0.0, 60],
     'Antiparalysis': [0.05, 0.0, 0.44, 0.1, 60],
     'Sol Atomizer': [0.15, 0.3, 0.15, 0.25, 300],
     'Moon Atomizer': [0.15, 0.25, 0.15, 0.3, 500],
     'Star Atomizer': [0.25, 0.25, 0.25, 0.25, 5000]}
itemTbl1 = {'Monomate': [0.05, 0.1, 0.0, -0.01, 50],
     'Dimate': [0.06, 0.15, 0.03, -0.03, 300],
     'Trimate': [0.12, 0.21, 0.04, -0.07, 2000],
     'Monofluid': [0.05, 0.0, 0.0, 0.08, 100],
     'Difluid': [0.07, 0.0, 0.03, 0.13, 500],
     'Trifluid': [0.07, -0.07, 0.06, 0.19, 3600],
     'Antidote': [0.0, 0.05, 0.15, 0.0, 60],
     'Antiparalysis': [-0.01, 0.0, 0.14, 0.05, 60],
     'Sol Atomizer': [0.1, 0.11, 0.08, 0.0, 300],
     'Moon Atomizer': [0.09, 0.0, 0.09, 0.11, 500],
     'Star Atomizer': [0.14, 0.09, 0.18, 0.11, 5000]}
itemTbl2 = {'Monomate': [0.01, 0.09, 0.0, -0.05, 50],
     'Dimate': [0.01, 0.13, 0.0, -0.1, 300],
     'Trimate': [0.08, 0.16, 0.02, -0.15, 2000],
     'Monofluid': [0.0, -0.05, 0.0, 0.09, 100],
     'Difluid': [0.04, -0.1, 0.0, 0.13, 500],
     'Trifluid': [0.06, -0.15, 0.05, 0.17, 3600],
     'Antidote': [-0.05, 0.04, 0.12, -0.05, 60],
     'Antiparalysis': [-0.05, -0.06, 0.11, 0.04, 60],
     'Sol Atomizer': [0.0, 0.11, 0.03, -0.05, 300],
     'Moon Atomizer': [0.04, -0.05, 0.0, 0.11, 500],
     'Star Atomizer': [0.07, 0.08, 0.06, 0.09, 5000]}
itemTbl3 = {'Monomate': [0.0, 0.03, 0.0, 0.0, 50],
     'Dimate': [0.05, 0.07, 0.0, -0.05, 300],
     'Trimate': [0.04, 0.14, 0.06, -0.1, 2000],
     'Monofluid': [0.0, 0.0, 0.0, 0.04, 100],
     'Difluid': [0.04, -0.05, 0.0, 0.08, 500],
     'Trifluid': [0.04, -0.1, 0.03, 0.15, 3600],
     'Antidote': [0.0, 0.0, 0.07, 0.0, 60],
     'Antiparalysis': [-0.04, -0.05, 0.2, -0.05, 60],
     'Sol Atomizer': [-0.1, 0.09, 0.06, 0.09, 300],
     'Moon Atomizer': [0.08, 0.05, -0.08, 0.07, 500],
     'Star Atomizer': [0.07, 0.07, 0.07, 0.07, 5000]}
itemTbl4 = {'Monomate': [-0.05, 0.09, -0.05, 0.0, 50],
     'Dimate': [0.0, 0.11, 0.0, -0.1, 300],
     'Trimate': [0.04, 0.14, 0.0, -0.15, 2000],
     'Monofluid': [-0.05, 0.0, -0.06, 0.1, 100],
     'Difluid': [0.0, -0.1, 0.0, 0.11, 500],
     'Trifluid': [0.04, -0.15, 0.0, 0.15, 3600],
     'Antidote': [-0.05, -0.05, 0.16, -0.05, 60],
     'Antiparalysis': [0.07, -0.03, 0.0, -0.03, 60],
     'Sol Atomizer': [0.05, 0.21, -0.05, -0.2, 300],
     'Moon Atomizer': [-0.05, -0.2, 0.05, 0.21, 500],
     'Star Atomizer': [0.04, 0.06, 0.08, 0.05, 5000]}
itemTbl5 = {'Monomate': [-0.04, 0.13, -0.05, -0.05, 50],
     'Dimate': [0.0, 0.16, 0.0, -0.15, 300],
     'Trimate': [0.03, 0.19, -0.02, -0.18, 2000],
     'Monofluid': [-0.04, -0.05, -0.05, 0.13, 100],
     'Difluid': [0.0, -0.15, 0.0, 0.16, 500],
     'Trifluid': [0.03, -0.2, 0.0, 0.19, 3600],
     'Antidote': [0.05, -0.06, 0.06, -0.05, 60],
     'Antiparalysis': [0.0, -0.04, 0.14, -0.1, 60],
     'Sol Atomizer': [0.04, 0.17, -0.05, -0.15, 300],
     'Moon Atomizer': [-0.1, -0.15, 0.05, 0.21, 500],
     'Star Atomizer': [0.02, 0.08, 0.03, 0.06, 5000]}
itemTbl6 = {'Monomate': [-0.03, 0.09, -0.03, -0.04, 50],
     'Dimate': [0.0, 0.11, 0.0, -0.1, 300],
     'Trimate': [0.02, 0.15, 0.0, -0.16, 2000],
     'Monofluid': [-0.03, -0.04, -0.03, 0.09, 100],
     'Difluid': [0.0, -0.1, 0.0, 0.11, 500],
     'Trifluid': [-0.02, -0.15, 0.0, 0.19, 3600],
     'Antidote': [0.0, 0.06, 0.09, -0.15, 60],
     'Antiparalysis': [0.0, -0.15, 0.09, 0.06, 60],
     'Sol Atomizer': [0.09, -0.2, -0.05, 0.17, 300],
     'Moon Atomizer': [-0.05, 0.2, 0.05, -0.2, 500],
     'Star Atomizer': [0.0, 0.11, 0.0, 0.11, 5000]}
itemTbl7 = {'Monomate': [-0.04, 0.21, -0.15, -0.05, 50],
     'Dimate': [-0.01, 0.27, -0.1, -0.16, 300],
     'Trimate': [0.05, 0.29, -0.07, -0.25, 2000],
     'Monofluid': [-0.1, -0.05, -0.1, 0.21, 100],
     'Difluid': [-0.05, -0.16, -0.05, 0.25, 500],
     'Trifluid': [-0.07, -0.25, 0.06, 0.29, 3600],
     'Antidote': [-0.1, -0.1, 0.28, -0.1, 60],
     'Antiparalysis': [0.09, -0.18, 0.25, -0.15, 60],
     'Sol Atomizer': [0.19, 0.18, -0.15, -0.2, 300],
     'Moon Atomizer': [-0.15, -0.2, 0.19, 0.18, 500],
     'Star Atomizer': [0.03, 0.07, 0.03, 0.03, 5000]}
itemTblList = [itemTbl0, itemTbl1, itemTbl2, itemTbl3, itemTbl4, itemTbl5, itemTbl6, itemTbl7]

# This function can get temp path for your resource file
# relative_path is your icon file name
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Mag: #includes init, setName, and feed
    def __init__(self, name, defense, power, dex, mind, targetLevel, item):
        self.name = name
        self.stats = [float(defense), float(power), float(dex), float(mind)]
        self.targetLevel = int(targetLevel)
        self.item = item
    def setName(self): #checks for evolutions
        global gender, secid, magFeedingTables, charProfession, secIDListA, secIDListB
        if self.level == 10: #first evos
            if charProfession == 'Hunter':
                self.name = 'Varuna'
            if charProfession == 'Ranger':
                self.name = 'Kalki'
            if charProfession == 'Force':
                self.name = 'Vritra'
        if self.level == 35: #second evos
            if self.name == 'Varuna':
                if all(self.power > n for n in [self.defense, self.dex, self.mind]):
                    self.name = 'Rudra'
                if all(self.dex > n for n in [self.defense, self.power, self.mind]):
                    self.name = 'Marutah'
                if all(self.mind > n for n in [self.defense, self.power, self.dex]):
                    self.name = 'Vayu'
            if self.name == 'Kalki':
                if all(self.power > n for n in [self.defense, self.dex, self.mind]):
                    self.name = 'Surya'
                if all(self.dex > n for n in [self.defense, self.power, self.mind]):
                    self.name = 'Mitra'
                if all(self.mind > n for n in [self.defense, self.dex, self.power]):
                    self.name = 'Tapas'
            if self.name == 'Vritra':
                if all(self.power > n for n in [self.defense, self.dex, self.mind]):
                    self.name = 'Sumba'
                if all(self.dex > n for n in [self.defense, self.power, self.mind]):
                    self.name = 'Ashvinau'
                if all(self.mind > n for n in [self.defense, self.power, self.dex]):
                    self.name = 'Namuci'
        if self.level in range(50, 96, 5): #third evos
            if charProfession == 'Hunter':
                if secid in secIDListA:
                    if self.power >= self.mind > self.dex:
                        self.name = 'Apsaras'
                    if self.mind > self.power >= self.dex:
                        self.name = 'Bana'
                    if self.dex > self.power > self.mind:
                        self.name = 'Garuda'
                    if (self.power >= self.dex >= self.mind) or (self.dex == self.mind and self.mind > self.power):
                        self.name = 'Kama'
                    if self.mind > self.dex > self.power:
                        self.name = 'Soma'
                    if self.dex > self.mind >= self.power:
                        self.name = 'Yaksa'
                if secid in secIDListB:
                    if self.power >= self.mind > self.dex:
                        self.name = 'Bhirava'
                    if self.dex > self.power > self.mind:
                        self.name = 'Ila'
                    if self.mind > self.power >= self.dex:
                        self.name = 'Kabanda'
                    if self.dex > self.mind >= self.power:
                        self.name = 'Nandin'
                    if self.mind > self.dex > self.power:
                        self.name = 'Ushasu'
                    if (self.power >= self.dex >= self.mind) or (self.dex == self.mind and self.mind > self.power):
                        self.name = 'Varaha'
            if charProfession == 'Ranger':
                if secid in secIDListA:
                    if self.mind > self.dex > self.power:
                        self.name = 'Durga'
                    if self.mind > self.power >= self.dex:
                        self.name = 'Kabanda'
                    if self.power > self.mind > self.dex or self.dex >= self.power > self.mind:
                        self.name = 'Kaitabha'
                    if self.power > self.dex >= self.mind:
                        self.name = 'Madhu'
                    if (self.dex >= self.mind >= self.power) or (self.power == self.mind and self.mind > self.dex):
                        self.name = 'Varaha'
                if secid in secIDListB:
                    if self.mind > self.dex > self.power:
                        self.name = 'Apsaras'
                    if self.power > self.mind > self.dex or self.dex >= self.power > self.mind:
                        self.name = 'Bhirava'
                    if (self.power > self.dex >= self.mind or self.dex >= self.mind >= self.power) or (self.power == self.mind and self.mind > self.dex):
                        self.name = 'Kama'
                    if self.mind > self.power >= self.dex:
                        self.name = 'Varaha'
            if charProfession == 'Force':
                if secid in secIDListA:
                    if self.defense >= 45 and all(self.power > n for n in [self.defense, self.dex, self.mind]):
                        self.name = 'Andhaka'
                    if self.dex > self.mind >= self.power:
                        self.name = 'Bhirava'
                    if self.mind >= self.dex > self.power:
                        self.name = 'Ila'
                    if (self.mind >= self.power >= self.dex) or (self.power == self.dex and self.dex > self.mind):
                        self.name = 'Kumara'
                    if self.power > self.dex >= self.mind:
                        self.name = 'Marica'
                    if self.power > self.mind > self.dex:
                        self.name = 'Naga'
                if secid in secIDListB:
                    if self.defense >= 45 and all(self.power > n for n in [self.defense, self.dex, self.mind]):
                        self.name = 'Andhaka'
                    if self.mind >= self.dex > self.power:
                        self.name = 'Kabanda'
                    if (self.mind >= self.power >= self.dex) or (self.power == self.dex and self.dex > self.mind):
                        self.name = 'Naga'
                    if self.power > self.dex >= self.mind:
                        self.name = 'Naraka'
                    if self.power > self.mind > self.dex:
                        self.name = 'Ravana'
                    if self.dex > self.power > self.mind:
                        self.name = 'Ribhava'
                    if self.dex > self.mind >= self.power:
                        self.name = 'Sita'
        if self.level in range(100, 191, 10): #fourth evos
            if self.name in thirdEvoMagList:
                if gender == 'feminine':
                    if charProfession == 'Hunter':
                        if (secid in ['Viridia', 'Bluefull', 'Redria', 'Whitill'] and ((self.defense + self.dex) == (self.power + self.mind))) or ((secid in ['Greenill', 'Purplenum', 'Oran']) and ((self.defense + self.mind) == (self.power + self.defense))) or ((secid in ['Skyly', 'Pinkal', 'Yellowboze']) and ((self.defense + self.power) == (self.dex + self.mind))):
                            self.name = 'Savitri'
                    if charProfession == 'Ranger':
                        if secid in ['Skyly', 'Pinkal', 'Yellowboze'] and ((self.defense + self.power) == (self.dex + self.mind)):
                            self.name = 'Diwari'
                        if (secid in ['Viridia', 'Bluefull', 'Redria', 'Whitill'] and ((self.defense + self.dex) == (self.power + self.mind))) or (secid in ['Greenill', 'Purplenum', 'Oran'] and ((self.defense + self.mind) == (self.power + self.dex))):
                            self.name = 'Rukmin'
                    if charProfession == 'Force':
                        if (secid in ['Greenill', 'Purplenum', 'Oran'] and ((self.defense + self.mind) == (self.power + self.dex))) or (secid in ['Skyly', 'Pinkal', 'Yellowboze'] and ((self.defense + self.power) == (self.dex + self.mind))):
                            self.name = 'Bhima'
                        if secid in ['Viridia', 'Bluefull', 'Redria', 'Whitill'] and ((self.defense + self.dex) == (self.power + self.mind)):
                            self.name = 'Sato'
                if gender == 'masculine':
                    if charProfession == 'Hunter':
                        if secid in ['Viridia', 'Bluefull', 'Redria', 'Whitill'] and ((self.defense + self.dex) == (self.power + self.mind)):
                            self.name = 'Deva'
                        if (secid in ['Greenill', 'Purplenum', 'Oran'] and ((self.defense + self.mind) == (self.power + self.dex))) or (secid in ['Skyly', 'Pinkal', 'Yellowboze'] and ((self.defense + self.power) == (self.dex + self.mind))):
                            self.name = 'Rati'
                    if charProfession == 'Ranger':
                        if (secid in ['Viridia', 'Bluefull', 'Redria', 'Whitill'] and ((self.defense + self.dex) == (self.power + self.mind))) or (secid in ['Greenill', 'Purplenum', 'Oran'] and ((self.defense + self.mind) == (self.power + self.dex))) or (secid in ['Skyly', 'Pinkal', 'Yellowboze'] and ((self.defense + self.power) == (self.dex + self.mind))):
                            self.name = 'Pushan'
                    if charProfession == 'Force':
                        if (secid in ['Viridia', 'Bluefull', 'Redria', 'Whitill'] and ((self.defense + self.dex) == (self.power + self.mind))) or (secid in ['Greenill', 'Purplenum', 'Oran'] and ((self.defense + self.mind) == (self.power + self.dex))) or (secid in ['Skyly', 'Pinkal', 'Yellowboze'] and ((self.defense + self.power) == (self.dex + self.mind))):
                            self.name = 'Nidra'
    def feed(self):
        global sessionMags, inventory, timeToSleep, meseta, threadSwitch
        if self.level < self.targetLevel:
            CL = self.level
            if inventory[self.item][1] < 4:
                buy(self.item)
                if threadSwitch == 4:
                    return
            keyPress(Key.f4)
            for a in range(sessionMags.index(self)):
                keyPress(Key.down)
            keyPress(Key.enter)
            keyPress(Key.enter)
            for b in range(inventory[self.item][0]):  
                keyPress(Key.down)
            keyPress(Key.enter)
            keyPress(Key.f12)
            self.stats = addList(self.stats, self.tbl[self.item])
            self.setName()
            inventory[self.item][1] -= 1
            if self.level > 1+CL:
                outPut(f"{self.name} increased two or more levels in one feed, level {CL} to level {self.level}.")
            if self.level >= self.targetLevel:
                outPut(f"{self.name} reached target level of {self.targetLevel}.")
        if self.level < self.targetLevel:
            CL = self.level
            keyPress(Key.f4)
            for a in range(sessionMags.index(self)):
                keyPress(Key.down)
            keyPress(Key.enter)
            keyPress(Key.enter)
            for b in range(inventory[self.item][0]):
                keyPress(Key.down)
            keyPress(Key.enter)
            keyPress(Key.f12)
            self.stats = addList(self.stats, self.tbl[self.item])
            self.setName()
            inventory[self.item][1] -= 1
            if self.level > 1+CL:
                outPut(f"{self.name} increased two or more levels in one feed, level {CL} to level {self.level}.")
            if self.level >= self.targetLevel:
                outPut(f"{self.name} reached target level of {self.targetLevel}.")
        if self.level < self.targetLevel:
            CL = self.level
            keyPress(Key.f4)        
            for a in range(sessionMags.index(self)):
                keyPress(Key.down)
            keyPress(Key.enter)
            keyPress(Key.enter)
            for b in range(inventory[self.item][0]):
                keyPress(Key.down)
            keyPress(Key.enter)
            keyPress(Key.f12)
            self.stats = addList(self.stats, self.tbl[self.item])
            self.setName()
            inventory[self.item][1] -= 1
            if self.level > 1+CL:
                outPut(f"{self.name} increased two or more levels in one feed, level {CL} to level {self.level}.")
            if self.level >= self.targetLevel:
                outPut(f"{self.name} reached target level of {self.targetLevel}.")
        if all(mag.level >= mag.targetLevel for mag in sessionMags):
            threadSwitch = 3
    @property
    def defense(self):
        return int(self.stats[0])
    @property
    def power(self):
        return int(self.stats[1])
    @property
    def dex(self):
        return int(self.stats[2])
    @property
    def mind(self):
        return int(self.stats[3])
    @property
    def level(self):
        return int(self.stats[0])+int(self.stats[1])+int(self.stats[2])+int(self.stats[3])
    @property
    def tbl(self):
        return itemTblList[magFeedingTables[self.name]]
def addList(l1, l2): #function that takes two lists and appends values of list 1 with values of list 2. prevents the values from going below the current int. to use during feed: stats = addList(stats, itemTbl['Monomate']) 
        l3 = []
        f0 = int(l1[0])
        f1 = int(l1[1])
        f2 = int(l1[2])
        f3 = int(l1[3])
        l3.append(max(f0, round((l1[0] + l2[0]), 2)))
        l3.append(max(f1, round((l1[1] + l2[1]), 2)))
        l3.append(max(f2, round((l1[2] + l2[2]), 2)))
        l3.append(max(f3, round((l1[3] + l2[3]), 2)))
        return l3

def outPut(n):
    global dateAndTime
    dateAndTime=datetime.datetime.now().strftime("%H:%M:%S")
    f=open('AutoMateLog.txt', 'a')
    f.write(dateAndTime)
    f.write(f' {n}')
    f.write('\n')
    outputBox.insert("end", dateAndTime)
    outputBox.insert("end", f" {n}")
    outputBox.insert("end", "\n")
    outputBox.see("end")

def addMag():
    global numMags
    if numMags==1:
        #root.geometry('1100x650')
        mag2Frame.grid(row=3, column=2, columnspan=2, rowspan=4, padx=10, pady=10)
        mag2NameLabel.grid(column=2, row=4, padx=10, pady=10, sticky='w')
        mag2NameInput.grid(column=3, row=4, padx=10, pady=10)
        mag2StatsLabel.grid(column=2, row=5, padx=10, pady=10, sticky='w')
        mag2StatsInput.grid(column=3, row=5, padx=10, pady=10)
        mag2ItemLabel.grid(column=2, row=6, padx=10, pady=10, sticky='w')
        mag2ItemInput.grid(column=3, row=6, padx=10, pady=10)
        mag2TargetLevelLabel.grid(column=2, row=7, padx=10, pady=10, sticky='w')
        mag2TargetLevelInput.grid(column=3, row=7, padx=10, pady=10)
        numMags+=1
        outPut("Mag Added")
    elif numMags==2:
        root.geometry('1300x680')
        mag3Frame.grid(row=3, column=4, columnspan=2, rowspan=4, padx=10, pady=10)
        mag3NameLabel.grid(column=4, row=4, padx=10, pady=10, sticky='w')
        mag3NameInput.grid(column=5, row=4, padx=10, pady=10)
        mag3StatsLabel.grid(column=4, row=5, padx=10, pady=10, sticky='w')
        mag3StatsInput.grid(column=5, row=5, padx=10, pady=10)
        mag3ItemLabel.grid(column=4, row=6, padx=10, pady=10, sticky='w')
        mag3ItemInput.grid(column=5, row=6, padx=10, pady=10)
        mag3TargetLevelLabel.grid(column=4, row=7, padx=10, pady=10, sticky='w')
        mag3TargetLevelInput.grid(column=5, row=7, padx=10, pady=10)
        numMags+=1
        outPut("Mag Added")
    elif numMags==3:
        root.geometry('1300x950')
        mag4Frame.grid(row=7, column=0, columnspan=2, rowspan=4, padx=10, pady=10)
        mag4NameLabel.grid(column=0, row=9, padx=10, pady=10, sticky='w')
        mag4NameInput.grid(column=1, row=9, padx=10, pady=10)
        mag4StatsLabel.grid(column=0, row=10, padx=10, pady=10, sticky='w')
        mag4StatsInput.grid(column=1, row=10, padx=10, pady=10)
        mag4ItemLabel.grid(column=0, row=11, padx=10, pady=10, sticky='w')
        mag4ItemInput.grid(column=1, row=11, padx=10, pady=10)
        mag4TargetLevelLabel.grid(column=0, row=12, padx=10, pady=10, sticky='w')
        mag4TargetLevelInput.grid(column=1, row=12, padx=10, pady=10)
        numMags+=1
        outPut("Mag Added")
    elif numMags==4:
        mag5Frame.grid(row=7, column=2, columnspan=2, rowspan=4, padx=10, pady=10)
        mag5NameLabel.grid(column=2, row=9, padx=10, pady=10, sticky='w')
        mag5NameInput.grid(column=3, row=9, padx=10, pady=10)
        mag5StatsLabel.grid(column=2, row=10, padx=10, pady=10, sticky='w')
        mag5StatsInput.grid(column=3, row=10, padx=10, pady=10)
        mag5ItemLabel.grid(column=2, row=11, padx=10, pady=10, sticky='w')
        mag5ItemInput.grid(column=3, row=11, padx=10, pady=10)
        mag5TargetLevelLabel.grid(column=2, row=12, padx=10, pady=10, sticky='w')
        mag5TargetLevelInput.grid(column=3, row=12, padx=10, pady=10)
        numMags+=1
        outPut("Mag Added")
    elif numMags==5:
        mag6Frame.grid(row=7, column=4, columnspan=2, rowspan=4, padx=10, pady=10)
        mag6NameLabel.grid(column=4, row=9, padx=10, pady=10, sticky='w')
        mag6NameInput.grid(column=5, row=9, padx=10, pady=10)
        mag6StatsLabel.grid(column=4, row=10, padx=10, pady=10, sticky='w')
        mag6StatsInput.grid(column=5, row=10, padx=10, pady=10)
        mag6ItemLabel.grid(column=4, row=11, padx=10, pady=10, sticky='w')
        mag6ItemInput.grid(column=5, row=11, padx=10, pady=10)
        mag6TargetLevelLabel.grid(column=4, row=12, padx=10, pady=10, sticky='w')
        mag6TargetLevelInput.grid(column=5, row=12, padx=10, pady=10)
        numMags+=1
        outPut("Mag Added")
    elif numMags==6:
        outPut("Maximum Mags Reached")

def removeMag():
    global numMags
    if numMags==1:
        outPut("Cannot Remove Only Mag")

    elif numMags==6:
        mag6Frame.grid_remove()
        mag6NameLabel.grid_remove()
        mag6NameInput.grid_remove()
        mag6StatsLabel.grid_remove()
        mag6StatsInput.grid_remove()
        mag6ItemLabel.grid_remove()
        mag6ItemInput.grid_remove()
        mag6TargetLevelLabel.grid_remove()
        mag6TargetLevelInput.grid_remove()
        numMags-=1
        outPut("Mag Removed")
    elif numMags==5:
        mag5Frame.grid_remove()
        mag5NameLabel.grid_remove()
        mag5NameInput.grid_remove()
        mag5StatsLabel.grid_remove()
        mag5StatsInput.grid_remove()
        mag5ItemLabel.grid_remove()
        mag5ItemInput.grid_remove()
        mag5TargetLevelLabel.grid_remove()
        mag5TargetLevelInput.grid_remove()
        numMags-=1
        outPut("Mag Removed")
    elif numMags==4:
        root.geometry('1300x680')
        mag4Frame.grid_remove()
        mag4NameLabel.grid_remove()
        mag4NameInput.grid_remove()
        mag4StatsLabel.grid_remove()
        mag4StatsInput.grid_remove()
        mag4ItemLabel.grid_remove()
        mag4ItemInput.grid_remove()
        mag4TargetLevelLabel.grid_remove()
        mag4TargetLevelInput.grid_remove()
        numMags-=1
        outPut("Mag Removed")
    elif numMags==3:
        root.geometry('1100x680')
        mag3Frame.grid_remove()
        mag3NameLabel.grid_remove()
        mag3NameInput.grid_remove()
        mag3StatsLabel.grid_remove()
        mag3StatsInput.grid_remove()
        mag3ItemLabel.grid_remove()
        mag3ItemInput.grid_remove()
        mag3TargetLevelLabel.grid_remove()
        mag3TargetLevelInput.grid_remove()
        numMags-=1
        outPut("Mag Removed")
    elif numMags==2:
        root.geometry('900x680')
        mag2Frame.grid_remove()
        mag2NameLabel.grid_remove()
        mag2NameInput.grid_remove()
        mag2StatsLabel.grid_remove()
        mag2StatsInput.grid_remove()
        mag2ItemLabel.grid_remove()
        mag2ItemInput.grid_remove()
        mag2TargetLevelLabel.grid_remove()
        mag2TargetLevelInput.grid_remove()
        numMags-=1
        outPut("Mag Removed")


            

def startFeedThread():
    #checks that fields are filled
    fieldCheckList = [charClassVar.get()=="",sectionIDVar.get()=="", mesetaInput.get()=="", mag1NameVar.get()=="", mag1StatsInput.get()=="", mag1ItemVar.get()=="", mag1TargetLevelInput.get()==""]
    if any(fieldCheckList):
        outPut("Please fill all fields and try again.")
        return
    if numMags >= 2:
        fieldCheckList = [mag2NameVar.get()=="", mag2StatsInput.get()=="", mag2ItemVar.get()=="", mag2TargetLevelInput.get()==""]
        if any(fieldCheckList):
            outPut("Please fill all fields and try again.")
            return
    if numMags >= 3:
        fieldCheckList = [mag3NameVar.get()=="", mag3StatsInput.get()=="", mag3ItemVar.get()=="", mag3TargetLevelInput.get()==""]
        if any(fieldCheckList):
            outPut("Please fill all fields and try again.")
            return
    if numMags >= 4:
        fieldCheckList = [mag4NameVar.get()=="", mag4StatsInput.get()=="", mag4ItemVar.get()=="", mag4TargetLevelInput.get()==""]
        if any(fieldCheckList):
            outPut("Please fill all fields and try again.")
            return
    if numMags >= 5:
        fieldCheckList = [mag5NameVar.get()=="", mag5StatsInput.get()=="", mag5ItemVar.get()=="", mag5TargetLevelInput.get()==""]
        if any(fieldCheckList):
            outPut("Please fill all fields and try again.")
            return
    if numMags >=6:
        fieldCheckList = [mag6NameVar.get()=="", mag6StatsInput.get()=="", mag6ItemVar.get()=="", mag6TargetLevelInput.get()==""]
        if any(fieldCheckList):
            outPut("Please fill all fields and try again.")
            return
    if grabGame():
        Thread(target = feedingFunction).start()
        

def delayedFeedThread():
    #checks that fields are filled
    fieldCheckList = [charClassVar.get()=="",sectionIDVar.get()=="", mesetaInput.get()=="", mag1NameVar.get()=="", mag1StatsInput.get()=="", mag1ItemVar.get()=="", mag1TargetLevelInput.get()==""]
    if any(fieldCheckList):
        outPut("Please fill all fields and try again.")
        return
    if numMags >= 2:
        fieldCheckList = [mag2NameVar.get()=="", mag2StatsInput.get()=="", mag2ItemVar.get()=="", mag2TargetLevelInput.get()==""]
        if any(fieldCheckList):
            outPut("Please fill all fields and try again.")
            return
    if numMags >= 3:
        fieldCheckList = [mag3NameVar.get()=="", mag3StatsInput.get()=="", mag3ItemVar.get()=="", mag3TargetLevelInput.get()==""]
        if any(fieldCheckList):
            outPut("Please fill all fields and try again.")
            return
    if numMags >= 4:
        fieldCheckList = [mag4NameVar.get()=="", mag4StatsInput.get()=="", mag4ItemVar.get()=="", mag4TargetLevelInput.get()==""]
        if any(fieldCheckList):
            outPut("Please fill all fields and try again.")
            return
    if numMags >= 5:
        fieldCheckList = [mag5NameVar.get()=="", mag5StatsInput.get()=="", mag5ItemVar.get()=="", mag5TargetLevelInput.get()==""]
        if any(fieldCheckList):
            outPut("Please fill all fields and try again.")
            return
    if numMags >=6:
        fieldCheckList = [mag6NameVar.get()=="", mag6StatsInput.get()=="", mag6ItemVar.get()=="", mag6TargetLevelInput.get()==""]
        if any(fieldCheckList):
            outPut("Please fill all fields and try again.")
            return
    Thread(target = delayedFeed).start()

def delayedFeed():
    global threadSwitch
    if grabGame():
        threadSwitch = 0
        outPut("Delayed Feed Scheduled")
        countdownTimer = 210.0
        while countdownTimer>1:
            time.sleep(.2)
            if grabGame() == False:
                return
            if threadSwitch == 1:
                outPut("Scheduled Feed Canceled")
                return
            countdownTimer-=.2
        startFeedThread()

def stopFeed():
    global threadSwitch
    threadSwitch = 1

def grabGame():
    global app, wizard
    try:
        app = pywinauto.application.Application().connect(handle=win32gui.FindWindow(None, "Ephinea: Phantasy Star Online Blue Burst"))
        wizard=app["Ephinea: Phantasy Star Online Blue Burst"]
        return True
    except:
        outPut("Game not detected. Please open PSO and try again.")
        return False

def keyPress(keyname): #presses keys with brief pauses so the game registers it
        global fromPynput, timeToSleep, threadSwitch
        if threadSwitch != 0:
            pass
        else:
            fromPynput=True
            realKeyboard.press(keyname)
            fromPynput=False
            time.sleep(.1)
            fromPynput=True
            realKeyboard.release(keyname)
            fromPynput=False
            time.sleep(.16)
            timeToSleep -= .25

def buy(itemToBuy): #buys items
    global inventory, meseta, itemTbl0, threadSwitch
    if meseta < ((10 - inventory[itemToBuy][1])*(itemTbl0[itemToBuy][4])):
        threadSwitch = 4
    else:
        meseta -= ((10 - inventory[itemToBuy][1])*(itemTbl0[itemToBuy][4]))
        i = 0
        keyPress(Key.enter)
        keyPress(Key.enter)
        match itemToBuy:
            case "Monomate":
                itemPosition = 0
            case "Dimate":
                itemPosition = 1
            case "Trimate":
                itemPosition = 2
            case "Monofluid":
                itemPosition = 3
            case "Difluid":
                itemPosition = 4
            case "Trifluid":
                itemPosition = 5
            case "Antiparalysis":
                itemPosition = -3
            case "Antidote":
                itemPosition = -4
            case "Star Atomizer":
                itemPosition = -5
            case "Moon Atomizer":
                itemPosition = -6
            case "Sol Atomizer":
                itemPosition = -7
        if itemPosition < 0 : 
            while i > itemPosition :
                keyPress(Key.up)
                i -= 1
        else :
            while i < itemPosition :
                keyPress(Key.down)
                i += 1
        keyPress(Key.enter)
        if inventory[itemToBuy][1] == 9: #doesn't input down press if you already have x9 of the item
            pass
        else:
            keyPress(Key.down)
        keyPress(Key.enter)
        keyPress(Key.enter)
        keyPress(Key.backspace)
        keyPress(Key.backspace)
        keyPress(Key.backspace)
        inventory[itemToBuy][1] = 10


def feedingFunction():
    global timeToSleep, wizard, numMags, threadSwitch, magFeedingTables, sessionMags, inventory, iterator, itemTbl0, itemTbl1, itemTbl2, itemTbl3, itemTbl4, itemTbl5, itemTbl6, itemTbl7, itemTblList, fromPynput, numberOfFeeds, gender, secid, secIDListA, secIDListB, thirdEvoMagList, app, wizard, realKeyboard, charProfession, charClassInput, mag1NameVar, mag1StatsInput, mag1ItemVar, mag1TargetLevelInput, mag2NameVar, mag2StatsInput, mag2ItemVar, mag2TargetLevelInput, mag3NameVar, mag3StatsInput, mag3ItemVar, mag3TargetLevelInput, mag4NameVar, mag4StatsInput, mag4ItemVar, mag4TargetLevelInput, mag5NameVar, mag5StatsInput, mag5ItemVar, mag5TargetLevelInput, mag6NameVar, mag6StatsInput, mag6ItemVar, mag6TargetLevelInput, meseta

    def resetTimer(): #resets the timer to 3:35
        global timeToSleep
        timeToSleep = 215

    def funcRelease(key): #kills program on key release if not from pynput
        global fromPynput, threadSwitch
        if fromPynput == False:
            threadSwitch = 2

    def funcPress(key): #kills program on keyPress if not from pynput
        global fromPynput, threadSwitch
        if fromPynput == False:
            threadSwitch = 2

    def altTab(): #alt tabs
        global fromPynput, threadSwitch
        if threadSwitch != 0:
            pass
        else:
            fromPynput=True
            realKeyboard.press(Key.alt)
            fromPynput=False
            time.sleep(.05)
            fromPynput=True
            realKeyboard.press(Key.tab)
            fromPynput=False
            time.sleep(.05)
            fromPynput=True
            realKeyboard.release(Key.alt)
            realKeyboard.release(Key.tab)
            fromPynput=False
    #variables
    threadSwitch = 0
    sessionMags = [] #list of all the mags entered
    inventory = {} #uses self.item and iterator to keep track of inv (syntax is {'itemname': [invposition, itemcount]})
    iterator = 0 #this is to, for each item, set item position to iterator and then add 1 to iterator to keep track of item positions
    fromPynput=False
    numberOfFeeds=0
    realKeyboard = Controller()
    meseta = int(mesetaInput.get())
    secid = sectionIDVar.get()
    #defines profession and gender
    if charClassVar.get()[0] == 'H':
        charProfession = 'Hunter'
    if charClassVar.get()[0] == 'R':
        charProfession = 'Ranger'
    if charClassVar.get()[0] == 'F':
        charProfession = 'Force'
    if charClassVar.get() in ['HUmar', 'HUcast', 'RAmar', 'RAcast', 'FOmar', 'FOnewm']:
        gender = 'masculine'
    if charClassVar.get() in ['HUnewearl', 'HUcaseal', 'RAmarl', 'RAcaseal', 'FOmarl', 'FOnewearl']:
        gender = 'feminine'

    #adds all mags
    sessionMags.append(Mag(mag1NameVar.get(), mag1StatsInput.get().split('/')[0], mag1StatsInput.get().split('/')[1], mag1StatsInput.get().split('/')[2], mag1StatsInput.get().split('/')[3], mag1TargetLevelInput.get(), mag1ItemVar.get()))
    if numMags >= 2:
        sessionMags.append(Mag(mag2NameVar.get(), mag2StatsInput.get().split('/')[0], mag2StatsInput.get().split('/')[1], mag2StatsInput.get().split('/')[2], mag2StatsInput.get().split('/')[3], mag2TargetLevelInput.get(), mag2ItemVar.get()))
    if numMags >=3:
        sessionMags.append(Mag(mag3NameVar.get(), mag3StatsInput.get().split('/')[0], mag3StatsInput.get().split('/')[1], mag3StatsInput.get().split('/')[2], mag3StatsInput.get().split('/')[3], mag3TargetLevelInput.get(), mag3ItemVar.get()))
    if numMags >=4:
        sessionMags.append(Mag(mag4NameVar.get(), mag4StatsInput.get().split('/')[0], mag4StatsInput.get().split('/')[1], mag4StatsInput.get().split('/')[2], mag4StatsInput.get().split('/')[3], mag4TargetLevelInput.get(), mag4ItemVar.get()))
    if numMags >= 5:
        sessionMags.append(Mag(mag5NameVar.get(), mag5StatsInput.get().split('/')[0], mag5StatsInput.get().split('/')[1], mag5StatsInput.get().split('/')[2], mag5StatsInput.get().split('/')[3], mag5TargetLevelInput.get(), mag5ItemVar.get()))
    if numMags >= 6:
        sessionMags.append(Mag(mag6NameVar.get(), mag6StatsInput.get().split('/')[0], mag6StatsInput.get().split('/')[1], mag6StatsInput.get().split('/')[2], mag6StatsInput.get().split('/')[3], mag6TargetLevelInput.get(), mag6ItemVar.get()))
    
    for mag in sessionMags:
        if mag.item not in inventory:
            inventory[mag.item] = []
            inventory[mag.item].append(iterator)
            inventory[mag.item].append(0)
            iterator += 1
        
    listener = keyboard.Listener( #defines kb listener functions
        on_press=funcPress,
        on_release=funcRelease)
    listener.start()
    #main loop
    while True:
        wizard.set_focus()
        for i in range(30):
            time.sleep(.1)
            if threadSwitch == 1:
                outPut("Stopped Feeding")
                return
        wizard.set_focus()
        fromPynput=False
        if threadSwitch == 1:
                outPut("Stopped Feeding")
                return
        resetTimer()
        if threadSwitch == 1:
                outPut("Stopped Feeding")
                return
        if grabGame() == False:
            return
        for mag in sessionMags:
            mag.feed()
        mag1StatsInput.delete("0", "end")
        mag1NameVar.set(f"{sessionMags[0].name}")
        mag1StatsInput.insert('end', f'{round(sessionMags[0].stats[0], 2)}/{round(sessionMags[0].stats[1], 2)}/{round(sessionMags[0].stats[2], 2)}/{round(sessionMags[0].stats[3], 2)}')

        if numMags >=2:
            mag2StatsInput.delete("0","end")
            mag2NameVar.set(f"{sessionMags[1].name}")
            mag2StatsInput.insert('end', f'{round(sessionMags[1].stats[0], 2)}/{round(sessionMags[1].stats[1], 2)}/{round(sessionMags[1].stats[2], 2)}/{round(sessionMags[1].stats[3], 2)}')

        if numMags >=3:
            mag3StatsInput.delete("0","end")
            mag3NameVar.set(f"{sessionMags[2].name}")
            mag3StatsInput.insert('end', f'{round(sessionMags[2].stats[0], 2)}/{round(sessionMags[2].stats[1], 2)}/{round(sessionMags[2].stats[2], 2)}/{round(sessionMags[2].stats[3], 2)}')

        if numMags >=4:
            mag4StatsInput.delete("0","end")
            mag4NameVar.set(f"{sessionMags[3].name}")
            mag4StatsInput.insert('end', f'{round(sessionMags[3].stats[0], 2)}/{round(sessionMags[3].stats[1], 2)}/{round(sessionMags[3].stats[2], 2)}/{round(sessionMags[3].stats[3], 2)}')
        
        if numMags >=5:
            mag5StatsInput.delete("0","end")
            mag5NameVar.set(f"{sessionMags[4].name}")
            mag5StatsInput.insert('end', f'{round(sessionMags[4].stats[0], 2)}/{round(sessionMags[4].stats[1], 2)}/{round(sessionMags[4].stats[2], 2)}/{round(sessionMags[4].stats[3], 2)}')

        if numMags >=6:
            mag6StatsInput.delete("0","end")
            mag6NameVar.set(f"{sessionMags[5].name}")
            mag6StatsInput.insert('end', f'{round(sessionMags[5].stats[0], 2)}/{round(sessionMags[5].stats[1], 2)}/{round(sessionMags[5].stats[2], 2)}/{round(sessionMags[5].stats[3], 2)}')
        
        mesetaInput.delete("0", "end")
        mesetaInput.insert("end", f"{meseta}")
        if threadSwitch ==4:
            outPut("Meseta depleted. Exiting to protect save data.")
            return
        if threadSwitch == 3:
            outPut("All desired levels acheived. Exiting.")
            return
        if threadSwitch == 2:
            outPut("Key pressed while feeding. Exiting to protect save data.")
            return
        if threadSwitch == 1:
            outPut("Stopped Feeding")
            return

        altTab()
        if threadSwitch == 2:
            outPut("Key pressed while feeding. Exiting to protect save data.")
            return
        fromPynput=True
        numberOfFeeds+=1
        if threadSwitch == 1:
                outPut("Stopped Feeding")
                return
        outPut(f'{numberOfFeeds} feeds completed.')
        for i in range(int(timeToSleep)*10):
            time.sleep(.1)
            if grabGame == False:
                return
            if threadSwitch == 1:
                outPut("Stopped Feeding")
                return

# create main window
root = tkinter.Tk()
root.geometry('900x680')
iconPath = resource_path('sato.ico')
root.iconbitmap(iconPath)
root.title("AutoMate v1.0 by Rich")

# labels
charInfoFrame = LabelFrame(root, text="Character Information", padx=5, pady=5)
charInfoFrame.grid(row=0, column=0, columnspan = 3, rowspan = 2, padx=10, pady=10, sticky='nw')

charClassLabel = tkinter.Label(charInfoFrame, text="Class", font=('Dotum', 11))

sectionIDLabel = tkinter.Label(charInfoFrame, text="Section ID", font=('Dotum', 11))

mesetaLabel = tkinter.Label(charInfoFrame, text="Meseta In Inventory", font=('Dotum', 11))

instructionsFrame = LabelFrame(root, text="How To Use", height=121, width=470, padx=5, pady=5)
instructionsFrame.grid(row=0, column=3, columnspan = 3, rowspan = 2, padx=10, pady=10, sticky='nw')
instructionsText = tkinter.Text(instructionsFrame, font=('Dotum', 10), width=50, height=10, bg='#f0f0f0')
instructionsText.grid(row=0, column=3, columnspan=3, rowspan=2, padx=5, pady=5, sticky='nw')
instructionsText.insert('end',"1. Enter information for the mags you wish to feed in\nthe order they appear in your inventory.\n\n2. Remove all OTHER mags and all FEEDABLE items from your inventory.\n\n3. Stand within range of the item shop seller.\n\n4. Press Start Feeding or, if your mag is not ready to be fed, Start Delayed Feed.")
instructionsText.config(state=DISABLED)
#instructionsCanvas = Canvas(instructionsFrame, height=121, width=470)
#instructionsCanvas.create_text(100, 50, text="TESTINGTESTING\nTESTINGTESTINGTESTING\nTESTINGTESTINGTESTING\nTESTINGTESTINGTESTING\nTESTINGTESTINGTESTING\nTESTINGTESTINGTESTINGTESTINGTESTINGTESTINGTESTINGTESTINGTESTINGTESTINGTESTINGTESTINGTESTINGTESTINGTESTING\n", font=('Dotum', 10), justify='left')
#instructionsCanvas.grid(row=0, column=3, columnspan=3, rowspan=2, sticky='nswe')

mag1Frame = LabelFrame(root, text="Mag 1", padx=10, pady=10)
mag1Frame.grid(row=3, column=0, columnspan=2, rowspan=4, padx=10, pady=10)
mag1NameLabel = tkinter.Label(mag1Frame, text="Name", font=('Dotum', 11))
mag1StatsLabel = tkinter.Label(mag1Frame, text="Stats (DEF/POW/DEX/MIND)", font=('Dotum', 11))
mag1ItemLabel = tkinter.Label(mag1Frame, text="Item", font=('Dotum', 11))
mag1TargetLevelLabel = tkinter.Label(mag1Frame, text="Target Level", font=('Dotum', 11))
mag1NameVar = tkinter.StringVar()
mag1NameVar.set("Mag")
mag1NameInput = tkinter.OptionMenu(mag1Frame, mag1NameVar, *sorted(magFeedingTables))
mag1StatsInput = tkinter.Entry (mag1Frame)
mag1StatsInput.insert('end', '5/0/0/0')
mag1ItemVar = tkinter.StringVar()
mag1ItemVar.set("")
mag1ItemInput = tkinter.OptionMenu(mag1Frame, mag1ItemVar, *itemTbl0)
mag1TargetLevelInput = tkinter.Entry (mag1Frame)
mag1TargetLevelInput.insert('end', "200")

mag2Frame = LabelFrame(root, text="Mag 2", padx=10, pady=10)
mag2NameLabel = tkinter.Label(mag2Frame, text="Name", font=('Dotum', 11))
mag2StatsLabel = tkinter.Label(mag2Frame, text="Stats (DEF/POW/DEX/MIND)", font=('Dotum', 11))
mag2ItemLabel = tkinter.Label(mag2Frame, text="Item", font=('Dotum', 11))
mag2TargetLevelLabel = tkinter.Label(mag2Frame, text="Target Level", font=('Dotum', 11))
mag2NameVar = tkinter.StringVar()
mag2NameVar.set("Mag")
mag2NameInput = tkinter.OptionMenu(mag2Frame, mag2NameVar, *sorted(magFeedingTables))
mag2StatsInput = tkinter.Entry (mag2Frame)
mag2StatsInput.insert('end', '5/0/0/0')
mag2ItemVar = tkinter.StringVar()
mag2ItemVar.set("")
mag2ItemInput = tkinter.OptionMenu(mag2Frame, mag2ItemVar, *itemTbl0)
mag2TargetLevelInput = tkinter.Entry (mag2Frame)
mag2TargetLevelInput.insert('end', "200")

mag3Frame = LabelFrame(root, text="Mag 3", padx=10, pady=10)
mag3NameLabel = tkinter.Label(mag3Frame, text="Name", font=('Dotum', 11))
mag3StatsLabel = tkinter.Label(mag3Frame, text="Stats (DEF/POW/DEX/MIND)", font=('Dotum', 11))
mag3ItemLabel = tkinter.Label(mag3Frame, text="Item", font=('Dotum', 11))
mag3TargetLevelLabel = tkinter.Label(mag3Frame, text="Target Level", font=('Dotum', 11))
mag3NameVar = tkinter.StringVar()
mag3NameVar.set("Mag")
mag3NameInput = tkinter.OptionMenu(mag3Frame, mag3NameVar, *sorted(magFeedingTables))
mag3StatsInput = tkinter.Entry (mag3Frame)
mag3StatsInput.insert('end', '5/0/0/0')
mag3ItemVar = tkinter.StringVar()
mag3ItemVar.set("")
mag3ItemInput = tkinter.OptionMenu(mag3Frame, mag3ItemVar, *itemTbl0)
mag3TargetLevelInput = tkinter.Entry (mag3Frame)
mag3TargetLevelInput.insert('end', "200")

mag4Frame = LabelFrame(root, text="Mag 4", padx=10, pady=10)
mag4NameLabel = tkinter.Label(mag4Frame, text="Name", font=('Dotum', 11))
mag4StatsLabel = tkinter.Label(mag4Frame, text="Stats (DEF/POW/DEX/MIND)", font=('Dotum', 11))
mag4ItemLabel = tkinter.Label(mag4Frame, text="Item", font=('Dotum', 11))
mag4TargetLevelLabel = tkinter.Label(mag4Frame, text="Target Level", font=('Dotum', 11))
mag4NameVar = tkinter.StringVar()
mag4NameVar.set("Mag")
mag4NameInput = tkinter.OptionMenu(mag4Frame, mag4NameVar, *sorted(magFeedingTables))
mag4StatsInput = tkinter.Entry (mag4Frame)
mag4StatsInput.insert('end', '5/0/0/0')
mag4ItemVar = tkinter.StringVar()
mag4ItemVar.set("")
mag4ItemInput = tkinter.OptionMenu(mag4Frame, mag4ItemVar, *itemTbl0)
mag4TargetLevelInput = tkinter.Entry (mag4Frame)
mag4TargetLevelInput.insert('end', "200")

mag5Frame = LabelFrame(root, text="Mag 5", padx=10, pady=10)
mag5NameLabel = tkinter.Label(mag5Frame, text="Name", font=('Dotum', 11))
mag5StatsLabel = tkinter.Label(mag5Frame, text="Stats (DEF/POW/DEX/MIND)", font=('Dotum', 11))
mag5ItemLabel = tkinter.Label(mag5Frame, text="Item", font=('Dotum', 11))
mag5TargetLevelLabel = tkinter.Label(mag5Frame, text="Target Level", font=('Dotum', 11))
mag5NameVar = tkinter.StringVar()
mag5NameVar.set("Mag")
mag5NameInput = tkinter.OptionMenu(mag5Frame, mag5NameVar, *sorted(magFeedingTables))
mag5StatsInput = tkinter.Entry (mag5Frame)
mag5StatsInput.insert('end', '5/0/0/0')
mag5ItemVar = tkinter.StringVar()
mag5ItemVar.set("")
mag5ItemInput = tkinter.OptionMenu(mag5Frame, mag5ItemVar, *itemTbl0)
mag5TargetLevelInput = tkinter.Entry (mag5Frame)
mag5TargetLevelInput.insert('end', "200")

mag6Frame = LabelFrame(root, text="Mag 6", padx=10, pady=10)
mag6NameLabel = tkinter.Label(mag6Frame, text="Name", font=('Dotum', 11))
mag6StatsLabel = tkinter.Label(mag6Frame, text="Stats (DEF/POW/DEX/MIND)", font=('Dotum', 11))
mag6ItemLabel = tkinter.Label(mag6Frame, text="Item", font=('Dotum', 11))
mag6TargetLevelLabel = tkinter.Label(mag6Frame, text="Target Level", font=('Dotum', 11))
mag6NameVar = tkinter.StringVar()
mag6NameVar.set("Mag")
mag6NameInput = tkinter.OptionMenu(mag6Frame, mag6NameVar, *sorted(magFeedingTables))
mag6StatsInput = tkinter.Entry (mag6Frame)
mag6StatsInput.insert('end', '5/0/0/0')
mag6ItemVar = tkinter.StringVar()
mag6ItemVar.set("")
mag6ItemInput = tkinter.OptionMenu(mag6Frame, mag6ItemVar, *itemTbl0)
mag6TargetLevelInput = tkinter.Entry (mag6Frame)
mag6TargetLevelInput.insert('end', "200")


# buttons
addMagButton = tkinter.Button(text='Add Mag', height=1, width=12, font=('Dotum', 10), command=addMag)
removeMagButton = tkinter.Button(text='Remove Mag', height=1, width=12, font=('Dotum', 10), command=removeMag)
feedButtonsFrame = Frame(root, padx=10, pady=10)
feedButtonsFrame.grid(row=20, column=3, columnspan=3, rowspan=1, padx=10, pady=10, sticky='se')
startFeedButton = tkinter.Button(feedButtonsFrame, text='Start Feeding!', height=2, width=12, font=('Dotum', 12), command=startFeedThread)
startFeedLaterButton = tkinter.Button(feedButtonsFrame, text='Start Delayed\nFeed', height=2, width=12, font=('Dotum', 11), command=delayedFeedThread)
stopFeedButton = tkinter.Button(feedButtonsFrame, text='Stop Feeding', height=2, width=12, font=('Dotum', 12), command=stopFeed)
startFeedLaterButton.grid(column=3, row=20, padx=10, pady=10)
startFeedButton.grid(column=4, row=20, padx=10, pady=10)
stopFeedButton.grid(column=5, row=20, padx=10, pady=10)

#fields
charClassVar = tkinter.StringVar()
charClassVar.set("HUmar")
charClassInput = tkinter.OptionMenu(charInfoFrame, charClassVar, *characterList)

sectionIDVar = tkinter.StringVar()
sectionIDVar.set("Viridia")
sectionIDInput = tkinter.OptionMenu(charInfoFrame, sectionIDVar, *secIDListAll)

mesetaInput = tkinter.Entry (charInfoFrame)
mesetaInput.insert('end', '999999')


#outputBox = tkinter.Text(root, width=70, height=5)
outputBox = scrolledtext.ScrolledText(root, width=70, height=5)
outputBox.bind("<Key>", lambda e:"break")

#putting it on the window
charClassLabel.grid(column=0, row=0, padx=10, pady=10, sticky='w')
sectionIDLabel.grid(column=1, row=0, padx=10, pady=10, sticky='w')
mesetaLabel.grid(column=2, row=0, padx=10, pady=10, sticky='w')

charClassInput.grid(column=0, row=1, padx=10, pady=10, sticky='w')
sectionIDInput.grid(column=1, row=1, padx=10, pady=10, sticky='w')
mesetaInput.grid(column=2, row=1, padx=10, pady=10, sticky='w')

mag1NameLabel.grid(column=0, row=4, padx=10, pady=10, sticky='w')
mag1NameInput.grid(column=1, row=4, padx=10, pady=10)

mag1StatsLabel.grid(column=0, row=5, padx=10, pady=10, sticky='w')
mag1StatsInput.grid(column=1, row=5, padx=10, pady=10)

mag1ItemLabel.grid(column=0, row=6, padx=10, pady=10, sticky='w')
mag1ItemInput.grid(column=1, row=6, padx=10, pady=10)

mag1TargetLevelLabel.grid(column=0, row=7, padx=10, pady=10, sticky='w')
mag1TargetLevelInput.grid(column=1, row=7, padx=10, pady=10)

addMagButton.grid(column=0, row=2, padx=10, pady=10)
removeMagButton.grid(column=1, row=2, padx=10, pady=10)

outputBox.grid(column=0, row=18, columnspan=4, padx=10, pady=10, sticky='w')


root.mainloop()


# to - do
# 
# more than 6 mags with scroll bar
# grab mags from item reader text file
# instructions box (DONE)
# make it change mag name and stats while feeding (DONE)
# prettier gui
# PICTURES
# swap to different item after evolution
# output "ready to be transferred to [CLASS] [SECID]
