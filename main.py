from telethon.sync import TelegramClient
from telethon.tl.types import Channel

    # معلومات الدخول
api_id = 12345678        # استبدله بـ API ID الخاص بك
api_hash = 'your hash'  # استبدله بـ API HASH الخاص بك

    # بدء الجلسة
with TelegramClient('anon', api_id, api_hash) as client:
        print("✅ Logged in as:", client.get_me().username)
        print("📋 List of all channels & groups:\n")

        async def list_all():
            async for dialog in client.iter_dialogs():
                entity = dialog.entity
                if isinstance(entity, Channel):
                    print(f"{entity.title} - ID: {entity.id} - Hash: {entity.access_hash}")

        client.loop.run_until_complete(list_all())
