
with open('obituary.txt', 'rb') as f:
        obituary = f.read()

obituary = obituary.decode('UTF-16')

obituary_words = obituary.split()
import string
obituary_words = [word.strip(string.punctuation) for word in obituary_words]
print("Word count")
print(len(obituary_words))
counter = 0
for character in obituary:
    if character in '!.?':
        counter+=1
print("Sentence count:", counter)
non_ascii = set()
import curses.ascii
for character in obituary:
    if not curses.ascii.isascii(character):
        non_ascii.add(character)
print(non_ascii)
replacements = {'”': '"', 'é': 'e', '’': "'", '“': '"', 'è': 'e', '–': '-'}

def replace_character(character, lookup):
    if character in lookup:
        return lookup[character]
    else:
        return character

ascii_obituary = "".join([replace_character(character, replacements) for character in obituary])
ascii_bytes = ascii_obituary.encode('ascii')

counter = 0
for word in obituary_words:
    if word[0] == word[0].upper() and not word[0] in string.digits:
        counter+=1

print("Words beginning with uppercase:", counter)
import statistics
print("Most common word is: ", statistics.mode(obituary_words))
print("The longest word is:", max(obituary_words, key=len))
