import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import optuna
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

# --- 1. SYNTHETIC DATA GENERATION (IEEE 30-bus) ---
def generate_opf_data(n_samples=5000):
    n_bus, n_gen, n_line = 30, 6, 41
    p_loads = np.random.uniform(0.5, 2.0, (n_samples, n_bus))
    q_loads = p_loads * 0.3 + np.random.normal(0, 0.05, (n_samples, n_bus))
    contingency = np.random.randint(0, 6, n_samples)
    
    # Simple linear simulation for Pg, Qg, V
    total_load = p_loads.sum(axis=1)
    Pg = np.random.rand(n_gen, n_bus) @ p_loads.T * 1.1
    V = 1.05 - (total_load / total_load.max() * 0.1)[:, np.newaxis] + np.random.normal(0, 0.01, (n_samples, n_bus))
    
    features = pd.DataFrame(np.hstack([p_loads, q_loads]), columns=[f'P_{i}' for i in range(n_bus)] + [f'Q_{i}' for i in range(n_bus)])
    features['Contingency'] = contingency
    targets = pd.DataFrame(V, columns=[f'V_{i}' for i in range(n_bus)])
    return features, targets

# --- 2. OPTUNA HYPERPARAMETER TUNING ---
def objective(trial, X, y):
    n_layers = trial.suggest_int('n_layers', 2, 3)
    model = keras.Sequential([layers.Input(shape=(X.shape[1],))])
    for i in range(n_layers):
        model.add(layers.Dense(trial.suggest_int(f'n_units_l{i}', 32, 128), activation='selu'))
        model.add(layers.BatchNormalization())
    model.add(layers.Dense(y.shape[1]))
    model.compile(optimizer=tf.keras.optimizers.Adam(trial.suggest_float('lr', 1e-4, 1e-2)), loss='mse')
    
    X_t, X_v, y_t, y_v = train_test_split(X, y, test_size=0.2)
    model.fit(X_t, y_t, validation_data=(X_v, y_v), epochs=10, verbose=0)
    return model.evaluate(X_v, y_v, verbose=0)

if __name__ == "__main__":
    X, y = generate_opf_data()
    X_scaled = StandardScaler().fit_transform(pd.get_dummies(X, columns=['Contingency']))
    
    study = optuna.create_study(direction='minimize')
    study.optimize(lambda t: objective(t, X_scaled, y), n_trials=10)
    print(f"Best Params: {study.best_params}")
