class Human():
    def __init__(self, name, weight, money):
        self.name = name
        self.weight = weight
        self.money = money
        # if self.money > 0:
        #     print("거지가 되었습니다.")
        print("이름은 {}, 몸무게는 {}kg, 자산은 {}원".format(self.name, self.weight, self.money))

    def __str__(self):
        return self.name

    def walk(self):
        self.weight -= 2
        print("{}의 몸무게가 {}이 되었습니다.".format(self.name, self.weight))

    def work(self):
        self.money += 500000
        print("{}이가 열심히 일해서 총 자산은 {}원이 되었습니다.".format(self.name, self.money))

    def play(self):
        self.money -= 3000000
        print("{}이가 열심히 번돈을 막써서 총 자산이 {}원이 되었습니다.".format(self.name, self.money))

man = Human("종민", 77.5, 20000000)
man.walk()
man.work()
man.play()
man.play()
print(man)




# class Human():
#     def create(name, weight):
#         person = Human()
#         person.name = name
#         person.weight = weight
#         return person
#
#     def walk(self):
#         self.weight -= 2
#         print("{}의 몸무게가 {}로 줄어들었습니다.".format(self.name, self.weight))
#
#     def eat(self):
#         self.weight += 2
#         print("{}의 몸무게가 {}로 늘었습니다.".format(self.name, self.weight))
#
#     def speck(self, message):
#         print(message)
#
#
# man = Human.create("종민", 76.3)
# print(man.name)
# man.walk()
# man.walk()
# man.walk()
# man.eat()
# man.speck("파이썬이 재밌구만~")