sozluk = { "kitap" : "Book", "bilgisayar" : "computer", "programlama" : "programming"}
def ara (sozcuk) :
        hata = "{} kelimesi sozlukte yok!"
        return sozluk.get(sozcuk, hata.format(sozcuk))
