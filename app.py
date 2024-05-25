import streamlit as st
from data_loader import load_data
from visualization import display_2d_visualization
from classification import classification_tab
from clustering import clustering_tab

st.title("Data Analysis Application")

# Load Data
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = load_data(uploaded_file)
    st.write("Data loaded successfully!")
    st.write(df)
    
    # 2D Visualization Tab
    if st.sidebar.checkbox('Enable 2D Visualization'):
        display_2d_visualization(df)
    
    # Classification Tab
    if st.sidebar.checkbox('Enable Classification'):
        classification_tab(df)
    
    # Clustering Tab
    if st.sidebar.checkbox('Enable Clustering'):
        clustering_tab(df)

# Info Tab
if st.sidebar.checkbox('Enable Info'):
    st.subheader("Application Information")
    st.write("""
    This application was developed for the Software Technology course. 
    It allows users to perform data analysis and machine learning tasks such as 
    classification and clustering. The application is built using Streamlit and Python, 
    and supports various features including data loading, visualization, and algorithm comparison.
    """)
