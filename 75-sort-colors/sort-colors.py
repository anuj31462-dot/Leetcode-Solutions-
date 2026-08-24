class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def sorting(arr):      

            n = len(arr)
            for i in range(n):
                for j in range(0,n-i-1):
                    if arr[j] > arr[j+1]:
                        arr[j],arr[j+1] = arr[j+1],arr[j]
            return arr             
        print(sorting(nums))