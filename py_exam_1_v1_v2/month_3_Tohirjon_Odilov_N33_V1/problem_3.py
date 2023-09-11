"""
Funksiya parametri sifatida string ma'lumoti berilgan va ushbu stringda
nechta raqam qatnashganini aniqlovchi funksiya tuzing.
"""


def count_digits(txt: str) -> int:
    """
    Berilgan text ichida nechta raqam borligini sanab o'sha sonni qaytaradi.
    """
    count = 0
    for i in txt:
        if i.isdigit():
            count += 1
    return count


print(count_digits("hi"))
print(count_digits("who is 1st here"))
print(count_digits("my numbers is 2"))
print(
    count_digits(
        "This picture is an oit on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
    )
)
print(count_digits(""))
