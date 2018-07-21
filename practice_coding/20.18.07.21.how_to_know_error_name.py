
# error name을 모를때
# except 뒤에 아무것도 안붙이면 예외처리가 가능하다.

# 하지만 어떤 에러인지 알고싶은경우
# except뒤에 Exception as ex를 붙이면

# ex에 에러 메세지의 정보가 출력된다.


try:
    list = []
    print(list[0])

    text = 'abc'
    print(int(text))
except Exception as ex:
    print('에러가 발생했습니다.', ex)
