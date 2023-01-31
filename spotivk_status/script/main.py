print("Запускаю скрипт...")

import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth as sOauth
from colorama import Fore
import vk_api
import time

from config import Config

if (Config.DEV == True):
    print("Включён режим разработчика (отладка)")
    print("STATUS = " + Config.STATUS)
    print("VK_TOKEN = " + Config.VK_TOKEN)
    print("CLIENT_ID = " + Config.CLIENT_ID)
    print("SECRET_CODE = " + Config.SECRET_CODE)
    print("REDIRECT_URI = " + Config.REDIRECT_URI)
    print("USERNAME = " + Config.USERNAME)

if (Config.DEV == True):
    print("Устанавливаю соединение с Spotify API...")
spotify = sp.Spotify(auth_manager=sOauth(scope=Config.SCOPE, client_id=Config.CLIENT_ID, client_secret=Config.SECRET_CODE, redirect_uri=Config.REDIRECT_URI, username=Config.USERNAME))
if (Config.DEV == True):
    print("Соединение установлено!")
if (Config.DEV == True):
    print("Устанавливаю соединение с VK API...")
try:
    vk = vk_api.VkApi(token=Config.VK_TOKEN).get_api()
    user = vk.account.getProfileInfo()
    if (Config.DEV == True):
        print("Соединение установлено!")
except:
    if (Config.DEV == True):
        print("Соединение не установлено!")

current_playing = []
last_playing = []

def update_status_to_standart():
    if (vk.status.get(user_id=user["id"])["text"] != Config.STATUS):
        vk.status.set(text=Config.STATUS)
        if (Config.DEV == True):
            print("Статус изменён на стандартный, так как ничего не воспроизводится!")

def update_status(last_playing: list) -> list:
    current_playing = spotify.current_user_playing_track()

    if current_playing is None:
        update_status_to_standart()
        return current_playing

    if (current_playing["currently_playing_type"] != "ad"):
        if current_playing["is_playing"] is False:
            update_status_to_standart()
            return current_playing

        #Если ничего не вернулось
        time.sleep(1)
        try:
            current_playing = [current_playing["item"]["name"], current_playing["item"]["artists"][0]["name"]]
        except:
            return current_playing

        if current_playing != last_playing:
            vk.status.set(text="Слушает Spotify | " + current_playing[0] + " - " + current_playing[1] + "\nGitHub: YanWebFly")
            print(Fore.GREEN + "Now playing: " + " " + current_playing[0] + " " + current_playing[1])
    else:
        vk.status.set(text="Слушает Spotify | Реклама\nGitHub: YanWebFly")
    return current_playing

while True:
    try:
        current_playing = update_status(current_playing)
    except (KeyboardInterrupt, SystemExit):
        update_status_to_standart()
        raise