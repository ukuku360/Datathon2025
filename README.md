# Inter-Uni Datathon 2025 - Project Setup

## Project Structure
```
Datathon/
├── .mcp.json           # MCP server configurations
├── data/               # Raw and processed datasets
├── notebooks/          # Jupyter notebooks for analysis
├── src/                # Source code modules
├── models/             # Trained models and model artifacts
├── outputs/            # Results, figures, reports
├── presentation/       # Final presentation materials
└── .claude/           # Claude Code custom commands
    └── commands/
```

## Available MCP Servers

### 🔧 Configured Servers
- **Jupyter MCP**: Real-time Jupyter notebook interaction
- **GitHub MCP**: Git operations and collaboration
- **Filesystem MCP**: Local file operations
- **Data Exploration MCP**: Automated data analysis

### 🚀 Quick Start

1. **Setup Environment**:
   ```bash
   cd /Users/nmduk/Datathon
   # Set your GitHub token (get from: https://github.com/settings/tokens)
   export GITHUB_PAT="your_github_token_here"
   ```

2. **Start Jupyter**:
   ```bash
   jupyter lab --port=8888 --token=datathon-token-2025
   ```

3. **Initialize with Claude Code**:
   ```bash
   claude-code
   ```

## Environment Setup Commands

### Python Dependencies
```bash
pip install pandas numpy scikit-learn matplotlib seaborn plotly
pip install jupyter jupyterlab
pip install tensorflow pytorch
```

### R Dependencies (if needed)
```bash
install.packages(c("tidyverse", "caret", "randomForest", "ggplot2"))
```

## Team Collaboration Guidelines

1. **Branching Strategy**: Use feature branches for different analysis approaches
2. **Notebook Naming**: `YYYY-MM-DD_AuthorInitials_Description.ipynb`
3. **Data Versioning**: Keep original data in `data/raw/`, processed in `data/processed/`
4. **Model Tracking**: Save models with descriptive names and metadata

## Custom Commands Available
- `/analyze-data`: Quick data exploration pipeline
- `/create-notebook`: Generate notebook template
- `/run-experiments`: Execute ML experiments
- `/generate-report`: Create presentation materials

---
*Generated for Inter-Uni Datathon 2025*
