from math import sqrt

class Punkt:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def drukuj(self):
        print(f"Punkt({self.x},{self.y})")
    def odlegosc_od(self, inny:"Punkt"):
        dx=self.x-inny.x
        dy=self.y-inny.y
        return sqrt(dx**2+dy**2)

p=Punkt(3,4)
q=Punkt(0,0)
p.drukuj()
q.drukuj()
print(f"odlegosc od punktow {p.odlegosc_od(q)}")
