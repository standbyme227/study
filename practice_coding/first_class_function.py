# first-class function에 대해서 알아보자

# first-class fuction 이란
# 프로그래밍 언어가 함수를 first class citizen으로 취급하는 것을 뜻함.
# ( 무슨 참신한 소리인지 이해가 아니된다)

# 설명 :
# 함수자체를 인자로써 다른 함수에 전달하거나
# 다른 함수의 결과값으로 리턴할 수도 있고
# 함수를 변수에 할당하거나 데이터 구조안에 저장할 수 있는 함수를 뜻함.

def square(x):
    return x * x


print(square(5))

f = square

print(square)
print(f)