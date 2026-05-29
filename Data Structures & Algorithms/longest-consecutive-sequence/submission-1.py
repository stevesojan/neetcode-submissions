class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #converting list to set, so lookup is always constant O(1)

        set_nums = set(nums)
        longest_seq = 0
        for i in set_nums:
            if i-1 not in set_nums: #so this is the start of a sequence
                length=1

                while i+length in set_nums:
                    length+=1
                longest_seq = max(longest_seq, length)
        return longest_seq
