""" **********MODUL TIPLERI*********
1. Ozel Moduller                  2.Hazir Moduller
                                          a. Standart kutuphane Modulleri   b.Ucuncu Sahis modulleri
"""
""" *** a.Standart Kutuphane Modulleri ***
python gelistiricileri tarafindan olusturulan modullerdir."""

#import os
##if os.name != 'nt' : #isletim sistemi, windows degilse
##    print(' Bu programi yalnizca windowsta kullanabilirsiniz.')
##else :
##    print("Bu program Windows'ta calisiyor.")

"""Herhangi bir python modulunu kullanmak icin iceri aktarmak gerekir. bunun icinde  'import' ifdesini
kullaniyoruz. kullandigimiz modulun ne gibi fonksiyon ve nitelik barindirdigini ogrenmek icin
'dir(os)' ifadesini kullaniyoruz."""
##import os
##print(dir(os))

##import ettigimiz modul ismini oldugu gibi kullanamazsak ne yapabiliriz?
##import subprocess
##subprocess.call('notepad.exe')

""" ornek kod : eger modul ismi cok uzun ise bunu asagidaki gibi 'as' ifadesini kullanarak yeni
kisa bir isim verebilir ve kullanabiliriz."""
##import subprocess as sbp
##sbp.call('notepad.exe')



""" *** Ucuncu Sahis modulleri ***
pythonda kod program yazabilen herkesin yazabilecegi modullerdir."""

## *** Kendi modulumuzu yaziyoruz.***
""" 1. oncelikle modul haline gericegimiz kodlari sozluk liste halinde yaziyoruz ve bir degiskene
atiyoruz
     2. sonra bunlari sozluk adinda bir dosyaya kaydediyoruz dosyanin ismi farkli olabilir. Burada
     onemli olan ya olusturdugumuz modul yazacagimmiz programla ayni dizinde yer alacak yada
     python dosyalarinin oldugu klasorde yer alacak.eger python klasorunde yer alirsa her yazdigimiz
     programda kulllanabiliriz. aksi halde sadece yazdigimiz programda yer alir calisir

     3. modulu tanimlamak icin kisa bir program yaziyoruz
     4. modul tanimlamak icin ozel bir kural yoktur. bu yuzden yazilan her python programi bir  moduludur.
     5. modulumuz sozluk.py isimli dosyada olusturduk.
     6. simdi program.py isimli dosya acip deniyoruz. eger sozluk.py ve program.py ayni dizinde olursa
     sorunsuz sozluk modulunun tum fonksiyonlari calisacaktir. Peki programin kendisiyle import edilen
     modulu ayni dizinde tutmak zorundamiyiz?
     7. Tabiki degiliz. bu sorunu asmak icin yazdigimiz modulu pythonin diger modullerinin oldugu dizine
     klasore atmamiz yeterlidir. bu dizinin hangi dizin oldugunu ogrenmek icin etkilesimli kabugu aciyoruz.
     8. sys modulunu import edelim. Ardindan sys.path komutunu enter edip calistiralim. idle yi acip su kodu
     yazarakta ogrenebiliriz import sys
print(sys.path).
     
     """
##sozluk = { "kitap" : "Book", "bilgisayar" : "computer", "programlama" : "programming"
##def ara (sozluk) :
##        hata = "{} kelimesi sozlukte yok!"
##        return sozluk.get(sozcuk, hata.format(sozcuk))
 
##import sys
##print(sys.path)
import testmodul
