"""
Bu problemde, bir dizi çitlerin uzunlukları verilmiştir ve bu çitler arasındaki maksimum dikdörtgen alanı bulmamız istenmektedir. Çitlerin genişliği 1 birimdir, bu nedenle sorunun çözümü, iki çit arasında kalan maksimum alanı bulmayı gerektirir.

Çözüm Yöntemi
Bu problemi çözmek için Two Pointer (İki Uçlu Gösterici) algoritmasını kullanabiliriz. Sol ve sağ uçtan başlayarak, her adımda küçük olan çiti seçeriz ve alanı hesaplayarak, maksimum alanı takip ederiz.


# Örnek 1
lengths1 = [2, 4, 3, 2, 1, 4, 1]
print(max_rectangle_area(lengths1))  # Çıktı: 16

# Örnek 2
lengths2 = [1, 2]
print(max_rectangle_area(lengths2))  # Çıktı: 1
Açıklama:
İki Gösterici Yöntemi: Başlangıçta bir gösterici sol uçta (0. indeks), diğeri sağ uçta (son indeks) konumlanır. Her adımda, iki çit arasındaki alanı hesaplarız ve daha kısa olan çiti hareket ettiririz.
Alan Hesaplama: Alan, iki çit arasındaki mesafe (genişlik) ile daha kısa olan çitin yüksekliğinin çarpımı ile bulunur.
Maksimum Alan Takibi: Her adımda hesaplanan alan, daha önceki maksimum alanla karşılaştırılır ve en büyük alan saklanır.
Bu çözümün zaman karmaşıklığı O(n) olup, n çit sayısına eşittir.
"""
"""

def max_area(lengths):
    # İki gösterici: sol başta, sağ sonda başlar
    sol = 0
    sag = len(lengths) - 1
    max_alan = 0

    # Sol gösterici, sağ göstericiyi geçene kadar devam eder
    while sol < sag:
        # Şu anki alanı hesapla (yükseklik, daha kısa olan çittir)
        yukseklik = min(lengths[sol], lengths[sag])
        genislik = sag - sol
        alan = yukseklik * genislik

        # Maksimum alanı güncelle
        max_alan = max(max_alan, alan)

        # Küçük olan çit tarafını hareket ettir
        if lengths[sol] < lengths[sag]:
            sol += 1
        else:
            sag -= 1

    return max_alan


# Kullanıcıdan girdi alalım
girdi = input("Çit yüksekliklerini aralarında boşluk bırakarak girin: ")

# Girdi stringini sayılara dönüştürelim
lengths = list(map(int, girdi.split()))

# Maksimum alanı hesaplayıp yazdır
print("Maksimum dikdörtgen alanı:", max_area(lengths))
"""

