def solution(rank, attendance):
    a,b,c = sorted([i for i,j in enumerate(attendance) if j], key = lambda i : rank[i])[:3]
    return 10000 * a + 100 * b + c
            