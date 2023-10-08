import pyautogui
from pynput import *
import time
print("Tıklanmasını istediğiniz koordinatı biliyorsanız 1 yazınız")
print("Tıklanmasını istediğiniz koordinatı bilmiyorsanız 0 yazınız")
secim = int(input())

if secim == 1:
    global xkordi
    global ykordi
    global rangeo
    global leftright
    print("Tıklanmasını istediğiniz koordinatın x konumunu yazınız")
    xkordi = int(input())
    time.sleep(0.3)
    print("TIklanmasını istediğiniz koordinatın y konumunu yazınız")
    ykordi = int(input())
    time.sleep(0.3)
    print("Tıklanmasını istediğiniz koordinata kaç kere tıklanacağını yazınız")
    rangeo = int(input())
    time.sleep(0.3)
    print("Tıklanmasını istediğiniz koordinata sağ click olarak tıklanmasını istiyorsanız 1 yazınız")
    print("Tıklanmasını istediğiniz koordinata sol click olarak tıklanmasını istiyorsanız 0 yazınız")
    leftright = int(input())
    if leftright == 1:
        for i in range(rangeo):
            pyautogui.rightClick(xkordi, ykordi)
    else:
        for i in range(rangeo):
            pyautogui.leftClick(xkordi, ykordi)

else:
    print("Konumunu bilmediğiniz için konum bulma mekanizması 2 saniye sonra başlatılacaktır")
    print("Konumu bulduktan sonra programı yeniden boşlatıp koordinatları girin")
    time.sleep(2)
    def get_coords(x, y):
        print("Kordinat paşam: {}".format((x, y)))
    with mouse.Listener(on_move=get_coords) as listen:
        listen.join()