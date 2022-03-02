This repository contains a telegram bot that downloads a video from TikTok and sends it to the specified chat.

# Running
1) Install necessary python libraries:
```bash
pip3 install -r requirements.txt
```

2) If you want to change the User-Agent header that sends with requests, change it in the *config.json* file.

3) Set env variables TELEGRAM_TOKEN and CHAT_ID with the api token of your bot and the chat id of the target chat.

4) Run the bot:
```bash
python3 src/main.py
```
