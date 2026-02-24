def solution(picture, k):
    for i in range(len(picture)):
        picture[i] = "".join([x for x in picture[i] for _ in range(k)])
    return [i for i in picture for _ in range(k)]
