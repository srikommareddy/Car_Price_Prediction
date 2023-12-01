#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('car_price.pkl', 'rb') 
classifier = pickle.load(pickle_in)

age = st.sidebar.number_input('Age')
km = st.sidebar.number_input('KM')
hp = st.sidebar.number_input('HP')
doors = st.sidebar.number_input('Doors')
gears = st.sidebar.number_input('Gears')
weight = st.sidebar.number_input('Weight')

if st.button("Predict_Price"): 
    d1 = {"Age":[age], "KM":[km], "HP":[hp], "Doors":[doors], "Gears":[gears], "Weight":[weight]}
    df = pd.DataFrame(d1)
    result = classifier.predict(df)
    #st.success('The predicted car price is {}'.format(result))
    st.write(result)

