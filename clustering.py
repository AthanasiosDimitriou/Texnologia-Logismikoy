import streamlit as st
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def clustering_tab(df):
    st.subheader("Clustering")
    k = st.slider("Select number of clusters (k) for k-means", 2, 10)
    X = df.iloc[:, :-1]
    model = KMeans(n_clusters=k, random_state=42)
    labels = model.fit_predict(X)
    silhouette = silhouette_score(X, labels)
    st.write(f"Silhouette Score: {silhouette:.2f}")
