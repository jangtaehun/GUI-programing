from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("ZZangtae GUI")
#root.geometry("720x640") #가로 x 세로
root.geometry("720x640+900+150") #가로 x 세로 + x좌표 + y좌표
#########################################################################

values = [str(i) + "일" for i in range(1, 32)]

combobox1 = ttk.Combobox(root, height=5, values=values)
combobox1.pack()
combobox1.set("카드 결제일") #최초 목록 제목 설정, 버튼 클릭을 통한 값 설정


combobox2 = ttk.Combobox(root, height=5, values=values, state="readonly")
combobox2.current(0) #0번째 인덱스 값 선택
combobox2.pack()


def btncmd():
    print(combobox.get())


btn = Button(root, text="선택", command=btncmd)
btn.pack()





#########################################################################
root.mainloop() #창이 닫히지 않도록 한다.