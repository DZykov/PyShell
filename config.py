import settings

NAME_ALIAS = (settings.A_NAME, "theta", "nabla", "си си", "карина")

TBR_ALIAS = ('скажи', 'покажи', 'ответь', 'произнеси', 'расскажи', 'сколько', 'show', 'how', 'what', 'whats', 'what\'s')

INTERJECTIONS = ('is', 'are', 'это') # not the right term

# commands are either from collection, built-in or cli/shell apps
CMD_LIST = {
    "mocp -S | mocp --append /home/demid/Music/Rock | mocp --play": ('play music', 'music please', 'поставь музыку', 'сыграй что-нибудь'),
    "mocp --exit": ('stop', 'enough', 'стоп', 'хватит'),
    "mocp --next": ('next', 'следующий'),
    "mocp --pause": ('pause', 'пауза',),
    "mocp --unpause": ('unpause', 'continue','продолжай'),
    "mocp --previous": ('previous', 'прошлый'),
    "help": ('help', 'помогите'),
    "save_mode t": ('safe mode on', 'включи безопасный режим'),
    "save_mode f": ('safe mode off', 'выключи безопасный режим'),
    "output_mode text": ('change to text', 'смени на текст'),
    "output_mode voice": ('talk to me', 'поговори со мной'),
    "input_mode text": ('change to keyboard', 'смени на клавиатуру'),
    "input_mode voice": ('change to voice','смени на голос'),
    "change_lang en": ('english', 'англиский'),
    "change_lang ru":('russian', 'русский'),
    "exit": ('exit', 'выход'),
}

CMD_OUT = {
    "mocp --play": {
                    "en": ('I am strating to sing'),
                    "ru": ('Начинаю петь')
                    },
}

CMD_INGORE = ["mocp --append /home/demid/Music/Rock", "mocp -S"]