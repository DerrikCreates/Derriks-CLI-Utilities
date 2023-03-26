import sys
import getopt
from termcolor import colored, cprint

myTools = ["DerrikSetup","webptosheet",]

def main(argv):

    opts, args = getopt.getopt(
        argv, "", ["help"])#help= for input

    for opt, arg in opts:
        if opt in ("--help"):
            cprint("--help help info", "green")

    for cmd in myTools:
        cprint(cmd,"cyan")
    


    

  


if __name__ == "__main__":
    main(sys.argv[1:])
 
