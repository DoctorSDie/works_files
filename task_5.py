
with open('words.txt', 'r', encoding='utf-8') as f:

    words = [line.strip() for line in f if line.strip()]

alpha_sorted = sorted(words)


length_sorted = sorted(words, key=len)


reverse_sorted = sorted(words, reverse=True)


def save_to_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(data))

save_to_file('sorted_alphabetically.txt', alpha_sorted)
save_to_file('sorted_by_length.txt', length_sorted)
save_to_file('sorted_reverse.txt', reverse_sorted)

print("Файлы созданы!")