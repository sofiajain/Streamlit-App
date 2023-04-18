import streamlit as st


st.title('title of application')
st.markdown('here is a **bold** text')

st.sidebar.title('sidebar')

agree = st.checkbox('Click Me')
if agree:
    st.write('Great!')
    st.markdown('this is *italic text*')

side_check = st.sidebar.checkbox('Click This Box')
if side_check:
     st.sidebar.write('sidebar has been clicked')

st.file_uploader('file uploader', 
                 type=None, 
                 accept_multiple_files=False, 
                 key=None, 
                 help=None, 
                 on_change=None, 
                 args=None, 
                 kwargs=None,
                 disabled=False, 
                 label_visibility="visible")