# Get last week's data
def get_last_week_data(weekly_data, date_column='WEEK_END_DATE'):
    last_week_date = weekly_data[date_column].max()
    return weekly_data[weekly_data[date_column] == last_week_date]

# Prepare features for the next week
def prepare_forecast_features(last_week_data, date_column='WEEK_END_DATE', category_column='SUB_CATEGORY'):
    new_week_features = last_week_data[[date_column, category_column]].copy()
    new_week_features['lag_1_week_units'] = last_week_data['UNITS']
    new_week_features['lag_2_week_units'] = last_week_data['lag_1_week_units']
    new_week_features['rolling_mean_4_weeks'] = last_week_data['rolling_mean_4_weeks']
    new_week_features['week_over_week_diff'] = last_week_data['week_over_week_diff']
    new_week_features['percentage_change'] = last_week_data['percentage_change']
    
    # Set date for next week
    new_week_features[date_column] = last_week_data[date_column].max() + pd.Timedelta(days=7)

    # Create date features
    date_features = pd.DataFrame({
        "year": new_week_features[date_column].dt.year,
        "month": new_week_features[date_column].dt.month,
        "day": new_week_features[date_column].dt.day,
        "week": new_week_features[date_column].dt.isocalendar().week,
        "quarter": new_week_features[date_column].dt.quarter
    })
    new_week_features = pd.concat([new_week_features, date_features], axis=1)
    return new_week_features

# Reorder columns to match training data
def reorder_columns(forecast_features, train_columns):
    return forecast_features[train_columns]

# Predict units for next week
def forecast_units(model, forecast_features):
    forecast_features['predicted_UNITS'] = model.predict(forecast_features)
    forecast_features['predicted_UNITS'] = forecast_features['predicted_UNITS'].round().astype(int)
    return forecast_features

# Run the forecasting pipeline
def main_forecasting(weekly_data, model, train_columns):
    last_week_data = get_last_week_data(weekly_data)
    forecast_features = prepare_forecast_features(last_week_data)
    forecast_features = reorder_columns(forecast_features, train_columns)
    forecasted_data = forecast_units(model, forecast_features)
    return forecasted_data

forecast = main_forecasting(weekly_data, trained_model, x_train.columns)
print(forecast)


