from googletrans import Translator  # type: ignore

translator = Translator(service_urls=['translate.googleapis.com'])

from googletrans import Translator  # type: ignore

def transLate(text: str, scr: str, dest: str) -> str:
    """Перекладає текст на задану мову за допомогою Google Translate."""
    translator = Translator(service_urls=['translate.googleapis.com'])
    try:
        # Переклад тексту
        print(f"Переклад з мови {scr} на мову {dest}: {text}")
        res = translator.translate(text, src=scr, dest=dest)
        return res.text
    except Exception as e:
        print(f"Помилка під час перекладу: {e}")
        return "Error in translation"

def LangDetect(text: str, set: str = "all") -> str:
    """Визначає мову та коефіцієнт довіри для тексту."""
    translator = Translator(service_urls=['translate.googleapis.com'])
    try:
        # Визначення мови
        detection = translator.detect(text)
        if set == "lang":
            return detection.lang
        elif set == "confidence":
            return detection.confidence
        else:
            return detection.lang, detection.confidence
    except Exception as e:
        print(f"Помилка під час визначення мови: {e}")
        return None, None

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

def CodeLang(lang):
    """Перетворює назву мови на її код або навпаки."""
    if lang.capitalize() in lang_dictionary:
        return lang_dictionary[lang.capitalize()]
    elif lang in lang_dictionary.values():
        for name, code in lang_dictionary.items():
            if code == lang:
                return name
    else:
        raise ValueError("Мова не знайдена в словнику")