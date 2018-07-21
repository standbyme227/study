
# '''
#     try:
#         에러가 발생할 가능성이 있는 코드
#     except:
#         에러가 발생 했을 경우 처리할 코드
#
#     # 예외처리 대신 if else를 사용할 수 있다.
# '''


def safe_pop_print(list, index):
    try:
        print(list.pop(index))
    except IndexError:
        print("{} index의 값을 가져올 수 없습니다.".format(index))

safe_pop_print([1,2,3,4,5], 10)


def safe_pop_print2(list, index):
    if index<len(list):
        print(list.pop(index))
    else:
        print("{} index값을 가져올 수 없습니다.".format(index))

safe_pop_print2([1,2,3,4], 5)
