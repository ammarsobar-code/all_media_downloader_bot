import os, telebot, time, sys, subprocess
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

# --- 2. وظيفة التنظيف التلقائي (Auto-Clean) ---
def auto_clean_environment():
    """تنظيف الذاكرة المؤقتة لضمان استقرار البوت"""
    try:
        # ملاحظة: pkill قد تغلق البوت نفسه إذا لم يتم تخصيصها، لذا يفضل تنظيف الـ Cache البرمجي
        import gc
        gc.collect() # تنظيف الذاكرة (Garbage Collection)
        print("清理 🧹 Menu Bot Environment Cleaned")
    except Exception as e:
        print(f"Clean error: {e}")

# --- 3. إعدادات البوت وروابط المنصات ---
API_TOKEN = os.getenv('BOT_TOKEN') 
bot = telebot.TeleBot(API_TOKEN)

INSTA_BOT = "https://t.me/Insta_1Downloader_Bot"
TIKTOK_BOT = "https://t.me/Tiktok_1Downloader_Bot"
X_BOT = "https://t.me/X_1Downloader_Bot"
SNAP_BOT = "https://t.me/Snap_1Downloader_Bot"

# --- 4. وظيفة إنشاء القائمة (لإعادة استخدامها) ---
def send_main_menu(message):
    user_id = message.chat.id
    
    welcome_text = (
        "<b>مرحباً بك في قائمة البوتات الشاملة 🤖⭐</b>\n\n"
        "يرجى اختيار المنصة التي تريد تحميل المقاطع منها من الأسفل:\n\n"
        "<b>Welcome to the Main Bot Menu 🤖⭐</b>\n"
        "Please select the platform you want to download from below:"
    )
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_insta = types.InlineKeyboardButton("انستجرام | Instagram 📸", url=INSTA_BOT)
    btn_tiktok = types.InlineKeyboardButton("تيك توك | TikTok 🎵", url=TIKTOK_BOT)
    btn_x = types.InlineKeyboardButton("منصة اكس | X (Twitter) 🐦", url=X_BOT)
    btn_snap = types.InlineKeyboardButton("سناب شات | Snapchat 👻", url=SNAP_BOT)
    
    markup.add(btn_insta, btn_tiktok, btn_x, btn_snap)
    
    # تنفيذ التنظيف قبل الإرسال
    auto_clean_environment()
    
    bot.send_message(user_id, welcome_text, reply_markup=markup, parse_mode='HTML')

# --- 5. معالجة أمر البداية وأي رسالة أخرى ---
@bot.message_handler(commands=['start'])
def start_command(message):
    send_main_menu(message)

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    # في حال أرسل المستخدم أي شيء، نعيد له القائمة الرئيسية
    send_main_menu(message)

# --- 6. التشغيل الآمن ---
if __name__ == "__main__":
    keep_alive()
    try:
        bot.remove_webhook()
    except:
        pass
    time.sleep(1)
    print("Main Menu Bot is starting...")
    # infinity_polling تضمن استمرار البوت حتى لو حدث خطأ في الشبكة
    bot.infinity_polling(timeout=20, long_polling_timeout=10)
