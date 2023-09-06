def popular_words(txt: str, lst: list) -> dict:
    """
    Berilgan textda list ichida berilgan so'zlarni nechtaligini qaytaradi.
    """
    mydict = dict()
    words = txt.split()

    for word in lst:
        mydict[word] = words.count(word)

    return mydict


print(
    popular_words(
        """
    When I was One 
    I had just begun
    When I was Two
    I was nearly new
""",
        ["I", "was", "three", "near"],
    )
)
