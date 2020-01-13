'''
# 문제 설명
트럭 여러 대가 강을 가로지르는 일 차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 
트럭은 1초에 1만큼 움직이며, 다리 길이는 bridge_length이고 다리는 무게 weight까지 견딥니다.
※ 트럭이 다리에 완전히 오르지 않은 경우, 이 트럭의 무게는 고려하지 않습니다.
예를 들어, 길이가 2이고 10kg 무게를 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 최소 8초가 걸립니다.
solution 함수의 매개변수로 다리 길이 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭별 무게 truck_weights가 주어집니다.
이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

# 제한 조건
1. bridge_length는 1 이상 10,000 이하입니다.
2. weight는 1 이상 10,000 이하입니다.
3. truck_weights의 길이는 1 이상 10,000 이하입니다.
4. 모든 트럭의 무게는 1 이상 weight 이하입니다.
'''


def solution(b_len, b_weight, truck_weight):   
    answer = b_len
    bridge = []
    
    while truck_weight:
        if sum(bridge) + truck_weight[0] <= b_weight:
            bridge.append(truck_weight.pop(0))
            if len(bridge) == b_len:
                bridge.pop(0)
                
        else:
            bridge.append(0)
            if len(bridge) == b_len:
                bridge.pop(0)
            
        answer += 1
        
    return answer
    

solution(2, 10, [7,4,5,6])
# 8

solution(100, 100, [10])
# 101

solution(100, 100, [10,10,10,10,10,10,10,10,10,10])
# 110
    
    
