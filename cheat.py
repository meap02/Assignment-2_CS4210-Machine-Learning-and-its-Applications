import math
import csv
from collections import Counter

def knn(filepath: str):
    # [number, x, y, class]
    string = "d(#10,#{point2})=√(({red1}-{red2})^2+({green1}-{green2})^2+({blue1}-{blue2})^2)={dist}"
    X=[]
    Y=[]
    testing_value = [154,205,50]
    with open(filepath, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
            if i > 0 and i != 10:
                X.append((float(row[1]), float(row[2]), float(row[3])))
                Y.append(float(row[4]))
    
    for i, point2 in enumerate(X[0:10]):
        print(point2)
    dist_list = []
    for i, point2 in enumerate(X):
        dist = math.sqrt((testing_value[0]-point2[0])**2 + (testing_value[1]-point2[1])**2 + (testing_value[2]-point2[2])**2)
        dist_list.append((dist, point2, Y[i], i))
        print(string.format(point2=i+1, red1=testing_value[0], red2=point2[0], green1=testing_value[1], green2=point2[1], blue1=testing_value[2], blue2=point2[2], dist=dist))
    s = sorted(dist_list, key=lambda x: x[0])
    print("The 3 closest neighbors are: " )
    c = Counter([x[2] for x in s[0:3]])
    for canidates in s[0:3]:
        print("point #{point} with distance {dist} and class {class_}".format(point=canidates[3]+1, dist=canidates[0], class_=canidates[2]))
    return c.most_common()[0][0]

print("This point is classified as class: " + str(knn("10.csv")))