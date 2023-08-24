# Q7:

# Foydalanuvchi string kiritadi. Shu stringdagi har bitta belgidan
# nechtadan borligini dictionary ga quyidagicha joylang:

# Input:     "w3resource"
# Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

txt = input("Nimadir yozing: ")
# txt = 'w3resource'
thisdict = dict()
for i in range(len(txt)):
    thisdict.update({txt[i]: txt.count(txt[i])})
print(thisdict)
