# Troubleshooting Guide

## Common Issues

### Setup Issues

**Error: `Python 3 is required but not installed`**
- Install Python 3.9+: https://python.org
- Or use your OS package manager

**Error: `config.yaml not found`**
- Run `bash setup.sh` first
- Or manually create config.yaml from template

**Error: `ModuleNotFoundError: No module named 'xxx'`**
```bash
pip install -r requirements.txt
```

---

### Runtime Issues

**Lobster won't start**
```bash
# Check Python version
python3 --version

# Check virtual environment
source venv/bin/activate

# Run with verbose output
python main.py 2>&1 | head -50
```

**Web interface not accessible**
- Check if running on `127.0.0.1:8000`: http://localhost:8000
- Check firewall isn't blocking port 8000
- Try a different port in config.yaml

**Chat apps not connecting**
- Verify tokens are correct in config.yaml
- Check bot has required permissions
- See [Chat Apps Setup](CHAT_APPS.md) for platform-specific help

---

### Voice Issues

**Microphone not detected**
```bash
python -c "import speech_recognition as sr; print(sr.Microphone.list_microphone_indexes())"
```

**No audio output**
- Check system volume
- Test speakers: `python -c "import pyttsx3; engine = pyttsx3.init(); engine.say('test'); engine.runAndWait()"`

**Speech not recognized**
- Speak clearly
- Reduce background noise
- Check microphone quality

---

### Memory Issues

**High RAM usage**
- Close other applications
- Reduce `max_context_length` in config.yaml
- Use a smaller model

**Database errors**
```bash
# Reset conversation history
rm memory.db
```

---

### Chat App Specific

#### Discord
**Bot not responding**
- Verify bot token is correct
- Check bot has "Send Messages" permission
- Try in DMs first

**"Invalid token" error**
- Regenerate token from Discord Dev Portal
- Ensure no spaces in token

#### Telegram
**Bot not responding**
- Verify token from @BotFather
- Make sure bot started: `/start` in Telegram
- Check Lobster is running: `ps aux | grep main.py`

#### Slack
**Events not working**
- Verify signing secret
- Check webhook URL is correct
- Ensure bot has event permissions

#### WhatsApp
**Can't scan QR code**
- Make sure you're in a separate browser tab
- Try clearing browser cache
- Use a different browser if needed

---

## Debug Mode

Enable verbose logging:

```yaml
# config.yaml
server:
  debug: true
```

Then run:
```bash
LOG_LEVEL=DEBUG python main.py
```

---

## Performance Tips

- **Faster responses:** Use a smaller model (mistral vs llama2)
- **Better privacy:** Keep localhost-only (host: 127.0.0.1)
- **More features:** Allocate more RAM for larger models
- **Battery life:** Disable unused integrations

---

## Getting Help

1. Check this guide first
2. Search GitHub issues: https://github.com/GmMars1/lobster-ai-assistant/issues
3. Enable debug mode and check logs
4. Open a new GitHub issue with:
   - Your OS and Python version
   - Full error message
   - Steps to reproduce
   - `config.yaml` (without tokens)

---

## System-Specific Notes

### macOS
- Use Homebrew: `brew install python3`
- Ensure Xcode Command Line Tools installed: `xcode-select --install`

### Linux
- Ubuntu/Debian: `sudo apt-get install python3-venv`
- Fedora: `sudo dnf install python3`
- Audio issues? Install: `sudo apt-get install portaudio19-dev`

### Windows
- Use Python from python.org (not Microsoft Store)
- Use PowerShell or Git Bash, not Command Prompt
- If issues: Try WSL2 (Windows Subsystem for Linux)
