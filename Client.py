from tkinter.filedialog import askdirectory
from pydub.playback import play
from tkinter import messagebox
from pydub import AudioSegment
from mutagen.id3 import ID3
import tinytag
import tkinter
import pygame
import random
import json
import glob
import time
import sys
import os

os.system("cls")
appDataDir = "F:\\Sandbox\\Wave Music Player\\"
settingsDict = {}
tk = tkinter.Tk().withdraw()

class Backend:
    '''Functions used for backend-like operations that the end user will not see.'''
    
    def __init__(self):
        pass

    def init(self):
        '''Self made init function that defines variables and starts program procedures.'''
        if not os.path.isdir(appDataDir):
            os.mkdir(appDataDir)
            settingsDict["firstTime"] = True
            appDataFile = open(appDataDir+"Main", "w")
            appDataFile.write("Sharp s")
            appDataFile.close()
        else:
            settingsDict["firstTime"] = False
            
        if settingsDict["firstTime"] == True:
            directoryToUse = askdirectory()
            fileDiscovery = glob.glob(directoryToUse+"\\*.*")
            cleanList = Backend.sanitize(None, fileDiscovery)
            with open(appDataDir+"settings.txt", "w") as settingsFile:
                settingsFile.write(f"musicDir = {directoryToUse}")
            shuffledList = Backend.shuffle(None, cleanList)
        elif settingsDict["firstTime"] == False:
            if os.path.isfile(appDataDir+"settings.txt"):
                Backend.parseSettings(None, appDataDir+"settings.txt")
                if os.path.isdir(settingsDict["musicDir"]):
                    pass
                else:
                    directoryToUse = askdirectory()
                    settingsDict["musicDir"] = directoryToUse
                shuffledList = Backend.shuffle(None, settingsDict["musicDir"])
            else:
                messagebox.showerror("Settings Not Found", "Settings file not found. Please update settings or move your settings file to the correct location.")
                sys.exit()
        
        Frontend.startMusic(None, shuffledList)

        #allFiles = glob.glob(usrInputDir)

    def sanitize(self, targetList) -> list:
        '''Sanitizes argument targetList and returns a list that contains only valid music files. Returns sanitizedList'''
        sanitizedList = []
        for item in glob.glob(targetList+"\\*.*"):
            with open(item, "rb") as targetFileOpen:
                targetFileRead = targetFileOpen.read()[:3]
                if "ID3".encode("utf-8") in targetFileRead or "ÿû".encode("utf-8") in targetFileRead:
                    sanitizedList.append(item)
                else:
                    pass
        return sanitizedList
    
    def shuffle(self, whatToShuffle) -> list:
        '''Shuffles argument whatToShuffle by choosing a random entry, putting that into shuffledList, and deleting the original. Returns shuffedList.'''
        while whatToShuffle:
            whatToShuffle = Backend.sanitize(None, whatToShuffle)
            shuffledList = []
            randSong = random.choice(whatToShuffle)
            shuffledList.append(randSong)
            del whatToShuffle[whatToShuffle.index(randSong)]
            return shuffledList
            
    def idMusicFile(self, musicFile) -> dict:
        '''Returns an object containing metadata for argument musciFile.'''
        metadata = tinytag.TinyTag.get(musicFile)

        return metadata
        
    def parseSettings(self, settingsLocation):
        '''Reads and parses settings file location in settingsLocation and converts them into a global dictionary for use in the program. Returns nothing.'''
        with open(settingsLocation, "r") as settingsFile:
            settings = settingsFile.read().split("\n")
        for setting in settings:
            settingsPair = setting.split(" = ")
            settingsDict[settingsPair[0]] = settingsPair[1]
        
class Frontend:
    '''Functions used for front-end like operations that will be used to interact with the end-user'''
    
    def __init__(self):
        pass
        
    def startMusic(self, shuffledList):
        '''Begins music playback.'''
        for song in shuffledList:
            songMetadata = Backend.idMusicFile(None, song)
            songArtist = songMetadata.artist
            songTitle = songMetadata.title
            print(f"{songTitle} by {songArtist}")
            sound = AudioSegment.from_mp3(song)
            play(sound)
    
    def main(self):
        '''Program endpoint and gui function'''
        #TODO: Make GUI
        #Start of the gui section
        
        #End of the gui section
        Backend.init(None)
    
Frontend.main(None)
print("Done.")