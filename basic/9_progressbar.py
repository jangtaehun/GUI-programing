from tkinter import *
import tkinter.ttk as ttk
import time


root = Tk()
root.title("ZZangtae GUI")
#root.geometry("720x640") #가로 x 세로
root.geometry("720x640+900+150") #가로 x 세로 + x좌표 + y좌표
#########################################################################

progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") #결정되지 않음, 언제 끝날지 모른다.
progressbar.start(10) #10ms 마다 움직임
progressbar.pack()

def btncmd():
    progressbar.stop() #작동 중지
btn = Button(root, text="중지", command=btncmd)
btn.pack()




progressbar2 = ttk.Progressbar(root, maximum=100, mode="determinate") 
progressbar2.start(10) #10ms 마다 움직임
progressbar2.pack()




p_var2 = DoubleVar()
progressbar3 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar3.pack()

def btncmd2():
    for i in range(1,101):
        time.sleep(0.01) #0.01초 딜레이
        p_var2.set(i)# progressbar의 값 설정
        progressbar3.update() #ui 업데이트
        print(p_var2.get())

btn1 = Button(root, text="시작", command=btncmd2)
btn1.pack()

#########################################################################
root.mainloop() #창이 닫히지 않도록 한다.