from src.preprocessing import load_and_clean_data, split_data
from src.model import train_model
from src.evaluate_model import evaluate_model

def main():
    # Load and preprocess dataset
    df, encoders = load_and_clean_data("data/student-mat.csv")

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = split_data(df)

    # Train model (choose 'linear' or 'tree')
    model = train_model(X_train, y_train, model_type='linear')

    # Evaluate model performance
    evaluate_model(model, X_test, y_test)

# Run the main function
if __name__ == "__main__":
    main()
