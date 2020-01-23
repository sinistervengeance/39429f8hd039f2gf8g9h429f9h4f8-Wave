from mutagen.mp3 import EasyMP3
import tinytag
import glob
import os

allFiles = glob.glob("F:\\Music\\*.*")

for files in allFiles:
    print(files)
    isolatedFile = files.split("F:\\Music\\")[1]
    print(isolatedFile)
    fileSplit = isolatedFile.split(" - ")
    print(fileSplit)
    tnytg = tinytag.TinyTag.get(files)
    metadata = EasyMP3()
    artist = fileSplit[0]
    song = fileSplit[1][:-4]
    metadata["Title"] = song
    metadata["Artist"] = artist
    metadata.save(files)

print("Done.")