from tkinter.filedialog import askdirectory
from mutagen.id3 import ID3
import tkinter
import pygame
import random
import json
import os

appDataDir = "F:\\Sandbox\\Wave Music Player\\"
globalVars = {}
tk = tkinter.Tk().withdraw()

class Backend:
    '''Functions used for backend-like operations that the end user will not see.'''
    
    def __init__():
        pass

    def init(self):
        try:
            os.mkdir(appDataDir)
            globalVars["firstTime"] = True
            with open(appDataDir+"Main", "wb") as appDataFile:
                appDataFile.write("/xab")
        except Exception as error:
            print(error)
            globalVars["firstTime"] = False
            
        if globalVars["firstTime"] == True:
            askdirectory()
        elif globalVar["firstTime"] == False:
            pass
        allFiles = glob.glob(usrInputDir)

    def sanitze(self, targetList):
        sanitizedList = []
        for item in targetList:
            with open(item, "rb") as targetFileOpen:
                if targetFileOpen.read()[:2] == "ÿû" or targetFileOpen.read()[:3] == "ID3":
                    sanitizedList.append(item)
                else:
                    pass
        return sanitizedList
    
    def shuffle(self, whatToShuffle):
        while whatToShuffle:
            whatToShuffle = Backend.sanitze(whatToShuffle)
            shuffledList = []
            randSong = random.choice(whatToShuffle)
            shuffledList.append(randSong)
            del whatToShuffle[whatToShuffle.index(randSong)]
            
class Playback:
    '''Functions used for media playback.'''
    
    def __init__():
        self.songToPlay = songToPlay
        pygame.mixer.init()
    
    def play():
        pass
        
    def pause():
        pass
        
    def stop():
        pass
        
class Frontend:
    '''Functions used for front-end like operations that will be used to interact with the end-user'''
    
    def __init__():
        pass
    
    def main():
        #Program endpoint
        Backend.init(None)
    
    
Frontend.main()
print("Done.")