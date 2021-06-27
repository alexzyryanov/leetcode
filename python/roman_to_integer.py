class Solution:

    """ Given a roman numeral, convert it to an integer. """

    def romanToInt(self, s: str) -> int:
        iteration = 0
        arab = 0

        # 0, 1, 2....
        while iteration < len(s):

            # check item +arab, if next item V, X, L, C, D, M +arab and iteration +2
            if s[iteration] == "I":
                try:
                    if s[iteration + 1] == "V":
                        arab += 4
                        iteration += 2
                    elif s[iteration + 1] == "X":
                        arab += 9
                        iteration += 2
                    elif True:
                        arab += 1
                        iteration += 1
                except Exception:
                    arab += 1
                    iteration += 1
                    continue

            elif s[iteration] == "X":
                try:
                    if s[iteration + 1] == "L":
                        arab += 40
                        iteration += 2
                    elif s[iteration + 1] == "C":
                        arab += 90
                        iteration += 2
                    elif True:
                        arab += 10
                        iteration += 1
                except Exception:
                    arab += 10
                    iteration += 1
                    continue

            elif s[iteration] == "C":
                try:
                    if s[iteration + 1] == "D":
                        arab += 400
                        iteration += 2
                    elif s[iteration + 1] == "M":
                        arab += 900
                        iteration += 2
                    elif True:
                        arab += 100
                        iteration += 1
                except Exception:
                    arab += 100
                    iteration += 1
                    continue

            # just check item
            elif s[iteration] == "V":
                arab += 5
                iteration += 1

            elif s[iteration] == "L":
                arab += 50
                iteration += 1

            elif s[iteration] == "D":
                arab += 500
                iteration += 1

            elif s[iteration] == "M":
                arab += 1000
                iteration += 1
        print(arab)
