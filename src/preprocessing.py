import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def load_and_clean_data(path):
    # Load dataset from CSV file
    df = pd.read_csv(path, sep=';')

    # Drop columns that are not useful for prediction
    df.drop([
        'school', 'sex', 'address', 'famsize', 'Pstatus',
        'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime',
        'schoolsup', 'famsup', 'paid', 'activities', 'nursery',
        'higher', 'internet', 'romantic', 'famrel', 'freetime',
        'Dalc', 'Walc'
    ], axis='columns', inplace=True)

    # print(df.head())

    # Encode all categorical string columns into numerical values
    label_encoders = {}
    for column in df.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le

    # Return processed dataframe and encoders (for future decoding if needed)
    return df, label_encoders

def split_data(df, target='G3', test_size=0.2, random_state=42):
    # Separate features (X) and target variable (y)
    X = df.drop(target, axis=1)
    y = df[target]

    # Split the dataset into training and testing sets
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
