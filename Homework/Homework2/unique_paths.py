
class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		# dynamic programming iteration solution, similar to mathematical also using math to calculate the number of paths
		# This method has the total number of unique paths at the bottom right corner instead of top left but still gives the same answer
		# initalize array with all 1s
		dp = [[1 for _ in range(n)] for _ in range(m)]

		for i in range(1, m):
			for j in range(1, n):
				#print(dp)
				dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
		#print(dp)
		return dp[m-1][n-1]
	
	def uniquePathsRecursive(self, m: int, n: int) -> int:
        #Recursive Solution
		result = {}
		# uses a dictionary/hash table to store the paths that it adds.
		# similar to the iterative approach that it goes from top left to bottom right, the last key should have the most paths.
		def uniquePathsHelper(row, col):

			if (row == 0 or col == 0):
				return 1

			elif (row, col) not in result: # Avoid duplicate results
				
				result[(row, col)] = uniquePathsHelper(row - 1, col) + uniquePathsHelper(row, col - 1)
			#print(result)
			return result[(row, col)]

		return uniquePathsHelper(m - 1, n - 1)

res = Solution()
print(res.uniquePaths(3,7))
print(res.uniquePathsRecursive(3,7))

# Output:
# 28
# 28
	