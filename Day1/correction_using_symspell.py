import datetime
import re
import pkg_resources
import json

from symspellpy import SymSpell, Verbosity

path_to_jsons = "./source/"
path_to_result = "./converted/"
path_to_dictionary = "russian.txt"

def clear_text(text: str) -> str:
    return text.replace("\n", " ").replace("\r", " ").replace("\t", " ").strip()

def process_file(symspell: SymSpell, filename):
    with open(filename, "r") as scan_data_file:
        scan_data_json = json.load(scan_data_file)

    scanned_text = clear_text(scan_data_json["data"]["text"])
    
    scanned_words = scanned_text.split(" ")
    converted_text = ""

    for word in scanned_words:
        prefix = ""
        suffix = ""
        core = word

        while core and not core[0].isalpha():
            prefix += core[0]
            core = core[1:]
        while core and not core[-1].isalpha():
            suffix = core[-1] + suffix
            core = core[:-1]

        clear_word = core.lower()
        if clear_word:
            suggestions = symspell.lookup(clear_word, Verbosity.CLOSEST, max_edit_distance=2)
            if suggestions:
                best_suggestion = suggestions[0].term

                if core.istitle():
                    best_suggestion = best_suggestion.capitalize()
                elif core.isupper():
                    best_suggestion = best_suggestion.upper()
                    
                print(f'Слово "{word}" исправлено на "{best_suggestion}"')
                converted_text += f"{prefix}{best_suggestion}{suffix} "
            else:
                print(f'Слово "{word}" не найдено в словаре')
                converted_text += f"{word} "
        else:
            converted_text += f"{word} "

    file_id = re.search(r"(\d+_\d+__\d+)", filename).group(1)
    result_filename = f"{path_to_result}{file_id}_converted.json"

    result = {}
    result["file_id"] = file_id
    result["result"] = converted_text.strip()

    with open(result_filename, "w", encoding="utf-8") as result_file:
        json.dump(result, result_file, ensure_ascii=False, indent=4)
    print(f"Результат сохранен в {result_filename}")

def main():
    sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=5)

    start_loading = datetime.datetime.now()
    with open(path_to_dictionary, "r", encoding="utf-8") as dict_file:
        if not sym_spell.create_dictionary(dict_file):
            raise Exception(f"Не удалось загрузить словарь из {path_to_dictionary}")
    print(f"Словарь загружен из {path_to_dictionary}. Время загрузки: {datetime.datetime.now() - start_loading}")

    for filename in pkg_resources.resource_listdir(__name__, path_to_jsons):
        full_path = f"{path_to_jsons}{filename}"
        print(f"\n\n\nОбработка файла {full_path}")
        process_file(sym_spell, full_path)

if __name__ == "__main__":
    main()