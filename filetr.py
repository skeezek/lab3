from deep_translator import GoogleTranslator
import os

from config import TARGET_LANGUAGE  # type: ignore

def read_file(file_path):
    """Читає вміст файлу за вказаним шляхом."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
        return None

def write_file(file_path, content):
    """Записує вміст у файл за вказаним шляхом."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        print(f"Помилка під час запису у файл: {e}")

def translate_text(text, target_lang):
    """Перекладає текст за допомогою GoogleTranslator."""
    try:
        translated_text = GoogleTranslator(target=target_lang).translate(text)
        return translated_text
    except Exception as e:
        print(f"Помилка під час перекладу: {e}")
        return None

def main():
    # Шляхи до вхідного та вихідного файлів
    input_file_path = os.path.join(os.getcwd(), 'text_to_translate.txt')
    output_file_path = os.path.join(os.getcwd(), 'translated_text.txt')

    # Читання тексту з файлу
    text = read_file(input_file_path)
    if text:
        print(f"Оригінальний текст:\n{text}")

        # Переклад тексту
        translated_text = translate_text(text, TARGET_LANGUAGE)
        if translated_text:
            print(f"\nПерекладений текст:\n{translated_text}")

            # Запис перекладеного тексту у файл
            write_file(output_file_path, translated_text)
            print(f"\nПерекладений текст збережено у {output_file_path}")

if __name__ == "__main__":
    main()