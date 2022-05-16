# Class practice 2

class Circle :
    
    def __init__(self,hdm) :
        """ hdm : half diameter 半径 """
        self.hankei = hdm

    def area(self) :
        import math
        return self.hankei ** 2 * math.pi

    print("Instance created")


han = int(input("hankei wo nyuryoku : "))
enn = Circle(han)  #Instanceを作ってから
men = enn.area()  #methodを呼ぶ
print("Menseki =", men)
    
