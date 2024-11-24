from deep_translator import GoogleTranslator
from langdetect import detect_langs

lang_dictionary = {
    "English": "en",
    "Ukrainian": "uk",
    "German": "de",
    "French": "fr",
    "Spanish": "es",
    "Chinese": "zh",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko"
}

def transLate(text, lang):
    try:
        # Використовуємо GoogleTranslator з бібліотеки deep_translator для перекладу
        translated_text = GoogleTranslator(source='auto', target=lang).translate(text)
        return translated_text
    except Exception as e:
        print(f"Помилка під час перекладу: {e}")
        return None

def LangDetect(text):
    try:
        # Використовуємо detect_langs з бібліотеки langdetect для визначення мови
        res = detect_langs(text)
        # res повертає список виявлених мов з оцінкою ймовірності
        return res[0].lang, res[0].prob
    except Exception as e:
        print(f"Помилка під час визначення мови: {e}")
        return None, None

def CodeLang(lang):
    if lang.capitalize() in lang_dictionary:
        return lang_dictionary[lang.capitalize()]
    elif lang in lang_dictionary.values():
        for name, code in lang_dictionary.items():
            if code == lang:
                return name
    else:
        raise ValueError("Мова не знайдена в словнику")