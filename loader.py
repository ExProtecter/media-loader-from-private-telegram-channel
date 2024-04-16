from pyrogram import Client
api_id = int(input('Введите API_ID: '))
api_hash = input('Введите API_hash: ')
ch_id = int(input('Введите ID канала: '))

with Client('my_account', api_id, api_hash) as app:
    channel = app.get_chat(ch_id)
    messages = app.get_chat_history(channel.id)

    for message in messages:
        if message.document:
            # Скачать документ
            app.download_media(message.document)
        elif message.photo:
            # Скачать фото
            app.download_media(message.photo)
        elif message.video:
            # Скачать видео
            app.download_media(message.video)
        # Добавьте другие типы файлов, если необходимо

print('Скачивание файлов успешно завершено!')
