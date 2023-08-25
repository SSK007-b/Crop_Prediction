import streamlit as st
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC


st.title(" CROP PREDICTION ")
def load_utils():
    model = joblib.load("konkan.pkl")
    scalar = joblib.load("Kscalar.pkl")
    return model , scalar

def load_data():
    model1 = joblib.load("Pune.pkl")
    scalar1 = joblib.load("Pscalar.pkl")
    return model1 , scalar1

def load_data1():
    model2 = joblib.load("Nagpur.pkl")
    scalar2 = joblib.load("ngscalar.pkl")
    return model2 , scalar2

def load_data2():
    model3 = joblib.load("Nashik.pkl")
    scalar3 = joblib.load("nsscalar.pkl")
    return model3 , scalar3

def load_data3():
    model4 = joblib.load("Kolhapur.pkl")
    scalar4 = joblib.load("koscalar.pkl")
    return model4 , scalar4

def load_data4():
    model4 = joblib.load("amravati.pkl")
    scalar4 = joblib.load("amscalar.pkl")
    return model4 , scalar4

def load_data5():
    model1 = joblib.load("aurangabad.pkl")
    scalar1 = joblib.load("auscalar.pkl")
    return model1 , scalar1

state = st.selectbox("Enter the state" , ("Konkan" , "Pune" , "Nagpur" , "Nashik" , "Amravati" , "Kolhapur" , "Aurangabad"))
soil = st.selectbox("Enter the soil type" , ("Sandy" , "Slit" , "Clay" , "Lomey"))
if(soil == "Sandy"):
    sty = 1
elif(soil == "Slit"):
    sty = 2
elif(soil == "Clay"):
    sty = 3
elif(soil == "Lomey"):
    sty = 4
ph = st.number_input("Enter the ph of the soil")
n = st.number_input("Enter the nitrogen precentage present in soil")
p = st.number_input("Enter the phosphrous precentage present in soil")
k = st.number_input("Enter the potassium precentage present in soil")

button = st.button("Predict crop")

if(state == "Konkan"):
    if(button):
        display = ""
        model , scalar = load_utils()
        ans = model.predict([[sty , ph , n , p ,k]])
        for i in ans:
            display = i + display
        st.write("# The Best crop is: " , (display))
        
    else:
        st.write("Prediction of the Crop")

elif(state == "Pune"):
    if(button):
        display = ""
        model , scalar = load_data()
        ans = model.predict([[sty , ph , n , p ,k]])
        for i in ans:
            display = i + display
        st.write("# The Best crop is: " , (display))
        
    else:
        st.write("Prediction of the Crop")

elif(state == "Nagpur"):
    if(button):
        display = ""
        model , scalar = load_data1()
        ans = model.predict([[sty , ph , n , p ,k]])
        for i in ans:
            display = i + display
        st.write("# The Best crop is: " , (display))
        
    else:
        st.write("Prediction of the Crop")

elif(state == "Nashik"):
    if(button):
        display = ""
        model , scalar = load_data2()
        ans = model.predict([[sty , ph , n , p ,k]])
        for i in ans:
            display = i + display
        st.write("# The Best crop is: " , (display))
        
    else:
        st.write("Prediction of the Crop")

elif(state == "Kolhapur"):
    if(button):
        display = ""
        model , scalar = load_data3()
        ans = model.predict([[sty , ph , n , p ,k]])
        for i in ans:
            display = i + display
        st.write("# The Best crop is: " , (display))
        
    else:
        st.write("Prediction of the Crop")

elif(state == "Amravati"):
    if(button):
        display =""
        model , scalar = load_data4()
        ans = model.predict([[sty , ph , n , p ,k]])
        for i in ans:
            display = i + display
        st.write("# The Best crop is: " , (display))
        
    else:
        st.write("Prediction of the Crop")

elif(state == "Aurangabad"):
    if(button):
        display = ""
        model , scalar = load_data5()
        ans = model.predict([[sty , ph , n , p ,k]])
        for i in ans:
            display = i + display
        st.write("# The Best crop is: " , (display))
        
    else:
        st.write("Prediction of the Crop")