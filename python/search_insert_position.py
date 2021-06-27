class Solution:

    """ Given a sorted array of distinct integers and a target value,
     return the index if the target is found.
     If not, return the index where it would be if it were inserted in order. """

    def searchInsert(self, nums, target):

        # check first and last element
        if nums[0] > target:
            print(0)
            return 0
        elif nums[len(nums)-1] < target:
            print(len(nums))
            return len(nums)

        # iteration list and search target
        else:
            for iteration in range(len(nums)):
                if nums[iteration] == target:
                    print(iteration)
                    return iteration
                elif nums[iteration + 1] > target:
                    print(iteration + 1)
                    return iteration + 1


app = Solution()
app.searchInsert([1, 3, 5, 6], 5)
app.searchInsert([1, 3, 5, 6], 2)
app.searchInsert([1, 3, 5, 6], 7)
app.searchInsert([1, 3, 5, 6], 0)
app.searchInsert([1], 0)
