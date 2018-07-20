# 특수한 메소드

# 초기화 함수 : __init__ 인스턴스를 만들때 실행되는 함수
# 문자열화 함수 : __str__ 인스턴스 자체를 출력할 때의 형식을 지정해주는 함수


class Human():
    '''
        인간
    '''

    def __init__(self, name, weight):
        '''초기화 함수, create의 역할을 한다.'''
        print("__init__실행")
        self.name = name
        self.weight = weight
        print("이름은 {}, 몸무게는 {}".format(name, weight))

    def __str__(self):
        '''
        인스턴스가 문자열로 어떻게 표현될지를 구현
        현재 class Human의 인스턴스를 string으로 표현할 때 어떻게 나타내는지를 구현하는 함수
        :return:
        '''
        return "{}(몸무게 {}kg)".format(self.name, self.weight)

    # def create(name, weight):
    #     person = Human()
    #     person.name = name
    #     person.weight = weight
    #     return person

    def eat(self):
        self.weight += 0.1
        print ("{}가 먹어서 {}kg이 되었습니다.".format(self.name, self.weight))

    def walk(self):
        self.weight -= 0.1
        print("{}가 걸어서 {}kg이 되었습니다.".format(self.name, self.weight))

person = Human('사람', 77)
print(person)
