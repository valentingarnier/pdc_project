import numpy as np


def cuttingData():
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

    print("this is only data: ", only_data)


    return only_data
