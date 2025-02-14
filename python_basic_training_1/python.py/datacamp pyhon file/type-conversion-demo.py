'''
   Daire alani     :  πr²
   Daire Cevresi : 2πr
   * Yari capi verilen bir dairenin alan ve cevresini hesaplayiniz. (r: 3.14)

'''

pi = 3.14
r = float( input('yaricap:'))

alan = pi * (r ** 2)

cevresi = 2 * pi * r

print(type(alan))
print(type(cevresi))

print('alan : ' + str(alan) + ' ' + 'cevresi : ' +   str(cevresi))
