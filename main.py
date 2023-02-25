class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def Perimeter(self):
        P = self.length * 2 + self.width * 2
        return P
    def Area (self):
        S = self.length * self.width
        return S
    def Display(self):
        print(f'длина = {self.length} ширина = {self.width} периметр = {self.Perimeter()} площадь = {self.Area()}')
rectangle1 = Rectangle(5,6)

rectangle1.Display()
