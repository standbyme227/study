# super에 대해서
# 자식 클래스에서 부모 클래스의 메소드를 쓰고 싶을때
# super().{메소드 이름} 이렇게 적으면된다.
# 나는 지금 일하면서 save를 그렇게 super로 불러왔는데 이렇게 기본적인것인줄은 몰랐다.

# super를 이용해서 init과 콜라보해봤다.

# __init__은 초기화 함수이다.


class Animal():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def walk(self):
        print("걷는다")

    def eat(self):
        print("먹는다")

    def greet(self):
        print("{}이/가 인사한다.".format(self.name))


class Human(Animal):
    def __init__(self, name, hand):
        super().__init__(name)
        self.hand = hand

    def wave(self):
        print("{}과 엉덩이를 흔들면서".format(self.hand))
        super().greet()


person = Human("종민", "오른손")
print(person)
person.wave()

person2 = Human("석재", "왼손")
print(person2)
person2.wave()