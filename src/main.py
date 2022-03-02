import os

from telebot import TeleBot
from telebot.types import Message

from api import api_download_video
from config import Config

bot = TeleBot(os.environ.get("TELEGRAM_TOKEN"))
config = Config()


@bot.message_handler(content_types=["text"])
def send_video(message: Message):
    try:
        url = message.text
        video = api_download_video(url, config)
        bot.send_video(int(os.environ.get("CHAT_ID")), video=video)
    except:
        bot.send_message(message.chat.id, "Sorry, an error occured")


def main():
    bot.polling(non_stop=True)


if __name__ == "__main__":
    main()
