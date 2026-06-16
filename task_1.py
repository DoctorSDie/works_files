try:
    with open('input.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)

    with open('statistics.txt', 'w', encoding='utf-8') as f_out:
        f_out.write (f"Количество строк: {line_count}\n")
        f_out.write (f"Количество слов: {word_count}\n")

except FileNotFoundError:
    print ("файл не найден!")