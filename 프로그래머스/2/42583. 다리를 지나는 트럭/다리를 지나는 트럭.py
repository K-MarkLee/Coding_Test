def solution(bridge_length, weight, truck_weights):
    bridge = [0]*bridge_length
    time = 0
    current_weight = 0
    
    while truck_weights:
        time += 1
        out = bridge.pop(0)
        current_weight -= out
        
        if current_weight + truck_weights[0] <= weight:
            new = truck_weights.pop(0)
            bridge.append(new)
            current_weight += new
        else:
            bridge.append(0)
            
    return time + bridge_length