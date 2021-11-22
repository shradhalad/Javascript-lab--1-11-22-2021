"""Python functions for JavaScript Trials 1."""

#
def output_all_items(items):
    """Outputs all items in list
    Expected output:
    >>> test_list = [4, 5, 6]
    >>> output_all_items(test_list)
    4
    5
    6
    """
    for item in items:
        print(item)


def get_all_evens(nums):
    """Gets all even numbers in a list and resturn them as a list.
    Expected output:

    >>> evens = get_all_evens(test_list)
    >>> evens
    [4, 6]
    >>> 
    """
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums


def get_odd_indices(items):
    """Returns all odd indices """
    result = []

    for i in range(len(items)):
        if i % 2 != 0:
            result.append(items[i])

    return result


def print_as_numbered_list(items):
    i = 1

    for item in items:
        print(f'{i}. {item}')

        i += 1


def get_range(start, stop):
    nums = []

    for num in range(start, stop):
        nums.append(num)
    
    return nums
    


def censor_vowels(word):
    chars = []

    for letter in word:
        if letter in "aeiou":
            chars.append("*")

        else:
            chars.append(letter)

    return "".join(chars)

            
    


def snake_to_camel(string):
    camel_case = []

    for word in string.split("_"):
        camel_case.append(f"{word[0].upper()}{word[1:]}")
    
    return "".join(camel_case)



def longest_word_length(words):
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)

    return longest


def truncate(string):
    result = []

    for char in string:
        if len(result) == 0 or char != result[-1]:
            result.append(char)

    return "".join(result)
    


def has_balanced_parens(string):
    parens = 0

    for char in string:
        if char == "(":
            parens += 1

        elif char == ")":
            parens -= 1

            if parens < 0:
                return False

    return parens == 0



def compress(string):
    compressed = []

    current_char = ""
    char_count = 0

    for char in string:
        if char != current_char:
            compressed.append(current_char)

            if char_count > 1:
                compressed.append(str(char_count))
            
            current_char = char
            char_count = 0

        char_count += 1

    compressed.append(current_char)
    if (char_count > 1):
        compressed.append(str(char_count))

    return "".join(compressed)