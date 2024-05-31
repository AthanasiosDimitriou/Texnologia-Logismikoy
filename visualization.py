import streamlit as st
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def display_2d_visualization(df):
    st.subheader("2D Visualization")
    method = st.selectbox("Επιλογή μεθόδου μείωσης διαστάσεων", ["PCA", "t-SNE"])
    
    # Εξασφάλιση ότι όλες οι στήλες, εκτός της τελευταίας, είναι αριθμητικές
    features = df.iloc[:, :-1]
    if not all(features.dtypes.apply(pd.api.types.is_numeric_dtype)):
        st.error("Όλες οι στήλες χαρακτηριστικών πρέπει να είναι αριθμητικές για PCA ή t-SNE.")
        return

    labels = df.iloc[:, -1]

    # Περιορισμός του αριθμού των δειγμάτων για το t-SNE
    max_samples = st.slider("Μέγιστα δείγματα για την t-SNE", 100, min(len(df), 2000), step=100)
    if method == "t-SNE" and len(df) > max_samples:
        df_sampled = df.sample(n=max_samples, random_state=42)
        features = df_sampled.iloc[:, :-1]
        labels = df_sampled.iloc[:, -1]
    
    if method == "PCA":
        reducer = PCA(n_components=2)
    elif method == "t-SNE":
        reducer = TSNE(n_components=2, perplexity=30, n_iter=300)
    
    components = reducer.fit_transform(features)
    components_df = pd.DataFrame(components, columns=["Component 1", "Component 2"])
    components_df["Label"] = labels.values

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))

    # Scatter plot
    sns.scatterplot(data=components_df, x="Component 1", y="Component 2", hue="Label", ax=ax1)
    ax1.set_title("Scatter Plot")

    # Density plot
    sns.kdeplot(data=components_df, x="Component 1", y="Component 2", hue="Label", fill=True, ax=ax2)
    ax2.set_title("Density Plot")

    # Histogram of Component 1
    sns.histplot(data=components_df, x="Component 1", hue="Label", kde=True, element="step", ax=ax3)
    ax3.set_title("Histogram of Component 1")

    # Histogram of Component 2
    sns.histplot(data=components_df, x="Component 2", hue="Label", kde=True, element="step", ax=ax4)
    ax4.set_title("Histogram of Component 2")

    plt.tight_layout()
    st.pyplot(fig)
