
import numpy as np
from sklearn.metrics import mean_squared_log_error

# Calculate RMSLE between actual and predicted values
def rmsle(y_true, y_pred):
    return np.sqrt(mean_squared_log_error(y_true, y_pred))

# Perform predictions and evaluate using RMSLE
def evaluate_xgb_model(model_xgb, x_test, y_test):
    pred_xgb = model_xgb.predict(x_test)  # Make predictions on test data
    rmsle_score = rmsle(y_test, pred_xgb)  # Compute RMSLE
    print(f"RMSLE Score: {rmsle_score:.4f}")  # Print the RMSLE score
    return rmsle_score

rmsle_score = evaluate_xgb_model(trained_model, x_test, y_test)

