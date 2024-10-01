import pandas as pd

# Aggregate data by specified columns and sum the target values
def aggregate_weekly_data(data, group_columns, agg_column):
    return data.groupby(group_columns).agg({agg_column: 'sum'}).reset_index()

# Create date-based features (year, month, day, week, quarter)
def create_date_features(data, date_column):
    return pd.DataFrame({
        "year": data[date_column].dt.year,
        "month": data[date_column].dt.month,
        "day": data[date_column].dt.day,
        "week": data[date_column].dt.isocalendar().week,
        "quarter": data[date_column].dt.quarter
    })

# Create lag and rolling mean features for time series
def create_lag_features(data, group_column, target_column):
    data['lag_1_week_units'] = data.groupby(group_column)[target_column].shift(1)
    data['lag_2_week_units'] = data.groupby(group_column)[target_column].shift(2)
    data['rolling_mean_4_weeks'] = data.groupby(group_column)[target_column].shift(1).rolling(window=4).mean()
    data['week_over_week_diff'] = data[target_column] - data['lag_1_week_units']
    data['percentage_change'] = data['week_over_week_diff'] / data['lag_1_week_units']
    return data

# Fill NaN values in specified columns
def fill_missing_values(data, columns, fill_value=0):
    for col in columns:
        data[col] = data[col].fillna(fill_value)
    return data

# Process data: aggregate, create features, and clean
def process_weekly_data(data, date_column, category_column, target_column):
    weekly_data = aggregate_weekly_data(data, [date_column, category_column], target_column)
    date_features = create_date_features(weekly_data, date_column)
    weekly_data = pd.concat([weekly_data, date_features], axis=1)
    weekly_data = create_lag_features(weekly_data, group_column=category_column, target_column=target_column)
    weekly_data = fill_missing_values(weekly_data, columns=['lag_1_week_units', 'lag_2_week_units'])
    weekly_data = weekly_data.dropna(subset=['rolling_mean_4_weeks', 'week_over_week_diff', 'percentage_change'])
    return weekly_data
