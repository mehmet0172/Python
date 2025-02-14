website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"
# 1 - ' Hello World ' karakter dizisinin bas ve sondaki bosluk karakterlerini silin.
#Cevap:
# a = ' Hello World '
# # a = a.lstrip()# sol boslugu alir
# # a = a.rstrip()#sag boslugu alir
# # a = website.lstrip('/:pth')#sagdan sola dogru giderek belirttigimi kasrakterleri alir
# print(a)

# 2 - 'www.sadikturan.com' icindeki sadikturan bilgisi haricindeki her karakteri silin.
# Cevap:
# website = website.split('.') # 1. secenek cumle icerisindeki noktalardan itibaren ayirir ve bir liste olusturur
# print(website[1]) listedeki indeks numarasini girerek istediginiz kelimeyi alirsin.

# # 2.Secenek ise yukaridaki gibi striple.
# result = website.strip('moc.w/:pth') 
# print(result)

# 3- 'course' karakterdizisinin tum karakterlerini kucuk harf yapin.
# Cevap:
# course = course.lower()
# course = course.upper()
# course = course.title()
# course = course.capitelize()
# print(course)

# 4- 'website' icinde kac tane a karakteri vardir?
# Cevap:
result = website.count('a') #cumle icerindeki karakter sayisini ogrenmemizi saglar
result = website.count('www') #cumle icerindeki karakter sayisini ogrenmemizi saglar
result = website.count('www', 0, 10) #cumle icerinde 0 ile 10 index araliginda arama yapar
# print(result)

# 5- 'website' www ile baslayip com ile bitiyor mu?
#Cevap:
# result =website.startswith('www')#False ama ikisini beraber calistirirsak yada http:// kaldirirsak sonuc True olacaktir
# result =website.endswith('com')#True
# print(result)

# 6- 'website' icinde .com ifadesi var mi?
#Cevap: 21 var bu index numarasidir
# result = website.find('.com') # 21 pozitif yani var
# result = website.find('.com', 0, 10) # -1 verir bu negatif yani olmadigini gosterir. yine belirttigimiz index araliginda arama yapar
# result = website.index('.com')#21 find metodunun alternatifi
# result = website.rindex('.com')#21 sagdan arama yapar find metodunun alternatifi
# result = website.rindex('.com')#21 sagdan arama yapar find metodunun alternatifi
# result = website.rindex('.comm')#exception hatanin karsiligina gelir aradigimiz sey eger yojksa find metodu gibi negatif bir sayi vermez find dan farkli olarak hata dondurur yani calismaya devam eder ama olmadigini soyler.
# print(result)

# 7- 'course' icindeki karakterlerin hepsi alfabetik mi?(isalpha, isdigit)
# result = course.isalpha()#False
# result = 'python'.isalpha()#True
# print(result)
# result = course.isdigit()#False
# result = '12345'.isdigit()#True
# print(result)

#8- 'Contents' ifadesini satirda 50 karakter icine yerlestirip sag ve soluna * ekleyin.
#cevap:
# result = 'Contents'.center( 50, '*')
# result = 'Contents'.ljust( 50, '*')#soluna ekler
# result = 'Contents'.rjust( 50, '*')#sagina ekler
# print(result)

# 9- 'course' karakter dizisindeki tum bosluk karaterlerini '-' ile degistirin.
#Cevap:
# result = course.replace(' ', '-')
# result = course.replace(' ', '-' , 5) #sinir belirleriz
# result = course.replace(' ', '')# tum bosluklari alir
# print(result)


# # 10- 'Hello World' karakter dizisinin 'World' ifadesin 'There' ile degistirin.
# #Cevap:
# result = 'Hello World'.replace('World', 'There')
# print(result)

# 11- 'course' karater dizisini bosluk karakterlerinden ayirin.
# #Cevap:
# result = course.split(' ')
# print(result)