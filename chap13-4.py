# chapter 13 no 4

class Horse :
    def __init__(self, color, age, rider) :
        self.color = color
        self.age = age
        self.rider = rider

class Rider :
    def __init__(self, name, sex) :
        self.name = name
        self.sex = sex

kisyu1 = Rider("Take", "male")
kisyu2 = Rider("Mio","female")
uma1 = Horse("Black", 3, kisyu1)
uma2 = Horse("Brown", 4, kisyu2)

print(uma1.rider.name, uma1.rider.sex)
print(uma2.rider.name, uma2.rider.sex)
