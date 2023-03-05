# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 00:39:23 2022

@author: vidur
"""
import pyrebase
import streamlit as st
from datetime import datetime

firebaseConfig = {

  'apiKey': "AIzaSyDdHjfPR20fgukaKo924L5C0F2NAvdFisA",

  'authDomain': "healthforfuture-e0f17.firebaseapp.com",

  'projectId': "healthforfuture-e0f17",

  'databaseURL':"https://healthforfuture-e0f17-default-rtdb.firebaseio.com/",

  'storageBucket': "healthforfuture-e0f17.appspot.com",

  'messagingSenderId': "749850797975",

  'appId': "1:749850797975:web:a294fc505ccd73bf2c06d2",

  'measurementId': "G-14JX6S8XVD"

};


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

#db

db = firebase.database()
storage = firebase.storage()

st.sidebar.title("Health for Future")


choice = st.sidebar.selectbox('Login/Signup',['Login','Signup'])

username = st.sidebar.text_input("add your username")
password = st.sidebar.text_input("add your passoword")
