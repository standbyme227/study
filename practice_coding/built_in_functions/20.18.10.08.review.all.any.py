# def all(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True
#
# def any(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False

def all(iterable):
    # iterable을 순회하면서 element 하나하나씩 검사한다.
    for element in iterable:
        # 하나라도 element가 거짓이면
        if not element:
            # False를 반환한다.
            # 고로 전부다 True여야한다.
            return False
    # 참이면 True 반환.
    return True

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False