# R4:

# Function tuzing. String qabul qilsin. Katta harflar sonini va kichik
# harflarni sonini qaytarsin.

# Input:     "Good Luck"
# Output:  [2, 6]

def countstr(txt):
    upper = int()
    lower = int()

    for i in txt:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
    return upper, lower


txt = "Good Luck"
str = list(countstr(txt))
print(str)
