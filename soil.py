import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.preprocessing import LabelEncoder

name = input("Enter the Location:")

print("Enter 1 for sandy soil")
print("Enter 2 for slit soil")
print("Enter 3 for clay soil")
print("Enter 4 for lomey soil")
soil = int(input())
n = float(input("Enter the percentage of nitrogen present in soil:"))
p = float(input("Enter the percentage of phosphorous present in soil:"))
k = float(input("Enter the percentage of potassium present in soil:"))
h = float(input("Enter the ph of the soil:"))

if(name == "Konkan" or name == "konkan"):
    dataset = pd.read_csv(r"D:\python\soilcsv\konkan.csv")
    inputs = dataset.drop('ph' , axis = 'columns')
    le_cropname = LabelEncoder()
    inputs['Cropname'] = le_cropname.fit_transform(inputs['Cropname'])
    print(inputs['Cropname'])
    X = dataset.iloc[: , :-1]
    y = dataset.iloc[: , -1]
    clf = svm.SVC(kernel= 'rbf' , C = 1000)
    clf.fit(X , y)

    newdata = [[soil , h , n , p , k]]
    if(newdata[0][1] <= 3):
        print("Soil is more acidic than required")
    if(newdata[0][1] > 8):
        print("Soil is not compatable for use")
    elif(newdata[0][1] > 3 and newdata[0][1] < 8):
        print(clf.predict(newdata))

if(name == "Pune" or name == "pune"):
    dataset = pd.read_csv(r"D:\python\soilcsv\pune.csv")
    inputs = dataset.drop('ph' , axis = 'columns')
    le_cropname = LabelEncoder()
    inputs['Cropname'] = le_cropname.fit_transform(inputs['Cropname'])
    print(inputs['Cropname'])
    X = dataset.iloc[: , :5]
    y = dataset.iloc[: , -1]
    clf = svm.SVC(kernel= 'linear' , C = 1000)
    clf.fit(X , y)

    newdata = [[soil , h , n , p , k]]
    if(newdata[0][1] <= 3):
        print("Soil is more acidic than required")
    if(newdata[0][1] > 8):
        print("Soil is not compatable for use")
    elif(newdata[0][1] > 3 and newdata[0][1] < 8):
        print(clf.predict(newdata))

if(name == "Nagpur" or name == "nagpur"):
    dataset = pd.read_csv(r"D:\python\soilcsv\nagpur.csv")
    inputs = dataset.drop('ph' , axis = 'columns')
    le_cropname = LabelEncoder()
    inputs['Cropname'] = le_cropname.fit_transform(inputs['Cropname'])
    print(inputs['Cropname'])
    X = dataset.iloc[: , :5]
    y = dataset.iloc[: , -1]
    clf = svm.SVC(kernel= 'linear' , C = 1000)
    clf.fit(X , y)

    newdata = [[soil , h , n , p , k]]
    if(newdata[0][1] <= 3):
        print("Soil is more acidic than required")
    if(newdata[0][1] > 8):
        print("Soil is not compatable for use")
    elif(newdata[0][1] > 3 and newdata[0][1] < 8):
        print(clf.predict(newdata))        

if(name == "Nashik" or name == "nashik"):
    dataset = pd.read_csv(r"D:\python\soilcsv\nashik.csv")
    inputs = dataset.drop('ph' , axis = 'columns')
    le_cropname = LabelEncoder()
    inputs['Cropname'] = le_cropname.fit_transform(inputs['Cropname'])
    print(inputs['Cropname'])
    X = dataset.iloc[: , :5]
    y = dataset.iloc[: , -1]
    clf = svm.SVC(kernel= 'linear' , C = 1000)
    clf.fit(X , y)

    newdata = [[soil , h , n , p , k]]
    if(newdata[0][1] <= 3):
        print("Soil is more acidic than required")
    if(newdata[0][1] > 8):
        print("Soil is not compatable for use")
    elif(newdata[0][1] > 3 and newdata[0][1] < 8):
        print(clf.predict(newdata)) 

if(name == "Aurangabad" or name == "aurangabad"):
    dataset = pd.read_csv(f"D:\python\soilcsv\{name}.csv")
    inputs = dataset.drop('ph' , axis = 'columns')
    le_cropname = LabelEncoder()
    inputs['Cropname'] = le_cropname.fit_transform(inputs['Cropname'])
    print(inputs['Cropname'])
    X = dataset.iloc[: , :5]
    y = dataset.iloc[: , -1]
    clf = svm.SVC(kernel= 'linear' , C = 1000)
    clf.fit(X , y)

    newdata = [[soil , h , n , p , k]]
    if(newdata[0][1] <= 3):
        print("Soil is more acidic than required")
    if(newdata[0][1] > 8):
        print("Soil is not compatable for use")
    elif(newdata[0][1] > 3 and newdata[0][1] < 8):
        print(clf.predict(newdata)) 

if(name == "Amravati" or name == "amravati"):
    dataset = pd.read_csv(r"D:\python\soilcsv\amravati.csv")
    inputs = dataset.drop('ph' , axis = 'columns')
    le_cropname = LabelEncoder()
    inputs['Cropname'] = le_cropname.fit_transform(inputs['Cropname'])
    print(inputs['Cropname'])
    X = dataset.iloc[: , :5]
    y = dataset.iloc[: , -1]
    clf = svm.SVC(kernel= 'linear' , C = 1000)
    clf.fit(X , y)

    newdata = [[soil , h , n , p , k]]
    if(newdata[0][1] <= 3):
        print("Soil is more acidic than required")
    if(newdata[0][1] > 8):
        print("Soil is not compatable for use")
    elif(newdata[0][1] > 3 and newdata[0][1] < 8):
        print(clf.predict(newdata)) 
    
if(name == "Kolhapur" or name == "kolhapur"):
    dataset = pd.read_csv(r"D:\python\soilcsv\kolhapur.csv")
    inputs = dataset.drop('ph' , axis = 'columns')
    le_cropname = LabelEncoder()
    inputs['Cropname'] = le_cropname.fit_transform(inputs['Cropname'])
    print(inputs['Cropname'])
    X = dataset.iloc[: , :5]
    y = dataset.iloc[: , -1]
    clf = svm.SVC(kernel= 'linear' , C = 1000)
    clf.fit(X , y)

    newdata = [[soil , h , n , p , k]]
    if(newdata[0][1] <= 3):
        print("Soil is more acidic than required")
    if(newdata[0][1] > 8):
        print("Soil is not compatable for use")
    elif(newdata[0][1] > 3 and newdata[0][1] < 8):
        print(clf.predict(newdata)) 

