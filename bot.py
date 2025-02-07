from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = "7783463727:AAHjbY9f92ISsmKEAZfVoJYMf-jdP0e1EB4"  # جایگزین کردن با توکن واقعی خود
ADMIN_ID = 5460232465  # آی‌دی خود را اینجا بگذارید

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
    # ایجاد Application
    application = Application.builder().token(TOKEN).build()

    # اضافه کردن هندلرها
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.CONTACT, contact_handler))  # اصلاح به filters
    
    # شروع گرفتن آپدیت‌ها
    application.run_polling()

if __name__ == "__main__":
    main()
