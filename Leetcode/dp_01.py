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



class Solution():
    def numTilings(self, N: int) -> int:
        tiles = [1, 2] + [0] * (N-2)
        
        for i in range(2, N):
            tiles[i] = (2 * sum(tiles[:i-2]) + tiles[i-2] + tiles[i-1] + 2) % 1000000007
        
        return tiles[-1]
        
        
solution = Solution()
solution.numTilings(0)
# 2
