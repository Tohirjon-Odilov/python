# SET indexlanmaydi va xotiradi bir nom ostida turadi
# SET unikallarini saqlaydi 
# bo'sh SET elon qilish -> st = set()
# SETga element qo'shish -> st.add("Nexia") 
# SETni ichini tozalaydi -> st.clear()
# bir SETni boshqa SETga qo'shadi -> st = st2.copy()
# SETdan random birorta elementni olib tashlaydi(return qaytaradigan metod) -> item = st.pop()
# SET dan elementni olib tashlash -> st.remove() //yoq narsada xato beradi
# SET dan elementni olib tashlash -> st.discard() // yoq narsada xato bermaydi

# aziz = {"Nexia","Damas","Mers","BMW","Nexia"}
# asadbek = {"Lambargini","Cadelac","Mers","Bentli","BMW"}

# .union return qaytaradi
# tohirjon = aziz.union(asadbek) -> tohirjon = {"BMW","Mers","Damas","Nexia","Lambargini","Bentli","Cadelac"}

# .update return qaytarmaydi
# aziz.update(asadbek) -> aziz = {"BMW","Mers","Benli","Cadelac","Lambargini","Damas","Nexia"}

# .intersection return qaytaradi
# tohirjon = aziz.intersection(asadbek) ->  tohirjon = {"BMW","Mers"}

# .intersection_update return qaytarmaydi
# aziz.intersection_update(asadbek,aziz) -> aziz = {"BMW","Mers"}
# aziz.intersection_update(asadbek) -> aziz = {"BMW","Mers"}

# .difference return qaytaradi -> faqat aziz da borini oladi
# tohirjon = aziz.difference(asadbek) #-> tohirjon = {"Damas","Nexia"}

# .difference_update return qaytarmaydi -> aziz da borni asadbekdan olib tashlaydi
# asadbek.difference_update(aziz) -> asadbel = {"Bentli", "Lambargini", "Cadelac"}

# .symmetric_difference return qaytaradi -> ikkalasida ham borlarini olmaydi
# tohirjon = asadbek.symmetric_difference(aziz) -> tohirjon = {"Cadelac","Damas","Lambargini","Nexia","bentli"}

# .symmetric_difference_update return qaytarmaydi -> asadbekdan o'zida ham azizda ham  borini olib tashlaydi
# asadbek.symmetric_difference_update(aziz) -> asadbek = {"Cadelac","Damas","Bentli","Lambargini","Nexia"}

