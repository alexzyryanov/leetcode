class Solution:

    """ Given an integer array nums, find the contiguous subarray (containing at least one number)
    which has the largest sum and return its sum. """

    def maxSubArray(self, nums):
        local_max = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            local_max = max(local_max + nums[i], nums[i])
            global_max = max(global_max, local_max)

        print(global_max)
        return global_max


app = Solution()
app.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
app.maxSubArray([1])
app.maxSubArray([5, 4, -1, 7, 8])
app.maxSubArray([-1])
app.maxSubArray([-2, -1])
