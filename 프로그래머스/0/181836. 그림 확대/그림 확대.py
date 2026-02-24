def solution(picture, k):
    return [
        "".join(i * k for i in j)
        for j in picture
        for _ in range(k)
    ]