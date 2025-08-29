"""
Datathon Utilities Module

Common utilities and helper functions for the datathon project.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

# Set plotting style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def load_and_inspect(filepath, sample_size=None):
    """
    Load dataset and provide initial inspection
    
    Args:
        filepath: Path to the dataset
        sample_size: Optional sample size for large datasets
    
    Returns:
        pandas.DataFrame: Loaded dataset
    """
    # Detect file type and load accordingly
    if filepath.endswith('.csv'):
        df = pd.read_csv(filepath)
    elif filepath.endswith('.json'):
        df = pd.read_json(filepath)
    elif filepath.endswith('.xlsx'):
        df = pd.read_excel(filepath)
    else:
        raise ValueError("Unsupported file format")
    
    # Sample if needed
    if sample_size and len(df) > sample_size:
        df = df.sample(n=sample_size, random_state=42)
    
    # Basic inspection
    print(f"Dataset shape: {df.shape}")
    print(f"Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    print("\nColumn info:")
    print(df.info())
    print("\nMissing values:")
    print(df.isnull().sum())
    
    return df

def quick_eda(df, target_col=None):
    """
    Perform quick exploratory data analysis
    
    Args:
        df: pandas DataFrame
        target_col: Target column name for supervised learning
    """
    print("=== QUICK EXPLORATORY DATA ANALYSIS ===\n")
    
    # Basic statistics
    print("Numerical columns summary:")
    print(df.describe())
    
    # Categorical columns
    cat_cols = df.select_dtypes(include=['object', 'category']).columns
    if len(cat_cols) > 0:
        print(f"\nCategorical columns: {list(cat_cols)}")
        for col in cat_cols:
            print(f"\n{col} value counts:")
            print(df[col].value_counts().head())
    
    # Target analysis if provided
    if target_col and target_col in df.columns:
        print(f"\nTarget variable ({target_col}) analysis:")
        if df[target_col].dtype in ['object', 'category']:
            print(df[target_col].value_counts())
        else:
            print(df[target_col].describe())
    
    return df

def create_baseline_plots(df, target_col=None, max_cols=10):
    """
    Create baseline visualization plots
    
    Args:
        df: pandas DataFrame
        target_col: Target column name
        max_cols: Maximum number of columns to plot
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns[:max_cols]
    
    # Correlation heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', center=0)
    plt.title('Feature Correlation Heatmap')
    plt.tight_layout()
    plt.show()
    
    # Distribution plots
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    axes = axes.ravel()
    
    for i, col in enumerate(numeric_cols[:4]):
        sns.histplot(df[col], kde=True, ax=axes[i])
        axes[i].set_title(f'Distribution of {col}')
    
    plt.tight_layout()
    plt.show()

def preprocess_data(df, target_col, test_size=0.2, random_state=42):
    """
    Basic preprocessing pipeline
    
    Args:
        df: pandas DataFrame
        target_col: Target column name
        test_size: Test set size
        random_state: Random seed
    
    Returns:
        X_train, X_test, y_train, y_test: Split datasets
    """
    # Separate features and target
    X = df.drop(columns=[target_col])
    y = df[target_col]
    
    # Handle categorical variables
    cat_cols = X.select_dtypes(include=['object', 'category']).columns
    for col in cat_cols:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col].astype(str))
    
    # Handle missing values (simple imputation)
    X = X.fillna(X.mean())
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y if y.dtype == 'object' else None
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test

def evaluate_model(model, X_test, y_test, model_name="Model"):
    """
    Evaluate model performance
    
    Args:
        model: Trained model
        X_test: Test features
        y_test: Test targets
        model_name: Name for display
    """
    predictions = model.predict(X_test)
    
    print(f"=== {model_name} Performance ===")
    print(classification_report(y_test, predictions))
    
    # Confusion matrix
    cm = confusion_matrix(y_test, predictions)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f'{model_name} Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()

def save_results(results_dict, filename):
    """
    Save results to file
    
    Args:
        results_dict: Dictionary of results
        filename: Output filename
    """
    import json
    import os
    
    os.makedirs('outputs', exist_ok=True)
    
    with open(f'outputs/{filename}', 'w') as f:
        json.dump(results_dict, f, indent=2, default=str)
    
    print(f"Results saved to outputs/{filename}")
