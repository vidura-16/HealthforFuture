# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 20:03:45 2022

@author: vidur
"""

import streamlit as st
import joblib
import pandas as pd
from streamlit_option_menu import option_menu
import streamlit.components.v1 as stc
HTML_BANNER = """

     <div style="background-color:#464e5f;padding:5px;border-radius:5px">
     <h1 style="color:white;text-align:center;">Health for Future </h1>
     </div>
     """
stc.html(HTML_BANNER)
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Thalassemia Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    st.write("# Diabetes Prediction")

    col1, col2 = st.columns(2)

# getting user input

    Age = col1.number_input("Enter your age")

    Gender = col2.selectbox("Gender",["Male", "Female"])

    Polyuria = col1.selectbox("Do you have Polyuria",["Yes", "No"])

    Polydipsia = col2.selectbox("Do you have Polydipsia",["Yes", "No"])

    suddenlweightloss = col1.selectbox("Are you currently feel suddenl weight loss?",["Yes","No"])

    weakness = col2.selectbox("Have you ever experienced weakness?",["Yes","No"])

    Polyphagia = col1.selectbox("Do you have Polyphagia?",["Yes","No"])

    Genitalthrush = col2.selectbox("Do you have Genital thrush?",["Yes","No"])

    visualblurring = col1.selectbox("Do you visual blurring?",["Yes","No"])

    Itching = col2.selectbox("Do you Itching?",["Yes","No"])

    Irritability = col1.selectbox("Do you Irritability?",["Yes","No"])

    delayedhealing = col2.selectbox("Do you have any delayed healing?",["Yes","No"])

    partialparesis = col1.selectbox("Do you have partial paresis?",["Yes","No"])

    musclestiffness = col2.selectbox("Do you have muscle stiffness?",["Yes","No"])

    Alopecia = col1.selectbox("Do you have Alopecia",["Yes", "No"])

    Obesity = col2.selectbox("Do you have Obesity",["Yes", "No"])
    
    diab = pd.DataFrame([[Age,Gender,Polyuria,Polydipsia,suddenlweightloss,weakness,Polyphagia,Genitalthrush,visualblurring,Itching,Irritability,delayedhealing,partialparesis,musclestiffness,Alopecia,Obesity]],
    columns= ['Age','Gender','Polyuria','Polydipsia','suddenlweightloss','weakness','Polyphagia','Genitalthrush',
              'visualblurring','Itching','Irritability','delayedhealing','partialparesis','musclestiffness','Alopecia','Obesity'])



    diab['Gender'] = diab['Gender'].apply(lambda x: 1 if x == 'Yes' else 0)

    diab['Polyuria'] = diab['Polyuria'].apply(lambda x: 1 if x == 'Yes' else 0)

    diab['Polydipsia'] = diab['Polydipsia'].apply(lambda x: 1 if x == 'Yes' else 0)

    diab['suddenlweightloss'] = diab['suddenlweightloss'].apply(lambda x: 1 if x == 'Yes' else 0)

    diab['weakness'] = diab['weakness'].apply(lambda x: 1 if x == 'Yes' else 0)

    diab['Polyphagia'] = diab['Polyphagia'].apply(lambda x: 1 if x == 'Yes' else 0)

    diab['Genitalthrush'] = diab['Genitalthrush'].apply(lambda x: 1 if x == 'Yes' else 0)

    diab['visualblurring'] = diab['visualblurring'].apply(lambda x: 1 if x == 'Yes' else 0)

    diab['Itching'] = diab['Itching'].apply(lambda x: 1 if x == 'Yes' else 0)

    diab['Irritability'] = diab['Irritability'].apply(lambda x: 1 if x == 'Yes' else 0)

    diab['delayedhealing'] = diab['delayedhealing'].apply(lambda x: 1 if x == 'Yes' else 0)

    diab['partialparesis'] = diab['partialparesis'].apply(lambda x: 1 if x == 'Yes' else 0)

    diab['musclestiffness'] = diab['musclestiffness'].apply(lambda x: 1 if x == 'Yes' else 0)

    diab['Alopecia'] = diab['Alopecia'].apply(lambda x: 1 if x == 'Yes' else 0)

    diab['Obesity'] = diab['Obesity'].apply(lambda x: 1 if x == 'Yes' else 0)



    model = joblib.load('C:/Users/vidur/Desktop/Final/diab_model.pkl')
    prediction = model.predict(diab)


    if st.button('Predict'):

        if(prediction[0]==0):
            st.write('<p class="big-font">You likely will not develop diab disease in 10 years.</p>',unsafe_allow_html=True)

        else:
            st.write('<p class="big-font">You are likely to develop diab disease in 10 years.</p>',unsafe_allow_html=True)
            

# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    

    st.write("# Heart Disease Prediction")

    col1, col2, col3 = st.columns(3)

# getting user input

    HighBP = col1.selectbox("Do you have HighBP",["Yes", "No"])

    HighChol = col2.selectbox("Do you have cholectrol",["Yes", "No"])
    
    CholCheck = col3.selectbox("Chol check",["Yes", "No"])

    BMI = col1.number_input("Enter your BMI level")

    Smoker = col2.selectbox("Are you currently a smoker?",["Yes","No"])

    Stroke = col3.selectbox("Have you ever experienced a stroke?",["Yes","No"])

    Diabetes = col1.selectbox("Do you have diabetes?",["Yes","No"])

    PhysActivity = col2.selectbox("Do you have Phsy activity?",["Yes","No"])

    Fruits = col3.selectbox("Do you eat Fruits?",["Yes","No"])

    Veggies = col1.selectbox("Do you eat Veggies?",["Yes","No"])

    HvyAlcoholConsump = col2.selectbox("Do you have Alchohol?",["Yes","No"])

    AnyHealthcare = col3.selectbox("Do you have any health activities?",["Yes","No"])

    NoDocbcCost = col1.selectbox("Do you have no docc cost?",["Yes","No"])

    DiffWalk = col2.selectbox("Do you have Diffwalk?",["Yes","No"])

    Sex = col3.selectbox("Enter your gender",["Male", "Female"])

    Age = col1.number_input("Enter your age")

    df_pred = pd.DataFrame([[HighBP,HighChol,CholCheck,BMI,Smoker,Stroke,Diabetes,PhysActivity,Fruits,Veggies,HvyAlcoholConsump,AnyHealthcare,NoDocbcCost,DiffWalk,Sex,Age]],
                           columns= ['HighBP','HighChol','CholCheck','BMI','Smoker','Stroke','Diabetes','PhysActivity','Fruits','Veggies','HvyAlcoholConsump',
                                     'AnyHealthcare','NoDocbcCost','DiffWalk','Sex','Age'])

    df_pred['HighBP'] = df_pred['HighBP'].apply(lambda x: 1 if x == 'Yes' else 0)

    df_pred['HighChol'] = df_pred['HighChol'].apply(lambda x: 1 if x == 'Yes' else 0)

    df_pred['CholCheck'] = df_pred['CholCheck'].apply(lambda x: 1 if x == 'Yes' else 0)

    df_pred['Smoker'] = df_pred['Smoker'].apply(lambda x: 1 if x == 'Yes' else 0)

    df_pred['Stroke'] = df_pred['Stroke'].apply(lambda x: 1 if x == 'Yes' else 0)

    df_pred['Diabetes'] = df_pred['Diabetes'].apply(lambda x: 1 if x == 'Yes' else 0)

    df_pred['PhysActivity'] = df_pred['PhysActivity'].apply(lambda x: 1 if x == 'Yes' else 0)

    df_pred['Fruits'] = df_pred['Fruits'].apply(lambda x: 1 if x == 'Yes' else 0)

    df_pred['Veggies'] = df_pred['Veggies'].apply(lambda x: 1 if x == 'Yes' else 0)

    df_pred['HvyAlcoholConsump'] = df_pred['HvyAlcoholConsump'].apply(lambda x: 1 if x == 'Yes' else 0)

    df_pred['AnyHealthcare'] = df_pred['AnyHealthcare'].apply(lambda x: 1 if x == 'Yes' else 0)

    df_pred['NoDocbcCost'] = df_pred['NoDocbcCost'].apply(lambda x: 1 if x == 'Yes' else 0)

    df_pred['DiffWalk'] = df_pred['DiffWalk'].apply(lambda x: 1 if x == 'Yes' else 0)

    df_pred['Sex'] = df_pred['Sex'].apply(lambda x: 1 if x == 'Yes' else 0)


    model = joblib.load('C:/Users/vidur/Desktop/Final/heart_model.pkl')
    prediction = model.predict(df_pred)


    if st.button('Predict'):

        if(prediction[0]==0):
            st.write('<p class="big-font">You likely will not develop heart disease in 10 years.</p>',unsafe_allow_html=True)

        else:
            st.write('<p class="big-font">You are likely to develop heart disease in 10 years.</p>',unsafe_allow_html=True)
            
            

# Thalassemia Prediction Page
if (selected == 'Thalassemia Prediction'):
    
    
    st.write("# Thalassemia Prediction")

    col1, col2 = st.columns(2)

# getting user input

    sex = col1.selectbox("Gender",["Male", "Female"])

    hb = col2.number_input("Hemoglobin concentration in grams per decilitre")

    pcv = col1.number_input("Pack cell volume/hematocrit ")

    rbc = col2.number_input("Red blood cell volume")

    rdw = col1.number_input("Red blood cell distribution ")

    wbc = col2.number_input("Total white blood cell count")

    neut = col1.number_input("Total white blood cell count with white blood cell types")

    plt = col2.number_input("Total platelet count ")

    thal = pd.DataFrame([[sex,hb,pcv,rbc,rdw,wbc,neut,plt]],
                            columns= ['sex','hb','pcv','rbc','rdw','wbc','neut','plt'])


    thal['sex'] = thal['sex'].apply(lambda x: 1 if x == 'Yes' else 0)


    model = joblib.load('C:/Users/vidur/Desktop/Final/thal_model.pkl')
    prediction = model.predict(thal)


    if st.button('Predict'):

        if(prediction[0]==0):
            st.write('<p class="big-font">You are not Alpha Thalassemia carrier.</p>',unsafe_allow_html=True)

        else:
            st.write('<p class="big-font">You are a Alpha Thalassemia carrier.</p>',unsafe_allow_html=True)




