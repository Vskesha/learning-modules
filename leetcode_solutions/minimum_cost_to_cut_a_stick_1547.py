from functools import lru_cache


class Solution:
    def minCost(self, n: int, cuts: list[int]) -> int:

        cuts = sorted([0] + cuts + [n])
        m = len(cuts)
        dp = [[0] * m for _ in range(m)]
        
        for width in range(2, m):
            for left in range(0, m - width):
                right = left + width
                dp[left][right] = dp[left+1][right]
                for mid in range(left + 2, right):
                    curr = dp[left][mid] + dp[mid][right]
                    dp[left][right] = min(dp[left][right], curr)
                dp[left][right] += cuts[right] - cuts[left]
        
        return dp[0][m-1]
    
    
    def minCost2(self, n: int, cuts: list[int]) -> int:
        
        @lru_cache
        def cost(left, right):
            if right - left == 1:
                return 0
            min_cost = min(cost(left, mid) + cost(mid, right) for mid in range(left + 1, right))
            return min_cost + cuts[right] - cuts[left]
            
        cuts = sorted([0] + cuts + [n])
        return cost(0, len(cuts) - 1)
                
                
if __name__ == '__main__':
    sol = Solution()
    print('16 ===', sol.minCost(n = 7, cuts = [1,3,4,5]))
    print('22 ===', sol.minCost(n = 9, cuts = [5,6,1,4,2]))
    print('10 ===', sol.minCost(n = 5, cuts = [3, 1, 4]))
    