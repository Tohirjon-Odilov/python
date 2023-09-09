class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_info(self):
        return (
            f"Rectangle:\n"
            f"Width: {self.width}\n"
            f"Height: {self.height}\n"
            f"Area: {self.get_area()}\n"
            f"Perimeter: {self.get_perimeter()}"
        )


rec1 = Rectangle(5, 10)
rec2 = Rectangle(10, 20)
print(rec1.get_info())
print(rec2.get_info())
