def find_common_characters(line1, line2):
    # Convert input lines to sets of characters
    set1 = set(line1)
    set2 = set(line2)

    # Find common characters using set intersection
    common_characters = set1.intersection(set2)

    return common_characters

if __name__ == '__main__':
    # Input lines from the user
    line1 = input("Введите первую строку: ")
    line2 = input("Введите вторую строку: ")

    # Find common characters
    common_chars = find_common_characters(line1, line2)

    if common_chars:
        print(f"Common characters: {', '.join(common_chars)}")
    else:
        print("No common characters.")
