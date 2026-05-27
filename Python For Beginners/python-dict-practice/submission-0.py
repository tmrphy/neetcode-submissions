from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    # iterate through word
        # if letter does not exist in dict, add to dict
        # if letter does exist in dict, add to count
    letter_dict = {}
    for char in word:
        if char in letter_dict:
            letter_dict[char] += 1
        else:
            letter_dict[char] = 1
    return letter_dict




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
