def solution(myString, pat):
    pl = list(pat)
    for i in range(len(pat)):
        if pat[i] == "A":
            pl[i] = "B"
        else:
            pl[i] = "A"
    return (1 if "".join(pl) in myString else 0)