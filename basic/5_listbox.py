from tkinter import *

root = Tk()
root.title("ZZangtae GUI")
#root.geometry("720x640") #가로 x 세로
root.geometry("720x640+900+150") #가로 x 세로 + x좌표 + y좌표
#########################################################################

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "사과")
listbox.insert(END, "사과")
listbox.pack()


def btncmd():
    #listbox.delete(END) #맨 뒤 항목 삭제
    #listbox.delete(0) #맨 앞에서 삭제

    print("리스트에는", listbox.size(), "개가 있어요") #개수 확인

    print("1번쨰부터 3번째까지의 항목: ", listbox.get(0, 2)) #첫 번째부터 세 번째까지 인덱스 출력(시작 인덱스, 끝 인덱스)

    print("선택된 항목: ", listbox.curselection()) # 선택된 항목 위치로 반환(인덱스)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()





#########################################################################
root.mainloop() #창이 닫히지 않도록 한다.