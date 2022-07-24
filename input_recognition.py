"""_summary_
    This is input recognition.
    Input recognition has 3 levels: voice, text, and command
    The hiearchy of levels: voice -> text -> command

    Voice input accepts sounds and transforms it to text.

    Text input accepts text and transforms it to command.

    Command input accepts command and checks it.
"""

import os
import settings


def in_text():
    settings.INFO=os.getcwd()
    left_t = settings.NAME+settings.SEPERATOR+settings.INFO+settings.ARROW
    inp = input("{} ".format(left_t))
    return inp


def in_voice():
    pass
