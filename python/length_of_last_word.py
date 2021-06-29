class Solution:

    """Given a string s consists of some words separated by spaces,
    return the length of the last word in the string.
    If the last word does not exist, return 0."""

    def lengthOfLastWord(self, s):
        x = []

        # split str and remove "", return last len item
        for item in s.split(" "):
            if item != "":
                x.append(item)
        if len(x) == 0:
            print(0)
            return 0
        print(len(x[len(x)-1]))
        return len(x[len(x)-1])


app = Solution()
app.lengthOfLastWord("Hello World")
app.lengthOfLastWord(" ")
app.lengthOfLastWord("a ")
app.lengthOfLastWord("b   a    ")
