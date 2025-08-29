"""
Data preprocessing and feature engineering utilities
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.feature_selection import SelectKBest, f_classif, mutual_info_classif

class DataPreprocessor:
    """
    Comprehensive data preprocessing pipeline
    """
    
    def __init__(self):
        self.scalers = {}
        self.encoders = {}
        self.imputers = {}
        self.feature_names = []
    
    def fit_transform(self, df, target_col=None):
        """
        Fit preprocessing steps and transform data
        """
        processed_df = df.copy()
        
        # Handle missing values
        processed_df = self._handle_missing_values(processed_df)
        
        # Encode categorical variables
        processed_df = self._encode_categorical(processed_df, target_col)
        
        # Scale numerical features
        processed_df = self._scale_features(processed_df, target_col)
        
        self.feature_names = processed_df.columns.tolist()
        if target_col in self.feature_names:
            self.feature_names.remove(target_col)
        
        return processed_df
    
    def transform(self, df):
        """
        Transform new data using fitted preprocessors
        """
        processed_df = df.copy()
        
        # Apply same transformations
        processed_df = self._apply_missing_values(processed_df)
        processed_df = self._apply_categorical_encoding(processed_df)
        processed_df = self._apply_feature_scaling(processed_df)
        
        return processed_df
    
    def _handle_missing_values(self, df):
        """Handle missing values in the dataset"""
        for col in df.columns:
            if df[col].isnull().sum() > 0:
                if df[col].dtype in ['object', 'category']:
                    # Most frequent for categorical
                    imputer = SimpleImputer(strategy='most_frequent')
                    df[col] = imputer.fit_transform(df[[col]]).ravel()
                    self.imputers[col] = imputer
                else:
                    # Median for numerical
                    imputer = SimpleImputer(strategy='median')
                    df[col] = imputer.fit_transform(df[[col]]).ravel()
                    self.imputers[col] = imputer
        
        return df
    
    def _encode_categorical(self, df, target_col):
        """Encode categorical variables"""
        cat_cols = df.select_dtypes(include=['object', 'category']).columns
        
        for col in cat_cols:
            if col != target_col:
                if df[col].nunique() <= 10:  # One-hot for low cardinality
                    encoder = OneHotEncoder(drop='first', sparse_output=False)
                    encoded = encoder.fit_transform(df[[col]])
                    encoded_cols = [f"{col}_{cat}" for cat in encoder.categories_[0][1:]]
                    encoded_df = pd.DataFrame(encoded, columns=encoded_cols, index=df.index)
                    df = pd.concat([df.drop(columns=[col]), encoded_df], axis=1)
                    self.encoders[col] = encoder
                else:  # Label encoding for high cardinality
                    encoder = LabelEncoder()
                    df[col] = encoder.fit_transform(df[col].astype(str))
                    self.encoders[col] = encoder
        
        return df
    
    def _scale_features(self, df, target_col):
        """Scale numerical features"""
        num_cols = df.select_dtypes(include=[np.number]).columns
        
        if target_col in num_cols:
            num_cols = num_cols.drop(target_col)
        
        if len(num_cols) > 0:
            scaler = RobustScaler()  # Robust to outliers
            df[num_cols] = scaler.fit_transform(df[num_cols])
            self.scalers['numerical'] = scaler
        
        return df

def create_features(df):
    """
    Create additional features from existing ones
    """
    df_features = df.copy()
    
    # Identify numerical columns
    num_cols = df_features.select_dtypes(include=[np.number]).columns
    
    if len(num_cols) >= 2:
        # Create interaction features for top correlated pairs
        corr_matrix = df_features[num_cols].corr().abs()
        
        # Get top 3 correlated pairs
        pairs = []
        for i in range(len(num_cols)):
            for j in range(i+1, len(num_cols)):
                pairs.append((num_cols[i], num_cols[j], corr_matrix.iloc[i, j]))
        
        top_pairs = sorted(pairs, key=lambda x: x[2], reverse=True)[:3]
        
        for col1, col2, corr in top_pairs:
            # Interaction features
            df_features[f"{col1}_x_{col2}"] = df_features[col1] * df_features[col2]
            df_features[f"{col1}_div_{col2}"] = df_features[col1] / (df_features[col2] + 1e-8)
    
    return df_features

def select_features(X, y, k=20):
    """
    Select top k features using statistical tests
    """
    if X.shape[1] <= k:
        return X, list(X.columns) if hasattr(X, 'columns') else list(range(X.shape[1]))
    
    # Use different methods based on target type
    if y.dtype in ['object', 'category'] or len(np.unique(y)) < 10:
        # Classification
        selector = SelectKBest(score_func=mutual_info_classif, k=k)
    else:
        # Regression
        selector = SelectKBest(score_func=f_classif, k=k)
    
    X_selected = selector.fit_transform(X, y)
    
    if hasattr(X, 'columns'):
        selected_features = X.columns[selector.get_support()].tolist()
    else:
        selected_features = list(selector.get_support().nonzero()[0])
    
    return X_selected, selected_features
