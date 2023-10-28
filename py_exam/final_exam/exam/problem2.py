# Parametr sifatida 16 lik sanoq tizimidagi son berilgan hex_to_decimal nomli funksiya yarating. Funksiya qaytaruvchi qiymat sifatida parametr sifatida kiritilgan 16 lik sanoq tizimidagi sonning 2 lik sanoq tizimiga o‘girilgandagi sonni qaytaradi. Agar 16 lik sanoq tizimiga mos kelmaydigan son kiritilsa “ERROR” chiqarilsi. TAYYOR BIR SANOQ TIZIMIDAN BOSHQA SANOQ TIZIMIGA O‘TKAZADIGAN FUNKSIYALAR ISHLATILISHI TAQIQLANADI.

# HEX_TO_BINARY
# input = "12DCEE"
# output = 000100101101110011101110
# don't use builtin functions

def hex_to_decimal(hex_number):
    hex_to_bin_dict = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    
    binary_number = ""
    for digit in hex_number:
        if digit.upper() in hex_to_bin_dict:
            binary_number += hex_to_bin_dict[digit.upper()]
        else:
            return "ERROR"
    return binary_number

print(hex_to_decimal(input(">>> ")))

    
    
     
