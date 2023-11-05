class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        arr = list()
        for i in zip(*matrix):
            arr.append(list(i))
        return list(map(sorted, arr)) == list(map(sorted, list(map(set, matrix))))
        
print(Solution().checkValid([[1,1,1],[1,2,3],[1,2,3]]))
print(Solution().checkValid([[1,2,3],[3,1,2],[2,3,1]]))
print(Solution().checkValid([[1,2],[2,2]]))