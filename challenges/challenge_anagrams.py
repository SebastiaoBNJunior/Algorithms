def merged(word, start=0, end=None):
    if end is None:
        end = len(word)
    if end - start > 1:
        mid = (start + end) // 2
        merged(word, start, mid)
        merged(word, mid, end)
        merge(word, start, mid, end)
    return word


def merge(word, start, mid, end):
    left = word[start:mid]
    right = word[mid:end]
    left_index, right_index = 0, 0
    index_geral = start

    while left_index < len(left):
        if right_index == len(right) or (
            left_index < len(left) and left[left_index] <= right[right_index]
        ):
            word[index_geral] = left[left_index]
            left_index += 1
        else:
            word[index_geral] = right[right_index]
            right_index += 1
        index_geral += 1
    return word


def is_anagram(first_string, second_string):
    first_string_orded = "".join(merged(list(first_string.lower())))
    second_string_orded = "".join(merged(list(second_string.lower())))

    if first_string == "" or second_string == "":

        return (first_string_orded, second_string_orded, False)
    elif first_string_orded == second_string_orded:

        return (first_string_orded, second_string_orded, True)
    else:

        return (first_string_orded, second_string_orded, False)


print(is_anagram("pedra", "teste"))
