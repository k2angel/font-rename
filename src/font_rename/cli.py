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
        "-d",
        "--dry-run",
        action="store_true",
        help="Displays the new file names without actually renaming the files.",
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="Recursively searches subdirectories for font files.",
    )

    args = parser.parse_args()
    for path in args.path:
        if os.path.isdir(path):
            font_files = get_fonts(path, recursive=args.recursive)
            for font_file in font_files:
                rename(font_file, dry_run=args.dry_run)
        else:
            rename(path, dry_run=args.dry_run)