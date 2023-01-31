class Config:
    STATUS = "GitHub - YanWebFly" #Статус, когда музыка не играет
    VK_TOKEN = "" #Токен VK API
    CLIENT_ID = "" #ID Приложения Spotify
    SECRET_CODE = "" #Токен Spotify API
    REDIRECT_URI = "http://localhost:8888/callback" #Не рекомендую менять эту строчку!
    USERNAME = "" #username из ссылки на ваш профиль spotify
    SCOPE = "user-read-playback-state user-library-read" #Не рекомендую менять эту строчку!
    DEV = False