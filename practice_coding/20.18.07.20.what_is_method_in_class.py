# 메소드 (Method)

# 함수와 비슷하다.

# 클래스에 묶여서 클래스의 인스턴스와 관계되는 일을 하는 함수를 말한다.

class Human():
    def create(name, weight):
        person = Human()
        person.name = name
        person.weight = weight
        return person

    def eat(self):
        self.weight += 0.5
        print("{}가 먹어서 {}kg이 되었습니다.".format(self.name, self.weight))
        # self를 쓰는 이유는 class의 instance가 그 자리를 차지해서 인거 같다.

    def walk(self):
        self.weight -= 0.5
        print("{}가 걸어서 {}kg이 되었습니다.".format(self.name, self.weight))

    def speak(self, message):
        print(message)

person = Human.create('철수', 60.6)
# person.walk()
# person.eat()
# person.walk()
person.speak("나하하하하핳")


# def create_human(name, weight):
#     person = Human()
#     person.name = name
#     person.weight = weight
#     return person
#
#
# Human.create = create_human
#
#
# def eat(person):
#     person.weight += 0.5
#     print("{}가 먹어서 {}kg이 되었습니다.".format(person.name, person.weight))
#
#
# def walk(person):
#     person.weight -= 0.5
#     print("{}가 걸어서 {}kg이 되었습니다.".format(person.name, person.weight))


# Human.eat = eat
# Human.walk = walk

