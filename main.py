#!/usr/bin/python3

# check https://www.youtube.com/watch?v=UtMMjXOlRQc
# idea: command.py --file/--folder=str --verbose --key=str


import os
import sys
import argparse
from pathlib import Path

import termcolor

from utils import get_all_files, File


def get_home_directory() -> str :
    return str(Path.home())


filename = os.path.basename(__file__)
home_directory = get_home_directory()

no_encrypt_list = [
    filename,
]


parser = argparse.ArgumentParser(
    description="Fun tool to encrypt your WHOLE user directory, so use it carefully"
)


for file in get_all_files(home_directory):
    print(file)
