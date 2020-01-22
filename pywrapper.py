import sys
import os

while True:
    print(os.system(f"python.lnk {input('Dir of file: ')}").read())


input("Input to kill:")
sys.exit()