import os
import glob
import random
import asyncio
from yt_dlp import YoutubeDL
from telethon import events
from Matrix import blal
from ..Config import Config

plugin_category = "الادوات"

def get_cookies_file():
    folder_path = f"{os.getcwd()}/devBiLaL"
    txt_files = glob.glob(os.path.join(folder_path, '*.txt'))
    if not txt_files:
        raise FileNotFoundError("No .txt files found in the specified folder.")
    cookie_txt_file = random.choice(txt_files)
    return cookie_txt_file


@blal.on(events.NewMessage)
async def handler(event):
    if event.message.text.startswith('.بحـث'):
        try:
            query = event.message.text.split(' ', 1)[1]  # احصل على استعلام البحث
            await event.reply('جاري البحث...')
            
            # إعداد خيارات البحث
            ydl_opts = {
                'format': 'bestaudio/best',
                'extractaudio': True,  # استخراج الصوت فقط
                'audioformat': 'mp3',  # تنسيق الصوت
                'outtmpl': 'downloads/%(title)s.%(ext)s',  # مسار حفظ الملف
                'cookiefile': 'get_cookies_file()',  # مسار ملف تعريف الارتباط
            }
            
            # البحث عن الفيديو باستخدام yt-dlp
            with YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(f"ytsearch:{query}", download=False)  # استخدم ytsearch للبحث
                video_url = info_dict['entries'][0]['url']  # الحصول على رابط أول نتيجة
            
                # تحميل الفيديو
                await event.reply('جاري تحميل الموسيقى...')
                os.makedirs('downloads', exist_ok=True)  # تأكد من وجود مجلد التحميل
                
                ydl.download([video_url])
                
                # احصل على اسم الملف المحمل
                filename = f'downloads/{info_dict["entries"][0]["title"]}.mp3'
                
                # أرسل الملف إلى Telegram
                await zq_lo.send_file(event.chat_id, filename)
                await event.reply('تم تحميل وإرسال الصوت بنجاح!')

        except Exception as e:
            await event.reply(f'حدث خطأ أثناء البحث أو التحميل: {str(e)}')
