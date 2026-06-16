def caesar_cipher(text, shift):
    result = ""
    for char in text:

        if char.isalpha():
            start = ord('а') if 'а' <= char.lower() <= 'я' else ord('a')
            alphabet_size = 32 if 'а' <= char.lower() <= 'я' else 26

            base = ord('А') if char.isupper() and 'А' <= char <= 'Я' else \
                ord('A') if char.isupper() else start


            result += chr((ord(char) - base + shift) % alphabet_size + base)
        else:
            result += char
    return result


try:
    with open('secret.txt', 'r', encoding='utf-8') as f:
        original_text = f.read()


    encrypted_text = caesar_cipher(original_text, 3)


    with open('encrypted.txt', 'w', encoding='utf-8') as f:
        f.write(encrypted_text)


    with open('encrypted.txt', 'r', encoding='utf-8') as f:
        to_decrypt = f.read()

    decrypted_text = caesar_cipher(to_decrypt, -3)

    with open('decrypted.txt', 'w', encoding='utf-8') as f:
        f.write(decrypted_text)

    print("Обработка завершена!")

except FileNotFoundError:
    print("Ошибка!")
