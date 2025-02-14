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
#print(sonuc)

# Pythonla dosyaya yazmak
#rehber = open("C:/Users/anyag/python uygulamaları/yeni isimler.txt", "w") # dosyanin adresini dogru bir sekilde yaziyoriuz
# erisim modu parametresinede w yaziyoruz
#deneme amacli bir karakter dizisi olusturuyoruz
#kayitlar = """ Ahmet Yilmaz    :  0555 111 11 11\n Murat Can    :  0555 222 22 22\n Vildan Poyraz    :  0555 333 33 33\n"""
# write komutuyla bunlari dosya yaziyorruz
#rehber.write(kayitlar) # ayni isimde dosya varsa ve doluysa icerigi silinip uzerine yalacaktir
'''isimiz bittikten sonra dosyalari  mutlaka kapatmaliyiz. Aksi halde isletim sistemini mesgul etmis oluruz.
bunun icin close() foksiyonunu yaziyoruz.'''
#rehber.close()
 

''' dosyalari kapatmanin bir diger guvenli yolu ' try , except, finally ' fonksiyonudur. bu fonksiyon her halukarda dosyayi kapatacaktir'''
#try: # try bolumune dosyayla ilgili yazma,,okuma,ekleme vs islemleri gerceklestirecegimiz kodlari yaziyoruz
    #rehber= open("C:/Users/anyag/python uygulamaları/yeni isimler.txt", "w")
#kayitlar = """ Ahmet Yilmaz    :  0555 111 11 11\n Murat Can    :  0555 222 22 22\n Vildan Poyraz    :  0555 333 33 33\n"""
    #rehber.write(kayitlar)
#except IOError:#  dosyayla ilgili hatalar ve sorunlarda ekrana bizim belirledigimiz bildiriyi yaziyor
   #print("bir hata olustu")
#finally:
    #rehber.close()# finally ise ne olursa olsun islem sonun da dosyayi kapatir
    
     # Pythonin guvenli kapatmak icin bir cozumu daha var.o da with fonksiyonudur.
     
#with open("C:/Users/anyag/python uygulamaları/yeni isimler.txt", "w") as dosya:
            #dosya.write(kayitlar)

#cnc_kod = """
#T0101\n G54\n G96 S200 M3\n G50 S2000\n G00 X81 Z-2 M8\n 
#"""
# with open("C:/Users/anyag/python uygulamaları/Самостоятельная работа 5.txt", "w") as dosya:
            #dosya.write(cnc_kod)


























            
