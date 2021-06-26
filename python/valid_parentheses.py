class Solution:

    """ Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.
    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order. """

    def isValid(self, s):
        stack = []
        flag = True
        for item in s:
            if item in "([{":
                stack.append(item)
            elif item in ")]}":
                if len(stack) == 0:
                    flag = False
                    break
                else:
                    re = stack.pop()
                    if re == "(" and item == ")":
                        continue
                    elif re == "[" and item == "]":
                        continue
                    elif re == "{" and item == "}":
                        continue
                    else:
                        flag = False
                        break
        if flag is True and len(stack) == 0:
            print(True)
        else:
            print(False)


app = Solution()
app.isValid("()")
app.isValid("()[]{}")
app.isValid("(]")
app.isValid("([)]")
app.isValid("{[]}")
