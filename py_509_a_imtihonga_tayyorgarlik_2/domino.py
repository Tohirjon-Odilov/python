def domino(nums:str) -> list[list[int]]:
    myList = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[2,2],[2,3],[2,4],[2,5],[2,6],[3,3],[3,4],[3,5],[3,6],[4,4],[4,5],[4,6],[5,5],[5,6],[6,6]]
    nums = eval(nums)
    for i in nums:
        if i in myList:
            print(i)
            myList.remove(i)
            continue
        i = i[::-1]
        if i in myList:
            print(i)
            myList.remove(i)

    return myList

# domino('[[0,0],[0,1],[0,5],[0,6],[1,1],[1,3],[1,4],[1,5],[1,6],[2,2],[2,5],[2,6],[3,5],[3,6],[4,4],[4,5],[4,6],[5,5]]')
# print(domino(input("Enter list: ")))
print(domino('[[1,6], [6,3], [0,5], [5,2], [4,1], [3,5], [5,1], [4,5], [5,5], [2,6], [6,0], [0,1], [0,0], [2,2], [1,1], [1,3], [4,6], [4,4]]'))