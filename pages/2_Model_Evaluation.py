import streamlit as slt

slt.title("Performance of each model by using precision recall plots")

slt.header("Logistic Regression")
slt.image("outputs/lr_plot.png")

slt.header("Decision Trees")
slt.image("outputs/dt_plot.png")

slt.header("Random Forests")
slt.image("outputs/rf_plot.png")

slt.header("K-Nearest Neighbour")
slt.image("outputs/knn_plot.png")

slt.header("Support Vector Machines")
slt.image("outputs/svm_plot.png")