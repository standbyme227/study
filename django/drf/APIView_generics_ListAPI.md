# APIView

## 용도

> 서버와 통신하기 위한 부분을 구현한다고 생각하면 된다.  

## 예시

```
class UserToUnitListView(APIView):
  permission_classes = (
    permissions.IsAuthenticated,
  )

  def get(self, request, format=None):
    units = UserToUnit.objects.all()
    serializer = UserToUnitDetailSerializer(units, many = True)

    return Response(serializer.data)
```

## 설명

> 클래스 APIView를 선언하고,  
허용되는 상태를 명시한다.  
get이라는 method를 사용할 것이,  
units들을 serializer로 걸러내서  
그 데이터를 Response로 제공한다.

# ListAPIView????

## 무엇인가?

> 사람들이 흔히 쓰는 API들을  
내부적으로 구성해서 편하게 사용할 수 있도록  
지정해 놓은 것들 중 하나.

## 장점.

> 좀 더 손쉽게, 간결하게 원하는 값을 얻을 수 있다.

## 단점.

> 내부적인 동작에 대해 조금은 이해도가 떨어질 수 있다.

## 방법

>
