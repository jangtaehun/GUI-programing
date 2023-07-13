from tkinter import *

root = Tk()
root.title("ZZangtae GUI")
#root.geometry("720x640") #가로 x 세로
root.geometry("720x640+900+150") #가로 x 세로 + x좌표 + y좌표
#########################################################################

frame11 = Frame(root)
frame11.pack()

Scrollbar11 = Scrollbar(frame11)
Scrollbar11.pack(side="right", fill="y")

#set이 없으면 scroll을 내려도 다시 올라온다.
listbox11 = Listbox(frame11, selectmode="extended", height=10, yscrollcommand=Scrollbar11.set)
for i in range(1, 32):
    listbox11.insert(END, str(i) + "일")
listbox11.pack(side="left")

Scrollbar11.config(command=listbox11.yview)

#########################################################################
root.mainloop() #창이 닫히지 않도록 한다.