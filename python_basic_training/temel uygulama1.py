__author__ = " Mehmet Sherif Bichen"

# kullanicidan cesitli degerler alip yapilan girdilere gore farkli mesajlar ureten python kodunu yazalim

# Kodumuzun biz durana kadar bir dongu icinde surekli calismasini isttiyorsak 'While  True' diye baslariz.
# Ardindan kullanicinin secim yapmasini istedigimiz degerleri ve anlamlari kullanici ekranina yazdiririz.
while True:
    print('Sabah  (1)')
    print('Ogle  (2)')
    print('Aksam  (3)')
    print('Gece  (4)')
    print('____________')
    print()
    # Bu uygulama icerisinde ekrana yazdirdiklarimiz, gun icerisindeki zaman dilimleri ve kullanicidan ogrenmek
    # istedigimiz isim bilgisidir. INPUT fonksiyonu kullanicidan cesitli degerler okunmasini yani kullanicinin
    # programa girdi yapmasini saglayan fonsiyondur.

    secim = input("Gun icerisindeki zaman dilimini giriniz...:")
    isim = input("Isminiz: ")
    # Ekrana yazilacak secim ve isim degerlerini kullanicidan input yani girdi fonksiyonu aldiktan sonra girilen
    # degerlere gore farkli cikti mesajlari uretilmesi, bir kontrol yapisi olan IF ve ELSE bloklari ile yapilir.
    if secim == "1":
        print("Good Morning", isim)

    elif secim == "2":
        print("Good Afternoon", isim)

    elif secim == "3":
        print("Good Evening", isim)

    elif secim == "4":
        print("Good Night", isim)
    else:
        print("Gun araligi gecersiz. Program sonlandiriliyor...")
        break
