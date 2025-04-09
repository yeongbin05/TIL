class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        n = len(nums)
        for i in range(n):
            if target - nums[i] in dic:
                return [dic[target-nums[i]],i]
            
            else :
                dic[nums[i]] = i