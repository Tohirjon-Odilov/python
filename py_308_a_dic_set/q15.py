# Q 15:

# User n kiritadi va  setga n ta ma'lumot qo'shib boradi. Sizning vazifangiz,
# ma'lumot kiritilishi yakunlanishiga qadar qaysi son necha marta
# kiritilganini dictionaryga o'zlashtirib borish.

n = int(input("Set'ni len'nini kiriting: "))
thisset = set()
thisdict = {}
thislist = list()
while n:
    set_input = input("Ma'lumot kiriting: ")
    thislist.append(set_input)
    thisset.add(set_input)
    thisdict.update({set_input: thislist.count(set_input)})
    n -= 1
print(thisdict)
