from telegram import Bot, Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os

TOKEN = os.getenv("TOKEN")  # دریافت توکن از محیط متغیرهای Render
ADMIN_ID = 123456789  # آی‌دی خود را اینجا بگذارید

def start(update: Update, context: CallbackContext):
    keyboard = [[KeyboardButton("📞 ارسال شماره تلفن", request_contact=True)]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    
    update.message.reply_text("لطفاً شماره تلفن خود را ارسال کنید:", reply_markup=reply_markup)

def contact_handler(update: Update, context: CallbackContext):
    user = update.message.from_user
    phone_number = update.message.contact.phone_number
    context.bot.send_message(chat_id=ADMIN_ID, text=f"📞 شماره جدید دریافت شد:\n👤 {user.full_name}\n📱 {phone_number}")
    update.message.reply_text("✅ شماره شما با موفقیت ثبت شد. متشکرم!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.contact, contact_handler))
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
