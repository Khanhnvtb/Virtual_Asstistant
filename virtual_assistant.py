from tkinter import *
from PIL import Image, ImageTk
from communicate import *
import threading
from threading import Thread
from internet import *
from introduce import *
from hardwareProcessing import *
from controlYoutube import *
from exception import *
from appcontrol import *

chatMode = 1

lg = "vi"
name = ""
chatBgColor = "#12232e"
state = 1


def raise_frame(frame):
    frame.tkraise()


def next():
    window.destroy()


def selectVn():
    def Vi():
        speakVi(
            "Chào mừng bạn đến với trợ lý ảo Ây Ai, Tôi là Tuesday. Tôi sẽ giải đáp và tâm sự cùng bạn")

    global lg
    lg = "vi"
    button1.destroy()
    button2.destroy()
    text = Label(f1,
                 text="Chào mừng bạn đến với trợ lý ảo AI\nTôi là Tuesday\nTôi sẽ giải đáp và tâm sự cùng bạn",
                 font=("font", 15), width=38, fg="red", bg="white")
    text.place(x=250, y=150)
    timer = threading.Timer(0.5, Vi)
    timer.start()
    timer = threading.Timer(9.5, lambda: raise_frame(f3))
    timer.start()


def selectEnglish():
    def En():
        speak(
            "Welcome to the vitual assistant AI, I'm Tuesday. I will answer and confide in you ")

    global lg
    lg = "en"
    button1.destroy()
    button2.destroy()
    text = Label(f1, text="Welcome to the virtual assistant AI\nI'm Tuesday\nI will answer and confide in you",
                 font=("font", 15), width=38, fg="red", bg="white")
    text.place(x=250, y=150)
    timer = threading.Timer(0.5, En)
    timer.start()
    timer = threading.Timer(6, lambda: raise_frame(f2))
    timer.start()


def start():
    speak("english or vietnamese")


window = Tk()
window.title("AI assistant")
w_width, w_height = 817, 459
s_width, s_height = window.winfo_screenwidth(), window.winfo_screenheight()
x, y = (s_width / 2) - (w_width / 2), (s_height / 2) - (w_height / 2)
window.geometry('%dx%d+%d+%d' % (w_width, w_height, x, y - 30))

icon = ImageTk.PhotoImage(Image.open("icon.jpg"))
window.iconphoto(True, icon)
timer = threading.Timer(0.5, start)
timer.start()

f2 = Frame(window)
f2.grid(row=0, column=0, sticky='news')
f3 = Frame(window)
f3.grid(row=0, column=0, sticky='news')
f1 = Frame(window)
f1.grid(row=0, column=0, sticky='news')

img2 = Image.open("background.jpg")
img = ImageTk.PhotoImage(img2)
label = Label(f1, image=img)
label.pack()

button1 = Button(f1, text="Việt Nam", font=(
    "Consolas", 20), command=selectVn, fg='blue', bg='pink')
button1.place(x=300, y=190)

button2 = Button(f1, text="English", font=(
    "Consolas", 20), command=selectEnglish, fg='blue', bg='pink')
button2.place(x=500, y=190)

img3 = Image.open("Page2En.jpg")
intro_img1 = ImageTk.PhotoImage(img3)
Label(f2, image=intro_img1).pack()
Button(f2, text="Go to Chatbot", font=(
    "Consolas", 17), fg='blue', bg='pink', command=next).place(x=300, y=410)

img4 = Image.open("Page2Vi.jpg")
intro_img2 = ImageTk.PhotoImage(img4)
Label(f3, image=intro_img2).pack()
Button(f3, text="Vào box chat", font=(
    "Consolas", 17), fg='blue', bg='pink', command=next).place(x=320, y=410)

window.mainloop()


def textToSpeech(text, display=True, icon=True):
    AITaskStatusLbl['text'] = 'Speaking...'
    if icon:
        Label(chat_frame, image=botIcon, bg=chatBgColor).pack(
            anchor='w', pady=0)
    if display:
        attachTOframe(text, True)
    words = text.split()
    text = ''
    for i in words:
        text += i + ' '
    if lg == 'vi':
        speakVi(text)
    else:
        speak(text)


def textWiki(content):
    words = content.split()
    cnt = 0
    txt = ''
    for word in words:
        cnt += 1
        txt += word + ' '
        if cnt == 8:
            txt += '\n'
            cnt = 0
    return txt


