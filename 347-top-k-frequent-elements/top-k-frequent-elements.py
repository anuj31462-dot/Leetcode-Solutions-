class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}
        for x in nums:
            if x in a :
                a[x] += 1
            else:
                a[x] = 1
        result = []
        for i in range(k):
            max_count = 0
            max_num = None

            for x , count in a.items():
                if count > max_count:
                    max_count = count
                    max_num = x
            result.append(max_num)
            del a[max_num]
        return result