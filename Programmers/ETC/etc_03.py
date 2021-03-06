'''
# 문제 설명
직사각형 종이를 n번 접으려고 합니다. 이때, 항상 오른쪽 절반을 왼쪽으로 접어 나갑니다.
종이를 모두 접은 후에는 종이를 전부 펼칩니다. 종이를 펼칠 때는 종이를 접은 방법의 역순으로 펼쳐서 처음 놓여있던 때와 같은 상태가 되도록 합니다. 
위와 같이 두 번 접은 후 종이를 펼치면 종이에 접은 흔적이 생기게 됩니다.
종이를 접은 횟수 n이 매개변수로 주어질 때, 종이를 절반씩 n번 접은 후 모두 펼쳤을 때 생기는 접힌 부분의 모양을 배열에 담아 return 하도록 solution 함수를 완성해주세요.

# 제한사항
1. 종이를 접는 횟수 n은 1 이상 20 이하의 자연수입니다.
2. 종이를 접었다 편 후 생긴 굴곡이 ∨ 모양이면 0, ∧ 모양이면 1로 나타냅니다.
3. 가장 왼쪽의 굴곡 모양부터 순서대로 배열에 담아 return 해주세요.
'''


# 시간 초과 (insert 때문에)
# def solution(n):
#     answer = [0]
#     fold = [0, 1]
    
#     for f in range(2, n+1):
#         for i in range(0, 2**(f-1)):
#             answer.insert(i*2, fold[i%2])
        
#     return answer


# 통과
def solution(n):
    def length(n):
        if n == 1:
            return 1
        return length(n - 1) * 2 + 1

    _len = length(n)
    mid = _len
    
    answer = [0] * _len
    
    while mid:
        mid //= 2
        for i, f in enumerate(range(mid, _len, (mid + 1) * 2)):
            answer[f] = [0, 1][i % 2]
        
    return answer


solution(1)
# [0]

solution(1)
# [0, 0, 1]

solution(1)
# [0, 0, 1, 0, 0, 1, 1]
