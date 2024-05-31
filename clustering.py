import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score

def clustering_tab(df):
    st.subheader("Ομαδοποίηση")
    algorithms = ["k-means", "Agglomerative Clustering"]
    algorithm = st.selectbox("Επιλογή Αλγορίθμου Ομαδοποίησης", algorithms)
    k = st.slider("Select number of clusters (k)", 2, 10)
    
    X = df.iloc[:, :-1]
    
    if algorithm == "k-means":
        model = KMeans(n_clusters=k, random_state=42)
    elif algorithm == "Agglomerative Clustering":
        model = AgglomerativeClustering(n_clusters=k)
    
    labels = model.fit_predict(X)
    silhouette = silhouette_score(X, labels)
    davies_bouldin = davies_bouldin_score(X, labels)
    calinski_harabasz = calinski_harabasz_score(X, labels)
    
    st.write(f"**Αλγόριθμος: {algorithm}**")
    st.write(f"Silhouette Score: {silhouette:.2f}")
    st.write(f"Davies-Bouldin Score: {davies_bouldin:.2f}")
    st.write(f"Calinski-Harabasz Score: {calinski_harabasz:.2f}")

    if st.checkbox("Σύγκριση με άλλο αλγόριθμο"):
        other_algorithm = [alg for alg in algorithms if alg != algorithm][0]
        st.write(f"Σύγκριση με {other_algorithm}")
        
        if other_algorithm == "k-means":
            other_model = KMeans(n_clusters=k, random_state=42)
        elif other_algorithm == "Agglomerative Clustering":
            other_model = AgglomerativeClustering(n_clusters=k)
        
        other_labels = other_model.fit_predict(X)
        other_silhouette = silhouette_score(X, other_labels)
        other_davies_bouldin = davies_bouldin_score(X, other_labels)
        other_calinski_harabasz = calinski_harabasz_score(X, other_labels)
        
        st.write(f"**Αλγόριθμος: {other_algorithm}**")
        st.write(f"Silhouette Score: {other_silhouette:.2f}")
        st.write(f"Davies-Bouldin Score: {other_davies_bouldin:.2f}")
        st.write(f"Calinski-Harabasz Score: {other_calinski_harabasz:.2f}")

        comparison = {
            "Metric": ["Silhouette Score", "Davies-Bouldin Score", "Calinski-Harabasz Score"],
            algorithm: [silhouette, davies_bouldin, calinski_harabasz],
            other_algorithm: [other_silhouette, other_davies_bouldin, other_calinski_harabasz]
        }
        comparison_df = pd.DataFrame(comparison)
        st.write("Πίνακας σύγκρισης:")
        st.write(comparison_df)
