class Animal():
    def __init__(self, name, height, weight):
        if isinstance(name, str):
            self.name = name
        else:
            print("name은 string이어야 합니다.")

        if isinstance(height, int) and height < 1000:
            self.height = height
        else:
            print("height는 0~1000 사이의 정수여야합니다.")

        if isinstance(weight, int) and weight < 500:
            self.weight = weight
        else:
            print("weight는 0~2000 사이의 정수여야합니다.")

    def move(self, distance):
        try:
            self.distance = int(distance)
        except ValueError:
            print("walk는 정수를 인수로 받습니다.")

    def walk(self, distance):
        distance = self.move(distance)
        print("{}m를 걷는다.".format(distance))

    def eat(self, amount):
        try:
            self.amount = int(amount)
        except ValueError:
            print("eat은 정수를 인수로 받습니다.")
        print("{}개를 먹는다.".format(amount))

    def run(self, distance):
        distance = self.move(distance)
        print("{}m를 걷는다.".format(distance))

class Human(Animal):
    def __init__(self, name, height, weight):
        super().__init__(name, height, weight)

    def with_two_legs(self):
        print("두발로")

    def walk(self, distance):
        self.with_two_legs()
        super().walk(distance)


class Dog(Animal):
    def __init__(self, name, height, weight):
        super().__init__(name, height, weight)

    def with_four_legs(self):
        print("네발로")

    def with_wag(self):
        print("꼬리를 흔들면서")

    def walk(self, distance):
        self.with_four_legs()
        self.with_wag()
        super().walk(distance)

person = Human("OOP를 공부하는 종민이", 177, 76)
print(person.name)
person.walk(2)

happy = Dog("OOP의 희생양이되는 강아지", 40, 13)
print(happy.name)
happy.walk(10)