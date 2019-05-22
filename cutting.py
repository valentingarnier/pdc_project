import numpy as np

with open("output.txt") as file:
    content = file.readlines()
content = [x.strip() for x in content]

edges = []
for i in range(0, len(content)):
    if content[i].endswith("e+00"):
        edges.append(i)

cutting_index = (0, 0)

for i in range(0, len(edges) - 1): #-1 car on est sur que le dernier n'est pas dans le decoupage et comme ca pas de index out of range
    if (edges[i + 1] - edges[i]) > 10:
        cutting_index = (edges[i], edges[i+1])

only_data = content[cutting_index[0] + 1:cutting_index[1]]

for i in only_data:
    print(i)
print(len(only_data))

dataSliced = []
for i in range(5, len(only_data), 100):
    if i + 90 > len(only_data):
        break
    dataSliced.append(only_data[i: i + 90])
    #print(len(only_data[i: i + 90]))