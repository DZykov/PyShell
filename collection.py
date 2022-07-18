"""_summary_
    This is collection of the commands. 
    This is just a collection: collection is linkage between commands and a shell.
    Collection is made of database and codebase.
    Database:
        __________________________________________________
        |Command name|Instruction|Description|Runner|Path|
        |____________|___________|___________|______|____|
    
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
        
        *none = -

        Example of database:
            ______________________________________________________________________________
            |Command name| Alias |        Instruction          |Description|Runner| Path |
            |------------|-------|-----------------------------|-----------|------|------|
            |   test_1   |   1   |    s [int] [str] [int]      |  descr_1  |  -   |path_1|
            |------------|-------|-----------------------------|-----------|------|------|
            |   test_2   |   2   |c [-n|int] [-s|str] [-nc|int]|  descr_2  |  -   |path_2|
            |----------------------------------------------------------------------------|

"""
import settings

class Collection:


    def __init__(self):
        self.cmds = {}
        self.src = settings.PATH_SRC
        self.load_src()


    def load_src(self):
        lines = []
        with open(self.src) as f:
            lines = f.readlines()
        for line in lines:
            line = line.strip('\n')
            cmd_lst = line.split(settings.SRC_SEPERATOR)
            # alias = [cmd_name, instruction, runner, path, description]
            #self.cmds[cmd_lst[1]] = [cmd_lst[0], cmd_lst[2], cmd_lst[4], cmd_lst[5], cmd_lst[3]]
            alias = cmd_lst[1]
            cmd_name = cmd_lst[0]
            instruction = cmd_lst[2].split(settings.ARG_SEPERATOR)
            if settings.ARG_PREFIX in instruction[0]:
                inst_dict = {}
                for inst in instruction:
                    inst = inst.split()
                    inst_dict[inst[0]] = inst[1]
                instruction = inst_dict
            runner = cmd_lst[4]
            path = cmd_lst[5]
            description = cmd_lst[3]
            self.cmds[alias] = {"instruction": instruction, "name": cmd_name, "runner": runner,
                                    "path": path, "description": description}
    

    def get(self, alias):
        """return string of alias or None"""
        return self.cmds.get(alias)
    
    
    def check_type(self, arg, type_):
        if "int" == type_:
            return self.is_int(arg)
        elif "str" == type_:
            return self.is_string(arg)
        elif "double" == type_:
            return self.is_double(arg)
        elif "pathd" == type_:
            return self.is_dir(arg)
        elif "pathf" == type_:
            return self.is_file(arg)
        else:
            return settings.WRONG_ARGS

    
    def check_classical_cmd(self, data, instruction):
        args = {}
        i = 0
        key = 0
        while i < len(data):
            if settings.ARG_PREFIX in data[i]:
                args[data[i]] = []
                key = i
            else:
                args[data[key]].append(data[i])
            i += 1
        for key in args:
            for element in args[key]:
                return check_type(element, instruction[key])
        return settings.WRONG_ARGS

    
    def check_sctrict_cmd(self, data, instruction):
        pass


    def check_command(self, data, check):
        """return true if command is correct"""
        if check == False:
            return settings.GOOD_ARGS
        cmd = data.split()
        alias = cmd[0]
        got_cmd = self.cmds.get(alias)
        if got_cmd == None:
            return settings.CMD_DNE
        if settings.ARG_PREFIX in data and isinstance(got_cmd, dict):
            return self.check_classical_cmd(cmd[1:], got_cmd['instruction'])
        if settings.ARG_PREFIX not in data and isinstance(got_cmd, list):
            return self.check_sctrict_cmd(cmd[1:], got_cmd['instruction'])
        if got_cmd['instruction'] == "-":
            return settings.NEUTRAL_ARGS
        return settings.WRONG_ARGS
    

    def check_arg(arg):
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

col = Collection()
c = col.check_command("t2 -n 25 -y -s mother -nc 85", True)
print(c)