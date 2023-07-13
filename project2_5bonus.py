import time
import keyboard
from PIL import ImageGrab

def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))

keyboard.add_hotkey("F9", screenshot)

keyboard.wait("esc")


# from PIL import ImageGrab
# time.sleep(5) #5초 대기: 사용자가 준비하는 시간

# for i in range(1,11):
#     img = ImageGrab.grab() #현재 스크린 이미지를 가져옴
#     img.save("image{}.png".format(i)) #파일로 저장
#     time.sleep(2) #2초 단위