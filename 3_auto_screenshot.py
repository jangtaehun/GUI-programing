# import time
# from PIL import ImageGrab

# time.sleep(5) #5초 대기: 사용자가 준비하는 시간

# for i in range(1,11):
#     img = ImageGrab.grab() #현재 스크린 이미지를 가져옴
#     img.save("image{}.png".format(i)) #파일로 저장
#     time.sleep(2) #2초 단위

kor = ["사과", "바나나", "오렌지"]
eng = ["apple", "banana", "orange"]

print(list(zip(kor, eng))) #세로로 합친다. [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]

mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]
print(list(zip(*mixed))) #[('사과', '바나나', '오렌지'), ('apple', 'banana', 'orange')]

kor2, eng2 = zip(*mixed)
print(kor2)
print(eng2)