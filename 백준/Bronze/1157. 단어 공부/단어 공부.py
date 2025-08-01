import sys
word = sys.stdin.readline().strip()
word = word.upper()

set_word = set(word)

count = 0
result = ""

for char in set_word:
    num = word.count(char)
    if num > count:
        count = num
        result = char
    elif num == count:
        result = "?"
        
print(result)