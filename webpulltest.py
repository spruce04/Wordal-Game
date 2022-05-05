from os import listdir
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "https://github.com/spruce04/Wordal-Game/blob/main/5LetterWords.txt"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")
for script in soup(["script", "style"]):
    script.extract()    
text = soup.get_text()
lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
text = str('\n'.join(chunk for chunk in chunks if chunk))
listtext = text.split()
print(listtext)
snipend = int(listtext.index('Copy'))
listtext = listtext[:snipend]    
print(listtext)
snipfront = listtext.index('aback')
prefix = listtext[snipfront:]
print(listtext)
for line in listtext :
    if len(line) != 5 :
        print('failed',line)
