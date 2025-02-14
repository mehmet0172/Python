"""" 
1- Bir musterinin asagidaki bilgileri icin bir degisken olusturunuz.

Müşterinin adı
Müşterinin soyadı
Müşteri adı + soyadı
Müşteri cinsiyet
Müşteri tc kimlik
Müşteri doğum yılı
Müşteri adres bilgisi
Müşteri yaşı

"""
musteriAdi = 'Ali'
musteriSoyadi = 'Yilmaz'
musteriAdsoyad = 'Ali Yilmaz'
musteriAdsoyad = musteriAdi + ' ' +  musteriSoyadi

print(musteriAdsoyad)

musteriCinsiyet = 'Kadin'
musteriCinsiyet = 'erkek'
musteriTCkimlik ='70765186033' #tirnak icine alinan her ifade bir str dir. bu sayilarla hesap yada islem yapmayacagimiz icin tirnaklaicerisine aliyoruz.

musteriDogumyili = 1988 #yasi hesapliyacagimiz icin bir int olarak kullanacagiz. tirnaklar icerisine almayacagiz.

musteriYasi =  2023 - musteriDogumyili

musteriAdresi = 'ulitsa gagarina 140'

print(musteriYasi)

print( 2023 - musteriDogumyili)

"""
  
  2- Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.
  
    sipariş 1 = 110 tl
    sipariş 2 = 1100.5 tl
    sipariş 3 = 356.95 tl
  
"""
order1 = 110 
order2 = 1100.5 
order3 = 356.95

total = order1 + order2 + order3

print('Total:', total)