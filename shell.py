"""_summary_
    This is shell for the programm. 
    Shell only executes commands.
"""


import os
import subprocess
import settings
from collection import Collection
from io import StringIO
import sys

collection = Collection()
collection.delete_long_cmds()

cmds_list = ["help", "cd", "save_mode"]

exec_out = "12"

def execute_commands(command):
    """piping and exec cmds"""
    try:     

        stream_in, stream_out = (0, 0)
        stream_in = os.dup(0)
        stream_out = os.dup(1)

        fdin = os.dup(stream_in)

        for cmd in command.split(settings.PIPE):
            os.dup2(fdin, 0)
            os.close(fdin)
            if cmd == command.split(settings.PIPE)[-1]:
                fdout = os.dup(stream_out)
            else:
                fdin, fdout = os.pipe()
            
            os.dup2(fdout, 1)
            os.close(fdout)
            
            try:
                run_command(cmd.strip())
            except:
                print(settings.CMD_DNE)

        os.dup2(stream_in, 0)
        os.dup2(stream_out, 1)

        os.close(stream_in)
        os.close(stream_out)

    except:
        return settings.CMD_DNE


def run_command(command):
    """run single cmd"""
    check = find_command(command)
    if check == settings.CMD_DNE or check == settings.WRONG_ARGS or check == None:
        try:
            process = subprocess.run(command.split(" "), capture_output=True)
            exec_out = process.stdout.decode("utf-8")
            # output recognition + no return
            print(exec_out)
            process.communicate(exec_out)
        except Exception:
            return check
    else:
        cmd_lst = command.split()
        cmd_name = cmd_lst[0]
        if cmd_name in cmds_list:
            # output recognition + no return
            return local_cmds(cmd_name, cmd_lst[1:])
        else:
            runner = collection.get_short(cmd_name)["runner"]
            if runner == settings.NONE:
                runner = ''
            exec_str = runner+" "+collection.get_short(cmd_name)["path"]+'/'+collection.get_short(cmd_name)["name"]
            subprocess.run(exec_str.split(" "))
            # make a function
            exec_out = process.stdout.decode("utf-8")
            # output recognition + no return
            print(exec_out)
            process.communicate(exec_out)


def local_cmds(cmd_name, cmd_lst):
     # no args
    if len(cmd_lst) == 0:
        if cmd_name == "help":
            return help()
    # single arg
    elif len(cmd_lst) == 1:
        try:
            data = cmd_lst[0]
            if cmd_name == "save_mode":
                return save_mode(data)
            elif cmd_name == "cd":
                return cd(data)
        except:
            return settings.WRONG_ARGS
    else: 
        pass
    # mutliple args


def find_command(command):
    try:
        if command.split()[0] in cmds_list:
            return settings.NEUTRAL_ARGS
    except:
        if command in cmds_list:
            return settings.NEUTRAL_ARGS
        check = collection.check_command(command, settings.SAVE_MODE)
        return check
    

def save_mode(save):
    settings.SAVE_MODE = bool(save)


def cd(path):
    """change directory, return abs path"""
    try:
        os.chdir(os.path.abspath(path))
        return ""
    except Exception:
        return("cd: no such file or directory: {}".format(path))


def help():
    return("""Shell implementation in Python.
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
            #sys.stdout = term_stdout
            a = execute_commands(inp)
            print("_"*20)
            print(a)
            #sys.stdout = sys.__stdout__
            #print(execute_commands(inp), end="\n")
        else:
            a = run_command(inp)
            print("_"*20)
            print(a)
            #print(run_command(inp), end="\n")
        print(exec_out)

if '__main__' == __name__:
    main()