def isContain(text, query):
    global state
    for i in range(len(text)):
        if text[i] in query:
            state = 1
            return True
    return False


def main(query):
    if isContain(["hello", "chào"], query):
        textToSpeech(speakHello(lg))
        return
    if isContain(["time", "giờ"], query):
        textToSpeech(speakTime(lg))
        return
    if isContain(["today", "hôm nay"], query):
        textToSpeech(speakToday(lg))
        return
    if isContain(["open app", "open file", "mở ứng dụng", "mở file"], query):
        if lg == 'en':
            text = 'Which one?'
        else:
            text = 'Cái nào?'
        textToSpeech(text)
        search = record(False)
        textToSpeech(open_application(lg, search))
        return
    if isContain(['lock', 'khóa'], query):
        textToSpeech(lockPC(lg))
        return
    if isContain(['shut down', 'tắt máy'], query):
        textToSpeech(shutDown(lg))
        return
    if isContain(['restart', 'khởi động lại'], query):
        textToSpeech(restart(lg))
        return
    if isContain(['empty recycle bin', "dọn sạch thùng rác", "làm rỗng thùng rác"], query):
        textToSpeech(emptyRecyclebin(lg))
        return
    if isContain(["close app", "tắt app", "tắt ứng dụng"], query):
        textToSpeech(closeApp(lg))
        return
    if isContain(["next song", "chuyển bài"], query):
        textToSpeech(nextSong(lg))
        return
    if isContain(["full screen", "toàn màn hình"], query):
        textToSpeech(fullScreen(lg))
        return
    if isContain(["forward", "tiến"], query):
        textToSpeech(forward(lg))
        return
    if isContain(["back", "lùi"], query):
        textToSpeech(back(lg))
        return
    if isContain(["pause", "tạm dừng"], query):
        textToSpeech(pause(lg))
        return
    if isContain(["play", "bắt đầu"], query):
        textToSpeech(play(lg))
        return
    if isContain(["volume up", "tăng âm lượng"], query):
        textToSpeech(volumeUp(lg))
        return
    if isContain(["volume down", "giảm âm lượng"], query):
        textToSpeech(volumeDown(lg))
        return
    if isContain(
            ["tên tôi", "tên tao", "tôi tên", "tao tên",
             "tên của tôi", "biết tên", "tên của tao", "my name"],
            query):
        textToSpeech(yourName(lg, name))
        return
    if isContain(["introduce", "giới thiệu"], query):
        textToSpeech(speakIntroduce(lg))
        return
    if isContain(["list", "help", "danh sách", "giúp"], query):
        textToSpeech(help_me(lg))
        return
    if isContain(
            ["tên là gì", "tên mày là gì", "tên bạn là gì", "mày tên là gì", "bạn tên là gì", "gọi bạn", "gọi mày",
             "your name", "call you"], query):
        textToSpeech(fullNameAI(lg))
        return
    if isContain(["sinh ra", "quê hương", "sống", "đến từ", "nơi sinh", "born", "living", "live", "from"], query):
        textToSpeech(countryAI(lg))
        return
    if isContain(["tuổi", "năm", "sinh", "age", "birth year", "how old are you"], query):
        textToSpeech(ageAI(lg))
        return
    if isContain(["người yêu", "lover", "boyfriend", "girlfriend"], query):
        textToSpeech(loverAI(lg))
        return
    if isContain(['google'], query):
        if lg == 'vi':
            textToSpeech('Bạn muốn tìm kiếm cái gì?')
        else:
            textToSpeech("tell me what you want to search")
        search = record(False)
        text = solveGoogle(lg, search)
        textToSpeech(text)
        return
    if isContain(['youtube'], query):
        if lg == 'vi':
            textToSpeech('Bạn muốn xem cái gì?')
        else:
            textToSpeech("What should I search boss")
        watch = record(False)
        text = solveYoutube(lg, watch)
        textToSpeech(text)
        return
    if isContain(["music", "nhạc"], query):
        if lg == 'vi':
            textToSpeech('Xin mời bạn chọn tên bài hát')
        else:
            textToSpeech("Please choose song name")
        song = record(False)
        text = play_song(lg, song)
        textToSpeech(text)
        return
    if isContain(["weather", "thời tiết"], query):
        if lg == 'vi':
            textToSpeech('Bạn muốn xem thời tiết ở đâu')
        else:
            textToSpeech("where you want to known")
        city = record(False)
        text = current_weather(lg, city)
        textToSpeech(text)
        return
    if isContain(["news", "tin tức", "báo"], query):
        text = read_news(lg)
        textToSpeech(text)
        return
    if isContain(["email", "gửi thư", "thư"], query):
        if lg == 'vi':
            textToSpeech('Bạn muốn gửi email cho ai')
        else:
            textToSpeech("Who do you email")
        user = record(False)
        if lg == 'vi':
            textToSpeech('Nội dung bạn muốn gửi là gì')
        else:
            textToSpeech("What content do you want to send?")
        content = record(False)
        text = send_email(lg, user, content)
        textToSpeech(text)
        return
    if isContain(["wiki"], query):
        if lg == 'vi':
            textToSpeech('Bạn muốn nghe về gì ạ')
        else:
            textToSpeech("What do you want to hear")
        content = record(False)
        contents = tell_me_about(lg, content)
        textToSpeech(textWiki(contents[0]))
        for content in contents[1:]:
            textToSpeech("Bạn muốn nghe thêm không")
            ans = record(False)
            if isContain(["no", "không"], ans):
                if lg == 'vi':
                    textToSpeech("Cảm ơn bạn đã lắng nghe")
                else:
                    textToSpeech("Thank you for listening")
                break
            textToSpeech(textWiki(content))
        return
    if isContain(['map', 'direction', 'bản đồ', 'đường đi'], query):
        if "direction" in query or "đường đi" in query:
            if lg == 'vi':
                textToSpeech("Bạn đang ở đâu")
            else:
                textToSpeech('What is your starting location?')
            startingPoint = record(False)
            if lg == 'vi':
                textToSpeech("Bạn muốn đi đâu", True, False)
            else:
                textToSpeech('Where do you want to go', True, False)
            destinationPoint = record(False)
            if lg == 'vi':
                textToSpeech("Đang lấy vị trí...", True, False)
            else:
                textToSpeech("Getting Directions...", True, False)
            result = giveDirections(lg, startingPoint, destinationPoint)
            textToSpeech(result, True, False)
        else:
            textToSpeech(maps(query))
            return
    if isContain(['tab', "trang"], query):
        textToSpeech(Tab_Opt(lg, query))
        return
    if isContain(['window', 'close that', 'cửa sổ'], query):
        textToSpeech(Win_Opt(lg, query))
        return
    if isContain(["bye", "goodbye", "tạm biệt", "out", "kết thúc"], query):
        textToSpeech(speakOut(lg))
        root.destroy()
        return
    global state
    state = 1
    textToSpeech(speakHandsome(lg))


