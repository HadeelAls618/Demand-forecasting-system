
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBRegressor

# Encode categorical columns
def encode_categorical_columns(data, columns):
    label_encoder = LabelEncoder()
    for col in columns:
        data[col] = label_encoder.fit_transform(data[col])
    return data

# Set date column as index and drop it
def preprocess_data(data, date_column):
    data[date_column] = pd.to_datetime(data[date_column])
    data.index = data[date_column]
    return data.drop(date_column, axis=1)

# Convert columns to int64 type
def convert_columns_to_int(data, columns):
    for col in columns:
        data[col] = data[col].astype('int64')
    return data

# Split data into train and test sets
def split_data(data, target_column, train_size=0.8):
    split_point = int(len(data) * train_size)
    train_data = data.iloc[:split_point]
    test_data = data.iloc[split_point:]
    return train_data.drop([target_column], axis=1), test_data.drop([target_column], axis=1), train_data[target_column], test_data[target_column]

# Build and train the model
def build_and_train_model(x_train, y_train, learning_rate=0.1, max_depth=5, n_estimators=200, reg_alpha=0.1, reg_lambda=10, random_state=0):
    model = XGBRegressor(learning_rate=learning_rate, max_depth=max_depth, n_estimators=n_estimators, reg_alpha=reg_alpha, reg_lambda=reg_lambda, random_state=random_state)
    model.fit(x_train, y_train)
    return model

# Main function to preprocess, split, and train
def main(weekly_data):
    weekly_data = encode_categorical_columns(weekly_data, columns=['SUB_CATEGORY'])
    weekly_data = preprocess_data(weekly_data, date_column='WEEK_END_DATE')
    weekly_data = convert_columns_to_int(weekly_data, columns=['week'])
    x_train, x_test, y_train, y_test = split_data(weekly_data, target_column='UNITS')
    model_xgb = build_and_train_model(x_train, y_train)
    return model_xgb

# Example usage:
# trained_model = main(weekly_data)
