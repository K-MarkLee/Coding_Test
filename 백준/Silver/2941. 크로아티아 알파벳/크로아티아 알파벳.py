import sys
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = sys.stdin.readline().strip()

for pattern in croatia:
    word = word.replace(pattern,"m")
    
print(len(word))