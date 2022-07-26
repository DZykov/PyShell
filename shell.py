"""_summary_
    This is shell for the programm. 
    Shell only executes commands.
"""


import os
import subprocess
import settings
import output
import input_recognition
import sys
import keyboard
from collection import Collection
from history import History
from io import StringIO


collection = Collection()
history = History()
collection.delete_long_cmds()


cmds_list = ["help", "cd", "save_mode", "output_mode", "input_mode", "change_lang"]


#############################################################################
####                                                                     ####
####                               Methods                               ####
####                                                                     ####
#############################################################################


def execute_commands(command):
    """Piping and exec cmds in order"""
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
                ouput_(settings.CMD_DNE)

        os.dup2(stream_in, 0)
        os.dup2(stream_out, 1)

        os.close(stream_in)
        os.close(stream_out)

    except:
        ouput_(settings.CMD_DNE)


def run_command(command):
    """Run single cmd"""
    history.add(command)
    check = find_command(command)
    if check == settings.CMD_DNE or check == settings.WRONG_ARGS or check == None:
        exec_subprocess(command)
    else:
        cmd_lst = command.split()
        cmd_name = cmd_lst[0]
        if cmd_name in cmds_list:
            ouput_(local_cmds(cmd_name, cmd_lst[1:]))
        elif check != None:
            runner = collection.get_short(cmd_name)["runner"]
            if runner == settings.NONE:
                runner = ''
            exec_str = runner+" "+collection.get_short(cmd_name)["path"]+'/'+collection.get_short(cmd_name)["name"]
            exec_subprocess(exec_str)


def exec_subprocess(exec_str):
    try:                                    #.split(" ")
        process = subprocess.run(exec_str, capture_output=True, shell=True)
        exec_out = process.stdout.decode("utf-8")
        ouput_(exec_out)
        if type(process) is subprocess.CalledProcessError:
            process.communicate(exec_out)
    except Exception as ex:
            ouput_(ex)


def find_command(command):
    """Find command and return it's status"""
    try:
        if command.split()[0] in cmds_list:
            return settings.NEUTRAL_ARGS
    except:
        if command in cmds_list:
            return settings.NEUTRAL_ARGS
        check = collection.check_command(command, settings.SAVE_MODE)
        return check


def local_cmds(cmd_name, cmd_lst):
    """Call the commands that are coded in shell itself"""
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
            elif cmd_name == "output_mode":
                return output_mode(data)
            elif cmd_name == "input_mode":
                return input_mode(data)
            elif cmd_name == "change_lang":
                return change_input_lang(data)
        except:
            return settings.WRONG_ARGS
    else: 
    # mutliple args
        try:
            data = cmd_lst[0:]
            """
            if cmd_name == "save_mode":
                return save_mode(data)
            elif cmd_name == "cd":
                return cd(data)
            """
        except:
            return settings.WRONG_ARGS


#############################################################################
####                                                                     ####
####                         Built-in commands                           ####
####                                                                     ####
#############################################################################


def change_input_lang(lang):
    if lang == "en":
        settings.IN_LANG = "en"
    elif lang == "ru":
        settings.IN_LANG = "ru"
    return "Input lang set to {}".format(settings.IN_LANG)


def save_mode(save):
    """Toogle save mode"""
    settings.SAVE_MODE = save in ("true", "True", "t")
    return "Save mode set to {}".format(settings.SAVE_MODE)


def input_mode(in_):
    """Toogle input mode"""
    settings.IN = in_
    return "Input mode set to {}".format(settings.IN)


def output_mode(out):
    """Toogle output mode"""
    settings.OUT = out
    return "Output mode set to {}".format(settings.OUT)


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

#############################################################################
####                                                                     ####
####                             [In][Out]put                            ####
####                                                                     ####
#############################################################################


def ouput_(out):
    """Produce output according to settings"""
    if out == None:
        return
    out = str(out).strip()
    if settings.OUT == settings.TEXT:
        output.print_text(out)
    if settings.OUT == settings.VOICE:
        output.put_voice(out)


def input_():
    """Take input according to settings"""
    if settings.IN == settings.TEXT:
        in_ = input_recognition.in_text()
        return in_
    if settings.IN == settings.VOICE:
        in_ = input_recognition.in_voice()
        return in_


#############################################################################
####                                                                     ####
####                                 Main                                ####
####                                                                     ####
#############################################################################


def main():
    while True:
        inp = input_()
        if inp == 1:
            pass
        elif inp == "exit":
            break
        elif settings.PIPE in inp:
            execute_commands(inp)
        else:
            run_command(inp)


if '__main__' == __name__:
    main()