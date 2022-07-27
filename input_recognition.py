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
import vosk
import sys
import queue
import sounddevice as sd
import json
import config
from fuzzywuzzy import fuzz


model_ru = vosk.Model("model_small_ru")
model_en = vosk.Model("model_small_en")
model = model_en
samplerate = 16000
# print(sd.query_devices())
device = settings.DEVICE # device has to be specified

q = queue.Queue()


def in_text():
    settings.INFO=os.getcwd()
    left_t = settings.NAME+settings.SEPERATOR+settings.INFO+settings.ARROW
    inp = input("{} ".format(left_t))
    return inp


def callback_(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


def in_voice():
    if settings.IN_LANG == settings.LANG_EN:
        model = model_en
    elif settings.IN_LANG == settings.LANG_RU:
        model = model_ru
    else:
        model = model_en
    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device, dtype='int16',
                           channels=1, callback=callback_):
        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                return beautify(json.loads(rec.Result())["text"])


def beautify(data):
    if settings.DEBUG:
        print('--------------------------')
        print(data)
    if data.startswith(config.NAME_ALIAS):
        cmd = find_weighted_cmd(filter(data))
        left_t = settings.NAME+settings.SEPERATOR+settings.INFO+settings.ARROW+" "
        print(left_t, end="")
        print(cmd)
        return cmd
    return 1


def filter(data):
    cmd = data
    for word in config.NAME_ALIAS:
        cmd = cmd.replace(word, '').strip()
    for word in config.TBR_ALIAS:
        cmd = cmd.replace(word, '').strip()
    for word in config.INTERJECTIONS:
        cmd = cmd.replace(word, '').strip()
    return cmd


def find_weighted_cmd(data):
    cmd = {'command': 'None', 'weight': 0}
    for command, aliases in config.CMD_LIST.items():
        for alias in aliases:
            weight = fuzz.ratio(data, alias)
            if weight > cmd['weight']:
                cmd['command'] = command
                cmd['weight'] = weight
    cmd1 = {'command': '', 'weight': 0}
    txt = data
    if len(data.split()) > 1:
        txt = data.split()[0]
    for command, aliases in config.CMD_LIST.items():
        for alias in aliases:
            weight = fuzz.ratio(txt, alias)
            if weight > cmd1['weight']:
                cmd1['command'] = command
                cmd1['weight'] = weight
    if cmd1['weight'] > cmd['weight']:
        cmd['command'] = cmd1['command'] 
        cmd['weight'] = cmd1['weight']
    if settings.DEBUG:
        print(cmd)
    if cmd['command'] in config.CMD_INPUT:
        n_data = data.split()
        n_data[0] = cmd['command']
        data = ' '.join(n_data)
        return data
    return cmd['command']