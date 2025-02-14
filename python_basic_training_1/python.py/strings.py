# ' my name is Mehmet Sherif and i am 35 years old.' ifadesisini yazdir.
name = 'Mehmet Sherif'
surname = 'Bichen'
age = 35
# age = '35' #bir str ile int toplayamazsin. ciktida hata verir. bunun icin ya age degiskeninin degerini iki tirnak arasina alarak str ye cevirirsin. yada print icerisindeki age ifadesinin basina str yazip age i parantez icerisine alarak str cevirisin.

# print('My name is' + ' ' + name + ' ' + surname + ' ' + 'and i am' + ' ' + str(age) + ' ' + 'years old.')
# yada print icerisindeki age ifadesinin basina str yazip age i parantez icerisine alarak str cevirisin.
greeting = 'My name is' + ' ' + name + ' ' + surname + ' ' + 'and \n i am' + ' ' + str(age) + ' ' + 'years old'
length = len(greeting) # artik length degiskeni greeting degiskeninin kac karakterli oldugunu soyluyor bize.
#print(greeting) # bu sekilde degisken olusturarak bir degisken araciligiyla da yazdira biliriz
# print(greeting[0]) #0 ci karakteri yazdirir
# print(greeting[3]) #3 cu karakteri yazdirir
# print(len(greeting)) #3 len modulu greeting degiskenindeki string ifadesinin kac karakter oldugunu sayar.
# print(greeting[length-1])
# print(greeting[-1]) # uzun islemler yerine index numarasini girerekte istedigimiz sonuca ulasabiliriz
# # print(greeting[2:7])#bu ifade ikinci indexten basla yediye kadar git
# print(greeting[2:])#ikinci indexten basla sonuna kadar git
# print(greeting[:15])# 0 dan baslar sonana kadar gider
# print(greeting[2:40:2]) #ikinci undexten baslar 40 kadar gider ama bir bir degil iki karakterde bir alir gider 
name = 'Мехмет'
age = 36
hobby = 'учиться'


print(f'''Меня зовут {name}
Мне {age} лет
Я люблю всегда {hobby} новый вешь кажды день''')
