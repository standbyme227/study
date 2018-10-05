def all(iterable):
    '''
    iterable에 포함된 element 전부가 참인지 거짓인지를 판별하는 함수

    :param iterable:
    :return: True or False
    '''
    for element in iterable:
        if not element:
            return False
    return True


# def _all(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True
#
#
# def __all(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True
#
# def __all_(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True
#
# def __all__(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True
#
# def all(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True