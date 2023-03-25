import requests
import getopt
import sys
import validators
import os.path
import subprocess
from termcolor import colored, cprint
from PIL import Image, ImageSequence


def main(argv):

    opts, args = getopt.getopt(argv, "", ["help", "path=", "columns="])

    
    path = ""
    columns = 5
    for opt, arg in opts:
        if opt in ("--help"):
            cprint("--path provide a webp path or url", "green")
            cprint("--columns the number of columns in the sprite sheet grid defaults to 5", "green")
        elif opt in ("--path"):
            path = str(arg)
        elif opt in ("--columns"):
            columns = int(arg)

    if not os.path.exists("temp"):
        os.makedirs("temp")

    savePath = f"{os.getcwd()}\\temp\\"

    cprint(f"Converting file at path {path}", "cyan")

    if validators.url(path):
        myfile = requests.get(path)
        open('temp.webp', 'wb').write(myfile.content)
        convert("temp.webp",columns)
    else:
        if os.path.isfile(path):
            convert(path,columns)


def convert(path,rows):

    webp_image = Image.open(path)
    sprites = [frame.copy().convert('RGBA')
               for frame in ImageSequence.Iterator(webp_image)]

    sheet = create_sprite_sheet(
        sprites, rows, webp_image.width, webp_image.height)

    sheet.save("Sprite_Sheet.png")
    cprint(f"Saved sprite sheet {os.getcwd()}\\Sprite_Sheet.png", "green")


def create_sprite_sheet(sprites, sprites_per_row, width, height):
    sheet_width = width * sprites_per_row
    sheet_height = height * \
        ((len(sprites) + sprites_per_row - 1) // sprites_per_row)
    sheet = Image.new('RGBA', (sheet_width, sheet_height), (0, 0, 0, 0))

    for i, sprite in enumerate(sprites):
        x = (i % sprites_per_row) * width
        y = (i // sprites_per_row) * height
        box = (x, y, x + width, y + width)
        sheet.paste(sprite, box=box)

    return sheet


if __name__ == "__main__":
    main(sys.argv[1:])
