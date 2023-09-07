class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def get_radius(self) -> int:
        return self.radius

    def set_radius(self, radius) -> None:
        self.radius = radius

    def get_color(self) -> str:
        return self.color

    def set_color(self, color) -> None:
        self.color = color

    def get_area(self) -> float:
        """
        Aylananing yuzasini topish
        """
        return 3.14 * (self.radius**2)

    def get_circumference(self) -> float:
        """
        Aylananing uzunligini topish
        """
        return 2 * 3.14 * self.radius

    def get_info(self) -> str:
        return (
            f"Aylana Radiusi: {self.radius}\n"
            f"Aylana Rangi: {self.color}\n"
            f"Aylana yuzasi: {self.get_area()}\n"
            f"Aylana uzunligi: {self.get_circumference()}"
        )


element = Circle(3, "crimson")
print(element.get_info())
element.set_radius(4)
element.set_color("blue")
print(element.get_info())
