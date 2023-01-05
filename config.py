import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
# للنشر المحلي
if os.path.exists(".env"):
    load_dotenv(".env")
# الفارات
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION")
HNDLR   =   نظام  التشغيل  getenv ( "HNDLR"  ،  "$" )

contact_filter    =    عوامل   التصفية . إنشاء (       lambda    _   ،   __   ،   الرسالة : ( message . from_user    و    message . from_user . is_contact )       أو    رسالة . صادرة )
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicTelethon"))
call_py = PyTgCalls(bot)
