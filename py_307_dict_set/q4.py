# Q4:

# Berilgan list larni rasmdagidek qilib dictionary ga o'tkazing

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

thisdict = dict()
for i in range(len(values)):
    thisdict.update({keys[i]: values[i]})

print(thisdict)
