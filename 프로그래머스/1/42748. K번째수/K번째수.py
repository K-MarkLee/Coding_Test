def solution(array, commands):
    result = []
    for command in commands:
        new_array = array[command[0]-1:command[1]]
        new_array.sort()
        result.append(new_array[command[2]-1])
    return result