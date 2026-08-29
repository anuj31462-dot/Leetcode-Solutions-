class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        store = ""
        for x in range(len(strs[0])):
            for y in strs:
                if x == len(y) or y[x] != strs[0][x]:
                    return store
            store += strs [0][x]
        return store        