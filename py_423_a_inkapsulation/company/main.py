from company import Company
from number import Number

beelineFile = open("Beeline.txt","r")
beelineNumbers = beelineFile.readlines()

beeline = Company(companyName="Beeline")
price = 1000
for i in beelineNumbers:
    price+=100
    beeline.addNumber(number=Number(company="Beeline",number=i,price=price))


beelinePhoneNumbers = beeline.getPhoneNumbers()
print(beelinePhoneNumbers[0])
beeline.sellNumber(beelinePhoneNumbers[0])
print(beeline)
