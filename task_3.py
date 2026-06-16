filenames = ['file1.txt', 'file2.txt', 'file3.txt']
output_filename = 'combined.txt'

with open(output_filename, 'w', encoding='utf-8') as outfile:
    for fname in filenames:

        outfile.write(f"--- Содержимое {fname} ---\n")

        try:
            with open(fname, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
        except FileNotFoundError:
            outfile.write("[Файл не найден]")

        outfile.write("\n\n")

print(f"Файлы объединены в {output_filename}")
