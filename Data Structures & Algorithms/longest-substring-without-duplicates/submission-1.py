class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # longest substring without repeating characters
        # the goal is to maintain a sliding window through a (contd. below) 
        # a hash map which stores the latest index where the character was found
        # window between l and r is maintained as a continuous substring


        l = 0
        h = {}
        max_count = 0

        for r, character in enumerate(s):

            if character in h and h[character]>=l:
                l = h[character] + 1
            
            h[character] = r

            max_count = max(max_count, r-l+1)

        return max_count


        '''
        l = 0
        hmap = {}
        max_count = 0

        for r, ch in enumerate(s):

            if ch in hmap and hmap[ch]>= l: #second check here i.e hmap[ch]>=1 is used to check if the index assigned to ch is latest and part of substring with l as left boundary
                l = hmap[ch] + 1

            hmap[ch] = r
            max_count = max(max_count, r-l + 1)

        return max_count
        '''