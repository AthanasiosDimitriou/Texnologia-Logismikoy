import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def classification_tab(df):
    st.subheader("Ταξινόμηση")
    algorithms = ["k-NN", "Decision Tree"]
    algorithm = st.selectbox("Επιλέξτε Αλγόριθμο Ταξινόμησης", algorithms)
    k = st.slider("Επιλέξτε k για k-NN", 1, 15) if algorithm == "k-NN" else None
    
    if df.iloc[:, -1].isnull().any():
        st.error("Output variable y contains missing values. Please handle them before proceeding.")
        return
    
    df = df.dropna()
    
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    if algorithm == "k-NN":
        model = KNeighborsClassifier(n_neighbors=k)
    elif algorithm == "Decision Tree":
        model = DecisionTreeClassifier(random_state=42)
    
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    
    st.write(f"**Αλγόριθμος: {algorithm}**")
    st.write(f"Accuracy: {accuracy:.2f}")
    st.write(f"Precision: {precision:.2f}")
    st.write(f"Recall: {recall:.2f}")
    st.write(f"F1 Score: {f1:.2f}")

    if st.checkbox("Σύγκριση με άλλο αλγόριθμο"):
        other_algorithm = [alg for alg in algorithms if alg != algorithm][0]
        st.write(f"Σύγκριση με {other_algorithm}")
        
        if other_algorithm == "k-NN":
            other_model = KNeighborsClassifier(n_neighbors=k)
        elif other_algorithm == "Decision Tree":
            other_model = DecisionTreeClassifier(random_state=42)
        
        other_model.fit(X_train, y_train)
        other_y_pred = other_model.predict(X_test)
        other_accuracy = accuracy_score(y_test, other_y_pred)
        other_precision = precision_score(y_test, other_y_pred, average='weighted')
        other_recall = recall_score(y_test, other_y_pred, average='weighted')
        other_f1 = f1_score(y_test, other_y_pred, average='weighted')
        
        st.write(f"**Algorithm: {other_algorithm}**")
        st.write(f"Accuracy: {other_accuracy:.2f}")
        st.write(f"Precision: {other_precision:.2f}")
        st.write(f"Recall: {other_recall:.2f}")
        st.write(f"F1 Score: {other_f1:.2f}")

        comparison = {
            "Metric": ["Accuracy", "Precision", "Recall", "F1 Score"],
            algorithm: [accuracy, precision, recall, f1],
            other_algorithm: [other_accuracy, other_precision, other_recall, other_f1]
        }
        comparison_df = pd.DataFrame(comparison)
        st.write("Comparison Table:")
        st.write(comparison_df)
