from telegram import Bot, Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CommandHandler, MessageHandler, filters, CallbackContext, Application
import os

# توکن ربات را به صورت مستقیم وارد کنید
TOKEN = "7783463727:AAHjbY9f92ISsmKEAZfVoJYMf-jdP0e1EB4"

ADMIN_ID = 5460232465

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
    # از Application به جای Updater استفاده می‌کنیم
    application = Application.builder().token(TOKEN).build()

    # اضافه کردن هندلرها به dispatcher
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.CONTACT, contact_handler))  # اصلاح به filters
    
    # شروع به دریافت پیام‌ها و پردازش آن‌ها
    application.run_polling()

if __name__ == "__main__":
    main()
