from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


ADMIN_ID = 5460232465  


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id == ADMIN_ID:
        await update.message.reply_text("سلام مدیر عزیز! من آماده‌ام که کمک کنم.")
    else:
        await update.message.reply_text("سلام! شما دسترسی به دستورات مدیریتی ندارید.")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("دستورات ربات:\n/start - شروع کار با ربات\n/help - راهنمای ربات")


async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id == ADMIN_ID:
        await update.message.reply_text("این یک دستور مدیریتی است که فقط برای شما قابل دسترسی است.")
    else:
        await update.message.reply_text("شما دسترسی به این دستور ندارید.")


def main():

    TOKEN = "7783463727:AAHjbY9f92ISsmKEAZfVoJYMf-jdP0e1EB4"


    application = Application.builder().token(TOKEN).build()


    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("admin", admin_command))


    application.run_polling()

if __name__ == '__main__':
    main()
