# 1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range (len(nums)):
            hashmap[nums[i]]=i
        
        for i in range (len(nums)):
            val= target-nums[i]
            if val in hashmap and hashmap[val]!=i:
                return [i, hashmap[val]]
        return []
        # arr = []
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             arr.append(i)
        #             arr.append(j)
        #             return arr   # return as soon as we find the pair
        # return []  # if no pair found