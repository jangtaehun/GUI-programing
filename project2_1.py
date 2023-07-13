from tkinter import *
import os
import tkinter.ttk as ttk
root = Tk()
root.title("ZZangtae Photo")
root.geometry("550x530+900+150")
root.resizable(True, True) #x, y 변경 가능
#########################################################################
####파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="both") #expand="True"

btn_add_file = Button(file_frame, text="파일 추가")
btn_add_file.pack(side="left", padx=5, pady=5)
btn_del_file = Button(file_frame, text="선택 삭제")
btn_del_file.pack(side="right", padx=5, pady=5)


####리스트 프레임, 스크롤
list_frame = Frame(root)
list_frame.pack(fill="x", padx=5, pady=5)

scrollbar_list = Scrollbar(list_frame)  #pack(side="right", fill="y")
scrollbar_list.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar_list.set)  #list_ file = Listbox(넣는곳)
list_file.pack(side="left", fill="both", expand=True, padx=5, pady=5)
scrollbar_list.config(command=list_file.yview) #list_file이 yvuew를 맵핑하도록


####저장 경로 프레임
path_frame = LabelFrame(root, text="저장 경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4, padx=5, pady=5)  #ipad=높이 변경

btn_dest_path = Button(path_frame, text="찾아보기", width=10)
btn_dest_path.pack(side="right", padx=5, pady=5)


####옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(fill= "x", padx=5, pady=5, ipady=5)

####가로 옵션
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left", padx=3, pady=3)
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10) #정의한 값만 받는다.
cmb_width.current(0) #0번째 인덱스 값 선택
cmb_width.pack(side="left")
####간격 옵션
lbl_space = Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left")
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10) #정의한 값만 받는다.
cmb_space.current(0) #0번째 인덱스 값 선택
cmb_space.pack(side="left")
####파일 포맷 옵션
lbl_format = Label(frame_option, text="포멧", width=8)
lbl_format.pack(side="left")
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10) #정의한 값만 받는다.
cmb_format.current(0) #0번째 인덱스 값 선택
cmb_format.pack(side="left")


####진행상황 progress bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)
p_var = DoubleVar()
progressbar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var) #결정되지 않음, 언제 끝날지 모른다.
progressbar.pack(fill="x", padx=5, pady=5)


#실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5, ipady=5)
btn_close = Button(frame_run, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=3, pady=3)
btn_start = Button(frame_run, text="시작", width=12)
btn_start.pack(side="right", padx=3, pady=3)

#########################################################################
root.mainloop() #창이 닫히지 않도록 한다.