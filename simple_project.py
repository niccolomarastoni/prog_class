import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

titanic_df = pd.read_csv('https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv')
titanic_df.info()

st.title('Titanic Project')
st.header('a simple project with the Titanic dataset')
st.text('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

st.sidebar.header('Settings')
if st.sidebar.checkbox('show dataframe'):
    st.write(titanic_df.head(5))

st.checkbox('fake checkbox')

col_1, col_2, col_3 = st.columns(3)

with col_1:
    st.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

with col_3:
    st.write(titanic_df)


st.sidebar.code(''' import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st''')

box_select = st.selectbox('select feature', ['Age', 'Pclass'])

if box_select == 'Age':
    fig, ax = plt.subplots()
    ax.hist(titanic_df.Age)
    st.write(fig)

else:
    fig, ax = plt.subplots()
    ax.hist(titanic_df.Pclass)
    st.write(fig)