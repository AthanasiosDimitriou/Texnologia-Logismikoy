import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def classification_tab(df):
    st.subheader("Classification")
    k = st.slider("Select k for k-NN", 1, 15)
    
    # Ελέγχουμε για απουσιάζουσες τιμές στη μεταβλητή εξόδου y
    if df.iloc[:, -1].isnull().any():
        st.error("Output variable y contains missing values. Please handle them before proceeding.")
        return
    
    # Αφαιρούμε τις γραμμές που περιέχουν απουσιάζουσες τιμές
    df = df.dropna()
    
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    st.write(f"Accuracy: {accuracy:.2f}")

# Χρήση της συνάρτησης classification_tab(df) όπου df είναι το DataFrame που περιέχει τα δεδομένα
