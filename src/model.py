from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

def train_model(X_train, y_train, model_type='linear'):
    # Choose model type based on user input
    if model_type == 'linear':
        model = LinearRegression()
    elif model_type == 'tree':
        model = DecisionTreeRegressor()
    else:
        raise ValueError("Model type not supported. Use 'linear' or 'tree'.")

    # Train the model with training data
    model.fit(X_train, y_train)

    # Return trained model
    return model
