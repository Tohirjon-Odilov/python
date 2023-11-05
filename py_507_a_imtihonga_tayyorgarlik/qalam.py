def paint(color:list)-> int:
    count = 2
    for i in range(1, len(color)):
        count += 2
        if color[i-1] != color[i]:
            count += 1
            
    return count if len(count) != 0 else 0



print(paint(["Red", "Blue", "Red", "Blue", "Red"]))
print(paint(["Red"]))
print(paint(["Red", "Yellow", "Green", "Blue"]))
print(paint(["Blue", "Blue", "Blue", "Red", "Red", "Red"]))