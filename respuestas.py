import random

def get_response(mesagge: str) -> str:
    # Convertir el mensaje a minúsculas y eliminar los acentos
    user_message = mesagge.lower()

    if user_message == 'hola':
        return 'Hola, ¿en qué puedo ayudarte?'

    if user_message == 'adios':
        return 'Hasta luego'
    
    if user_message in ['¿cómo estás?','¿como estas?', 'como estas', 'como estas?']:
        return '¡Poro! ¡Poro! Estoy bien, gracias por preguntar, ¡Poro!'

    if user_message in ['¿quién eres?','¿quien eres?', 'quien eres', 'quien eres?']:
        return '¡Poro! ¡Poro! Soy un bot de discord de proposito particular del LOL, ¡Poro!'
    
    if contains_any(['recomendación', 'recomendacion', 'recomienda', 'recomiéndame', 'consejo', 'recomendar'], user_message) or (contains('mejorar', user_message)):
        return 'Mi consejo para mejorar en el juego es practicar, aprender de cada derrota y, sobre todo, ¡divertirse en la Grieta del Invocador!'
    
    if contains('tu', user_message) and contains('mascota', user_message) and contains_any(['favorita', 'preferida'], user_message):
        return 'Mi mascota favorita es un Poro hacker para poder espiar estrategias enemigas!'

    # Give me if statemenst to check for messages related to the gaame league of legends
    
    return 'Creo que no te entiendo, ¿podrías repetirlo?'


def contains(word: str, message: str) -> bool:
    return word in message.split()

def contains_any(words: list, message: str) -> bool:
    msj_words = message.split()
    for word in words:
        if word in msj_words:
            return True
    return False
