#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

#loop your data to allow each instance to be your test set
correct = 0
incorrect = 0
for exclude_index in range(len(db)):
    X = []
    Y = []
    for sample in db[1:exclude_index] + db[exclude_index+1:]:
       
        #add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]. Convert each feature value to
        # float to avoid warning messages
        #--> add your Python code here
        X.append([float(sample[0]), float(sample[1])])
        #transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]. Convert each
        #  feature value to float to avoid warning messages
        #--> add your Python code here
        Y.append(float(1) if sample[2] == '+' else float(0))

    #store the test sample of this iteration in the vector testSample
    #--> add your Python code here
    testSample = [float(db[exclude_index][0]), float(db[exclude_index][1]), float(1) if db[exclude_index][2] == '+' else float(0)]
        #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

        #use your test sample in this iteration to make the class prediction. For instance:
    class_predicted = clf.predict([[float(testSample[0]), float(testSample[1])]])[0]
    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here
    if class_predicted == testSample[2]:
        correct += 1
    else:  
        incorrect += 1
errorrate = incorrect/(correct+incorrect)
print(errorrate)

#print the error rate
#--> add your Python code here






