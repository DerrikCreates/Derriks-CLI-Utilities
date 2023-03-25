import os
import subprocess
import pathlib
import sys
import getopt

from termcolor import colored, cprint
## Requires magick installed and set in your system path
def main(argv):

    opts, args = getopt.getopt(argv, "hs:e:n:")

    path = os.getcwd()+"\\"

    start = None
    end = None
    fileName = ""
    for opt, arg in opts:
        if opt in ("-s"):
            start = int(arg)
        elif opt in ("-e"):
            end = int(arg)
        elif opt in ("-n"):
            fileName = str(arg)
        elif opt in ("-h"):
            cprint("-s is the start image","green")
            cprint("-e is the end image index","green")
            cprint("-n is the name of the file with a * where the index should be ex output_*.png would resolve to output_1.png and so on","green")
            quit()
    sheetFiles = ""
    
    for i in range(start, end + 1):
        sheetFiles = sheetFiles +" "+ fileName.replace("*",str(i))

    print(path)
   

    result = subprocess.call(
        f'magick montage {sheetFiles} -tile x3 -geometry +0+0 spritesheet.png', cwd=path, shell=True)

    if result != 0:
        cprint("magick command failed to create sprite sheet!")
        quit()

    cprint(f"Created sprite sheet at {path}spritesheet.png","green")
    


if __name__ == "__main__":
    main(sys.argv[1:])
