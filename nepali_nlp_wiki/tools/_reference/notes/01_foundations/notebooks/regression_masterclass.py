"""
📊 REGRESSION MASTERCLASS: LSM to XGBOOST
-----------------------------------------
A comprehensive exploration of regression models:
1. Pure NumPy: LSM, Batch GD, SGD, Mini-batch.
2. Sklearn: Linear, Ridge, RandomForest, MLP (Neural Net).
3. Advanced: XGBoost with GridSearchCV & K-Fold CV.

Datasets: Linear, Quadratic, and Tabular (train.csv).
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.metrics import mean_squared_error

# --- 1. THE FOUNDATION: SCRATCH OPTIMIZATION ---
class ScratchRegression:
    def __init__(self):
        self.theta = None

    def solve_lsm(self, X, y):
        # theta = (X^T * X)^-1 * X^T * y
        self.theta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

    def solve_gd(self, X, y, lr=0.1, n_epochs=50, batch_size=32):
        m = len(y)
        self.theta = np.random.randn(X.shape[1], 1)
        for epoch in range(n_epochs):
            indices = np.random.permutation(m)
            X_s, y_s = X[indices], y[indices]
            for i in range(0, m, batch_size):
                xi, yi = X_s[i:i+batch_size], y_s[i:i+batch_size]
                gradients = 2/len(xi) * xi.T.dot(xi.dot(self.theta) - yi)
                self.theta -= lr * gradients

# --- 2. THE PIPELINE: FEATURE ENGINEERING ---
def prepare_full_pipeline(train_df, test_df, target_col='price'):
    num_features = ['weight', 'table_pct', 'depth_pct', 'd1', 'd2', 'd3']
    cat_features = ['cut_quality', 'hue', 'purity']
    
    # 1. Impute & Poly
    imputer = SimpleImputer(strategy='mean')
    X_train_num = imputer.fit_transform(train_df[num_features])
    X_test_num = imputer.transform(test_df[num_features])
    
    poly = PolynomialFeatures(degree=2, include_bias=False)
    X_train_poly = poly.fit_transform(X_train_num)
    X_test_poly = poly.transform(X_test_num)
    
    # 2. Scale
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train_poly)
    X_test_scaled = scaler.transform(X_test_poly)
    
    # 3. Categorical (One-Hot)
    train_cat = pd.get_dummies(train_df[cat_features])
    test_cat = pd.get_dummies(test_df[cat_features])
    
    # Align categorical columns
    test_cat = test_cat.reindex(columns=train_cat.columns, fill_value=0)
    
    # 4. Combine
    X_train_final = np.hstack([X_train_scaled, train_cat.values])
    X_test_final = np.hstack([X_test_scaled, test_cat.values])
    
    return X_train_final, X_test_final, train_df[target_col]

# --- 3. THE OPTIMIZER: GRID SEARCH ---
def tune_xgboost(X, y):
    param_grid = {
        'n_estimators': [200, 400],
        'learning_rate': [0.01, 0.1],
        'max_depth': [5, 9]
    }
    grid = GridSearchCV(XGBRegressor(random_state=42), param_grid, 
                        cv=3, scoring='neg_root_mean_squared_error', verbose=1)
    grid.fit(X, y)
    print(f"Best RMSE: {-grid.best_score_}")
    return grid.best_estimator_

if __name__ == "__main__":
    print("Regression Masterclass Pipeline Initialized.")
    # In a real run, you would load train.csv here.
