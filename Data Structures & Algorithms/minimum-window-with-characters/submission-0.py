class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        need = {}
        window = {}

        for char in t:
            need[char] = need.get(char, 0) + 1

        have = 0
        need_count = len(need)

        result = [-1, -1]
        min_length = float("inf")

        left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == need_count:
                # update best answer
                if right - left + 1 < min_length:
                    result = [left, right]
                    min_length = right - left + 1

                # remove left character
                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        left, right = result

        if min_length == float("inf"):
            return ""

        return s[left:right + 1]