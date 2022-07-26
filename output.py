"""_summary_
    This is output.
    Input recognition has 3 levels: command, text, and voice.
    The hiearchy of levels: command -> text -> voice

    Command output shows the ouput.
    
    Text output accepts command output and transforms it to text.

    Voice output accepts text and transforms it to voice.
"""


import settings
import regex
import torch
import time
from history import History
import config
import sounddevice as sd


sleep_ = lambda audio: (len(audio) / sample_rate) + 0.5

history = History()

sample_rate = 48000
device = torch.device('cpu')
put_accent = True
put_yo = True


model_ru, _= torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language=settings.LANG_RU,
                                     speaker=settings.LANG_MODEL_RU)

model_en, _= torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language=settings.LANG_EN,
                                     speaker=settings.LANG_MODEL_EN)


model_ru.to(device)
model_en.to(device)


def beautifyT(data):
    # TODO: add some colours or style to text.
    return data


def beautifyV(data):
    # TODO: add some human touch to the output
    cmd = history.get_last()
    if cmd in config.CMD_INGORE:
        data = ""
    elif cmd in config.CMD_OUT:
        data = config.CMD_OUT[cmd][settings.IN_LANG]
    return data



def print_text(data):
    print(beautifyT(data))


def put_voice(data):
    is_cyrillic = regex.search(r'\p{IsCyrillic}', data)
    
    txt = beautifyV(data)
    if txt == "":
        return
    if is_cyrillic is None:
        english_voice(txt)
    else:
        russian_voice(txt)



def russian_voice(data):
    audio = model_ru.apply_tts(text=data,
                            speaker=settings.SPEAKER_RU,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)
    sd.play(audio, sample_rate)
    time.sleep(sleep_(audio))
    sd.stop()


def english_voice(data):
    audio = model_en.apply_tts(text=data,
                            speaker=settings.SPEAKER_EN,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)
    sd.play(audio, sample_rate)
    time.sleep(sleep_(audio))
    sd.stop()
