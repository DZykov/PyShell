"""_summary_
    This is shell for the programm. 
    Shell only executes commands.
"""


import os
import subprocess
import settings


def execute_command(command):
    """piping and exec cmds"""
    pass

def run_command(command):
    """run single cmd"""
    pass


def find_command(command):
    """find cmd in db"""
    pass


def cd(path):
    """change directory, return abs path"""
    try:
        os.chdir(os.path.abspath(path))
    except Exception:
        print("cd: no such file or directory: {}".format(path))


def help():
    print("""Shell implementation in Python.
          Supports something.""")


def main():
    while True:
        inp = input("{} ".format(settings.SEPERATOR))
        # inp =  input recognition
        if inp == "exit":
            break
        elif settings.PIPE in inp:
            execute_command(inp)
        else:
            run_command(inp)