class Solution:
    VALID_BRACKETS = {
        '[': ']',
        '(': ')',
        '{': '}',
    }

    def isValid(self, string):
        brackets = []
        for b in string:
            if b in self.VALID_BRACKETS.keys():
                brackets.append(b)
            elif b in self.VALID_BRACKETS.values():
                if brackets:
                    bracket = brackets.pop()
                    if self.VALID_BRACKETS[bracket] != b:
                        return False
                else:
                    return False

        if not brackets:
            return True


s = Solution()
print(s.isValid("(2 + 3 (9 - 1))"))
