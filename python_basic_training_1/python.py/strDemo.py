website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"
# 1- 'course' karakter dizesinde kac karakter bulunmaktadir?
# print(len(course))
# Cevap: 65
# 2- 'website' icinden www karakterlerini alin.
# Cevap print( website[7:10])
# 3- 'website' icinden com karakterlerini alin.
# Cevap print( website[-3:])
# 4- 'course' icinden ilk 15 ve son 15 karakteri alin.
# print(course[:15]) ilk 15
# print(course[50:]) son 15
# 5- 'course' ifadesindeki karakterleri tersten yazdiriniz.
#Cevap print(course[::-1])
name, surname, age, job = 'Bora', 'Yilmaz', 32, 'muhendis'
# 6- Yukarida verilen degiskenler ile ekrana asagidaki ifadeyi yazdiriniz.
#'Benim adim Bora Yilmaz, yasim 32 ve meslegim muhendis.'
# Cevap:
# print('Benim adim {} {}, yasim {} ve meslegim {}' .format(name, surname, age, job))
# print(f'Benim adim {name} {surname}, yasim {age} ve meslegim {job}' )

# 7- 'Hello word' ifadesindeki w harfini W harfi ile degistirin.
# Cevap :
# s = 'Hello Word'
# s = s[:6] + 'W' + s[-3:]
# print(s)

# 8- 'abc' ifadesini yanyana 3 defa yazdirin.
# Cevap :
# b = 'abc' * 3
# print(b)
# # print('abc' * 3)
N = int(input('bir sayi giriniz'))
# toplam = 0
# i = 1
# while i <= N :
  
#     toplam += i
#     i += 1
  
  
#     print('toplam:',toplam)
for a in range(0, N, 5):
  print(a)