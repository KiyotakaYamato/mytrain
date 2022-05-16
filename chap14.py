# chapter 14

class Square :
    square_list = list()
    
    def __init__(self, ln) :
        self.length = ln
        self.square_list.append(self.length)
    def __repr__(self) :
        return "{} by {} by {} by {}".format(self.length, self.length,\
                                             self.length, self.length)

masikaku1 = Square(5)
print(masikaku1)
masikaku2 = Square(12)
print(masikaku2)
print(Square.square_list)

def comp_obj(ob1, ob2) :
    return ob1 is ob2

if comp_obj(masikaku1, masikaku2) :
    print("Same!")
else :
    print("Different")
