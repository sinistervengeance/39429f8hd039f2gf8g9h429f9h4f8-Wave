import os
import glob
import tinytag

allFiles = glob.glob("F:\\Music\\*.*")

for files in allFiles:
    print(files)
    isolatedFile = files.split("F:\\Music\\")[1]
    print(isolatedFile)
    fileSplit = isolatedFile.split(" - ")
    print(fileSplit)
    tnytg = tinytag.TinyTag.get(files)
    tnytg.artist = fileSplit[0]
    tnytg.title = fileSplit[1]

print("Done.")