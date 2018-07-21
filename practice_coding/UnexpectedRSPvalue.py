# Error의 최상위 class는 Exception Class
# 혹시나 특수한 ValueError를 내고 싶으면 ValueError class를 상속해도 됨.

class UnexpectedRSPValue(ValueError):
    '''가위 바위 보 가운데 하나가 아닌 값인 경우에 밣생하는 에러'''