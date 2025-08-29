#!/bin/bash

# Inter-Uni Datathon 2025 - Setup Script

echo "🚀 Setting up Inter-Uni Datathon 2025 environment..."

# Create virtual environment
echo "Creating virtual environment..."
python -m venv datathon_env
source datathon_env/bin/activate

# Install requirements
echo "Installing Python packages..."
pip install --upgrade pip
pip install -r requirements.txt

# Install additional MCP tools
echo "Installing MCP tools..."
pip install uv

# Set up Jupyter kernel
echo "Setting up Jupyter kernel..."
python -m ipykernel install --user --name=datathon_env --display-name="Datathon 2025"

# Create environment file template
cat > .env << EOF
# GitHub Personal Access Token (get from: https://github.com/settings/tokens)
GITHUB_PAT=your_token_here

# Jupyter Configuration
JUPYTER_TOKEN=datathon-token-2025

# API Keys (add as needed)
OPENAI_API_KEY=your_key_here
HUGGINGFACE_API_KEY=your_key_here
EOF

echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Set your GitHub token: export GITHUB_PAT='your_token_here'"
echo "2. Activate environment: source datathon_env/bin/activate"
echo "3. Start Jupyter: jupyter lab --port=8888 --token=datathon-token-2025"
echo "4. Start Claude Code: cd /Users/nmduk/Datathon && claude-code"
echo ""
echo "Available custom commands:"
echo "- /analyze-data <dataset_name>"
echo "- /create-notebook <analysis_name>"
echo "- /run-experiments <model_type>"
echo "- /generate-report <project_name>"
