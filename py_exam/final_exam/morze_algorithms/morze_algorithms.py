def create_morse_alphabet():
    morse_alphabet = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z'
    }
    
    with open("./morze_algorithms/input.txt") as file:
        text = file.read().split("  ")
    de_text = str()
    for i in text:
        txt = str()
        for j in i.split(" "):
            txt += morse_alphabet[j]
        de_text += txt.lower() + " "
    with open("./morze_algorithms/output.txt", "w") as file:
        file.write(de_text)
    
    return morse_alphabet

create_morse_alphabet()


