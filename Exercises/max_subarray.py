#Leetcode 53
#Dynamic programming runtime 97.15% memory 13%
# O(N) runtime O(1) Space
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0] # keep track on max sum
        curr_sum = nums[0] # keep track of current sum
        # alternative code for second part using max
        # for i in range(1, len(nums)):
        #     curr_sum = max(nums[i], curr_sum + nums[i]) # see if the sum increases if we add a number from the array
        #     max_sum = max(max_sum, curr_sum) # see if the current sum is larger than the max sum

        for i in range(1, len(nums)):
            if(nums[i] > curr_sum + nums[i]):
                curr_sum = nums[i]
            else:
                curr_sum = curr_sum + nums[i]

            if(curr_sum > max_sum):
                max_sum = curr_sum

        return max_sum
