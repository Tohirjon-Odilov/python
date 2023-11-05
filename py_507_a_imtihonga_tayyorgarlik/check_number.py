import re

def chick_phone(input_text):
    pattern = re.compile(r"\(998\) \d\d-\d\d\d-\d\d-\d\d")
    return True if pattern.match(input_text) else False
    
print(chick_phone('(998) 98-596-99-99'))