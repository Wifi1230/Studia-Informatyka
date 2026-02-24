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

class Punkt3D(Punkt):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    def drukuj(self):
        print(f"Punkt({self.x},{self.y},{self.z})")
    def odlegosc_od(self, inny:"Punkt"):
        dx=self.x-inny.x
        dy=self.y-inny.y
        dz=self.z-inny.z
        return sqrt(dx**2+dy**2+dz**2)
    
if __name__ == "__main__":
    print("--- Testy 2D ---")
    p1 = Punkt(3, 4)
    p2 = Punkt(0, 0)
    p1.drukuj()
    print(f"Odległość 2D: {p1.odlegosc_od(p2):.2f}")

    print("\n--- Testy 3D ---")
    p3d_1 = Punkt3D(3 , 4, 2)
    p3d_2 = Punkt3D(1, 8, 5)
    p3d_1.drukuj()
    p3d_2.drukuj()
    print(f"Odległość 3D: {p3d_1.odlegosc_od(p3d_2):.2f}")
