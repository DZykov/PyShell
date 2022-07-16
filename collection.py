"""_summary_
    This is collection of the commands. 
    This is just a collection: collection is linkage between commands and a shell.
    Collection is made of database and codebase.
    Database:
        __________________________________________________
        |Command name|Instruction|Description|Runner|Path|
        |____________|___________|___________|______|____|
    
        Command name -  name by which script/command is executed
        Instruction  -  how command is run.
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
        
        Description - the description of a command.
        Runner - what runs a command/script. If no runner needed, write -
        Path - path to a command/script.

        Example of database:
            ______________________________________________________________________
            |Command name|        Instruction          |Description|Runner|Path  |
            |------------|-----------------------------|-----------|------|------|
            |   test_1   |    s [int] [str] [int]      |  descr_1  |  -   |path_1|
            |------------|-----------------------------|-----------|------|------|
            |   test_2   |c [-n|int] [-s|str] [-nc|int]|  descr_2  |  -   |path_2|
            |--------------------------------------------------------------------|

"""
import settings

class Collection:


    def __init__(self):
        self.path = settings.PATH_DB
        self.make_db()


    def make_db(self):
        pass

    
    def write(self, name, instruction, description, runner, path):
        pass


    def delete(self):
        pass
    

    def get(self, command):
        pass


    def check_command(self):
        pass


    def is_int(self, data):
        pass


    def is_double(self, data):
        pass
    
    
    def is_string(self, data):
        pass


    def is_file(self, data):
        pass


    def is_dir(self, data):
        pass