import telebot
from telegram import BOT_TOKEN, CLIENT, song_callback_query,\
    album_callback_query, new_message, artist_callback_query,\
    playlist_callback_query

if __name__ == '__main__':
    try:
        print('[BOT] Starting...')
        CLIENT.start(bot_token=BOT_TOKEN)
        CLIENT.run_until_disconnected()
    except Exception as e:
        print(f'[BOT] Error: {e}')