import telebot
import re

# Initialize bot with token
bot = telebot.TeleBot("7694475974:AAETAH61B9uYTNoE07rnhufTCZ7wcNKv3tc")

# Character mappings for Arabic to Yazidi
ar_to_yazidi = {
    'ا': '𐺀', 'أ': '𐺀', 'إ': '𐺀', 'ة': '𐺀', 'ى': '𐺀',
    'ب': '𐺁', 'پ': '𐺂', 'ت': '𐺄', 'ث': '𐺅',
    'ج': '𐺆', 'چ': '𐺇', 'ح': '𐺉', 'خ': '𐺊',
    'د': '𐺋', 'ذ': '𐺌', 'ر': '𐺍', 'ڕ': '𐺎',
    'ز': '𐺏', 'ژ': '𐺐', 'س': '𐺑', 'ش': '𐺒',
    'ص': '𐺓', 'ض': '𐺔', 'ط': '𐺕', 'ظ': '𐺖',
    'ع': '𐺗', 'غ': '𐺘', 'ف': '𐺙', 'ڤ': '𐺚',
    'ق': '𐺜', 'ك': '𐺝', 'گ': '𐺟', 'ل': '𐺠',
    'م': '𐺡', 'ن': '𐺢', 'و': '𐺣', 'ۆ': '𐺥', 'ؤ': '𐺥',
    'ه': '𐺧', 'ح': '𐺨', 'ي': '𐺨', 'ێ': '𐺩', 'ئ': '𐺩'
}

# Create reverse mapping for Yazidi to Arabic with primary mappings
yazidi_to_ar = {
    '𐺀': 'ا', '𐺁': 'ب', '𐺂': 'پ', '𐺄': 'ت', '𐺅': 'ث',
    '𐺆': 'ج', '𐺇': 'چ', '𐺉': 'ح', '𐺊': 'خ',
    '𐺋': 'د', '𐺌': 'ذ', '𐺍': 'ر', '𐺎': 'ڕ',
    '𐺏': 'ز', '𐺐': 'ژ', '𐺑': 'س', '𐺒': 'ش',
    '𐺓': 'ص', '𐺔': 'ض', '𐺕': 'ط', '𐺖': 'ظ',
    '𐺗': 'ع', '𐺘': 'غ', '𐺙': 'ف', '𐺚': 'ڤ',
    '𐺜': 'ق', '𐺝': 'ك', '𐺟': 'گ', '𐺠': 'ل',
    '𐺡': 'م', '𐺢': 'ن', '𐺣': 'و', '𐺥': 'ۆ',
    '𐺧': 'ه', '𐺨': 'ي', '𐺩': 'ێ'
}

def convert_to_yazidi(text):
    """Convert Arabic text to Yazidi script"""
    result = ''
    for char in text:
        result += ar_to_yazidi.get(char, char)
    return result

def convert_to_arabic(text):
    """Convert Yazidi script to Arabic"""
    result = ''
    for char in text:
        result += yazidi_to_ar.get(char, char)
    return result

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = """مرحباً! أنا بوت تحويل النصوص بين العربية والإيزيدية.
للتحويل من العربية إلى الإيزيدية، أرسل النص العربي مباشرة.
للتحويل من الإيزيدية إلى العربية، أرسل النص الإيزيدي مباشرة.تم برمجة البوت بواسطة @darweshshngale3"""
    bot.reply_to(message, welcome_text)

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """كيفية استخدام البوت:
1. للتحويل من العربية إلى الإيزيدية: أرسل النص العربي مباشرة
2. للتحويل من الإيزيدية إلى العربية: أرسل النص الإيزيدي مباشرة
البوت سيتعرف تلقائياً على نوع النص ويقوم بالتحويل المناسب.تم برمجة البوت بواسطة @darweshshngale3"""
    bot.reply_to(message, help_text)

@bot.message_handler(func=lambda message: True)
def convert_text(message):
    text = message.text

    # Check if text contains Yazidi characters
    if any(char in yazidi_to_ar for char in text):
        result = convert_to_arabic(text)
        response = f"\n{result}"
    else:
        result = convert_to_yazidi(text)
        response = f"\n{result}"

    bot.reply_to(message, response)

# Start the bot
if __name__ == "__main__":
    print("Bot is running...")
    try:
        bot.infinity_polling()
    except Exception as e:
        print(f"Error occurred: {e}")
        from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()
