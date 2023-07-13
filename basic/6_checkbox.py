from tkinter import *

root = Tk()
root.title("ZZangtae GUI")
#root.geometry("720x640") #가로 x 세로
root.geometry("720x640+900+150") #가로 x 세로 + x좌표 + y좌표
#########################################################################

chkvar = IntVar() #chvar에 int형으로 값을 저장
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
#chkbox.select() #쟈동으로 선택
#chkbox.deselect() #선택 해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일 동안 보지 않기", variable=chkvar2)
chkbox2.pack()




def btncmd():
    print(chkvar.get()) #0= 체크 해제, 1= 체크
    print(chkvar2.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()





#########################################################################
root.mainloop() #창이 닫히지 않도록 한다.