"""Configuration management."""

import yaml
from pathlib import Path
from typing import Dict


def load_config() -> Dict:
    """Load configuration from config.yaml."""
    config_path = Path("config.yaml")
    
    if not config_path.exists():
        raise FileNotFoundError("config.yaml not found. Please run setup.sh first.")
    
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    return config or {}
