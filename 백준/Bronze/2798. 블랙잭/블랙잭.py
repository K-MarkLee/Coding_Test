import sys

def newblackjack(n,m,cards):
    final = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                total = cards[i]+cards[j]+cards[k]
                if total == m:
                    return m
                elif total < m and total > final:
                    final = total
    return final
                
n,m,*cards = map(int,sys.stdin.read().strip().split())

print(newblackjack(n,m,cards))