"""
def max_area(lengths):
    # Устанавливаем два указателя: левый в начале, правый в конце
    left = 0
    right = len(lengths) - 1
    max_area = 0  # Переменная для хранения максимальной площади

    # Пока левый указатель меньше правого
    while left < right:
        # Высота определяется минимальной высотой между двумя заборами
        height = min(lengths[left], lengths[right])

        # Ширина равна расстоянию между заборами
        width = right - left

        # Площадь равна высоте умноженной на ширину
        area = height * width

        # Обновляем максимальную площадь, если нашли больше
        max_area = max(max_area, area)

        # Двигаем указатели: если левый забор ниже, перемещаем его вправо
        if lengths[left] < lengths[right]:
            left += 1
        else:
            right -= 1

    return max_area


# Получаем данные от пользователя
user_input_heights = input("Введите высоты заборов через пробел: ")

# Преобразуем строку в список целых чисел
lengths = list(map(int, user_input_heights.split()))

# Выводим максимальную площадь
print("Максимальная площадь:", max_area(lengths))


def max_area(lengths):
    left = 0
    right = len(lengths) - 1
    max_area = 0

    while left < right:
        height = min(lengths[left], lengths[right])
        width = right - left
        area = height * width
        max_area = max(max_area, area)

        if lengths[left] < lengths[right]:
            left += 1
        else:
            right -= 1

    return max_area


# Kullanıcıdan girdi alıyoruz
line = input()  # Örneğin: "2 4 3 2 1 4 1"
lengths = list(map(int, line.split()))  # Boşlukla ayrılmış sayıları diziye çeviriyoruz

# Maksimum alanı hesaplayıp yazdırıyoruz
print(max_area(lengths))  # Örneğin: 16
"""
"""
 def max_area(lengths):
Türkçe Açıklama: Bu satırda, yeni bir fonksiyon oluşturuyoruz. Fonksiyonun adı max_area. Bu fonksiyon, bir liste alacak (çit uzunluklarını) ve en büyük dikdörtgen alanını bulacak.
Rusça Açıklama: В этой строке мы создаем новую функцию. Имя функции — max_area. Эта функция будет принимать список (высоты заборов) и находить наибольшую площадь прямоугольника.
python
Копировать код
    left = 0
    right = len(lengths) - 1
    max_area = 0
Türkçe Açıklama:
left = 0: Çitlerin en solundaki işaretçiyi oluşturuyoruz. Yani sol uçtaki çiti işaretliyoruz.
right = len(lengths) - 1: Çitlerin en sağındaki işaretçiyi oluşturuyoruz. Bu da en sağdaki çiti gösteriyor.
max_area = 0: Şu an için en büyük alanı bilmiyoruz, bu yüzden başlangıçta alanı 0 olarak ayarlıyoruz.
Rusça Açıklama:
left = 0: Создаем указатель на самый левый забор. Это указывает на забор в начале списка.
right = len(lengths) - 1: Создаем указатель на самый правый забор. Это указывает на забор в конце списка.
max_area = 0: Пока что мы не знаем наибольшую площадь, поэтому изначально устанавливаем её в 0.
python
Копировать код
    while left < right:
Türkçe Açıklama: Sol ve sağ uçlar birbirine yaklaşmadığı sürece bu döngü devam edecek. Yani iki çit arasında hala boşluk olduğu sürece işlem yapacağız.
Rusça Açıklama: Этот цикл будет продолжаться, пока левый и правый указатели не встретятся. То есть, пока между заборами есть пространство, мы продолжаем.
python
Копировать код
        height = min(lengths[left], lengths[right])
Türkçe Açıklama: İki çitin yüksekliğine bakıyoruz ve kısa olanı seçiyoruz. Çünkü dikdörtgenin yüksekliği, kısa olan çitle sınırlıdır.
Rusça Açıklама: Мы смотрим на высоту двух заборов и выбираем меньший. Потому что высота прямоугольника ограничена самым низким забором.
python
Копировать код
        width = right - left
Türkçe Açıklama: İki çit arasındaki mesafeyi hesaplıyoruz. Genişlik, sağ çit ile sol çit arasındaki farktır.
Rusça Açıklама: Мы считаем расстояние между двумя заборами. Ширина — это разница между правым и левым заборами.
python
Копировать код
        area = height * width
Türkçe Açıklama: Alanı bulmak için yüksekliği genişlikle çarpıyoruz. Dikdörtgenin alanı yükseklik x genişlik formülüne göre hesaplan
 
         area = height * width
Türkçe: Şimdi dikdörtgenin alanını buluyoruz. Alan = Yükseklik x Genişlik.
Rusça: Теперь мы находим площадь прямоугольника. Площадь = Высота x Ширина.


     max_area = max(max_area, area)
Türkçe: Burada, şu ana kadar bulduğumuz en büyük alanı kontrol ediyoruz. Eğer yeni bulduğumuz alan (yani area) daha büyükse, max_area değişkenini güncelliyoruz. Bu, en büyük alanı hep aklımızda tutmamıza yarıyor.
Rusça: Здесь мы проверяем, является ли найденная площадь (area) больше максимальной найденной ранее площади. Если да, то мы обновляем переменную max_area. Это помогает нам всегда помнить самую большую площадь.
python
Копировать код
        if lengths[left] < lengths[right]:
            left += 1
        else:
            right -= 1
Türkçe: Şimdi, iki çitin yüksekliğine bakıyoruz. Eğer sol çit (left) sağ çitten (right) daha kısa ise, sol çiti bir adım sağa kaydırıyoruz (left += 1). Eğer sağ çit daha kısa veya eşitse, sağ çiti bir adım sola kaydırıyoruz (right -= 1). Bu, alanı büyütebilmek için çitlerin yerini değiştirmemize yarıyor.
Rusça: Теперь мы смотрим на высоты двух заборов. Если левый забор (left) ниже, чем правый забор (right), мы сдвигаем левый указатель на одну позицию вправо (left += 1). Если правый забор ниже или равен, то сдвигаем правый указатель на одну позицию влево (right -= 1). Это позволяет нам изменить расположение заборов, чтобы найти большее пространство.

  if lengths[left] < lengths[right]:
            left += 1
        else:
            right -= 1
Türkçe: Şimdi, iki çitin yüksekliğine bakıyoruz. Eğer sol çit (left) sağ çitten (right) daha kısa ise, sol çiti bir adım sağa kaydırıyoruz (left += 1). Eğer sağ çit daha kısa veya eşitse, sağ çiti bir adım sola kaydırıyoruz (right -= 1). Bu, alanı büyütebilmek için çitlerin yerini değiştirmemize yarıyor.
Rusça: Теперь мы смотрим на высоты двух заборов. Если левый забор (left) ниже, чем правый забор (right), мы сдвигаем левый указатель на одну позицию вправо (left += 1). Если правый забор ниже или равен, то сдвигаем правый указатель на одну позицию влево (right -= 1). Это позволяет нам изменить расположение заборов, чтобы найти большее пространство.
python
Копировать код
    return max_area
Türkçe: Bu satırda, en büyük bulduğumuz alanı geri döndürüyoruz. Artık döngü bittiği için, en büyük dikdörtgenin alanını hesaplamış oluyoruz ve bu sonucu geri veriyoruz.
Rusça: В этой строке мы возвращаем максимальную найденную площадь. Цикл завершён, и мы нашли самый большой прямоугольник, так что возвращаем результат.
python
Копировать код
line = input()
Türkçe: Kullanıcıdan çitlerin yüksekliklerini bir satır olarak girmesini bekliyoruz. Örneğin: "2 4 3 2 1 4 1" gibi. Bu girdi bir dizi sayı olacak.
Rusça: Мы ожидаем, что пользователь введёт высоты заборов в одну строку. Например: "2 4 3 2 1 4 1". Это ввод будет состоять из чисел.
python
Копировать код
lengths = list(map(int, line.split()))
Türkçe: Kullanıcının verdiği satırı alıp, boşluklardan ayırarak her bir değeri tam sayıya çeviriyoruz ve bir liste haline getiriyoruz. Yani, artık elimizde çitlerin yüksekliği olan bir liste var.
Rusça: Мы берём введённую строку, разделяем её по пробелам, преобразуем каждое число в целое и помещаем в список. Теперь у нас есть список высот заборов.
python
Копировать код
print(max_area(lengths))
Türkçe: Son olarak, max_area fonksiyonunu çağırıp, bulduğu en büyük dikdörtgenin alanını ekrana yazdırıyoruz.
Rusça: Наконец, мы вызываем функцию max_area и выводим на экран максимальную найденную площадь прямоугольника.
Özet:
Bu kod, çitlerin yüksekliğini kullanarak, iki çitin arasındaki en büyük dikdörtgen alanını bulur. Sol ve sağ taraftan başlayarak çitleri karşılaştırır, kısa olanı seçer ve alanı hesaplar. Sonunda en büyük alanı bulur ve sonucu ekrana yazdırır.


 """

