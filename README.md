# 🦞 Lobster AI Assistant

**Your Personal AI. Your Device. Your Control.**

A private, fast, and completely local AI assistant that integrates seamlessly with your favorite chat apps. Run it on your own hardware—no cloud, no tracking, just you and your assistant.

## Features

✨ **Core Capabilities**
- 🏠 Completely local—runs on your device
- 🔒 Private by default—your data never leaves your machine
- ⚡ Fast and responsive—optimized for low latency
- 🎙️ Voice support—talk to your assistant on any device
- 💬 Chat integration—WhatsApp, Discord, Telegram, Slack
- 🦞 Quirky lobster personality—always ready to help with a pinch of charm

## Supported Platforms

- **Chat Apps:** WhatsApp, Discord, Telegram, Slack
- **Voice:** iOS, Android, Web
- **OS:** Linux, macOS, Windows
- **Hardware:** Any device with 4GB+ RAM (runs on RPi 4+)

## Quick Start

```bash
bash setup.sh
```

This guided setup will:
1. Check system requirements
2. Install dependencies
3. Walk you through connecting your chat accounts
4. Configure voice capabilities
5. Start your local assistant

## Project Structure

```
lobster-ai-assistant/
├── core/                    # Core AI engine
│   ├── llm/                # Language model integration
│   ├── voice/              # Voice processing (STT/TTS)
│   └── memory/             # Local memory & context
├── integrations/           # Chat app connectors
│   ├── whatsapp/
│   ├── discord/
│   ├── telegram/
│   └── slack/
├── setup/                  # Installation & configuration
│   ├── setup.sh            # Main setup script
│   └── config.yaml         # Configuration template
├── docs/                   # Documentation
└── tests/                  # Test suite
```

## Documentation

- [Installation Guide](docs/INSTALLATION.md)
- [Configuration](docs/CONFIGURATION.md)
- [Chat App Setup](docs/CHAT_APPS.md)
- [Voice Setup](docs/VOICE.md)
- [API Reference](docs/API.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md)

## License

MIT License - See LICENSE file for details

## Community

Questions? Ideas? Found a bug? Open an issue or start a discussion!

---

*Built with 🦞 for privacy-first AI assistants*
