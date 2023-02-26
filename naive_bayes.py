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
from sklearn.naive_bayes import GaussianNB
import csv

#reading the training data in a csv file
dbTrain = []
with open("weather_training.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            dbTrain.append(row)
        else:
            header = row 

#transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
X = []
Y = []

for i, row in enumerate(dbTrain):
    X.append([])
    #Outlook
    match row[1]:
        case 'Sunny':
            X[i].append(1)
        case 'Overcast':
            X[i].append(2)
        case 'Rain':
            X[i].append(3)
    
    #Temperature
    match row[2]:
        case 'Hot':
            X[i].append(1)
        case 'Mild':
            X[i].append(2)
        case 'Cool':
            X[i].append(3)

    #Humidity
    match row[3]:
        case 'High':
            X[i].append(1)
        case 'Normal':
            X[i].append(2)
        
    #Wind
    match row[4]:
        case 'Weak':
            X[i].append(1)
        case 'Strong':
            X[i].append(2)

#transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    match row[5]:
        case 'Yes':
            Y.append(1)
        case 'No':
            Y.append(2)




#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the test data in a csv file
dbTest = []
with open("weather_test.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            dbTest.append(row)      

#printing the header os the solution
Xtest = []
Ytest = []

for i, row in enumerate(dbTest):
    Xtest.append([])
    #Outlook
    match row[1]:
        case 'Sunny':
            Xtest[i].append(1)
        case 'Overcast':
            Xtest[i].append(2)
        case 'Rain':
            Xtest[i].append(3)
    
    #Temperature
    match row[2]:
        case 'Hot':
            Xtest[i].append(1)
        case 'Mild':
            Xtest[i].append(2)
        case 'Cool':
            Xtest[i].append(3)

    #Humidity
    match row[3]:
        case 'High':
            Xtest[i].append(1)
        case 'Normal':
            Xtest[i].append(2)
        
    #Wind
    match row[4]:
        case 'Weak':
            Xtest[i].append(1)
        case 'Strong':
            Xtest[i].append(2)

#transform the original training classes to numbers and add them to the vector Ytest.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    match row[5]:
        case 'Yes':
            Ytest.append(1)
        case 'No':
            Ytest.append(2)

#use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
format_rows = "{:<13}"*(len(header)+1) # For the formatted table
for row, prob in zip(dbTest, clf.predict_proba(Xtest)):
    if prob[0] > 0.75:
        row[5] = 'Yes'
        row.append(prob[0])
    elif prob[1] > 0.75:
        row[5]='No'
        row.append(prob[1])
    else:
        row[5]='Unknown'
        row.append(prob[0] if prob[0] > prob[1] else prob[1])
print(format_rows.format(*header, 'Confidence'))
for i, row in enumerate(dbTest):
    print(format_rows.format(*row))