# Мы просим пользователя ввести высоту забора через пробел.
line = input("Пожалуйста,введите высоту забора через пробел. ")

# Мы берем значения, разделенные пробелами, преобразуем каждое из них в целое число и добавляем его в список.
fence_lengths = []
for i in line.split():
    fence_lengths.append(int(i))
# В начале слева находится в самом начале (0), а справа в конце (индекс в конце списка).
left_side = 0
right_side = len(fence_lengths) - 1

# Мы начинаем самое большое поле нулем.
max_area = 0

# Мы устанавливаем цикл, который продолжается до тех пор, пока левая и правая границы не пройдут друг друга.
while left_side < right_side:
    # Берем высоту более коротких левого и правого ограждений
    if fence_lengths[left_side] < fence_lengths[right_side]:
        heights = fence_lengths[left_side]
    else:
        heights = fence_lengths[right_side]

    # Рассчитываем ширину (расстояние между правым и левым).
    width = right_side - left_side
    # Рассчитываем площадь (высота*ширина).
    area = heights * width
    # Если это поле больше, чем самое большое поле, которое мы нашли до сих пор, мы обновляем его.
    if area > max_area:
        max_area = area
    # Продвигаем более короткий забор. Если левый забор короче, мы сдвигаем левый забор вправо.
    if fence_lengths[left_side] < fence_lengths[right_side]:
        left_side += 1
    else:
        right_side -= 1
# Печатаем наибольшую площадь на экране.
print("Самая большая площадь прямоугольника: ", max_area)


def max_area(lengths):
    left = 0
    right = len(lengths) - 1
    max_area = 0

    while left < right:
        height = min(lengths[left], lengths[right])
        width = right - left
        area = height * width
        max_area = max(max_area, area)

        if lengths[left] < lengths[right]:
            left += 1
        else:
            right -= 1

    return max_area


line = input()
lengths = list(map(int, line.split()))

print(max_area(lengths))