def record(iconDisplay=True):
    AITaskStatusLbl['text'] = 'Listening...'
    said = hear(lg)
    AITaskStatusLbl['text'] = 'Processing...'
    if said != '':
        print(f"\nUser said: {said}")
        if iconDisplay:
            Label(chat_frame, image=userIcon, bg=chatBgColor).pack(
                anchor='e', pady=0)
        attachTOframe(said)
        return said.lower()
    else:
        return 'None'


def voiceMedium():
    if lg == 'en':
        loi_chao_AI = ["Hello, tell me your name please",
                       "Hi, what your name, boss?",
                       "To use, tell me your name ",
                       "What can I call you?",
                       "For convenience, let me know your name"]
        textToSpeech(choice(loi_chao_AI))
    else:
        loi_chao_AI = ["Xin chào, cho tôi biết tên của cậu chủ nào",
                       "Chào bạn, Tên của bạn là gì nhỉ?",
                       "Để sử dụng, Cho tôi biết tên của bạn nhé",
                       "Tôi có thể gọi bạn là gì nhỉ?",
                       "Để tiện xưng hô, cho tôi biết tên của bạn nào"]
        text = choice(loi_chao_AI)
        textToSpeech(text)
    global name
    name = record(False)
    textToSpeech(speakGreeting(lg, name))
    global state
    while True:
        clearChatScreen()
        query = record()
        if query == 'None':
            if state == 1:
                state = 0
                textToSpeech(speakAgain(lg))
            continue
        main(query.lower())
        time.sleep(3)


def keyboardInput(e):
    user_input = UserField.get().lower()
    if user_input != "":
        clearChatScreen()
        Label(chat_frame, image=userIcon, bg="#12232e").pack(
            anchor='e', pady=0)
        attachTOframe(user_input.capitalize())
        Thread(target=main, args=(user_input,)).start()
    UserField.delete(0, END)


