def convert_number(num):
    num = int(num)
    units = (
        "",
        "one ",
        "two ",
        "three ",
        "four ",
        "five ",
        "six ",
        "seven ",
        "eight ",
        "nine ",
        "ten ",
        "eleven ",
        "twelve ",
        "thirteen ",
        "fourteen ",
        "fifteen ",
        "sixteen ",
        "seventeen ",
        "eighteen ",
        "nineteen ",
    )
    tens = (
        "",
        "",
        "twenty ",
        "thirty ",
        "forty ",
        "fifty ",
        "sixty ",
        "seventy ",
        "eighty ",
        "ninety ",
    )

    if num < 0:
        return "minus" + convert_number(-num)

    if num < 20:
        return units[num]

    if num < 100:
        return tens[num // 10] + units[int(num % 10)]

    if num < 1000:
        return units[num // 100] + "hundred " + convert_number(int(num % 100))

    if num < 1000000:
        return (
            convert_number(num // 1000) + "thousand " + convert_number(int(num % 1000))
        )

    if num < 1000000000:
        return (
            convert_number(num // 1000000)
            + "million "
            + convert_number(int(num % 1000000))
        )

    return (
        convert_number(num // 1000000000)
        + "billion "
        + convert_number(int(num % 1000000000))
    )
