def uzbek_convert(num):
    units = ("", "bir ", "ikki ", "uch ", "to'rt ","besh ", "olti ", "yetti ","sakkiz ", "to'qqiz ", "o'n ", "o'n bir ", "o'n ikki ", "o'n uch ", "o'n to'rt ", "o'n besh ","o'n olti ", "o'n yetti ", "o'n sakkiz ", "o'n to'qqiz ")
    tens =("", "", "yigizma ", "o'ttiz ", "qiriq ", "ellik ","oltmish ","yetmush ","sakson ","to'qson ")

    if num < 0:
        return "minus "+uzbek_convert(-num)

    if num<20:
        return  units[num] 

    if num<100:

        return  tens[num // 10]  +units[int(num % 10)] 

    if num<1000:
        return units[num // 100]  +"yuz " +uzbek_convert(int(num % 100))

    if num<1000000: 
        return  uzbek_convert(num // 1000) + "ming " + uzbek_convert(int(num % 1000))

    if num < 1000000000:    
        return uzbek_convert(num // 1000000) + "milion " + uzbek_convert(int(num % 1000000))

    return uzbek_convert(num // 1000000000)+ "miliard "+ uzbek_convert(int(num % 1000000000))

def ingliz_convert(num):
    units = ("", "one ", "two ", "three ", "four ","five ", "six ", "seven ","eight ", "nine ", "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ","sixteen ", "seventeen ", "eighteen ", "nineteen ")
    tens =("", "", "twenty ", "thirty ", "forty ", "fifty ","sixty ","seventy ","eighty ","ninety ")

    if num < 0:
        return "minus "+ingliz_convert(-num)

    if num<20:
        return  units[num] 

    if num<100:

        return  tens[num // 10]  +units[int(num % 10)] 

    if num<1000:
        return units[num // 100]  +"hundred " +ingliz_convert(int(num % 100))

    if num<1000000: 
        return  ingliz_convert(num // 1000) + "thousand " + ingliz_convert(int(num % 1000))

    if num < 1000000000:    
        return ingliz_convert(num // 1000000) + "million " + ingliz_convert(int(num % 1000000))

    return ingliz_convert(num // 1000000000)+ "billion "+ ingliz_convert(int(num % 1000000000))
