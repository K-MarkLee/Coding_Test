import sys
word = sys.stdin.readline().strip()
result = 1
for i in range(len(word)//2):
    if word[i] != word[-(i+1)]:
        result = 0
        break  
print(result)