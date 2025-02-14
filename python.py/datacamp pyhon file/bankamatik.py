#Bankamatik Uygulamasi



AnnaHesap = {
    'ad':'Anna Bichen',
    'hesapNo': '1234567',
    'bakiye': 3000,
    'ekHesap': 2000
}


    


MehmetHesap = {
    'ad':'Mehmet Bichen',
    'hesapNo': '1234567',
    'bakiye': 2000,
    'ekHesap': 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print('paranizi alabilirsiniz.')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanimi = input('ek hesap kullanilsin mi?(evet/hayir)')
            if ekHesapKullanimi == 'evet':
               
                ekhesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekhesapKullanilacakMiktar
                

                print('paranizi alabilirsiniz.')
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} TL bulunmaktadir.")
        else:
            print('uzgunuz bakiye yetersiz')
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} TL bulunmaktadir. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadir.")

          

paraCek(AnnaHesap, 3000)

print('***********')
paraCek(AnnaHesap, 2000)

nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
nums = filter(lambda x: x > 1, nums)
print(len(list(nums)))

def power(x, y):
  if y == 0:
    return 1
  else:
    return x * power(x, y-1)
		
print(power(2, 3))

def func(**kwargs):
  print(kwargs["zero"])

func(a = 0, zero = 8)
with open("/usercode/files/books.txt") as f:
   #your code goes here
   j = 1
   for line in f:
      print( "Line " +str(j) +": "+str(len(line.split(" ")))+" words ")
      j+=1
