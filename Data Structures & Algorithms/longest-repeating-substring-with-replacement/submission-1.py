from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # for longest repeating with k character replacement problem
        # use the logic, window_size - max_count(of a char in the window) > k

        #e.g AABAB and k = 1
        # case 1 - replace middle B with A, to give AAAA = 4
        # case 2 - replace last A with B to give BBB = 3

        # case 1 is ideal, because by replacing 1 element we can get consecutive 4
        # in this window, max_count = 3 i.e 3 elements of A, so in the sliding window k determines how many elements of the min_count elements here 2 i.e two counts of B can be replaced i.e times

        
        l = 0
        h_count = defaultdict(int)
        max_count = 0

        for r, ch in enumerate(s):

            h_count[ch] += 1
            max_count = max(max_count, h_count[ch])

            # if window_size - max_count > k, then slide window forward
            # because only either k elements or lees than k elements can be accomodated
            # so the moment gets full we slide it forward

            while (r-l + 1 - max_count) > k:
                h_count[s[l]] -= 1
                l+=1

            res = max(max_count, r-l+1)

        return res

