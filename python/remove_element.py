class Solution:

    """Given an integer array nums and an integer val,
    remove all occurrences of val in nums in-place.
    The relative order of the elements may be changed."""

    def removeElement(self, nums, val):
        iteration = 0

        # remove element if == val
        while iteration != len(nums):
            if nums[iteration] == val:
                nums.remove(nums[iteration])
                iteration -= 1
            iteration += 1
        print(len(nums))
        return len(nums)


app = Solution()
app.removeElement([3, 2, 2, 3], 3)
app.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
