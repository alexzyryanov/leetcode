class Solution:

    """Given an integer array nums sorted in non-decreasing order,
    remove the duplicates in-place such that each unique element appears only once.
    The relative order of the elements should be kept the same."""

    def removeDuplicates(self, nums):
        iteration = 0

        # 0, 1, 2...
        while iteration != len(nums):
            try:

                # remove duplicates
                if nums[iteration] == nums[iteration + 1]:
                    nums.remove(nums[iteration])
                    iteration -= 1
                iteration += 1
            except IndexError:
                print(len(nums))
                return len(nums)
        print(nums)
        return len(nums)


app = Solution()
app.removeDuplicates([1, 1, 2])
app.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