def attachTOframe(text, bot=False):
    if bot:
        botchat = Label(chat_frame, text=text, bg="#007cc7", fg="white",
                        justify=LEFT, wraplength=700, font=('Montserrat', 12, 'bold'))
        botchat.pack(anchor='w', ipadx=5, ipady=5, pady=5)
    else:
        userchat = Label(chat_frame, text=text, bg="#4da8da", fg='white',
                         justify=RIGHT, wraplength=300, font=('Montserrat', 12, 'bold'))
        userchat.pack(anchor='e', ipadx=2, ipady=2, pady=5)


def changeChatMode():
    global chatMode
    if chatMode == 1:
        VoiceModeFrame.pack_forget()
        TextModeFrame.pack(fill=BOTH)
        UserField.focus()
        chatMode = 0
    else:
        TextModeFrame.pack_forget()
        VoiceModeFrame.pack(fill=BOTH)
        root.focus()
        chatMode = 1


def clearChatScreen():
    for wid in chat_frame.winfo_children():
        wid.destroy()


root = Tk()
root.title('AI VIRTUAL')
icon = ImageTk.PhotoImage(Image.open("icon.jpg"))
root.iconphoto(True, icon)
w_width, w_height = 600, 800
s_width, s_height = root.winfo_screenwidth(), root.winfo_screenheight()
x, y = (s_width / 2) - (w_width / 2), (s_height / 2) - (w_height / 2)
root.geometry('%dx%d+%d+%d' % (w_width, w_height, x, y - 30))
root.pack_propagate(0)
chat_frame = Frame(root)
chat_frame.pack()

chat_frame = Frame(root, width=600, height=700, bg='#12232e')
chat_frame.pack(padx=10)
chat_frame.pack_propagate(0)

bottomFrame1 = Frame(root, bg='#dfdfdf', height=100)
bottomFrame1.pack(fill=X, side=BOTTOM)

VoiceModeFrame = Frame(bottomFrame1, bg='#dfdfdf')
VoiceModeFrame.pack(fill=BOTH)

TextModeFrame = Frame(bottomFrame1, bg='#dfdfdf')
TextModeFrame.pack(fill=BOTH)

TextModeFrame.pack_forget()

cblDarkImg = PhotoImage(file='centralButton.png')
cbl = Label(VoiceModeFrame, fg='white',
            image=cblDarkImg, bg='#dfdfdf')
cbl.pack(pady=17)
AITaskStatusLbl = Label(VoiceModeFrame, text='  Offline',
                        fg='white', bg="#203647", font=('montserrat', 16))
AITaskStatusLbl.place(x=235, y=32)

sphLight = PhotoImage(file="setting.png")
sphLight = sphLight.subsample(2, 2)
settingBtn = Button(VoiceModeFrame, image=sphLight, height=30, width=30, bg='#dfdfdf',
                    borderwidth=0, activebackground="#dfdfdf")
settingBtn.place(relx=1.0, y=30, x=-20, anchor="ne")

kbphLight = PhotoImage(file="keyboard.png")
kbphLight = kbphLight.subsample(2, 2)
kbBtn = Button(VoiceModeFrame, image=kbphLight, height=30, width=30, bg='#dfdfdf',
               borderwidth=0, activebackground="#dfdfdf", command=changeChatMode)
kbBtn.place(x=25, y=30)

micImg = PhotoImage(file="images/mic.png")
micImg = micImg.subsample(2, 2)
micBtn = Button(TextModeFrame, image=micImg, height=30, width=30, bg='#dfdfdf',
                borderwidth=0, activebackground="#dfdfdf", command=changeChatMode)
micBtn.place(relx=1.0, y=30, x=-40, anchor="ne")

TextFieldImg = PhotoImage(file='images/textField.png')
UserFieldLBL = Label(TextModeFrame, fg='white',
                     image=TextFieldImg, bg='#dfdfdf')
UserFieldLBL.pack(pady=17, side=LEFT, padx=50)
UserField = Entry(TextModeFrame, fg='white', bg='#203647', font=(
    'Montserrat', 16), bd=6, width=16, relief=FLAT)
UserField.place(x=80, y=30)
UserField.insert(0, "Ask me anything...")
UserField.bind('<Return>', keyboardInput)

userIcon = PhotoImage(
    file="images/avatars/ChatIcons/a1.png")
botIcon = PhotoImage(file="images/assistant2.png")
botIcon = botIcon.subsample(2, 2)

Thread(target=voiceMedium).start()
root.mainloop()
