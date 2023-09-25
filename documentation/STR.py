# print('saLOm'.capitalize()) -> Salom -> birinchisini katta qolganini kichik
# print('SAloM'.casefold()) -> salom -> barchasini kichik
# print('Salom'.center(20, '.')) -> .......Salom........
# print('text\ttext2\ttext3'.expandtabs(10)) -> text      text2     text3 
# print('{subject} is doing {action}.'.format(subject='cat',action='meow')) -> cat is doing meow
# print('-'.join('salom')) -> s-a-l-o-m
# print('salom'.rjust(20,'.')) -> ...............salom
# print('salom_qale_zormi'.rpartition('_')) -> ('salom_qale', '_', 'zormi')
# print('salom_qale_zormi'.partition('_')) -> ('salom', '_', 'qale_zormi')
# print('salom_dunyo'.rsplit(sep = '_')) -> ['salom', 'dunyo']
# print('salom_dunyo_k'.split('_')) =-> ['salom', 'dunyo', 'k']
# print('salom nima salom salom'.rstrip('salom')) -> salom nima salom
# print('salom\nnima\nqale'.splitlines(keepends=True)) -> ['salom\n', 'nima\n', 'qale']
# print('salom\nnima\nqale'.splitlines(keepends=False)) -> ['salom', 'nima', 'qale']
# print('salom qale zormi'.strip('salom')) -> qale zormi
# print('salom qale zormi'.strip('zormi')) -> salom qale
# print('salom nima gaplar'.swapcase()) -> SALOM NIMA GAPLAR
# print('salom dunyo'.title()) -> Salom Dunyo
# print('saLOM'.upper()) -> SALOM
# print('salom'.zfill(14)) -> 000000000salom

# print('salom_dunyo'.count('o')) -> 2 -> return sum
# print('salom'.index('a')) -> 1 -> return index
# print('salom'.find('l')) -> 1 -> return index
# print('salom'.rfind('l')) -> 2 -> return index
# print('salom'.rindex('l')) -> 2 -> retuern index

# print('salom'.endswith('m')) -> True -> oxirgisi 'm' bo'lsa true ask holda false
# print('salom88'.isalnum()) -> harf va raqamlarda true qaytaradi
# print('salom'.isalpha()) -> barchasi harflar bo'lsa true qaytaradi
# print('salom😔'.isascii()) -> barchasi ASCII TABLEdagi belgilar bo'lsa true qaytaradi
# print("123".isdecimal()) -> barchasi qaramlar bo'lsa tru qaytaradi
# print('123'.isdigit()) -> barchasi raqamlarda iborat bo'lsa true qaytaradi
# print('sample-test'.isidentifier()) -> o'zgaruvchiga shunday nom qo'yish mumkin bo'lsa true qaytaradi
# print('salOm'.islower()) -> barchasi kichik harf bo'lsa true qaytaradi
# print('salom\t'.isprintable()) -> \t,\n,\b kabi belgilar qatnashsa false qaytaradi
# print('    '.isspace()) -> bo'sh joy bo'lsa true qaytaradi
# print('Salom Dunyo'.istitle()) -> bosh bir so'zni bosh harfi katta bo'lsa true qaytaradi
# print("SALOM".isupper()) -> barchasi katta harf bo'lsa true qaytaradi
# print('SALOM'.lower()) -> salom
# print('salom dunyo '.lstrip('salom')) -> dunyo -> agar birinchisi bo'lsa ochirib tashlaydi
# print('a+b=c'.partition('=')) -> ('a+b', '=', 'c')
# print('salom dunyo'.removeprefix('salom')) -> dunyo
# print('salom qale nima gap'.removesuffix('gap')) -> salom qale nima
# print('salom dunyo'.replace('dunyo','qale')) -> salom qale
# print('Salom'.startswith('S')) -> birinchi harfiga teng bo'lsa true qaytaradi