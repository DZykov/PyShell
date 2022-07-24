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
import sounddevice as sd


sleep_ = lambda audio: (len(audio) / sample_rate) + 0.5

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


def beautify(data):
    return data


def print_text(data):
    print(beautify(data))


# have to accept cmd_name
def put_voice(data):
    is_cyrillic = regex.search(r'\p{IsCyrillic}', data)
    
    if is_cyrillic is None:
        english_voice(data)
    else:
        russian_voice(data)



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
