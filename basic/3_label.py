from tkinter import *

root = Tk()
root.title("ZZangtae GUI")
# root.geometry("720x640") #가로 x 세로
root.geometry("720x640+900+150")  # 가로 x 세로 + x좌표 + y좌표
#########################################################################
label1 = Label(root, text="안녕하세요")
label1.pack()


photo = PhotoImage(file="basic/img.png")
label2 = Label(root, image=photo)
label2.pack()

photo2 = PhotoImage(file="basic/img2.png")


def change():
    label1.config(text="또 만나요")
    # global photo2
    # photo2 = PhotoImage(file="img2.png") #전역변수가 아니여서 garbage collection(불필요한 메모리 공간 해제)이 쓰레기를 줍는다.
    label2.config(image=photo2)


btn = Button(root, text="change", command=change)
btn.pack()


#########################################################################
root.mainloop()  # 창이 닫히지 않도록 한다.
