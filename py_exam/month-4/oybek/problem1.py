class Book:
    def __init__(self, name, count_pages, price):
        self.name = name
        self.count_pages = count_pages
        self.price = price

    @classmethod
    def price_one_page(self, books):
        total_pages = sum(book.count_pages for book in books)
        total_prices = sum(book.price for book in books)

        return total_prices / total_pages

    @classmethod
    def price_for_programming_books(self, books):
        for book in books:
            if "programming" in book.name.lower():
                book.price *= 2

book1 = Book("Python programming", 150, 350000)
book2 = Book("Javascript Programming", 280, 250000)
book3 = Book("Machine Learning", 300, 300000)
book4 = Book("Learn Web Development", 400, 150000)
book5 = Book("Data Science", 350, 290000)

books = [book1, book2, book3, book4, book5]

average_price = Book.price_one_page(books)
print(f"Barcha kitoblar orasida bitta sahifaning o'rtacha narxi: {average_price:.2f} so'm")

Book.price_for_programming_books(books)
print("\nKitoblar narxlari:")
for book in books:
    print(f"{book.name}: {book.price:.2f} so'm")
