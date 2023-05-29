import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from pandas.api.types import is_numeric_dtype
from pandas.api.types import is_string_dtype
from scipy.stats import gaussian_kde
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)


st.title('Stats 21 Discussion Project')
st.subheader('Sofia Jain')

imported_file = st.file_uploader('Upload CSV File', 
                 type=None, 
                 accept_multiple_files=False, 
                 key=None, 
                 help=None, 
                 on_change=None, 
                 args=None, 
                 kwargs=None,
                 disabled=False, 
                 label_visibility="visible")

if imported_file is not None:   
    file_data = pd.read_csv(imported_file)
    st.write(file_data.head())
    st.write('Rows:', file_data.shape[0])
    st.write('Columns:' , file_data.shape[1])
    st.write('Count for variable types:', file_data.dtypes.value_counts())

    col_names = list(file_data.columns.values)
    option = st.selectbox('Select Column', (col_names))

    if(is_numeric_dtype(file_data[option])):
        st.write('Summary Statistics')
        st.write(file_data[option].describe())
        sns.kdeplot(file_data[option], color='purple', fill=True, alpha=.3, linewidth=0)
        st.pyplot()

    if(is_string_dtype(file_data[option])):
        st.write('Proportions of Each Category Level')
        st.write(file_data[option].value_counts(normalize=True))
        my_plot = sns.countplot(x=file_data[option], data=file_data)
        my_plot.set_xticklabels(my_plot.get_xticklabels(), rotation=40, ha="right")
        my_plot.set( ylabel='Count')
        st.pyplot()



    
    


