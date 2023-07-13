from tkinter import *

root = Tk()
root.title("ZZangtae GUI")
#root.geometry("720x640") #가로 x 세로
root.geometry("720x640+900+150") #가로 x 세로 + x좌표 + y좌표
#########################################################################

Label(root, text="메뉴를 선택해 주세요.").pack(side="top")
Button(root, text="주문하기").pack(side="bottom")

#버거 프레임
frame_burger = Frame(root, relief="solid", bd=1)

frame_burger.pack(side="left", fill="both", expand="True")

Button(frame_burger, text="햄버거", width=7).pack()
Button(frame_burger, text="치즈버거", width=7).pack()
Button(frame_burger, text="치킨버거", width=7).pack()


#음료 프레임
frame_drink = LabelFrame(root,text="음료")

frame_drink.pack(side="right", fill="both", expand="True")

Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()

#########################################################################
root.mainloop() #창이 닫히지 않도록 한다.