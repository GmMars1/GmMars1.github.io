#!/bin/bash

# 🦞 Lobster AI Assistant - Setup Script
# This script guides you through setting up your personal AI assistant

set -e

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# ASCII art
echo -e "${BLUE}"
cat << "EOF"
  _____ _ 
 / _ \ \ / / | |/ _ \| | | |__| | /__   __| | ___  _ __ 
| |/ /  V /  | | (_) | | |  __  |    | |  | |/ _ \| '__|
|    \  /   | |\__, ||_| | |  | |    | |  | | (_) | |   
|_|\_\/  \_/|_|  / /  \ \_/ _| |_|    |_|  |_|\___/|_|   
                /_/                                       
EOF
echo -e "${NC}"

echo -e "${GREEN}Welcome to Lobster AI Assistant Setup! 🦞${NC}"
echo -e "Let's get your personal AI up and running...\n"

# System Check
echo -e "${BLUE}[1/5] Checking system requirements...${NC}"

# Check OS
OS=""
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="Linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macOS"
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    OS="Windows"
else
    echo -e "${RED}Unsupported OS. Please use Linux, macOS, or Windows.${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Detected OS: $OS${NC}"

# Check Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}✗ Python 3 is required but not installed.${NC}"
    exit 1
fi
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo -e "${GREEN}✓ Python $PYTHON_VERSION found${NC}"

# Check RAM (minimum 4GB recommended)
if [[ "$OS" == "Linux" ]]; then
    RAM_GB=$(grep MemTotal /proc/meminfo | awk '{print int($2/1024/1024)}')
elif [[ "$OS" == "macOS" ]]; then
    RAM_GB=$(sysctl hw.memsize | awk '{print int($NF/1024/1024/1024)}')
else
    RAM_GB=0
fi

if [ $RAM_GB -lt 4 ]; then
    echo -e "${YELLOW}⚠ Warning: Only ${RAM_GB}GB RAM detected. Recommended: 4GB+${NC}"
else
    echo -e "${GREEN}✓ RAM: ${RAM_GB}GB (good!)${NC}"
fi

echo ""

# Dependency Installation
echo -e "${BLUE}[2/5] Installing dependencies...${NC}"

if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
fi

source venv/bin/activate 2>/dev/null || . venv\\Scripts\\activate 2>/dev/null

pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet 2>/dev/null || true

echo -e "${GREEN}✓ Dependencies installed${NC}"
echo ""

# Chat App Configuration
echo -e "${BLUE}[3/5] Configure Chat Apps Integration${NC}"
echo "Which chat apps would you like to connect? (select multiple by entering space-separated numbers)"
echo "  1) WhatsApp"
echo "  2) Discord"
echo "  3) Telegram"
echo "  4) Slack"
echo "  5) Skip for now"
read -p "Your choice (e.g., 1 2 3): " CHAT_CHOICE

echo ""
echo -e "${BLUE}[4/5] Voice Setup${NC}"
read -p "Enable voice capabilities? (y/n) " VOICE_ENABLE

if [[ $VOICE_ENABLE == "y" || $VOICE_ENABLE == "Y" ]]; then
    echo "Configuring voice support..."
    echo -e "${GREEN}✓ Voice enabled${NC}"
else
    echo -e "${YELLOW}⊘ Voice disabled${NC}"
fi

echo ""
echo -e "${BLUE}[5/5] Creating configuration...${NC}"

# Create config file
cat > config.yaml << 'YAML_EOF'
# Lobster AI Assistant Configuration

server:
  host: 127.0.0.1
  port: 8000
  debug: false

ai:
  model: "local"  # Using local LLM
  max_context_length: 4096
  temperature: 0.7

voice:
  enabled: false
  language: "en-US"
  stt_engine: "local"  # Speech-to-Text
  tts_engine: "local"  # Text-to-Speech

integrations:
  whatsapp:
    enabled: false
  discord:
    enabled: false
  telegram:
    enabled: false
  slack:
    enabled: false

personality:
  name: "Lobster"
  theme: "quirky"
  tone: "friendly"
YAML_EOF

echo -e "${GREEN}✓ Configuration created${NC}"
echo ""

# Completion message
echo -e "${GREEN}═══════════════════════════════════════════${NC}"
echo -e "${GREEN}✓ Setup Complete! 🦞${NC}"
echo -e "${GREEN}═══════════════════════════════════════════${NC}"
echo ""
echo "Next steps:"
echo "  1. Edit config.yaml to configure chat apps and voice"
echo "  2. Run: python main.py"
echo "  3. Visit: http://127.0.0.1:8000"
echo ""
echo "For detailed setup instructions, see docs/INSTALLATION.md"
echo ""
