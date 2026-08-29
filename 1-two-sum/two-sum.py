class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashe = {}
        for i in range(len(nums)):
            if target - nums[i] in hashe:
                return [hashe[target - nums[i]],i]
            hashe[nums[i]] = i