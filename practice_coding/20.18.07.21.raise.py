# raise란 Error를 발생시키는 구문이다.
# 해야할건 에러를 발생시키는 작업을 구현하고
# try except문으로 잡아서
# print 하면된다.

# for 문을 돌리는 상태에서 하나의 오류가 떴을때나 하나의 값을 찾을때
# raise를 이용하면 유용하다.

school = {
    '1반':[172,185,198,177,165,199,144],
    '2반':[162,177,154,188,192,193,155,200]
}

try:
    for class_number, students in school.items():
        for student in students:
            if student>195:
                print(class_number, '반에 195를 넘는 학생이 있습니다.')
                # break
                raise StopIteration
except StopIteration:
    print("정상종료")