import settings

NAME_ALIAS = (settings.A_NAME, "theta", "nabla", "си си", "карина")

TBR_ALIAS = ('скажи', 'покажи', 'ответь', 'произнеси', 'расскажи', 'сколько', 'show', 'how', 'what', 'whats', 'what\'s')

INTERJECTIONS = ('is', 'are', 'это') # not the right term

# commands are either from collection, built-in or cli/shell apps
CMD_LIST = {
    "mocp -S | mocp --append /home/demid/Music/Rock | mocp --play": ('play music', 'music please', 'поставь музыку', 'сыграй что-нибудь'),
    "mocp --exit": ('stop', 'enough', 'стоп', 'хватит'),
    "mocp --next": ('next'),
    "mocp --pause": ('pause', 'пауза',),
    "mocp --unpause": ('unpause', 'continue','продолжай'),
    "mocp --previous": ('previous', 'прошлый'),
    "exit": ('exit', 'выход'),
}
