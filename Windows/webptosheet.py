import shutil
import requests
import getopt
import sys
import validators
import os.path
import subprocess
from termcolor import colored, cprint
from PIL import Image, ImageSequence


def main(argv):

    opts, args = getopt.getopt(
        argv, "", ["help", "path=", "columns=", "name="])

    path = ""
    columns = 5
    outputName = ""

    for opt, arg in opts:
        if opt in ("--help"):
            cprint("--path provide a webp path or url", "green")
            cprint(
                "--columns the number of columns in the sprite sheet grid defaults to 5", "green")
            cprint("--the sprite sheet output name ", "green")
        elif opt in ("--path"):
            path = str(arg)
        elif opt in ("--columns"):
            columns = int(arg)
        elif opt in ("--name"):
            outputName = str(arg)

    cprint(f"Converting file at path {path}", "cyan")

    if validators.url(path):
        myfile = requests.get(path)
        open('temp.webp', 'wb').write(myfile.content)
        convert("temp.webp", columns, outputName)

    else:
        if os.path.isfile(path):
            convert(path, columns, outputName)

    os.remove("temp.webp")


def convert(path, rows, outputName):

    print(outputName)
    webp_image = Image.open(path)
    sprites = [frame.copy().convert('RGBA')
               for frame in ImageSequence.Iterator(webp_image)]

    sheet = create_sprite_sheet(
        sprites, rows, webp_image.width, webp_image.height)

    sheet.save(outputName)
    cprint(f"Saved sprite sheet {os.getcwd()}\\{outputName}", "green")


def create_sprite_sheet(sprites, sprites_per_row, width, height):

    cprint(f"w:{width},h:{height}", "green")
    sheet_width = width * sprites_per_row
    sheet_height = height * \
        ((len(sprites) + sprites_per_row - 1) // sprites_per_row)
    sheet = Image.new('RGBA', (sheet_width, sheet_height), (0, 0, 0, 0))

    for i, sprite in enumerate(sprites):

        temp_image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        temp_image.paste(sprite)
        x = (i % sprites_per_row) * width

        y = (i // sprites_per_row) * height

        box = (x, y, x + width, y + height)

        sheet.paste(temp_image, box=box)

    return sheet


if __name__ == "__main__":
    main(sys.argv[1:])
