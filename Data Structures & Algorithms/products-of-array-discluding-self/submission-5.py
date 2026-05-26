
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        # build prefix and suffix products per index

        res = [1]*len(nums) #create resultant array with exact number of indices as much as in nums

        prefix = 1 #prefix products of first element can be 1 since there is no true elemnt prior to first element

        for i in range(len(nums)):
            res[i] = prefix
 #will naturally set the prefix products of first elemnt as 1
            prefix*=nums[i]


        #now build suffix products per index by iterating from the back and multiply with existing prefix products at each index of res

        suffix = 1 # because last element does not have any other element after, so suffix product =1
        for i in range(len(nums)-1, -1, -1): # "-1" as stop because it must go till beginning of nums i.e 0th index inclusive, so stop = -1
            res[i] *= suffix #multiplies existing prefix product at that index and suffix product starts from last index with suffix=1
            suffix*=nums[i]


        return res