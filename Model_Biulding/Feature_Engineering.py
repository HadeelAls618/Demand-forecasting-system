
weekly_data = data.groupby([data['WEEK_END_DATE'], data['SUB_CATEGORY']]).agg({
    'UNITS': 'sum',  # Sum of units sold within the week per category
}).reset_index()

data_feat = pd.DataFrame({ "year": weekly_data['WEEK_END_DATE'].dt.year,
                          "month": weekly_data['WEEK_END_DATE'].dt.month,
                          "day": weekly_data['WEEK_END_DATE'].dt.day,
                          "week": weekly_data['WEEK_END_DATE'].dt.isocalendar().week,
                          "quarter": weekly_data['WEEK_END_DATE'].dt.quarter,
                         })

weekly_data= pd.concat([weekly_data, data_feat], axis=1)

# 2. Create new weekly features based on the aggregated weekly data
weekly_data['lag_1_week_units'] = weekly_data.groupby('SUB_CATEGORY')['UNITS'].shift(1)
weekly_data['lag_2_week_units'] = weekly_data.groupby('SUB_CATEGORY')['UNITS'].shift(2)
weekly_data['rolling_mean_4_weeks'] = weekly_data.groupby('SUB_CATEGORY')['UNITS'].shift(1).rolling(window=4).mean()
weekly_data['week_over_week_diff'] = weekly_data['UNITS'] - weekly_data['lag_1_week_units']
weekly_data['percentage_change'] = weekly_data['week_over_week_diff'] / weekly_data['lag_1_week_units']

### Fill lag features with zeros
weekly_data['lag_1_week_units'] = weekly_data['lag_1_week_units'].fillna(0)
weekly_data['lag_2_week_units'] = weekly_data['lag_2_week_units'].fillna(0)

# Drop rows where rolling mean or other computed features are NaN
weekly_data = weekly_data.dropna(subset=['rolling_mean_4_weeks', 'week_over_week_diff', 'percentage_change'])

