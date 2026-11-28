class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        # prev2 = ways to decode up to i - 2
        # prev1 = ways to decode up to i - 1
        prev2, prev1 = 1, 1

        for i in range(1, len(s)):
            curr = 0
            # Single-digit decode (valid if not '0')
            if s[i] != "0":
                curr += prev1
            # Two-digit decode (valid if between '10' and '26')
            if "10" <= s[i - 1 : i + 1] <= "26":
                curr += prev2

            prev2, prev1 = prev1, curr

        return prev1