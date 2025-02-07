from telegram import Bot, Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
import os

TOKEN = "7783463727:AAHjbY9f92ISsmKEAZfVoJYMf-jdP0e1EB4"
ADMIN_ID = 5460232465  

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
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(filters.CONTACT, contact_handler))  # اصلاح به filters
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

