# chapter 13 no 3

class Shape :
    def what_am_i(self) :
        return "I am a shape."

class Rectangle(Shape) :
    def __init__(self, w, hi) :
        self.width = w
        self.hight = hi
    def calculate_perimiter(self) :
        return self.width * 2 + self.hight *2

class Square(Shape) :
    def __init__(self, l) :
        self.length = l
    def calculate_perimiter(self) :
        return self.length * 4
    def change_size(self,ch) :
        self.changes = ch
        self.length = self.length + self.changes

print("長方形")
nagasikaku = Rectangle(15, 20)
#print("外周 :", nagasikaku.calculate_perimiter())
print(nagasikaku.what_am_i())

print("正方形")
masikaku = Square(15)
#print("外周", masikaku.calculate_perimiter())
#print("長さ変更")
#masikaku.change_size(10)
#print("外周2", masikaku.calculate_perimiter())
print(masikaku.what_am_i())
