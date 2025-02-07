from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import os

TOKEN = "7783463727:AAHjbY9f92ISsmKEAZfVoJYMf-jdP0e1EB4"

ADMIN_ID = 5460232465

# Webhook URL
WEBHOOK_URL = "https://your-domain.com/your-webhook-endpoint"  # جایگزین با URL صحیح

async def start(update: Update, context: CallbackContext):
    keyboard = [[KeyboardButton("📞 ارسال شماره تلفن", request_contact=True)]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text("لطفاً شماره تلفن خود را ارسال کنید:", reply_markup=reply_markup)

async def contact_handler(update: Update, context: CallbackContext):
    user = update.message.from_user
    phone_number = update.message.contact.phone_number
    await context.bot.send_message(chat_id=ADMIN_ID, text=f"📞 شماره جدید دریافت شد:\n👤 {user.full_name}\n📱 {phone_number}")
    await update.message.reply_text("✅ شماره شما با موفقیت ثبت شد. متشکرم!")

def main():
    application = Application.builder().token(TOKEN).build()

    # اضافه کردن هندلرها
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.CONTACT, contact_handler))

    # فعال‌سازی Webhook به جای Polling
    application.bot.set_webhook(url=WEBHOOK_URL)
    application.run_polling(drop_pending_updates=True)  # optional, if you want to drop updates before the bot starts

if __name__ == "__main__":
    main()
