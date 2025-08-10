import glob
import os

from fontTools.ttLib import TTFont


def get_fonts(directory, recursive=False) -> list:
    font_files = []
    for file in glob.glob("**", root_dir=directory, recursive=recursive):
        ext = os.path.splitext(file)[1].lower()
        if ext == ".ttf" or ext == ".otf":
            font_files.append(os.path.join(directory, file))
    return font_files


def rename(font_file, dry_run=False):
    try:
        directory, filename = os.path.split(font_file)
        name, ext = os.path.splitext(filename)
        ext = ext.lower()
        if ext == ".ttf" or ext == ".otf":
            postscript_name = TTFont(font_file)["name"].getDebugName(6)  # type: ignore
            if not postscript_name.isascii():
                print(f"Error: Postscript name is not ASCII. {font_file}")
                return
            if name != postscript_name:
                print(f"Rename: {font_file} -> {postscript_name}{ext}")
                if not dry_run:
                    os.rename(font_file, os.path.join(directory, postscript_name + ext))
        else:
            print(f"Error: Not a TTF or OTF. {font_file}")
    except Exception as e:
        print(f"Error: {e} {font_file}")