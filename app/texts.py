def WELCOME_TEXT(user_name): 
    text = f"Привет, <strong>{user_name}</strong>, это бот для <strong>перевода речи в текст!</strong>\nЧтобы попробовать, выберите метод перевода речи в текст и отправьте <strong>голосовое сообщение</strong> или <strong>аудио файл</strong>"
    return text

def MAIN_TEXT(user_name): 
    text = f"<strong>{user_name}</strong>, выберите метод перевода речи в текст."
    return text

def SEND_AUDIO_OR_VOICE(user_name): 
    text = f"<strong>{user_name}</strong>, отправьте <strong>голосовое сообщение</strong> или <strong>аудио файл</strong>"
    return text

SPEECH_RECOGNITION = "Cинтезировано с помощью <strong>SpeechRecognition</strong>:"
SPEECH_FLOW = "Cинтезировано с помощью <strong>SpeechFlow</strong>:"

INFO_TEXT = "Speech Recognition обрабатывает файлы/гс длительностью не более 1 минуты и весом до 10 Мб.\n\nSpeechFlow обрабатывает не более 5 часов в месяц."

UNKNOWN_TEXT = "Не удалось распознать текст."