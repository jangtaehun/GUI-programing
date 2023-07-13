from tkinter import *

root = Tk()
root.title("ZZangtae GUI")
#root.geometry("720x640") #가로 x 세로
root.geometry("720x640+900+150") #가로 x 세로 + x좌표 + y좌표
#########################################################################

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요") # 여러 줄 가능

e = Entry(root, width=30) #한 줄로만 가능 -> 아이디, 비밀번호...
e.pack()
e.insert(0,"한 줄만 가능")


def btncmd():
    #출력
    print(txt.get("1.0", END)) #1행 0번째 컬럼 인덱스
    print(e.get())

    #삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()





#########################################################################
root.mainloop() #창이 닫히지 않도록 한다.