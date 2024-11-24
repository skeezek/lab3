from mod2 import transLate, LangDetect, CodeLang

def main():
    # Словник мов
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
            texttransl = input("Введіть текст для перекладу: ").strip()

            # Виведення доступних мов
            print("Доступні мови:")
            for lang, code in lang_dictionary.items():
                print(f"{lang}: {code}")

            # Вибір мови для перекладу (назва або код)
            chooselg = input("Введіть мову, на яку хочете перекласти (назва або код): ").strip().capitalize()

            # Перевірка введеної мови та її перетворення
            if chooselg in lang_dictionary:
                chooselg = CodeLang(chooselg)  # Якщо введено назву мови
            elif chooselg not in lang_dictionary.values():
                raise ValueError("Невірний код мови або назва. Спробуйте ще раз.")

            break  # Вихід з циклу, коли вибір валідний

        except ValueError as ve:
            print(ve)

    # Виконання перекладу
    translated_text = transLate(texttransl, chooselg)
    if translated_text:
        print(f"Перекладений текст: {translated_text}")

    # Визначення мови оригінального тексту за допомогою langdetect
    detected_lang, confidence = LangDetect(texttransl)
    if detected_lang:
        print(f"Визначена мова: {detected_lang} з довірою: {confidence}")
    else:
        print("Не вдалося визначити мову.")

    # Виведення повного імені або коду мови
    print(f"Повне ім'я або код: {CodeLang(chooselg)}")

if __name__ == "__main__":
    main()