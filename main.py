class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # Create a DP table with (m + 1) x (n + 1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # An empty t can be formed by any prefix of s in exactly 1 way (by taking nothing)
        for i in range(m + 1):
            dp[i][0] = 1
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    # If characters match, we can either use this character or not
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # If characters do not match, we cannot use this character
                    dp[i][j] = dp[i - 1][j]
        
        return dp[m][n]

# Example usage:
solution = Solution()
print(solution.numDistinct("rabbbit", "rabbit"))  # Output: 3
print(solution.numDistinct("babgbag", "bag"))     # Output: 5
