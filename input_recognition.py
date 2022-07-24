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


model_ru = vosk.Model("model_small_ru")
model_en = vosk.Model("model_small_en")
model = model_en
samplerate = 16000
# print(sd.query_devices())
device = 18 # device has to be specified

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
    if settings.IN_LANG == "en":
        model = model_en
    elif settings.IN_LANG == "ru":
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
    if settings.A_NAME in data:
        left_t = settings.NAME+settings.SEPERATOR+settings.INFO+settings.ARROW
        print(left_t, end="")
        data = data.replace("settings.A_NAME", "")

        # transform to commands with NLTK
        print(data)
        return data
    return 1