from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            nums_c = nums.copy()
            nums_c.remove(i)
            res.append(prod(nums_c))
        return res



'''
        total_prod = prod(nums)

        # for prod without 0

        # filter and remove 0 from list using list comprehension
        filtered_nums = [x for x in nums if x!=0]
        if not filtered_nums:
            return [0]*len(nums)
        prod_0 = prod(filtered_nums)




        res = []
        for i in nums:
            if i==0:
                i_num=prod_0
            else:
                i_num = total_prod/i
            res.append(int(i_num))
        return res
'''

