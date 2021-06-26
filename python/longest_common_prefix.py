class Solution:

    """ Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "". """

    def longestCommonPrefix(self, strs):
        count = {}
        prefix = ""
        flag = ""

        # iteration 0, 1, 2...  min len
        for iteration in range(len(min(strs, key=len))):

            # add first item into count
            for word in strs:
                flag = word[iteration]
                if word[iteration] not in count:
                    count.update({word[iteration]: 1})
                else:
                    count[word[iteration]] += 1

            # if count first item == len str, add item into prefix
            if count[flag] == len(strs):
                prefix += flag
                count = {}
            else:
                break
        print(prefix)


app = Solution()
app.longestCommonPrefix(["flower", "flow", "flight"])
app.longestCommonPrefix(["dog", "racecar", "car"])
