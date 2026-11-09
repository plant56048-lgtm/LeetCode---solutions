class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """ length_str = len(s)
        if length_str <= 1:
            return length_str
        seen = {}
        left = 0
        max_len = 0
        for right, char in enumerate(s):
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            seen[char] = right
            if max_len < right - left +1 :
                max_len = right - left + 1
        return max_len"""

        left = 0
        last = {}
        ans = 0

        for right, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                left = last[ch] + 1

            last[ch] = right
            ans = max(ans, right - left + 1)

        return ans
            
        



