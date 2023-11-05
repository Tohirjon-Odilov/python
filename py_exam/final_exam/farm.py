def count_animals(animal):
    animals_len = ['dog', 'cat', 'bat', 'cock', 'cow', 'pig', 'fox', 'ant', 'bird', 'lion', 'wolf', 'deer', 'bear', 'frog', 'hen', 'mole', 'duck', 'goat']    
    
    sorted_animals = list()
    for i in animals_len:
        text = str()
        for j in i:
            if j in animal:
                text += j
        if len(i) == len(text):
            sorted_animals.append(text)
            
    animals_len = len(sorted_animals)
    dublicate_len = animal.count(sorted_animals[0])
    sorted_animals = ",".join(list(set(sorted_animals)))

    if animals_len < dublicate_len:
        return f"{dublicate_len} ({sorted_animals})"
    return f"{animals_len} ({sorted_animals})"

print(count_animals("goatcode"))
print(count_animals("cockdogwdufrbir"))
print(count_animals("dogdogdogdogdog"))
# print(count_animals("salom"))
