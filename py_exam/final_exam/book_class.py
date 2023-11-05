class Book:
    def __init__(self, name, count_pages, price) -> None:
        self.name = name
        self.count_pages = count_pages
        self.price = price

        if self.name.lower().find("programming") != -1:
            self.price *= 2
    
    def avarege(self):
        return self.price / self.count_pages
    def pages(self):
        return self.count_pages
    
    def __str__(self) -> str:
        return f"{self.name}\n{self.count_pages}\n{self.price}"

book1 = Book("Python Programming", 400, 25.99)
book2 = Book("Data Science Handbook", 600, 35.50)
book3 = Book("Algorithms and Data Structures", 300, 20.00)
book4 = Book("Machine Learning Basics", 450, 30.75)
book5 = Book("Web Development with Django", 350, 27.80)

lst = [book1, book2, book3, book4, book5]
price = list()
for i in lst:
    price.append(i.avarege())
print("O'rtacha sahifa narxi =",sum(price)/len(price))

print(book1)
print(book2)
print(book3)
print(book4)
print(book5)