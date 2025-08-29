# Datathon 2025 - Specialized Agents

This directory contains 5 specialized agents designed specifically for the Inter-Uni Datathon 2025 competition. Each agent is optimized for different phases of the data science pipeline.

## Available Agents

### 🔍 Data Analysis Agent (`data-analyst`)
**Focus**: Exploratory Data Analysis, Statistical Analysis, Visualization

Perfect for initial data exploration, correlation analysis, and generating insights to guide your modeling approach.

```bash
/agent data-analyst "Analyze the customer data and identify the top predictive features"
```

### 🤖 ML Pipeline Agent (`ml-engineer`) 
**Focus**: Model Training, Hyperparameter Tuning, Ensemble Methods

Specialized in building high-performance ML models with proper validation for competitive environments.

```bash
/agent ml-engineer "Train XGBoost and LightGBM models with 5-fold CV optimization"
```

### 🔧 Data Preprocessing Agent (`data-preprocessor`)
**Focus**: Data Cleaning, Feature Engineering, Transformation Pipelines  

Expert in comprehensive preprocessing while preventing data leakage and building reusable pipelines.

```bash
/agent data-preprocessor "Create preprocessing pipeline handling missing values and categorical encoding"
```

### 🎯 Competition Submission Agent (`submission-manager`)
**Focus**: Final Model Selection, Submission Formatting, Validation

Handles the critical final step of creating competition-ready submissions with proper formatting and validation.

```bash  
/agent submission-manager "Generate final submission using ensemble of top 3 models"
```

### 📋 Code Review Agent (`datathon-reviewer`)
**Focus**: Code Quality, Reproducibility, Best Practices

Ensures your code follows datathon best practices and is free from common pitfalls like data leakage.

```bash
/agent datathon-reviewer "Review ML pipeline for data leakage and reproducibility issues"
```

## Quick Start Workflow

1. **Initial Data Exploration**: Use `data-analyst` to understand your dataset
2. **Data Preparation**: Use `data-preprocessor` to clean and engineer features  
3. **Model Development**: Use `ml-engineer` to train and optimize models
4. **Code Quality Check**: Use `datathon-reviewer` to validate your approach
5. **Final Submission**: Use `submission-manager` to create competition files

## Agent Usage Syntax

```bash
# Basic usage
/agent [agent-name] "[task description]"

# Examples
/agent data-analyst "Profile the training dataset and identify data quality issues"
/agent ml-engineer "Build ensemble model optimizing for F1 score"
/agent data-preprocessor "Handle missing values in categorical features using target encoding"
```

## Tips for Effective Agent Usage

- **Be Specific**: Provide clear, detailed task descriptions
- **Sequential Workflow**: Use agents in logical order for best results
- **Cross-Validation**: Always mention validation strategy preferences
- **Competition Context**: Reference specific competition metrics and constraints
- **Iterative Refinement**: Use multiple agents to refine your approach

## Competition-Specific Configurations

Each agent is configured with:
- **Proper CV strategies** for temporal/stratified data
- **Competition metric optimization** (AUC, F1, RMSE, etc.)
- **Data leakage prevention** protocols
- **Ensemble and stacking** methodologies
- **Submission format validation** for common platforms

## Integration with Project Structure

```
Datathon/
├── data/                 # Raw/processed data (agents read from here)
├── notebooks/            # Jupyter notebooks (agents execute here)  
├── src/                  # Source code modules (agents modify/create)
├── models/               # Model artifacts (agents save here)
├── outputs/              # Results and submissions (agents write here)
└── .claude/agents/       # Agent configurations (this directory)
```

---
*Optimized for Inter-Uni Datathon 2025 competitive environment*