import pyjokes
from translate import Translator
import time
import pyautogui as pag
import os
import subprocess
import webbrowser
from datetime import datetime
import pyautogui
import pyowm
import pyttsx3
import speech_recognition
from pyowm.utils.config import get_default_config
owm = pyowm.OWM('7d49b7a2809575465817c860e90404b5')
config_dict = get_default_config()
config_dict['language'] = 'ru'

place = 'Раменское'
mgr = owm.weather_manager()
observation = mgr.weather_at_place("place")
w = observation.weather
while True:
    temp = w.temperature('celsius')["temp"]
    status = w.detailed_status
    translator = Translator(to_lang="ru")
    translation = translator.translate(pyjokes.get_joke())
    lol = translation
    now = datetime.now()
    hour = now.strftime("%H")
    minutes = now.strftime("%M")

    sr = speech_recognition.Recognizer()
    sr.pause_threshold = 0.5
    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.5)
        audio = sr.listen(source=mic)
        query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()

    def volume_up():
        return 'Прибавляю громкость, сэр.'

    def volume_down():
        return 'Убавляю громкость, сэр.'

    def volume_mute():
        return 'Выключаю громкость, сэр.'

    def hello():
        return 'Здравствуйте, хозяин!'

    def goodbye():
        return 'До свидания, хозяин!'

    def thanks():
        return 'Спасибо, сэр!'

    def you():
        return 'Отлично, сэр!'

    def stop():
        return 'Уже ухожу, хозяин!'

    def openbrowser():
        return 'Открываю браузер, сэр.'

    def search():
        return 'Открываю, сэр.'

    def whatsapp():
        return 'Открываю Whatsapp, сэр.'

    def iam_here():
        return 'Я тут, хозяин.'

    def telegram():
        return 'Открываю Telegram, сэр!'

    def weather():
        return "Сейчас в " + "Раменском" + ": " + str(temp) + "°C, " + status + "."

    def shutdown():
        return 'Выключаю компьютер, сэр.'

    def shutdown1():
        return 'Перезагружаю компьютер, сэр.'

    def on():
        return 'Включаю, сэр.'

    def create_task():
        return 'Что добавим в список дел, сэр?'

    def search_in_yandex():
        return 'Что найти, сэр?'

    def write():
        return 'Что написать, сэр?'

    def no_thanks():
        return 'Не за что, сэр!'

    def joke():
        return lol

    def whats_time():
        return "Сейчас " + str(hour) + " часов " + str(minutes) + " минут."

    if 'привет' in query:
        print(hello())
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(hello())
        engine.runAndWait()
    elif 'спасибо' in query:
        print(no_thanks())
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(no_thanks())
        engine.runAndWait()
    elif 'как дела' in query:
        print(you())
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(you())
        engine.runAndWait()
    elif 'молодец' in query:
        print(thanks())
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(thanks())
        engine.runAndWait()
    elif 'добавь задачу' in query:
        print(create_task())
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(create_task())
        engine.runAndWait()
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            todo_word = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        with open('todo-list.txt', 'a') as file:
            file.write(f'{todo_word}\n')
        print(f'Задача {todo_word} добавлена в список дел, сэр')
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(f'Задача {todo_word} добавлена в список дел, сэр')
        engine.runAndWait()
    elif 'найди' in query:
        print(search_in_yandex())
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(search_in_yandex())
        engine.runAndWait()
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            search = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        webbrowser.open(f'https://ya.ru/search/?text={search}&lr=10750&search_source=yaru_desktop_common&search_domain=yaru')
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(f'Ищю в Яндексе {search}, сэр')
        engine.runAndWait()
    elif 'открой браузер' in query:
        print(openbrowser())
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(openbrowser())
        engine.runAndWait()
        subprocess.call("C:/Users/pavmi/AppData/Local/Yandex/YandexBrowser/Application/browser.exe")
    elif 'открой whatsapp' in query:
        print(whatsapp())
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(whatsapp())
        engine.runAndWait()
        subprocess.call("C:/Program Files/WindowsApps/5319275A.WhatsAppDesktop_2.2314.6.0_x64__cv1g1gvanyjgm/WhatsApp.exe")
    elif 'открой telegram' in query:
        print(telegram())
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(telegram())
        engine.runAndWait()
        subprocess.call("C:/Users/pavmi/AppData/Roaming/Telegram Desktop/Telegram.exe")
    elif 'ау' in query:
        print(iam_here())
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(iam_here())
        engine.runAndWait()
    elif 'сколько время' in query:
        print(whats_time())
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(whats_time())
        engine.runAndWait()
    elif 'какая сейчас погода' in query:
        print(weather())
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(weather())
        engine.runAndWait()
    elif 'открой google' in query:
        print(str(search()))
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(search())
        engine.runAndWait()
        webbrowser.open('https://www.google.ru/')
    elif 'открой яндекс' in query:
        print(str(search()))
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(search())
        engine.runAndWait()
        webbrowser.open('https://ya.ru/')
    elif 'открой школьный портал' in query:
        print(str(search()))
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(search())
        engine.runAndWait()
        webbrowser.open('https://school.mosreg.ru/userfeed')
    elif 'открой youtube' in query:
        print(str(search()))
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(search())
        engine.runAndWait()
        webbrowser.open('https://www.youtube.com/')
    elif 'включи музыку' in query:
        print(str(on()))
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(on())
        engine.runAndWait()
        webbrowser.open('https://music.yandex.ru/home')
        time.sleep(15)
        pag.click(577, 561)
    elif 'нажми пробел' in query:
        pag.typewrite(' ')
    elif 'нажми f' in query:
        pag.typewrite('f')
    elif 'во весь экран' in query:
        pag.hotkey('f11')
    elif 'следующий трек' in query:
        pag.click(190,986)
    elif 'расскажи шутку' in query:
        print(joke())
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(joke())
        engine.runAndWait()
    elif 'напиши' in query:
        print(write())
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(write())
        engine.runAndWait()
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            writing = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        pyautogui.write(f'{writing}', interval=0.25)
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(f'Я написал {writing}, сэр')
        engine.runAndWait()
        print(f'Я написал {writing}, сэр')
    elif 'выключи компьютер' in query:
        print(shutdown())
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(shutdown())
        engine.runAndWait()
        os.system('shutdown -s')
        break
    elif 'перезагрузи компьютер' in query:
        print(shutdown1())
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(shutdown1())
        engine.runAndWait()
        os.system("shutdown /r /t 1")
        break
    elif 'прибавь громкость' in query:
        print(volume_up())
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(volume_up())
        engine.runAndWait()
        # Прибавить громкость
        pyautogui.press("volumeup")
    elif 'убавь громкость' in query:
        print(volume_down())
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(volume_down())
        engine.runAndWait()
        # Убавить громкость
        pyautogui.press("volumedown")
    elif 'выключи звук' in query:
        print(volume_mute())
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(volume_mute())
        engine.runAndWait()
        # Убавить громкость
        pyautogui.press("volumemute")
    elif 'пока' in query:
        print(goodbye())
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(goodbye())
        engine.runAndWait()
        break
    elif 'стоп' in query:
        print(stop())
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(stop())
        engine.runAndWait()
        break
    else:
        print('Я вас не понял, сэр.')
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say('Я вас не понял, сэр.')
        engine.runAndWait()
