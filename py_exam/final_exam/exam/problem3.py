def typing_hand() -> str:
    left = {
        '1': 1,
        'Q': 1,
        'A': 1,    
        'Z': 1,   
        '2': 1,    
        'W': 1,   
        'S': 1,    
        'X': 1,    
        '3': 1,    
        'E': 1,    
        'D': 1,    
        'C': 1,    
        '4': 1,    
        'R': 1,    
        'F': 1,    
        'V': 1,    
        '5': 1,    
        'T': 1,    
        'G': 1,    
        'B': 1,    
    }
    right = {
        '6': 1,
        'Y': 1,
        'H': 1,    
        'N': 1,   
        'M': 1,    
        '7': 1,   
        'U': 1,    
        'J': 1,    
        'M': 1,    
        '8': 1,    
        'I': 1,    
        'K': 1,    
        ',': 1,    
        '-': 1,    
        '9': 1,    
        'O': 1,    
        'L': 1,    
        '.': 1,    
        'O': 1,    
        'P': 1,    
        ';': 1,    
        '/': 1,    
    }
    left_count, right_count = 0, 0
    with open("problem3.txt") as f:
        data = f.read()
        for i in data:
            if i.upper() in left.keys():
                left_count += 1
            elif i.upper() in right.keys():
                right_count += 1
                
    return f"Left={left_count} Right={right_count}"

print(typing_hand())