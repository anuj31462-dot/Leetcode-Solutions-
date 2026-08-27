class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frequency = {}

        for x in arr:
            if x in frequency:
                frequency[x] += 1
            else:
                frequency[x] = 1
        frequent_values = []
        for key in frequency:
            frequent_values.append(frequency[key])
        if len(frequent_values) == len(set(frequent_values)):
            return True
        else:
            return False



        