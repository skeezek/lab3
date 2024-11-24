import translators as ts  # type: ignore
from googletrans import Translator  # type: ignore

from mod1 import transLate, LangDetect, CodeLang

translator = Translator(service_urls=['translate.googleapis.com'])

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

while True:
    try:
        # Введення тексту для перекладу
        texttransl = input("Введіть текст для перекладу: ").lower().strip()

        # Виведення доступних мов
        for lang, code in lang_dictionary.items():
            print(f"{lang}: {code}")

        # Вибір мови перекладу
        chooselg = input("Введіть мову для перекладу (назва або код): ").strip().capitalize()

        # Перевірка, чи вибір є валідним
        if chooselg in lang_dictionary:
            chooselg = CodeLang(chooselg)
            break
        elif chooselg in lang_dictionary.values():
            break
        else:
            raise ValueError("Невірний код мови. Спробуйте ще раз.")

    except ValueError as ve:
        print(ve)

# Виконання перекладу
translated_text = transLate(texttransl, "auto", chooselg)
print(f"Перекладений текст: {translated_text}")

# Визначення мови оригінального тексту
detected_lang, confidence = LangDetect(texttransl)
print(f"Виявлена мова: {detected_lang} з достовірністю: {confidence}")

# Виведення повної назви або коду мови
print("Повне ім'я або код: ", CodeLang(chooselg))