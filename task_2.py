target_word = input("Введите слово для поиска: ").strip()

try:
    with open('text.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    line_numbers = []
    total_count = 0

    for idx, line in enumerate(lines, 1):

        words_in_line = line.split()
        count_in_line = words_in_line.count(target_word)

        if count_in_line > 0:
            line_numbers.append(idx)
            total_count += count_in_line

    found = total_count > 0
    result_str = (
        f"Найдено ли слово: {'Да' if found else 'Нет'}\n"
        f"Сколько раз встречается: {total_count}\n"
        f"Номера строк: {', '.join(map(str, line_numbers)) if found else '-'}\n"
    )

    print(result_str)

    with open('search_results.txt', 'w', encoding='utf-8') as out_file:
        out_file.write(result_str)

except FileNotFoundError:
    print("Ошибка: файл text.txt не найден.")
