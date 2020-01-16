'''
We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape. These shapes may be rotated.

  XX  <- domino
  
  XX  <- "L" tromino
  X
  
Given N, how many ways are there to tile a 2 x N board? Return your answer modulo 10^9 + 7.
(In a tiling, every square must be covered by a tile.
Two tilings are different if and only if there are two 4-directionally adjacent cells on the board
such that exactly one of the tilings has both squares occupied by a tile.)

# Note:
- N  will be in range [1, 1000].
'''


# 점화식 : P(N) = 2 * summation(P(1~(N-3))) + P(N-2) + P(N-1) + 2
# 예) N = 6
    # ■■■■■■ --> ■■■■■■ 1*2
    # □■■■■■ --> □ P(1)  *  ■■■■■ 1*2
    # □□■■■■ --> □□ P(2)  *  ■■■■ 1*2
    # □□□■■■ --> □□□ P(3)  *  ■■■ 1*2
    # □□□□■■ --> □□□□ P(N-2)  *  ■■ 1
    # □□□□□■ --> □□□□□ P(N-1)  *  ■ 1


# □ : 이전에 구했던 경우의 수(□가 하나 더해져도 경우의 수는 동일)

# ■ : 쪼개지지 않는 새로운 타일 조합 (경우의 수 : 1*2)
    # ■■■■■■ : xxvvxx
    #          xyyzzx
    
    # ■■■■■ : xxyyx
    #         xzzxx
    
    # ■■■■ : xxyy
    #        xzzy
    
    # ■■■ : xxy
    #       xyy
    
    # ■■ : xx 
    #      yy (상하반전이 같아서 *2 안함)
    
    # ■ : x
    #     x (상하반전이 같아서 *2 안함)

# *2 : 상하반전 경우의 수


class Solution():
    def numTilings(self, N: int) -> int:
        # 0 리스트, 초기값 설정
        tiles = [1, 2] + [0] * (N-2)
        
        for i in range(2, N):
            # 점화식
            tiles[i] = (2 * sum(tiles[:i-2]) + tiles[i-2] + tiles[i-1] + 2) % 1000000007
        
        return tiles[-1]
        
        
solution = Solution()
solution.numTilings(3)
# 5
