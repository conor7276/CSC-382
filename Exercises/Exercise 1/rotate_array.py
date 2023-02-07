#Given an integer array nums, rotate the array to the right by k steps, where k is non negative
# leetcode 189




# Attempt #2  O(N) Solution Faster 16% but worse on memory 28%
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """     
        if(k > 0):
            for _ in range(k):

                nums.insert(0,nums.pop(len(nums)-1))
        else:
            for _ in range(abs(k)):
                nums.append(nums.pop(0))
            



# My Solution O(N) Slow 9.93% but Very good on memory 98.69%
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #print(nums)
        if k > 0:
            for _ in range(k):
                rotated_arr = nums
                #print(rotated_arr)
                temp = rotated_arr.pop(len(rotated_arr)- 1) # pop from end
                rotated_arr.insert(0,temp) # insert at front
                nums = rotated_arr
                #print(nums)
        else: # not sure if negative works
            for _ in range(abs(k)):
                rotated_arr = nums
                temp = rotated_arr.pop(0) # pop from front
                rotated_arr.append(temp) # insert at back
                nums = rotated_arr