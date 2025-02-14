cnc_kod = """
T0101 M6\n G54\n G96 S200 M3\n G50 S2000\n G0 X81 Z-2 M8\n G1 X-1.6   F0.2\n G00  Z2\n G00    X70\n G01   Z-80\n
G00  X72  Z2\n X60\n G01  Z-70\n G00  X62  Z2\n X52\n G01 Z-51\n G00 X54 Z2\n X40\n G01 Z-40\n G00 X42 Z2\n X0 Z0\n
G03 X26 Z-13 R13\n G01 X40 Z-20\n Z-40\n G03 X52 Z-46 R6\n G1 Z-51\n X60 Z-55\n Z-70/n G00 X62 Z2\n X100 Z100 M9\n T0202 M6\n
G00 X0 Z0 M8\n G03 X26 Z-13 R13\n G1 X40 Z-20\n Z-40\n G03 X52 Z-46 R6\n G1 Z-51\n X60 Z-55\n Z-70\n X70\n Z-80\n G00 X72 Z2 M9\n
X100 Z100\n M5\n M30\n
"""
#with open("C:/Users/anyag/python uygulamaları/Самостоятельная работа 5.txt", "w") as dosya:
            #dosya.write(cnc_kod)
with open("C:/Users/anyag/python uygulamaları/Сам.раб Задание 1.pdf", "a") as dosya:
            dosya.write(cnc_kod)
print(dosya)
