import sys
n = int(sys.stdin.readline().strip())

for _ in range(n):
    word = sys.stdin.readline().strip()
    already = []
    last = ''
    
    for char in word:
        if char != last:
            if char in already:
                n -= 1
                break
            already.append(char)
        last = char

print(n)