# Voice Capabilities Setup

Talk to Lobster with voice on iOS, Android, or web browsers.

## Overview

Voice support includes:
- **STT (Speech-to-Text):** Convert your voice to text
- **TTS (Text-to-Speech):** Hear Lobster's responses
- **All local:** No cloud API required

## Enable Voice

1. Edit `config.yaml`:
```yaml
voice:
  enabled: true
  language: "en-US"      # Change as needed
  stt_engine: "local"
  tts_engine: "local"
```

2. Install voice dependencies:
```bash
pip install SpeechRecognition pyttsx3 librosa
```

3. Restart Lobster:
```bash
python main.py
```

## On Mobile

### iOS

1. Access Lobster via: `http://your-computer-ip:8000`
2. Click the microphone icon
3. Speak your question
4. Hear the response

**Note:** Ensure your iPhone is on the same network as your device running Lobster.

### Android

1. Access Lobster via: `http://your-computer-ip:8000`
2. Tap the microphone icon
3. Speak your question
4. Hear the response

## Supported Languages

```yaml
voice:
  language: "en-US"      # English (US)
  # language: "en-GB"   # English (UK)
  # language: "es-ES"   # Spanish
  # language: "fr-FR"   # French
  # language: "de-DE"   # German
  # language: "it-IT"   # Italian
  # language: "ja-JP"   # Japanese
  # language: "zh-CN"   # Mandarin Chinese
```

## Network Configuration

For mobile access:

1. Find your computer's IP:
   ```bash
   # macOS/Linux
   ifconfig | grep "inet "
   
   # Windows
   ipconfig
   ```

2. Update `config.yaml`:
   ```yaml
   server:
     host: 0.0.0.0    # Listen on all interfaces
     port: 8000
   ```

3. Access from phone: `http://YOUR_IP:8000`

## Voice Quality

### STT (Speech Recognition)
- **Default:** Uses device microphone
- **Accuracy:** ~95% in quiet environments
- **Languages:** 100+ supported

### TTS (Text-to-Speech)
- **Voices:** Multiple available per language
- **Speed:** Adjustable
- **Quality:** Natural-sounding local voices

## Advanced Voice Configuration

```yaml
voice:
  enabled: true
  language: "en-US"
  stt_engine: "local"
  stt_options:
    microphone: 0          # Microphone device index
    timeout: 10            # Seconds to listen
    phrase_time_limit: 15  # Max phrase length
  
  tts_engine: "local"
  tts_options:
    rate: 150              # Words per minute
    volume: 0.9            # 0.0 - 1.0
```

## Troubleshooting

**Microphone not detected?**
```bash
cd core/voice && python test_audio.py
```

**Speech not recognized?**
- Speak clearly and in a quiet environment
- Increase `phrase_time_limit` for slower speech
- Check microphone volume

**No audio output?**
- Check system volume is up
- Verify speakers are connected
- Check `tts_engine` is set to "local"

**Mobile can't connect?**
- Ensure both devices are on same network
- Check firewall isn't blocking port 8000
- Use device IP, not "localhost"
