import math
import csv


def knn(filepath: str):
    # [number, x, y, class]
    data=[]
    correct = 0
    incorrect = 0
    with open(filepath, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
            data.append((int(row[0]), int(row[1]), int(row[2])))
    
    print(data)
    for i, point1 in enumerate(data):
        dist_list = []
        for j, point2 in enumerate(data):
            if i != j:
                dist = math.sqrt((point1[1]-point2[1])**2 + (point1[2]-point2[2])**2)
                dist_list.append((dist, point2))
        s = sorted(dist_list)
        print(s)
        mini = s[0]
        print(mini)
        if mini[1][2] == point1[2]:
            correct += 1
        else:
            incorrect += 1
    return incorrect/(correct+incorrect)


print(knn("points.csv"))