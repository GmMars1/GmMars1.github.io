# Configuration Guide

## config.yaml Overview

The main configuration file is `config.yaml`. Generated during setup, it contains:

### Server Settings

```yaml
server:
  host: 127.0.0.1    # Listen on localhost only (private)
  port: 8000         # Web server port
  debug: false       # Debug mode (disable in production)
```

### AI Engine

```yaml
ai:
  model: "local"              # Using local LLM
  max_context_length: 4096    # Maximum conversation context
  temperature: 0.7            # Randomness (0.0-1.0)
```

**Temperature Guide:**
- `0.0`: Deterministic (same output every time)
- `0.7`: Balanced (recommended)
- `1.0`: Very creative but sometimes nonsensical

### Voice Settings

```yaml
voice:
  enabled: false
  language: "en-US"      # Language code
  stt_engine: "local"    # Speech-to-Text
  tts_engine: "local"    # Text-to-Speech
```

### Chat Integrations

```yaml
integrations:
  whatsapp:
    enabled: false
  discord:
    enabled: false
    token: "YOUR_TOKEN_HERE"
  telegram:
    enabled: false
    token: "YOUR_TOKEN_HERE"
  slack:
    enabled: false
    bot_token: "YOUR_BOT_TOKEN"
    signing_secret: "YOUR_SIGNING_SECRET"
```

### Personality

```yaml
personality:
  name: "Lobster"
  theme: "quirky"        # quirky, professional, casual
  tone: "friendly"       # friendly, formal, humorous
```

## Environment Variables

Optionally, use `.env` file for sensitive data:

```bash
# .env
DISCORD_TOKEN=your_discord_token
TELEGRAM_TOKEN=your_telegram_token
SLACK_BOT_TOKEN=your_slack_bot_token
SLACK_SIGNING_SECRET=your_slack_signing_secret
```

## Local Model Configuration

### Using Ollama

1. Install Ollama: https://ollama.ai
2. Pull a model: `ollama pull mistral`
3. Ollama runs on `http://localhost:11434`

### Using Llama.cpp

1. Download a model file (`.gguf`)
2. Configure in `config.yaml`:

```yaml
ai:
  model: "local"
  model_path: "./models/mistral-7b.gguf"
```

## Privacy & Security

✅ **What stays local:**
- All your conversations
- Models and weights
- Configuration data
- Memory and history

✅ **Best practices:**
- Keep `host: 127.0.0.1` (not `0.0.0.0`)
- Use `debug: false` in production
- Regularly backup your memory database
- Review model sources before use

## Advanced Configuration

For more options, see individual module documentation:
- [Voice Setup](VOICE.md)
- [Chat Apps Setup](CHAT_APPS.md)
