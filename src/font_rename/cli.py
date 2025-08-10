import argparse
import os

from font_rename.main import rename, get_fonts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        dest="path",
        nargs="*",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
    )

    args = parser.parse_args()
    for path in args.path:
        if os.path.isdir(path):
            font_files = get_fonts(path, recursive=args.recursive)
            if font_files:
                for font_file in font_files:
                    rename(font_file)
        else:
            rename(path)