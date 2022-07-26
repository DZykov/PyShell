# PyShell: Simple shell with voice assistant written in python.
-    Simple shell made with python. Shell itself supports all cli commands, such as cd, ls, head, tail, etc. Voice assistant has to be configurated manually. Additionaly, voice assistant supports two languages: english and russian. 

## Index
   - [Demo](#Demo "Goto Demo")
   - [Installation](#Installation "Goto Installation")
   - [Features](#Features "Goto Features")
   - [Voice assistant configutation](#Voice_assistant_configutation "Goto Voice assistant configutation")
   - [shellsrc](#.shellsrc "Goto shellsrc")

## Demo

![alt text](https://github.com/DZykov/PyShell/blob/master/demo.png)


## Installation
#### Build from source
You need to have python 3.8 and json installed for this option.

Clone the repo, open the folder and run the source file


    $ git clone https://github.com/DZykov/PyShell.git
    $ cd PyShell
    $ python3 ./shell.py

## Features
   - Shell supports all comands and unix based packages
   - Voice assistant supports two languages: english and russian
   - Easy configuaration of shell scripts and voice assistant
   - Easy change of voice
   - Supports piping
   - Supports safe entry for custom scripts
   - Fully customizable and hackable

## Structure
- /settings.py - contains all constants and decorations for shell
- /config.py - contains all commands and outputs for voice assistant. This is the only file that should be edited to add commands to the voice assistant. Check the file for more specific instructions.
- /.shellsrc containes custom scripts for the shell. This file should be edited to add more commands to the shell.

## Voice_assistant_configutation

- NAME_ALIAS is a list of how to call the voice assistant.
- TBR_ALIAS is a list of key words in a voice command
- CMD_LIST is a dictionary of commands and voice input
- CMD_OUT is a dictionary of custom ouputs for specific commands
- CMD_INGORE is a list of commands whose output should be igored by voice assisant

## shellsrc

- all added scripts have to be in a format: file_name=alias=instruction=description=runner=path

    Example: test.sh=test=*=Example of .shellsrc=bash=/home/demid/Documents/Projects/shell


        Structure of the format:
        _____________________________________________________
        |File name|Alias|Instruction|Description|Runner|Path|
        |_________|_____|___________|___________|______|____|
    
        Command name -  name by which script/command is executed. Can be none.*
        Instruction  -  how command is run. Can be none.* If none, command is not checked in shell.
            Instruction is written in a format of arguments and the type of an argument.
            
            Types of arguments: int, str, double, pathd, and pathf
                int     -   integer
                str     -   string
                double  -   double
                pathd   -   path to a folder/directory
                pathf   -   path to a file

            There are two type of instructions: strict and classical. The begining of the instructions starts with its type: s or c
                Strict   :  order of arguments matters and cannot be changed.
                    Example: s [pathd]
                Classical:  order of arguments does not matter; however, each ergument has its own unique prefix.
                    Example: c [-s|str]
        
        Description - the description of a command. Can be none.*
        Runner - what runs a command/script. Can be none.*
        Path - path to a command/script.
        
        *none = * (by default, could be changed in settings.py)

        Example of database:
            ______________________________________________________________________________
            |Command name| Alias |        Instruction          |Description|Runner| Path |
            |------------|-------|-----------------------------|-----------|------|------|
            |   test_1   |   1   |      [int] [str] [int]      |  descr_1  |  -   |path_1|
            |------------|-------|-----------------------------|-----------|------|------|
            |   test_2   |   2   |  [-n|int] [-s|str] [-nc|int]|  descr_2  |  -   |path_2|
            |----------------------------------------------------------------------------|