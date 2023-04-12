# This Kata is intended as a small challenge for my students
#
# Create a function, called removeVowels
# (or remove_vowels), that takes a string argument and returns that same string with all
#     vowels removed (vowels are "a", "e", "i", "o", "u").






def remove_vowels(strng):
    vowels_lst = ["a", "e", "i", "o", "u"]
    new_str = ""
    for i in strng:
        if i not in vowels_lst:
            new_str += i
    print(new_str)
    return new_str






remove_vowels("drake")          #"drk"
remove_vowels("aeiou")          #""

