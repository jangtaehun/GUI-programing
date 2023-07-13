from tkinter import *

root = Tk()
root.title("ZZangtae GUI")
#root.geometry("720x640") #가로 x 세로
root.geometry("720x640+900+150") #가로 x 세로 + x좌표 + y좌표
#########################################################################

label1 = Label(root, text="메뉴를 선택하세요")#.pack() 가능
label1.pack()
 
burger_var = IntVar() #int 형으로 값 저장
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger2 = Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="치킨거", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()


label2 = Label(root, text="음료를 선택하세요").pack()
dirnk_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=dirnk_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=dirnk_var)
btn_drink3 = Radiobutton(root, text="환타", value="환타", variable=dirnk_var)
btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()


def btncmd():
    print(burger_var.get()) #햄버거 중 선택된 라이오 항목의 값(value)을 출력
    print(dirnk_var.get())


btn = Button(root, text="주문", command=btncmd)
btn.pack()





#########################################################################
root.mainloop() #창이 닫히지 않도록 한다.