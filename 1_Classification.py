import streamlit as slt
import joblib


slt.set_page_config(
    page_title="IRIS CLASSIFICATION",
    page_icon= "🌼"
)

slt.title("IRIS Classification")

slt.image("images/main_img.png")
slt.text("Input the details of a flower and predict which species they belong to (versicolor, setosa, virginica)")

def check_valid(i):
    if i is None or i <= 0:
        slt.markdown('<span style="color:red">Please enter a valid number greater than 0</span>', unsafe_allow_html=True)
        

slt.text("Fill the following inputs")

sepal_lengths = slt.number_input(label="sepal Length (CM)", value=0.1)
check_valid(sepal_lengths)

sepal_width = slt.number_input(label="sepal width (CM)", value=0.1)
check_valid(sepal_width)

petal_lengths = slt.number_input(label="petal length (CM)", value=0.1)
check_valid(petal_lengths)

petal_width = slt.number_input(label="petal width (CM)", value=0.1)
check_valid(petal_width)

option = ["Logistic Regression", "Decision Trees", "Random Forest", "Support Vector Machines", "K-Nearest Neighbors"]
options = slt.selectbox(label="Multi Class Classification Model",options=option)
classify_btn = slt.button(label="Classify")

if classify_btn:
    
    if options == "Logistic Regression":
       model = joblib.load("models/lr_model")
       score = joblib.load("scores/lr_score")
    elif options == "Decision Trees":
        model = joblib.load("models/dt_model")
        score = joblib.load("scores/dt_score")
    elif options == "Random Forest":
        model = joblib.load("models/rf_model")
        score = joblib.load("scores/rf_score")  
    elif options == "Support Vector Machines":
        model = joblib.load("models/svm_model")
        score = joblib.load("scores/svm_score")
    elif options == "K-Nearest Neighbors":
        model = joblib.load("models/knn_model")
        score = joblib.load("scores/knn_score")
    
    sample = [[sepal_lengths,sepal_width,petal_lengths,petal_width]]
    result = model.predict(sample)[0]
    score = (round(score,4))*100
    slt.text("A. The Predicted Species is: "+result)
    slt.text("B. The selected model is: "+options)
    slt.text("C. Model accuracy score is: "+str(score)+"%")