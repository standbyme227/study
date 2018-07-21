# class의 괄호안에 다른 class를 넣는걸 상속한다라고 함.
# 상속을 받은 클래스는 상속한 클래스의 자식 클래스가 됨.
# 현재는 Animal이 부모, Human, Dog가 자식

class Animal():
    def walk(self):
        print("걷는다")

    def eat(self):
        print("먹는다")

class Human(Animal):

    def wave(self):
        print("손을 흔든다")

    def speak(self):
        print("말을 한다")

class Dog(Animal):

    def wag(self):
        print("꼬리를 흔든다.")

    def bark(self):
        print("짖는다.")

class JongMin(Animal):
    def eateat(self):
        print("많이 먹는다.")

    def run(self):
        print("뛴다")

    def workout(self):
        print("운동한다.")

person = Human()
dog = Dog()
mini = JongMin()

print("--------person's action")
person.walk()
person.eat()
person.wave()
person.speak()
print("--------dog's action")
dog.walk()
dog.eat()
dog.wag()
dog.bark()
print("--------mini's action")
mini.eat()
mini.walk()
mini.eateat()
mini.run()
mini.workout()