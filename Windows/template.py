import sys
import getopt
from termcolor import colored, cprint

def main(argv):

    opts, args = getopt.getopt(
        argv, "", ["help"])#help= for input

    for opt, arg in opts:
        if opt in ("--help"):
            cprint("--help help info", "green")

    action("test")

def action(test):
    cprint("this is a template for my console app utils","red")

  


if __name__ == "__main__":
    main(sys.argv[1:])
 
