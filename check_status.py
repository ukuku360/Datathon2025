#!/usr/bin/env python3
"""
Datathon Environment Status Checker
"""

import os
import sys
import subprocess
import json

def check_python_packages():
    """Check if required packages are installed"""
    required_packages = [
        'pandas', 'numpy', 'matplotlib', 'seaborn', 'sklearn', 
        'jupyter', 'plotly', 'xgboost'
    ]
    
    print("📦 Checking Python packages...")
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"  ✅ {package}")
        except ImportError:
            print(f"  ❌ {package} - Not installed")
            missing_packages.append(package)
    
    return missing_packages

def check_mcp_servers():
    """Check MCP server configuration"""
    print("\n🔧 Checking MCP configuration...")
    
    mcp_file = '.mcp.json'
    if os.path.exists(mcp_file):
        with open(mcp_file, 'r') as f:
            config = json.load(f)
            servers = config.get('mcpServers', {})
            print(f"  ✅ MCP config found with {len(servers)} servers:")
            for server_name in servers.keys():
                print(f"    - {server_name}")
    else:
        print("  ❌ .mcp.json not found")

def check_directories():
    """Check project directory structure"""
    print("\n📁 Checking project structure...")
    
    expected_dirs = [
        'data', 'notebooks', 'src', 'models', 'outputs', 
        'presentation', '.claude/commands', 'data/raw', 'data/processed'
    ]
    
    for directory in expected_dirs:
        if os.path.exists(directory):
            print(f"  ✅ {directory}/")
        else:
            print(f"  ❌ {directory}/ - Missing")

def check_environment_variables():
    """Check for required environment variables"""
    print("\n🔐 Checking environment variables...")
    
    env_vars = ['GITHUB_PAT']
    for var in env_vars:
        if os.environ.get(var):
            print(f"  ✅ {var} - Set")
        else:
            print(f"  ⚠️  {var} - Not set (optional but recommended)")

def main():
    print("🚀 Inter-Uni Datathon 2025 - Environment Status Check\n")
    
    # Check if we're in the right directory
    if not os.path.exists('.mcp.json'):
        print("❌ Please run this script from the Datathon project directory")
        sys.exit(1)
    
    missing_packages = check_python_packages()
    check_mcp_servers()
    check_directories()
    check_environment_variables()
    
    print("\n" + "="*50)
    
    if missing_packages:
        print("⚠️  Setup incomplete - install missing packages:")
        print("   pip install " + " ".join(missing_packages))
    else:
        print("✅ Environment looks good!")
    
    print("\n🎯 Next steps:")
    print("1. Set GitHub token: export GITHUB_PAT='your_token'")
    print("2. Start Jupyter: jupyter lab --port=8888 --token=datathon-token-2025")
    print("3. Start Claude Code: claude-code")
    print("4. Try custom commands like: /analyze-data your_dataset.csv")

if __name__ == "__main__":
    main()
