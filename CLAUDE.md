# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Environment Setup

### Development Environment
```bash
# Activate the datathon virtual environment
source datathon_env/bin/activate

# Install all dependencies
pip install -r requirements.txt

# Check environment status
python check_status.py

# Start Jupyter Lab with configured token
jupyter lab --port=8888 --token=datathon-token-2025
```

### Environment Variables Required
- `GITHUB_PAT`: GitHub Personal Access Token for MCP GitHub server
- Optional: `JUPYTER_TOKEN=datathon-token-2025` (pre-configured)

## Specialized Agent Architecture

This repository uses 5 specialized agents optimized for datathon workflows:

### Agent Usage Patterns
```bash
/agent data-analyst "Analyze dataset and identify key predictive features"
/agent ml-engineer "Train ensemble with XGBoost and LightGBM using 5-fold CV"
/agent data-preprocessor "Create preprocessing pipeline preventing data leakage"
/agent submission-manager "Generate final competition submission with model ensemble"
/agent datathon-reviewer "Review code for reproducibility and competition compliance"
```

### Agent Specializations
- **data-analyst**: EDA, statistical analysis, visualization, correlation analysis
- **ml-engineer**: Model training, hyperparameter tuning, ensemble methods, CV strategies
- **data-preprocessor**: Data cleaning, feature engineering, leakage prevention
- **submission-manager**: Final model selection, submission formatting, validation
- **datathon-reviewer**: Code quality, reproducibility, competition best practices

## MCP Server Configuration

Four MCP servers are configured in `.mcp.json`:
- **Jupyter MCP**: Direct notebook interaction and code execution
- **GitHub MCP**: Git operations and collaboration (requires GITHUB_PAT)
- **Filesystem MCP**: Local file operations scoped to project directory
- **Data Exploration MCP**: Automated data analysis workflows

## Data Science Pipeline Architecture

### DataPreprocessor Class Pattern
```python
from src.preprocessing import DataPreprocessor

# Initialize with state tracking
preprocessor = DataPreprocessor()

# Fit and transform training data
train_processed = preprocessor.fit_transform(train_df, target_col='target')

# Transform test data with same parameters
test_processed = preprocessor.transform(test_df)

# Access fitted components
feature_names = preprocessor.feature_names
scalers = preprocessor.scalers
encoders = preprocessor.encoders
```

### Feature Engineering Utilities
- `create_features()`: Generates interaction features from top correlated pairs
- `select_features(X, y, k=20)`: Statistical feature selection using mutual_info_classif
- Preprocessing handles missing values, categorical encoding, and robust scaling

## Custom Command System

### /analyze-data Pipeline
7-step comprehensive EDA process:
1. Data loading & inspection (shape, dtypes, missing values)
2. Exploratory data analysis with summary statistics
3. Data quality assessment (outliers, duplicates)
4. Feature analysis (distributions, correlations)
5. Initial insights and modeling recommendations
6. Visualization generation
7. Next steps suggestions

### Other Commands
- `/create-notebook`: Generate template with datathon structure
- `/run-experiments`: Execute ML experiments with proper validation
- `/generate-report`: Create presentation materials

## Competition Workflow Standards

### Data Organization
- `data/raw/`: Original datasets (never modified)
- `data/processed/`: Cleaned and transformed data
- `models/`: Trained models with descriptive names and metadata
- `outputs/`: Results, figures, and submission files

### Naming Conventions
- Notebooks: `YYYY-MM-DD_AuthorInitials_Description.ipynb`
- Models: Include algorithm, features, and CV score in filename
- Submissions: Version with timestamp and model ensemble details

### Key Libraries Stack
- **ML**: scikit-learn, xgboost, lightgbm, catboost
- **Deep Learning**: tensorflow, torch, transformers
- **Analysis**: pandas, numpy, scipy, statsmodels
- **Visualization**: matplotlib, seaborn, plotly
- **Interpretation**: shap, lime

## Validation and Competition Compliance

### Cross-Validation Strategy
- Use stratified splits for classification
- Time-series splits for temporal data
- Proper validation set holdout for final model selection
- Avoid data leakage in preprocessing steps

### Model Training Workflow
1. Split data before any preprocessing
2. Fit preprocessing on training fold only
3. Apply same preprocessing to validation fold
4. Train models with hyperparameter optimization
5. Evaluate using competition-specific metrics
6. Create ensembles with diverse base models

### Submission Preparation
- Validate submission format against competition requirements
- Check prediction ranges and data types
- Generate multiple submission variants
- Document model selection methodology