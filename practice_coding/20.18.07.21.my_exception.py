# 사용자가 직접 예외처리를 해서 코드의 직관성을 높일 수 있다.
# Exception 클래스를 상속받아서 만


from UnexpectedRSPvalue import UnexpectedRSPValue

value = '가'

try:
    if value not in ['가위', '바위', '보']:
        raise UnexpectedRSPValue
except UnexpectedRSPValue:
    print("에러가 발생했습니다.")


# def sign_up():
#     '''회원가입 함수'''
#
# try:
#     sign_up()
# except BadUserName:
#     print("이름으로 사용할 수 없는 입력입니다.")
