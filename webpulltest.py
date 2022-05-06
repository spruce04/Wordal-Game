import urllib.request

try:
   with urllib.request.urlopen('https://raw.githubusercontent.com/spruce04/Wordal-Game/main/5LetterWords.txt') as f:
    Wopen = f.read().decode('utf-8').split()
except urllib.error.URLError as e:
   print(e.reason)

WordBase = list()
for word in Wopen:
    word1 = word.upper().split()
    WordBase = WordBase + word1
print(WordBase)

