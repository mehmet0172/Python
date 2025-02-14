"""
Вы работаете в команде веб-платформы с прогнозом погоды. hava tahmini yapan web-platformunda çalışıyoruz.
Вы работаете над модулем, который будет выдавать статистическую информацию о температуре за определенный период.
Belirli bir zaman dilimindeki sıcaklık hakkında istatistiksel bilgi sağlayacak bir modül üzerinde çalışıyorsunuz.

На вход подается список из целых чисел.- kullanıcıdan girdi olarak tam sayıların olduğu bir liste alıyoruz.
Ваша задача — определить, сколько чисел в этом списке являются положительными, сколько отрицательными и сколько из них равны нулю.
sizin göreviniz kaç tana pozitive, negatif, ve 0 ra eşit sayı olduğunu tahmin etmek.
Вам нужно вывести не сами числа, а их количество в каждой категории.sayıların kendisini değil, kategorilerine göre kaç tane olduğunu bulmak.

Формат ввода Входные данные состоят из одной строки, в которой чередуются целые числа, разделенные пробелами.
Длина списка не превышает 100 элементов.
Формат вывода Одна строка в формате: «выше нуля: A, ниже нуля: B, равна нулю: C», где A, B и C — количество положительных,
отрицательных и нулевых чисел в списке соответственно. Будьте внимательны с пробелами и знаками препинания.
Пример 1 Входные данные: 5 -2 0 0 7 8 -1 Выходные данные: выше нуля: 3, ниже нуля: 2, равна нулю: 2


Bu problemi anlamak için öncelikle görevimizi ve nasıl bir çözüm geliştireceğimizi belirleyelim.

Problemin Tanımı
Bir dizi tam sayı alacağız ve bu tam sayılar arasında pozitif (sıfırdan büyük), negatif (sıfırdan küçük)
 ve sıfıra eşit olan sayıların sayısını bulmamız gerekiyor. Sonuçları belirli bir formatta çıktı olarak vereceğiz.

Algoritmanın Adımları
Girdi Alma: Kullanıcıdan bir satır uzunluğunda tam sayılar alınacak.
Verileri Ayırma: Girilen veriyi boşluklara göre ayırarak bir liste haline getireceğiz.
Sayıları Sayma: Pozitif, negatif ve sıfır olan sayıların sayısını tutmak için 3 değişken tanımlayacağız ve
her bir sayı için bu değişkenleri güncelleyeceğiz.
Sonucu Yazdırma: Sayım tamamlandıktan sonra, elde edilen değerleri belirli bir formatta çıktı olarak vereceğiz.
Kod
Aşağıda belirtilen adımları takip eden Python kodunu yazalım:
"""


# Girdi al
input_data = input()

# Girdi verisini boşluklardan ayır ve tam sayılara çevir
numbers = list(map(int, input_data.split()))

# Sayıların kategorilerini saymak için değişkenler
positive_count = 0
negative_count = 0
zero_count = 0

# Her bir sayıyı kontrol et ve kategorilere göre say
for number in numbers:
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1

# Sonucu belirlenen formatta yazdır
print(f"выше нуля: {positive_count}, ниже нуля: {negative_count}, равна нулю: {zero_count}")

"""
Açıklama
input() fonksiyonu, kullanıcıdan bir girdi alır.
split() metodu, girilen veriyi boşluk karakterlerinden ayırarak bir liste oluşturur.
map(int, ...) kullanarak, liste elemanlarını tam sayılara dönüştürüyoruz.
for döngüsü ile her bir sayıyı kontrol ederiz. Pozitif, negatif ve sıfır olan sayılar için sayaçları güncelleriz.
Son olarak, sayım sonuçlarını istenilen formatta çıktı olarak basarız.
Bu adımlar ve kod ile verilen problem başarıyla çözülmektedir.
"""


# daha kisa bir fonksiyon olusturalim
# bir fonksiyon tanimliyoruz
def process(input_string):

    temps = list(map(int, input_string.split()))
    pos_count = sum(1 for temp in temps if temp > 0)
    neg_count = sum(1 for temp in temps if temp < 0)
    zer_count = sum(1 for temp in temps if temp == 0)
    return f"выше нуля: {pos_count}, ниже нуля: {neg_count}, равна нулю: {zer_count}"
input_string = input()
output_string = process(input_string)
print(output_string)

# Yada boyle
def count_temperature_stats():
    temps = list(map(int, input().split()))
    poS_count = sum(1 for temp in temps if temp > 0)
    nega_count = sum(1 for temp in temps if temp < 0)
    zeRo_count = sum(1 for temp in temps if temp == 0)
    print(f"выше нуля: {poS_count}, ниже нуля: {nega_count}, равна нулю: {zeRo_count}")

count_temperature_stats()

scores = list(map(int, scores_input.split(',')))
excellent_count = sum(1 for score in scores if score >= 50)
good_count = sum(1 for score in scores if 35 <= score < 50)
poor_count = sum(1 for score in scores if score < 35)
result = f"Отлично: {excellent_count}\nХорошо: {good_count}\nНеудовлетворительно: {poor_count}"
    return result