list = ["a", "b", "c", "d"]

for list_idx, list_val in enumerate(list):
    print(list_idx, list_val)


# dic = {"a": 1, "b": 2, "c": 3}

# for sub, num in enumerate(dic):
#     print(sub, num)


# def solution(q, r, code):
#    return code[r::q]
# 문자열 code의 index를 q로 나누면 q-1까지의 나머지가 q간격으로 반복되니 target 나머지가 곧 시작 index가 되고 그걸 code의 끝까지 q간격으로 반환하는거나 다름없습니다.ㅎ
