import re

at_regex = re.compile(r'.at')

print(at_regex.findall('The cat in the hat sat on the flat mat.'))
# ['cat', 'hat', 'sat', 'lat', 'mat']



if 0:
   whole_string_is_num = re.compile(r'^\d+#39;')
   # 
   print(whole_string_is_num.search('1234567890'))
   # <_sre.SRE_Match object; span=(0, 10), match='1234567890'>
   # 
   whole_string_is_num.search('12345xyz67890') is None
   # True
   # 
   whole_string_is_num.search('12 34567890') is None
   # True
   pass

if 0:
   begins_with_hello = re.compile(r'^Hello')
   print(begins_with_hello.search('Hello world!'))
   # <_sre.SRE_Match object; span=(0, 5), match='Hello'>

   print(begins_with_hello.search('He said hello.') is None)
   # True\

if 0:
   consonant_regex = re.compile(r'[^Robocop]')
   print(consonant_regex.findall('Robocop eats baby food. BABY FOOD.'))
   # ['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', '
   # ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']

if 0:
   vowel_regex = re.compile(r'[Odilov]')
   print(vowel_regex.findall('Robocop eats baby food. BABY FOOD.'))
   # ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']


if 0:
   phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups

   print(phone_num_regex.findall('Cell: 45-555-9999 Work: 212-555-0000'))
   # ['415-555-9999', '212-555-0000']



if 0:
   greedy_ha_regex = re.compile(r'(Ha){3,5}')

   mo1 = greedy_ha_regex.search('HaHaHaHaHa')
   print(mo1.group())
   # 'HaHaHaHaHa'

   non_greedy_ha_regex = re.compile(r'(Ha){3,5}?')
   mo2 = non_greedy_ha_regex.search('HaHaHaHaHa')
   print(mo2.group())
   # 'HaHaHa'


if 0:
   ha_regex = re.compile(r'(Ha){1,5}')
   mo1 = ha_regex.search('HaHaHaHa')
   print(mo1.group())
   # 'HaHaHa'
   
   ha_regex = re.compile(r'(Ha){1}')

   mo1 = ha_regex.search('HaHaHa')
   print(mo1.group())
   # Ha

   mo2 = ha_regex.search('Ha')
   mo2 is None
   # True

if 0:
   bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
   mo = bat_regex.search('Batbat lost a wheel')

   mo.group()
   # 'Batmobile'
   print(mo.group())
   mo.group(1)
   # 'mobile'
   print(mo.group(0))
if 0:
   bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
   mo = bat_regex.search('Batmobile lost a wheel')

   mo.group()
   # 'Batmobile'

   print(mo.group(1))
   # 'mobile'
   
if 0:
   bat_regex = re.compile(r'Bat(wo)?ma')

   mo1 = bat_regex.search('The Adventures of Batman')
   mo1.group()
   # 'Batman'

   mo2 = bat_regex.search('The Adventures of Batwoman')
   print(mo2.group())
   # 'Batwoman'

if 0:
   bat_regex = re.compile(r'Bat(wo)*man')
   mo1 = bat_regex.search('The Adventures of Batman')
   mo1.group()
   'Batman'

   mo2 = bat_regex.search('The Adventures of Batwoman')
   print(mo2.group())
   # 'Batwoman'

   mo3 = bat_regex.search('The Adventures of Batwowowowoman')
   print(mo3.group())
   # 'Batwowowowoman'

if 0:
   bat_regex = re.compile(r'Bat(wo)+mann')

   mo1 = bat_regex.search('The Adventures of Batwoman')
   print(mo1.group())
   # 'Batwoman'

   mo2 = bat_regex.search('The Adventures of Batwowowowoman')
   print(mo2.group())
   # 'Batwowowowoman'

   mo3 = bat_regex.search('The Adventures of Batman')
   mo3 is None
   # True





