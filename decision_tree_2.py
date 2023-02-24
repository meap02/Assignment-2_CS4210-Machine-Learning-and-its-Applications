#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import csv
import matplotlib.pyplot as plt

#BUILD TEST SET FEATURE MATRIX AND CLASS VECTOR
#transform the features of the test instances to numbers following the same strategy done during training,
Xtest = []
Ytest = []
dbTest = []
with open("contact_lens_test.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            dbTest.append(row)        
for i, row in enumerate(dbTest):
    Xtest.append([])
    match row[0]:
        case 'Young':
            Xtest[i].append(1)
        case 'Prepresbyopic':
            Xtest[i].append(2)
        case 'Presbyopic':
            Xtest[i].append(3)
        case _: # default
            Xtest[i].append(0)

    #Spectacle
    match row[1]:
        case 'Myope':
            Xtest[i].append(1)
        case 'Hypermetrope':
            Xtest[i].append(2)
        case _: # default
            Xtest[i].append(0)
    
    #Astigmatism
    match row[2]:
        case 'Yes':
            Xtest[i].append(1)
        case 'No':
            Xtest[i].append(2)
        case _: # default
            Xtest[i].append(0)

    #Tear Production Rate
    match row[3]:
        case 'Reduced':
            Xtest[i].append(1)
        case 'Normal':
            Xtest[i].append(2)
        case _: # default
            Xtest[i].append(0)
    
    match row[4]:
        case 'Yes':
            Ytest.append(1)
        case 'No':
            Ytest.append(2)
        case _: # default
            Ytest.append(0)


#START OF TRAINING
dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:
    print("using data:" + ds)
    dbTraining = []
    X = []
    Y = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append(row)

    #transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    X = [] #to store the training features
    Y = [] #to store the training class labels
    for i, row in enumerate(dbTraining):
        X.append([])
        match row[0]:
            case 'Young':
                X[i].append(1)
            case 'Prepresbyopic':
                X[i].append(2)
            case 'Presbyopic':
                X[i].append(3)
            case _: # default
                X[i].append(0)

        #Spectacle
        match row[1]:
            case 'Myope':
                X[i].append(1)
            case 'Hypermetrope':
                X[i].append(2)
            case _: # default
                X[i].append(0)
        
        #Astigmatism
        match row[2]:
            case 'Yes':
                X[i].append(1)
            case 'No':
                X[i].append(2)
            case _: # default
                X[i].append(0)

        #Tear Production Rate
        match row[3]:
            case 'Reduced':
                X[i].append(1)
            case 'Normal':
                X[i].append(2)
            case _: # default
                X[i].append(0)
 

        #transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
        #Recommendation
        match row[4]:
            case 'Yes':
                Y.append(1)
            case 'No':
                Y.append(2)
            case _: # default
                Y.append(0)
 
    #loop your training and test tasks 10 times here
    accuracy_sum = 0
    for i in range (10):
        #fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
        clf = clf.fit(X, Y) 
        #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
        #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
        results = clf.predict(Xtest)

        #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
        TP = 0
        TN = 0
        FP = 0
        FN = 0
        for compare in zip(results, Ytest):
            if compare[0] == compare[1]:
                if compare[0] == 1:
                    TP += 1
                else:
                    TN += 1
            else:
                if compare[0] == 1:
                    FP += 1
                else:
                    FN += 1
        
        accuracy_sum += (TP + TN) / (TP + TN + FP + FN)

    #print the average accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    accuracy = accuracy_sum / 10
    print("Final accuracy when training on " + ds + ": " + str(accuracy))

        





