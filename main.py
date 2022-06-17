#!/usr/bin/python3

# check https://www.youtube.com/watch?v=UtMMjXOlRQc
# idea: command.py --file/--folder=str --verbose --key=str


import os
import sys
import argparse
from pathlib import Path

import termcolor

from utils import get_all_files, File



ascii_art = """
 dP""b8 88""Yb Yb  dP 88""Yb 888888 Yb        dP    db    88""Yb 888888 
dP   `" 88__dP  YbdP  88__dP   88    Yb  db  dP    dPYb   88__dP 88__   
Yb      88"Yb    8P   88\"""    88     YbdPYbdP    dP__Yb  88"Yb  88""   
 YboodP 88  Yb  dP    88       88      YP  YP    dP"\"""Yb 88  Yb 888888
"""

print(termcolor.colored(ascii_art, 'green'))


def get_home_directory() -> str :
    return str(Path.home())


filename = os.path.basename(__file__)
home_directory = get_home_directory()
COLORED_STAR = termcolor.colored('*', 'green')

no_encrypt_list = [
    filename,
]


parser = argparse.ArgumentParser(
    description="Fun tool to encrypt your WHOLE user directory, so use it carefully"
)

parser.add_argument(
    "--encrypt",
    action="store_true",
    help="Encrypt your directory"
)

parser.add_argument(
    "--decrypt",
    action="store_true",
    help="Decrypt your directory"
)

parser.add_argument(
    "-k",
    "--key",
    type=str,
    help="Key to encrypt/decrypt files",
)

parser.add_argument(
    "-v",
    "--verbose",
    action="store_true",
    help="Prints all files that are encrypted/decrypted"
)

args = parser.parse_args()

if (args.encrypt and args.decrypt) or (not args.encrypt and not args.decrypt):
    warning_text = termcolor.colored("[/!\\] Invalid usage of flags\n", "yellow")


action: str = "Encrypting" if args.encrypt else "Decrypting"

for file in get_all_files(home_directory):
    if args.verbose:
        print(f"[{COLORED_STAR}] {action} file {file}...")
    
    #File(file).encrypt(args.key)
    pass



# TODO : different verbose level like "--verbose=(int)" if it is 0 or no verbose flag is given then nothing is shown, if it is 1 only files that are not hidden and if it is 2 everything is shown
