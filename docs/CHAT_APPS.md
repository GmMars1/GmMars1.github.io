# Chat Apps Integration Guide

Connect Lobster to your favorite chat apps and message your assistant like a real person.

## WhatsApp

### Setup

1. Enable in `config.yaml`:
```yaml
integrations:
  whatsapp:
    enabled: true
```

2. Run setup:
```bash
python -m integrations.whatsapp
```

3. Scan QR code with your phone
4. Done! Message your assistant on WhatsApp

### Privacy Note
WhatsApp integration runs locally on your device using WhatsApp Web protocol. No data is sent to external servers.

---

## Discord

### Setup

1. **Create a Discord Bot**
   - Go to https://discord.com/developers/applications
   - Click "New Application"
   - Go to "Bot" → "Add Bot"
   - Copy the token

2. **Configure Lobster**
   ```yaml
   integrations:
     discord:
       enabled: true
       token: "YOUR_BOT_TOKEN"
   ```

3. **Add bot to your server**
   - Applications → OAuth2 → URL Generator
   - Select scopes: `bot`
   - Select permissions: `Send Messages`, `Read Messages`
   - Open the generated URL and add to your server

4. **Start Lobster**
   ```bash
   python main.py
   ```

5. **Message your bot**
   - Send DMs to your bot in Discord
   - It will respond with Lobster's replies

---

## Telegram

### Setup

1. **Create a Telegram Bot**
   - Message `@BotFather` on Telegram
   - Type `/newbot`
   - Follow the prompts
   - Copy the API token

2. **Configure Lobster**
   ```yaml
   integrations:
     telegram:
       enabled: true
       token: "YOUR_API_TOKEN"
   ```

3. **Start Lobster**
   ```bash
   python main.py
   ```

4. **Message your bot**
   - Search for your bot name in Telegram
   - Send any message
   - It will respond with Lobster's reply

---

## Slack

### Setup

1. **Create a Slack App**
   - Go to https://api.slack.com/apps
   - Click "Create New App"
   - Choose "From scratch"
   - Give it a name and select your workspace

2. **Configure the bot**
   - Go to "OAuth & Permissions"
   - Add scopes: `chat:write`, `channels:read`, `im:read`, `im:write`
   - Go to "Install to Workspace"
   - Copy the "Bot User OAuth Token"
   - Go to "Basic Information" → Copy "Signing Secret"

3. **Configure Lobster**
   ```yaml
   integrations:
     slack:
       enabled: true
       bot_token: "YOUR_BOT_TOKEN"
       signing_secret: "YOUR_SIGNING_SECRET"
   ```

4. **Configure webhook URL**
   - In Slack app settings: "Event Subscriptions"
   - Enable Events
   - Request URL: `http://your-ip:8000/slack/events`
   - Subscribe to bot events: `message.im`

5. **Start Lobster**
   ```bash
   python main.py
   ```

6. **Message your bot**
   - Send DMs to your Lobster app in Slack
   - It will respond

---

## Multiple Chat Apps

You can enable multiple integrations simultaneously:

```yaml
integrations:
  whatsapp:
    enabled: true
  discord:
    enabled: true
    token: "..."
  telegram:
    enabled: true
    token: "..."
  slack:
    enabled: true
    bot_token: "..."
    signing_secret: "..."
```

Run `python main.py` once and Lobster will be available on all enabled platforms.

---

## Troubleshooting

**Bot not responding?**
- Check that `enabled: true` in config
- Verify tokens are correct
- Check logs: `python main.py 2>&1 | grep ERROR`

**Invalid token error?**
- Regenerate the token from the app settings
- Make sure there are no extra spaces

**Permission denied?**
- Check bot has appropriate permissions in the chat app
- On Slack/Discord: re-invite the bot to the server
