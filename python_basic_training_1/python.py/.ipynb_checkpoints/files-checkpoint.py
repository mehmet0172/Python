# Dosya acmak ve olusturmak 'icin open fonksiyonuna ihtiyac duyariz
# Kulllanimi : open(dosya_adi,dosya_erisme_modu)
# dosya_erisme_modu => dosyayi hangi amacla actigimizi belirtir.

# "w": (Write) yazma modu. Dosyayi konumda olusturur.
# "a" : (append) ekleme. dosya konumda yoksa olusturur.
# "x": (create) olustuma . dosya zaten varsa hata verir. amacimiz sadece dosya acmaksa bunu kullaniriz.
# "r" : (read) okuma. varsayilan dosya konumda yoksa hata verir.
'''dosyalara erismek icin open() fonksiyonundan yararlaniyoruz. erisim modu parametresiylede dosyayla ilgili okuma mi yazma mi yad
degistirmemi gibi islemleri gerceklestirebiliriz. ornegin'''
tahsilat_dosyasi=open("tahsilatlar.txt", "w")
#dosya=open("/dosyayi/olusturacagimiz/dizin/dosyaadi", "w") burada da dosyayi olusturacagimiz  dizini belirliyoruz.
dosya = open("C:/Users/anyag/python uygulamaları/tahsilat_dosyasi", "w")
print(dosya)

#rehber = open("C:/Users/anyag/python uygulamaları/tahsilat_dosyasi.txt", "r") #bu fonksiyon sadece dosyayi okuyacaktir

# dolayisiyla sonucu biryere atamamiz gerekiyor. bu yuzden sonuc degiskenini kullaniyoruz.

#sonuc=rehber.read()
#print(sonuc)   #okudugumuz dosyayi ekrana yazdirmak icin sonuc degiskenini yazdiriyoruz
#diyelim ki dosyanin ilk satirini okumak istiyoruz o zaman readline() fonksiyonunu kullaniyoruz.

#sonuc = rehber.readline()
#print(sonuc)

#readline fonksiyonunu tekrar cagirirsak ne olur? dosyanin diger satirini okuruz yada yazdiririz.bu fonksiyon her cagirilisinda son satira kadar hep bir sonraki satiri dondurecektir
#Son satira ulastigimiz python bize bir cevap yada hata vermeyecektir.


#sonuc = rehber.readlines()# diyelimki dosyanin her satirini bir dosya halinde almak istiyoruz o zaman readlines() fonksiyonunu kullaniyoruz.
print(sonuc)

# Pythonla dosyaya yazmak
rehber = open("C:/Users/anyag/python uygulamaları/yeni isimler.txt", "w") # dosyanin adresini dogru bir sekilde yaziyoriuz
# erisim modu parametresinede w yaziyoruz
#deneme amacli bir karakter dizisi olusturuyoruz
kayitlar = """ Ahmet Yilmaz    :  0555 111 11 11\n Murat Can    :  0555 222 22 22\n Vildan Poyraz    :  0555 333 33 33\n"""
# write komutuyla bunlari dosya yaziyorruz
rehber.write(kayitlar) # ayni isimde dosya varsa ve doluysa icerigi silinip uzerine yalacaktir
'''isimiz bittikten sonra dosyalari  mutlaka kapatmaliyiz. Aksi halde isletim sistemini mesgul etmis oluruz.
bunun icin close() foksiyonunu yaziyoruz.'''
rehber.close()


