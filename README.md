# ScoreGenie 🎓

**ScoreGenie** is a simple machine learning project that predicts a student’s final exam grade based on their personal and academic data. This project demonstrates data preprocessing, model training, evaluation, and an interactive web app using Streamlit.

---

## Features

- Data cleaning and encoding of categorical features  
- Exploratory Data Analysis (EDA) with visualizations  
- Model training with Linear Regression and Decision Tree Regressor  
- Model evaluation using MAE, RMSE, and R² score  
- Interactive Streamlit app for live predictions  

---

## Dataset

The project uses the [Student Performance Dataset](https://archive.ics.uci.edu/ml/datasets/Student+Performance) from the UCI Machine Learning Repository.

---

## Project Structure

ScoreGenie/
│
├── data/
│ └── student-mat.csv # Dataset
├── notebooks/
│ └── eda.py # Exploratory Data Analysis
├── src/
│ ├── preprocessing.py # Data loading and preprocessing
│ ├── model.py # Model training code
│ └── evaluate.py # Model evaluation metrics
├── app/
│ └── streamlit_app.py # Interactive Streamlit app
├── main.py # Main script to train and evaluate model
├── requirements.txt # Dependencies
└── README.md # Project overview and instructions

---

## Setup and Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/ScoreGenie.git
    cd ScoreGenie
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the main training and evaluation script:
    ```bash
    python main.py
    ```

4. (Optional) Launch the Streamlit app for interactive predictions:
    ```bash
    streamlit run app/streamlit_app.py
    ```

---

## Usage

- Use `main.py` to train the model and see evaluation metrics in the console.
- Use the Streamlit app (`streamlit_app.py`) to input student data and get predicted final grades via a simple web interface.

---

## License

This project is open-source and available under the MIT License.

---

## Acknowledgments

- Dataset from UCI Machine Learning Repository  
- Built with Python, scikit-learn, pandas, and Streamlit

---

Feel free to reach out if you want to contribute or have questions!
