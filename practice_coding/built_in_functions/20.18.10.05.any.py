def any(iterable):
    '''
    iterable에 포함된 element중에 하나라도 참인것이 있으면 True를
    전부 거짓이면 False를 반환한다.

    :param iterable:
    :return: True or False, Boolean
    '''
    for element in iterable:
        if element:
            return True
    return False


# def _any(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False
#
# def __any(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False
#
# def __any_(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False
#
# def __any__(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False