import os, telebot, time
from telebot import types
from flask import Flask
from threading import Thread

# --- 1. سيرفر Flask للحفاظ على نشاط البوت ---
app = Flask('')
@app.route('/')
def home(): return "Main Menu Bot Live"
def run(): app.run(host='0.0.0.0', port=8080)
def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()

# --- 2. إعدادات البوت (ضع توكن بوت القائمة هنا) ---
API_TOKEN = os.getenv('BOT_TOKEN') 
bot = telebot.TeleBot(API_TOKEN)

# روابط بوتاتك (استبدل كلمة YourBot_Username بيوزر كل بوت عندك)
INSTA_BOT = "https://t.me/Insta_1Downloader_Bot"
TIKTOK_BOT = "https://t.me/Tiktok_1Downloader_Bot"
X_BOT = "https://t.me/X_1Downloader_Bot"
SNAP_BOT = "https://t.me/Snap_1Downloader_Bot"

# --- 3. معالج أمر البداية /start ---
@bot.message_handler(commands=['start'])
def main_menu(message):
    user_id = message.chat.id
    
    welcome_text = (
        "<b>مرحباً بك في قائمة البوتات الشاملة 🤖⭐</b>\n\n"
        "يرجى اختيار المنصة التي تريد تحميل المقاطع منها من الأسفل:\n\n"
        "<b>Welcome to the Main Bot Menu 🤖⭐</b>\n"
        "Please select the platform you want to download from below:"
    )
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    # أزرار البوتات
    btn_insta = types.InlineKeyboardButton("انستجرام | Instagram 📸", url=INSTA_BOT)
    btn_tiktok = types.InlineKeyboardButton("تيك توك | TikTok 🎵", url=TIKTOK_BOT)
    btn_x = types.InlineKeyboardButton("منصة اكس | X (Twitter) 🐦", url=X_BOT)
    btn_snap = types.InlineKeyboardButton("سناب شات | Snapchat 👻", url=SNAP_BOT)
    
    # إضافة الأزرار للماركب
    markup.add(btn_insta, btn_tiktok, btn_x, btn_snap)
    
    bot.send_message(user_id, welcome_text, reply_markup=markup, parse_mode='HTML')

# --- 4. معالج لأي رسالة أخرى ---
@bot.message_handler(func=lambda message: True)
def hint(message):
    bot.reply_to(message, "<b>يرجى استخدام القائمة في الأعلى للانتقال إلى البوت المطلوب 👆🏼</b>", parse_mode='HTML')

# --- 5. التشغيل الآمن ---
if __name__ == "__main__":
    keep_alive()
    try:
        bot.remove_webhook()
    except:
        pass
    time.sleep(1)
    print("Main Menu Bot is starting...")
    bot.infinity_polling(timeout=20, long_polling_timeout=10)
