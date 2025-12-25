@bot.message_handler(commands=['start'])
def main_menu(message):
    user_id = message.chat.id
    
    welcome_text = (
        "<b>مرحباً بك في ALL MEDIA DOWNLOADER 🤖⭐</b>\n"
        "البوت الشامل لتحميل المقاطع من جميع المنصات بجودة عالية.\n\n"
        "يرجى اختيار المنصة التي تريد التحميل منها:\n\n"
        "<b>Welcome to ALL MEDIA DOWNLOADER 🤖⭐</b>\n"
        "The all-in-one bot for high-quality media downloads.\n"
        "Please select the platform you want to use:"
    )
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    # تذكر استبدال الروابط بالروابط الفعلية لبوتاتك
    markup.add(
        types.InlineKeyboardButton("Instagram 📸", url=INSTA_BOT),
        types.InlineKeyboardButton("TikTok 🎵", url=TIKTOK_BOT),
        types.InlineKeyboardButton("X (Twitter) 🐦", url=X_BOT),
        types.InlineKeyboardButton("Snapchat 👻", url=SNAP_BOT)
    )
    
    bot.send_message(user_id, welcome_text, reply_markup=markup, parse_mode='HTML')
