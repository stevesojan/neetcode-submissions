class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # longest substring without repeating characters
        # the goal is to maintain a sliding window through a (contd. below) 
        # a hash map which stores the latest index where the character was found
        # window between l and r is maintained as a continuous substring

        l = 0
        hmap = {}
        max_count = 0

        for r, ch in enumerate(s):

            if ch in hmap and hmap[ch]>= l:
                l = hmap[ch] + 1

            hmap[ch] = r
            max_count = max(max_count, r-l + 1)

        return max_count
