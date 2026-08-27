class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        hashi = {}
        for x in nums:
            if x in hashi:
                hashi[x] += 1
            else:
                hashi[x] = 1
        for x in hashi:
            if hashi[x] > n/2:
                return x

        
        
        