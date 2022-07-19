"""_summary_
    This is shell for the programm. 
    Shell only executes commands.
"""


import os
import subprocess
import settings
from collection import Collection

collection = Collection()
collection.delete_long_cmds()

cmds_list = ["help", "cd", "save_mode"]


def execute_commands(command):
    """piping and exec cmds"""
    pass


def run_command(command):
    """run single cmd"""
    check = find_command(command)
    if check == settings.CMD_DNE or check == settings.WRONG_ARGS:
        try:
            subprocess.run(command.split(" "))
        except Exception:
            return check
    else:
        cmd_lst = command.split()
        cmd_name = cmd_lst[0]
        
        if cmd_name in cmds_list:
           return local_cmds(cmd_name, cmd_lst[1:])
        else:
            runner = collection.get_short(cmd_name)["runner"]
            if runner == settings.NONE:
                runner = ''
            exec_str = runner+" "+collection.get_short(cmd_name)["path"]+'/'+collection.get_short(cmd_name)["name"]
            subprocess.run(command.split(" "))


def local_cmds(cmd_name, cmd_lst):
     # no args
    if cmd_name == "help":
        help()
    # single arg
    try:
        data = cmd_lst[0]
        if cmd_name == "save_mode":
            save_mode(data)
        elif cmd_name == "cd":
            cd(data)
    except:
        return settings.WRONG_ARGS
    # mutliple args


def find_command(command):
    if command.split()[0] in cmds_list:
        return settings.NEUTRAL_ARGS
    check = collection.check_command(command, settings.SAVE_MODE)
    return check
    

def save_mode(save):
    settings.SAVE_MODE = bool(save)


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
        settings.INFO=os.getcwd()
        left_t = settings.NAME+settings.SEPERATOR+settings.INFO+settings.ARROW
        inp = input("{} ".format(left_t))
        # inp =  input recognition
        # change print for output recognition
        if inp == "exit":
            break
        elif settings.PIPE in inp:
            print(execute_commands(inp))
        else:
            print(run_command(inp))

if '__main__' == __name__:
    main()