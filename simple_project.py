import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

titanic_df = pd.read_csv('https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv')
titanic_df.info()

st.title('Titanic Project')