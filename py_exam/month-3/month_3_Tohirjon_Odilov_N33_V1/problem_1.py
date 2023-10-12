"""
Dictionary MORSE azbukasi berilgan. Ushbu shifrlangan ma'lumotni chiqarib bering.
"""

MORSE = {
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}


def morse_to_number(morse_string: str) -> int:
    """
    Kiritilgan morse azbukasini deshifrlab beradi.
    """
    return int("".join([MORSE[i] for i in morse_string.split()])) 

print(morse_to_number(input()))
