import streamlit as st
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def display_2d_visualization(df):
    st.subheader("2D Visualization")
    method = st.selectbox("Select Dimensionality Reduction Method", ["PCA", "t-SNE"])
    
    # Εξασφάλιση ότι όλες οι στήλες, εκτός της τελευταίας, είναι αριθμητικές
    features = df.iloc[:, :-1]
    if not all(features.dtypes.apply(pd.api.types.is_numeric_dtype)):
        st.error("All feature columns must be numeric for PCA or t-SNE.")
        return

    labels = df.iloc[:, -1]
    
    if method == "PCA":
        reducer = PCA(n_components=2)
    elif method == "t-SNE":
        reducer = TSNE(n_components=2)
    
    components = reducer.fit_transform(features)
    
    fig, ax = plt.subplots()
    sns.scatterplot(x=components[:, 0], y=components[:, 1], hue=labels, ax=ax)
    st.pyplot(fig)
