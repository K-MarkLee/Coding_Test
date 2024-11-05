def solution(players, callings):
    answer = {player: i for i, player in enumerate(players)}
    for person in callings:
        idx = answer[person]
        answer[person] -= 1
        answer[players[idx-1]] += 1
        players[idx-1], players[idx] = players[idx], players[idx-1] 
    return players
            