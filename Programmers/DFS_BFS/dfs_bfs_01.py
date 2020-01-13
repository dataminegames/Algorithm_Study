'''
# 문제 설명
n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때
숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
1. 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
2. 각 숫자는 1 이상 50 이하인 자연수입니다.
3. 타겟 넘버는 1 이상 1000 이하인 자연수입니다.
'''


import copy

answer = 0
def solution(numbers, target):
    def dfs(num, curr):
        global answer
        if not num:
            if curr == target:
                answer += 1
            return
        
        else:
            nxt = num.pop(0)
            dfs(copy.deepcopy(num), curr - nxt)
            dfs(copy.deepcopy(num), curr + nxt)
    
    dfs(numbers, 0)
    return answer
    

solution([1, 1, 1, 1, 1], 3)
# 5
