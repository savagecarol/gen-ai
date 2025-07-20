import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

df,target_names = load_data()
st.title("Iris Classification App")
st.write("This app classifies iris species based on features.")
st.write("Dataset:")
st.dataframe(df)      

model = RandomForestClassifier()
model.fit(df.iloc[:, :-1] , df['species'])

st.sidebar.header("User Input Features")
sepal_length = st.sidebar.slider("Sepal Length", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()), float(df['sepal length (cm)'].mean()))
sepal_width = st.sidebar.slider("Sepal Width", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()), float(df['sepal width (cm)'].mean()))
petal_length = st.sidebar.slider("Petal Length", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()), float(df['petal length (cm)'].mean()))
petal_width = st.sidebar.slider("Petal Width", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()), float(df['petal width (cm)'].mean()))
input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = model.predict(input_data)

predicted_Species = target_names[prediction][0]
st.write(f"Predicted Species: {predicted_Species}")
st.write("Model Accuracy on Training Data:", accuracy_score(df['species'], model.predict(df.iloc[:, :-1])))
st.write("Model Parameters:")
st.write(model.get_params())
st.write("Feature Importances:")
importance_df = pd.DataFrame({
    "Feature": df.columns[:-1],
    "Importance": model.feature_importances_
})
st.bar_chart(importance_df.set_index("Feature"))
st.write("Model Predictions on Training Data:")
predictions = model.predict(df.iloc[:, :-1])
df['predicted_species'] = predictions
st.write(df[['species', 'predicted_species']].head(10))
