"""_summary_
    This is output.
    Input recognition has 3 levels: command, text, and voice.
    The hiearchy of levels: command -> text -> voice

    Command output shows the ouput.
    
    Text output accepts command output and transforms it to text.

    Voice output accepts text and transforms it to voice.
"""


import settings
import torch
import sounddevice as sd
import time


sample_rate = 48000
device = torch.device('cpu')
put_accent = True
put_yo = True


model, _= torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language=settings.LANG,
                                     speaker=settings.LANG_MODEL)


model.to(device)


def print_text(data):
    print(data)


def put_voice(data):
    audio = model.apply_tts(text=data,
                        speaker=settings.SPEAKER,
                        sample_rate=sample_rate,
                        put_accent=put_accent,
                        put_yo=put_yo)

    sd.play(audio, sample_rate)
    time.sleep((len(audio) / sample_rate) + 0.5)
    sd.stop()
