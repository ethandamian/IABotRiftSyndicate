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

    # Give me if statemenst to check for messages related to the gaame league of legends
    
    return 'Creo que no te entiendo, ¿podrías repetirlo?'