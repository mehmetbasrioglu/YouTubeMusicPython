import vlc # VLC BILGISAYARINIZDA KURULU DEGILSE CALISMAZ AYNI SEKILDE PIP INSTALL PYTHON-VLC KURMALISINIZ
import pafy # PIP INSTALL PAFY  --USER KURMALISINIZ
from gtts import gTTS # PIP INSTALL gTTS --USER KURMALISINIZ
import playsound # PIP INSTALL PLAYSOUND --USER
import ctypes #DLL Windows Erişim

# KONSOL YAZI RENGI
from termcolor import colored, cprint

# TEXT TO SPEECH API
def konus(yazi):
    tts = gTTS(text=yazi,lang="tr")
    filename = "ses.mp3"
    tts.save(filename)
    playsound.playsound(filename)

isPlaying = False

# VLC ILE VIDEO OYNATMA FONKSIYONU
def videoOynat(urladresi):
    global player
    video = pafy.new(urladresi)
    best = video.getbest()
    playurl = best.url
    ins = vlc.Instance()
    player = ins.media_player_new()
    Media = ins.media_new(playurl)
    player.set_media(Media)
    player.play()
    player.audio_set_volume(150)

# KULLANICIDAN VERI ALMA
def kullanicidanVeriAl(string):
    return input(colored(string, 'yellow'))

url = kullanicidanVeriAl("Lütfen YouTube Link Yapıştırın:")

# KULLANICININ GIRDIĞI URL ADRESLERI KONTROLU SADECE YOUTUBE KABUL ET
if url.__contains__("https://www.youtube.com/watch?v") :
    print("Video Başarıyla Doğrulandı")
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, 'Python YouTube Müzik', url, 0)
    konus("Şuanda youtube üzerinden müzik dinliyorsunuz")
    videoOynat(url)
    isPlaying = True
else:
     print("Hata: %s" %colored("Girdiğiniz Video Linki doğru değil", 'red'))
     konus("Hata Girdiğiniz Video Linki doğru değil")

# KULLANICININ GIRDIGI URL
def suandaCalaniYazdir(degisken):
    
    return print("Şuanda Caliyor: %s" %colored(degisken, 'green')) 

# PROGRAM TERMINAL KAPANMASIN DIYE WHILE YAPTIRDIM

durumlar = ["State.Playing", "State.NothingSpecial", "State.Opening"]
while str(player.get_state()) in durumlar:
    try:
        if isPlaying:
            isPlaying = isPlaying
           # suandaCalaniYazdir(format(player.get_state())) - kaldırıldı isterseniz ekleyebilirsiniz
        else:
           
            break;
    except:
        break;
player.stop()

