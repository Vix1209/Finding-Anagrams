# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = input('word: ')
    anagram = input('anagram: ')
    word_sorted = sorted(word)
    anagram_sorted = sorted(anagram)
    if word_sorted == anagram_sorted:
        return True
    else: 
        return False


result = find_anagram('word','anagram')
print (result)

