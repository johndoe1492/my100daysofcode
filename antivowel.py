'''Define a function called anti_vowel that takes one string, 
text, as input and returns the text with all of the vowels removed.

For example: anti_vowel("Hey You!") should return 
"Hy Y!". Don't count Y as a vowel. Make sure to remove lowercase and uppercase vowels.'''

def anti_vowel(text):
    text = raw_input("Enter text here ")
    vowels = ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u")
    de_voweled = ""
    for a in text:
        if a in vowels:
            

anti_vowel("big")




n = ["Michael", "Lieberman"]

def join_strings(words):
  result = ""
  for n in words:
    result.append(n)
    return result


print join_strings(n)
