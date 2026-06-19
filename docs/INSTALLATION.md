# Installation Guide

## System Requirements

- **OS:** Linux, macOS, or Windows
- **Python:** 3.9 or higher
- **RAM:** 4GB minimum (8GB+ recommended for better performance)
- **Storage:** 2GB for models and dependencies

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/GmMars1/lobster-ai-assistant.git
cd lobster-ai-assistant
```

### 2. Run Setup

```bash
bash setup.sh
```

The setup script will:
- Check your system requirements
- Create a Python virtual environment
- Install all dependencies
- Guide you through chat app configuration
- Set up voice capabilities (optional)
- Generate a configuration file

### 3. Start the Assistant

```bash
python main.py
```

You should see:
```
🦞 Lobster AI Assistant is running!
 Web Interface: http://127.0.0.1:8000
```

## Manual Installation

If you prefer manual setup:

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python main.py
```

## Troubleshooting

### Python not found
```bash
# macOS
brew install python3

# Ubuntu/Debian
sudo apt-get install python3 python3-venv

# Windows: Download from python.org
```

### Permission denied (Linux/macOS)
```bash
chmod +x setup.sh
bash setup.sh
```

### Module not found errors
```bash
# Reinstall dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

## Next Steps

1. Read [Configuration Guide](CONFIGURATION.md)
2. Set up [Chat Apps](CHAT_APPS.md)
3. Configure [Voice](VOICE.md)
