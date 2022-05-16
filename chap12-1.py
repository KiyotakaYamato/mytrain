# class practice

class Apple :
    def __init__(self,kd,cl,w,sg) :
        """
        kd : kind = 品種
        cl : color 色
        w : weight 重さ
        sg : suger = 糖度
        """
        self.kind = kd
        self.color = cl
        self.weight = w
        self.suger = sg

        print("created.")

apl = Apple("王林", "赤", 102, 10)
print(apl)
