#class practice 3

class Triangle :
    def __init__(self, bo, hi) :
        """
        bo : bottom 底辺の長さ
        hi : height 高さ
        """
        self.bottom = bo
        self.height = hi
        print("Now created instance.")

    def area(self) :
        return self.bottom * self.height / 2

print("At first, make triangle")
try :
    teihen = int(input("Teihen : "))
    takasa = int(input("Takasa : "))
    sankaku = Triangle(teihen, takasa)
    men = sankaku.area()
    print("Menseki ha ", men)
except :
    print("Pls input numbers")

