import json
import string


def distance(word_1: str, word_2: str):
    table = [[0 for i in range(len(word_1))] for j in range(len(word_2))]

    table[0][0] = 0

    for i in range(1, len(word_1)):
        table[0][i] = table[0][i - 1] + (0 if word_2[0] == word_1[i] else 1)

    for i in range(1, len(word_2)):
        table[i][0] = table[i - 1][0] + (0 if word_2[i] == word_1[0] else 1)

    for i in range(1, len(word_2)):
        for j in range(1, len(word_1)):

            cost = 0 if word_1[j] == word_2[i] else 1
            table[i][j] = min(
                table[i - 1][j - 1] + cost,
                table[i - 1][j] + cost,
                table[i][j - 1] + cost,
            )

    return table[len(word_2) - 1][len(word_1) - 1]


def clear_text(text: str) -> str:
    translation_table = str.maketrans(
        dict.fromkeys(",.:;-!?|" + string.digits)
    )
    return (
        text.translate(translation_table)
        .replace("\n", " ")
        .replace("\r", " ")
        .replace("\t", " ")
        .replace("  ", " ")
        .strip()
        .lower()
    )


def main():
    path_to_json = "./1019641987_02__1_res.json"
    path_to_vocabulary = "./russian.txt"

    all_words = []
    with open(path_to_vocabulary, "r") as vocab_file:
        all_words = [line.strip() for line in vocab_file.readlines()]

    with open(path_to_json, "r") as scan_data_file:
        scan_data_json = json.load(scan_data_file)

    scanned_text_clear = clear_text(scan_data_json["data"]["text"])
    scanned_words = scanned_text_clear.split(" ")

    converted_text = ""
    for word in scanned_words:
        if word in all_words:
            print(f'Слово "{word}" найдено в словаре')
            converted_text = " ".join([converted_text, word])
        else:
            min_dist = len(word)
            min_dist_word = ""

            for chk_word in all_words:
                chk_distance = distance(word, chk_word)

                if chk_distance < min_dist:
                    min_dist = chk_distance
                    min_dist_word = chk_word

                if min_dist == 0:
                    break

            print(
                f'Слово "{word}" было заменено на слово "{min_dist_word}". Расстояние Левенштейна - {min_dist}'
            )
            converted_text = " ".join([converted_text, min_dist_word])

    print("\n\n\nРеузльтат преобразования текста\n:")
    print(converted_text)


if __name__ == "__main__":
    main()
