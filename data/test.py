import pandas as pd

df = pd.read_csv('student-mat.csv', sep=';')

print(df.head())

df.drop([
        'school', 'sex', 'address', 'famsize', 'Pstatus',
        'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime',
        'schoolsup', 'famsup', 'paid', 'activities', 'nursery',
        'higher', 'internet', 'romantic', 'famrel', 'freetime',
        'Dalc', 'Walc'
    ], axis='columns', inplace=True)

print(df)