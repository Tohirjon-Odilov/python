# Q6:

# "city" keyni "location" ga o'zgartirib qo'ying

sample_dict = {
    "name": "Tohirjon",
    'age': 20,
    'salary': 1000,
    'city': 'London'
}

if 'city' in sample_dict.keys():
    sample_dict.pop("city")
    sample_dict.update({"location": "London"})

print(sample_dict)
