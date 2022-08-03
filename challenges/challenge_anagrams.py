def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    first_list = list(first_string.lower())
    second_list = list(second_string.lower())
    for letter in first_list:
        try:
            second_list.remove(letter)
        except ValueError:
            return False
    return True
