import joblib 
import pandas as pd

forest_pipeline = joblib.load('./models/finished_model.joblib')
encoder = joblib.load('./models/encoder.joblib')

columns = ['Age', 'Department', 'DistanceFromHome', 'Education', 'EducationField',
       'EnvironmentSatisfaction', 'JobSatisfaction', 'MaritalStatus',
       'MonthlyIncome', 'NumCompaniesWorked', 'WorkLifeBalance',
       'YearsAtCompany']

df = pd.DataFrame(columns=columns)

df[0] = [41, 'Sales',1,2,'Life' 'Sciences',2,4,'Single',5993,8,1,6,]

prediction = forest_pipeline.predict(df)

threshold = 0.18

y_pred_proba = forest_pipeline.predict_proba(df)[:, 1]

binary_prediction = (y_pred_proba >= threshold)

print(binary_prediction)