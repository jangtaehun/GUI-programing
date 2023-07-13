from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("ZZangtae GUI")
#root.geometry("720x640") #가로 x 세로
root.geometry("720x640+900+150") #가로 x 세로 + x좌표 + y좌표
#########################################################################

#기차 예매 시스템
def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")

def warn():
    msgbox.showwarning("경고", "잔액이 부족합니다.")

def error():
    msgbox.showerror("에러", "결재 오류가 발생했습니다.")

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()


def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다.")

def retrycancel():
    res = msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")
    if res == 1: #재시도
        print("쫀떡")
    elif res == 0: #취소
        print("준덕")

def yesno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다.")

def yesnocancel():
    response = msgbox.askyesnocancel(title =None, message="예매 내역이 저장되지 않았습니다.\n저장 후 프로그램을 종료하시겠습니까?")
    #네: 저장 후 종료
    #아니오: 저장하지 않고 종료
    #취소: 프로그램 종료 취소
    print("응답:", response) #True, False, None -> 예=1, 아니오=0, 그 외
    if response == 1:
        print("쫀떡")
    elif response == 0:
        print("준덕", response)
    else:
        print("똥떡", response)

Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()



#########################################################################
root.mainloop() #창이 닫히지 않도록 한다.