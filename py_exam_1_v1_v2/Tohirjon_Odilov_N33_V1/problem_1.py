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
    morse_string = morse_string.split()
    morse_string = [MORSE[i] for i in morse_string]
    morse_string = "".join(morse_string)
    return int(morse_string)


print(morse_to_number(input()))
