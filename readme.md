# 🌸 Iris Classification App

This project is a **machine learning web application** built with **Streamlit** that classifies Iris flowers using five different algorithms:

-   **Logistic Regression**
-   **K-Nearest Neighbors (KNN)**
-   **Support Vector Machine (SVM)**
-   **Decision Tree**
-   **Random Forest**

The app visualizes **Precision-Recall Curves** to evaluate the models' performance and helps users interactively explore how different classifiers perform on the Iris dataset.

## 🚀 Live Demo

[🔗 Click here to try the app](https://iris-classification-v4hjbnlnwm2noqhedlxbjr.streamlit.app/)

* * *

## 📊 Features

-   🧠 Train and test five popular ML models on the Iris dataset.
-   📈 Visual comparison of performance using **Precision-Recall Curves**.
-   🔍 Interactive UI with options to choose model and visualize results.

* * *

## 🛠️ Installation

1.  **Clone the repository:**

    bash

    CopyEdit

    `git clone https://github.com/your-username/iris-classification-app.git cd iris-classification-app`

2.  **Create a virtual environment (optional but recommended):**

    bash

    CopyEdit

    `` python -m venv venv source venv/bin/activate  # On Windows use `venv\Scripts\activate` ``

3.  **Install dependencies:**

    bash

    CopyEdit

    `pip install -r requirements.txt`

4.  **Run the app:**

    bash

    CopyEdit

    `streamlit run app.py`

* * *

## 🧪 Evaluation Metrics

We use **Precision-Recall Curves** to evaluate model performance, especially useful for imbalanced datasets. The app displays:

-   Precision
-   Recall
-   PR Curve (one-vs-rest for multi-class)
* * *

## 📊 Dataset

-   **Source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris)
-   **Classes**: Setosa, Versicolor, Virginica
-   **Features**: Sepal length/width, Petal length/width
* * *

## 📦 Dependencies

-   `scikit-learn`
-   `matplotlib`
-   `pandas`
-   `numpy`
-   `joblib`
-   `streamlit`

You can find all dependencies in the `requirements.txt`.

* * *

## 📤 Deployment

To deploy the app using Streamlit Cloud:

1.  Push the code to a GitHub repo.
2.  Go to Streamlit Cloud, sign in with GitHub, and select the repo.
3.  Set the main file path to `1_classification.py`.
4.  Click **Deploy**.
* * *

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo, open issues, or submit PRs.


* * *

## 📬 Contact

-   **Author**: Apoorv Tripathi
-   **Email**: apoorvtripathi537@gmail.com
-   **LinkedIn**: [@your-username](https://www.linkedin.com/in/apoorv-tripathi-19b132178/)
