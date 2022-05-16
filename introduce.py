from random import choice


def speakIntroduce(lg):
    if lg == 'vi':
        return "Xin chào.\n" + \
               "Rất hân hạnh được phục vụ bạn.\n" + \
               "Tôi là Tuesday.\n" + \
               "Tôi là trợ lý ảo được tạo ra dựa trên\n" + \
               "ngôn ngữ lập trình Python kết hợp với AI.\n" + \
               "Tôi sinh ra vào ngày 01/12/2021.\n" + \
               "Hiện tại bạn đang sử dụng phiên bản AI\n" + \
               "thử nghiệm và cũng đang là phiên bản mới nhất HIHI!."
    else:
        return "Hi.\n" + \
               "We are pleased to serve you.\n" + \
               "I'm Tuesday.\n" + \
               "I am a virtual assistant created based on the\n" + \
               "Python programming language combined with AI.\n" + \
               "I was born on December 01, 2021.\n" + \
               "Currently you are using the experimental\n" + \
               "version of AI and also the latest version HIHI!."


# Hướng dẫn
def help_me(lg):
    if lg == "vi":
        return "Tôi có thể giúp bạn thực hiện các công việc sau đây:\n" + \
               "1. Tôi biết chào hỏi bạn nè\n2. Cho bạn biết về thời gian và giờ giấc nè\n" + \
               "3. Mở các trang website, và các ứng dụng nè\n" + "4. Giúp bạn Tìm kiếm trên Google nữa\n" + \
               "5. Gửi Email cho bạn nè\n" + "6. Cho bạn xem dự báo thời tiết\n" + \
               "7. Mở cho bạn một bản nhạc mà bạn yêu cầu\n" + "8. Tôi có thể đọc báo cho bạn nghe nè\n" + \
               "9. Kể bạn biết về thế giới này nè\n" + "10. Tôi có thể tắt máy tính cho bạn nè\n" + \
               "11. Chỉ đường cho bạn nè"
    else:
        return "I can help you with the following tasks:\n" + "1. I know how to greet you\n" + \
               "2. I can tell you about the time\n" + "3. Open websites, and apps\n" + \
               "4. Help you Search on Google and Youtube\n" + "5. Send an email on your behalf\n" + \
               "6. Show you the weather forecast\n" + "7. Open a song you requested\n" + \
               "8. I can read the newspaper to you\n" + "9. I can tell you about this world\n" + \
               "10. I can tell you a joke\n" + "11. I can turn off your computer for you"


# Phần giới thiệu
def fullNameAI(lg):
    if lg == 'vi':
        ho_va_ten_AI = ["Tôi tên là Tuesday",
                        "Bạn thử đoán xem tôi tên là gì nào?",
                        "Đố bạn biết tôi tên là gì?",
                        "Bạn cứ gọi tôi là Tuesday nhé"]
        return choice(ho_va_ten_AI)
    else:
        ho_va_ten_AI = ["My name is Tuesday",
                        "Try to guess my name. Hihi",
                        "Just call me Tuesday"]
        return choice(ho_va_ten_AI)


# giới thiệu quê hương
def countryAI(lg):
    if lg == 'vi':
        que_huong_noi = ["Tôi được sinh ra và lớn lên tại Việt Nam nè",
                         "Tôi từ khi sinh ra đã ở trong tim cậu rồi. HiHi",
                         "Tôi sinh ra ở trong tim cậu nè"]
        return choice(que_huong_noi)
    else:
        que_huong_noi = ["I was born in Vietnam",
                         "I've been in your heart since I was born",
                         "I was born in your heart"]
        return choice(que_huong_noi)


# giới thiệu tuổi
def ageAI(lg):
    if lg == 'vi':
        tuoi_tac_noi = ["Tôi chỉ mới được ba ngày tuổi thôi.\n" + "Tôi vẫn còn bé lắm",
                        "Từ lúc sinh ra đến nay tôi chỉ mới\n" + "đươc vài ngày tuổi thôi à",
                        "Tôi ra đời từ năm 2021.\n" + "Có thể nói tôi còn khá trẻ.\n" +
                        "Nhưng tôi biết khá nhiều điều đó"]
        return choice(tuoi_tac_noi)
    else:
        tuoi_tac_noi = ["I'm only three days old, I'm still very young",
                        "It's only been a few days since I was born",
                        "I was born in 2021. I am quite young,\nbut I know quite a lot of things"]
        return choice(tuoi_tac_noi)


# Người yêu
def loverAI(lg):
    if lg == 'vi':
        nguoi_yeu_noi = ["Tôi làm gì đã có người yêu, tôi còn đang sợ ế đây này",
                         "Tôi vẫn còn bé lắm",
                         "người yêu của tôi chính là cậu đấy"]
        return choice(nguoi_yeu_noi)
    else:
        nguoi_yeu_noi = ["I don't have a lover , I'm afraid to be lonely right now",
                         "I'm still very young",
                         "You are my lover"]
        return choice(nguoi_yeu_noi)
