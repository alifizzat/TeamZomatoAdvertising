import streamlit as st
import pandas as pd
import seaborn as sns
from sklearn. import

st.write("# Simple Advertising Prediction App")
st.write("This app predicts the **Advertising Sales** type!")

st.sidebar.headesr('User Input Parameters')

st.subheader('Class labels and their corresponding index number')
st.write(Y.unique())

st.subheader('Prediction')
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
