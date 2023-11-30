def count_vowels(input_line):
    vowels = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}

    input_line_lower = input_line.lower()
    vowels_in_line = set(input_line_lower) & vowels

    return len(vowels_in_line)

if __name__ == '__main__':
    user_input = input("Введите предложение: ")
    vowels_count = count_vowels(user_input)

    print(f"Количество гласных в строке: {vowels_count}")
