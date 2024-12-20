import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from PIL import Image
import os

st.write("""
# Simple Iris Flower Prediction App
This app predicts the **Iris flower** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
predicted_class = iris.target_names[prediction][0]
st.write(predicted_class)

# Dynamically construct the path to images folder
current_dir = os.path.dirname(os.path.abspath(__file__))
image_folder = os.path.join(current_dir, "images")

# Load and display the corresponding image
if predicted_class == 'setosa':
    image_path = os.path.join(image_folder, 'setosa.jpg')
elif predicted_class == 'versicolor':
    image_path = os.path.join(image_folder, 'versicolor.jpg')
else:
    image_path = os.path.join(image_folder, 'virginica.jpg')

try:
    image = Image.open(image_path)
    st.image(image, caption=f'This is a {predicted_class} iris flower.', use_column_width=True)
except FileNotFoundError:
    st.error(f"Image file not found at {image_path}. Please ensure the file exists.")

st.subheader('Prediction Probability')
st.write(prediction_proba)
