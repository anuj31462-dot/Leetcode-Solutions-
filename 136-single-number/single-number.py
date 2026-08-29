class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for x in nums:
            if x in seen:
                seen[x] += 1
            else:
                seen[x] = 1
        for x,count in seen.items():
            if count == 1:
                return x