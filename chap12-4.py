# class practice 4

class Hexagon :
    def __init__(self,ln) :
        """ ln : 六角形の1辺の長さ """
        self.hen = ln
        print("Instance created.")
    def culculate_perimeter(self) :
        return self.hen * 6

print("1辺の長さを入力")
try :
    hen1 = int(input())
    #create instance
    rokkaku = Hexagon(hen1)
    #call method
    gaisyu = rokkaku.culculate_perimeter()
    print("外周： ",gaisyu)
except :
    print("Check your input.")
