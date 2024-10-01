import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from feature_engineering import process_weekly_data  # Import from feature_engineering.py

# Split data into train and test sets
def split_data(data, target_column, test_size=0.2):
    features = data.drop(columns=[target_column])
    target = data[target_column]
    return train_test_split(features, target, test_size=test_size, random_state=0)

# Train an XGBoost model
def train_xgb_model(x_train, y_train, learning_rate=0.1, max_depth=5, n_estimators=200, reg_alpha=0.1, reg_lambda=10, random_state=0):
    model = XGBRegressor(
        learning_rate=learning_rate,
        max_depth=max_depth,
        n_estimators=n_estimators,
        reg_alpha=reg_alpha,
        reg_lambda=reg_lambda,
        random_state=random_state
    )
    model.fit(x_train, y_train)
    return model

# Main function to integrate processing and training
def main(data):
    weekly_data = process_weekly_data(data, date_column='WEEK_END_DATE', category_column='SUB_CATEGORY', target_column='UNITS')
    x_train, x_test, y_train, y_test = split_data(weekly_data, target_column='UNITS')
    model = train_xgb_model(x_train, y_train)
    return model, x_test, y_test

# Example usage:
# data = pd.read_csv('path_to_data.csv')  # Load your dataset here
# trained_model, x_test, y_test = main(data)
