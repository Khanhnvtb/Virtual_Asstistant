import playsound
from gtts import gTTS
import pyttsx3
import speech_recognition as sr
import os
from datetime import datetime
from datetime import date
from random import choice

robot_mouth = pyttsx3.init()


def speak(robot_brain):
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()


def speakVi(robot_brain):
    tts = gTTS(text=robot_brain, lang="vi", slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3")
    os.remove("sound.mp3")


def hear(lg):
    c = sr.Recognizer()
    with sr.Microphone() as Source:
        c.pause_threshold = 1
        audio = c.listen(Source)
    try:
        query = c.recognize_google(audio, language=lg)
    except sr.UnknownValueError:
        query = ''
    return query.lower()


def speakHello(lg):
    hour = datetime.now().hour
    if 6 <= hour <= 12:
        if lg == 'en':
            return 'Good Morning sir'
        else:
            return 'Buổi sáng vui vẻ'
    elif 12 <= hour <= 18:
        if lg == 'en':
            return 'Good Afternoon sir'
        else:
            return 'Chào buổi chiều'
    elif 18 <= hour <= 24:
        if lg == 'en':
            return 'Good Night sir'
        else:
            return 'Ngài ăn cơm chưa'


def speakTime(lg):
    if lg == 'en':
        Time = datetime.now().strftime('%I:%M:%p')
        return Time
    else:
        now = datetime.now()
        return 'Bây giờ là %d giờ %d phút' % (now.hour, now.minute)


def speakToday(lg):
    if lg == 'en':
        today = date.today().strftime("%B %d, %Y")
        return today
    else:
        now = datetime.now()
        return "Hôm nay là ngày %d tháng %d năm %d" % (now.day, now.month, now.year)


def speakOut(lg):
    if lg == 'en':
        return 'Bye'
    else:
        return 'Tạm biệt'


def speakGreeting(lg, name):
    if lg == "en":
        loiChao = ["Hi {}, how can I help you?".format(name),
                   "Hello {}, how can Tuesday help you?".format(name),
                   "Hello {}".format(name)]
        return choice(loiChao)
    else:
        loiChao = ["Chào {}, Tôi có thể giúp gì cho Cậu ạ?".format(name),
                   "Chào bạn {}, Tuesday có thể giúp gì cho bạn ạ?".format(name),
                   "Xin chào bạn {} nhé".format(name)]
        return choice(loiChao)


# nếu hỏi tên bạn là gì?
def yourName(lg, name):
    if lg == 'en':
        name_ban = ["Your name is {}".format(name),
                    "Do you think Tuesday forgot your name? Your name is {}".format(name),
                    "Hi {}, I don't forget your name".format(name),
                    "I have a super memory, my buddy {}!! Hihi...".format(name)]
        return choice(name_ban)
    else:
        name_ban = ["Tên của bạn là: {} nè".format(name),
                    "Bạn tưởng Tuesday quên tên bạn sao? tên bạn là {}".format(name),
                    "Chào bạn {} nhé, tôi không quên tên của bạn đâu".format(name),
                    "Tôi có trí nhớ siêu việt đấy bạn {} ạ!! Hihi...".format(name)]
        return choice(name_ban)
