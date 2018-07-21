# 부모 Animal이라는 class를 상속받는데
# 자식에서 같은 이름의 함수를 생성하면 덮어쓰기가 가능해진다.

# 이 덮어쓰기를 override라고 한다.
# Override란 같은 이름을 가진 메소드를 덮어쓴다는 의미

class Animal():

    def walk(self):
        print("걷는다")

    def eat(self):
        print("먹는다")

    def greet(self):
        print("인사한다")

class Human(Animal):
    '''사람'''
    def wave(self):
        print("손을 흔든다.")

    def greet(self):
        self.wave()

class Dog(Animal):
    '''개'''
    def wag(self):
        print("꼬리를 흔든다.")

    def greet(self):
        self.wag()

class Cow(Animal):
    '''소'''
    def eat(self):
        print("소가 먹는다")

person = Human()
dog = Dog()
cow = Cow()

person.greet()
dog.greet()
cow.greet()

person.eat()
dog.eat()
cow.eat()
