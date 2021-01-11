import os

os.system('clear')

try:
    jawab = int(input("Cetak : "))
    print(jawab)
except ValueError:
    jawab = input("Apakah anda ingin keluar : ")
    if (jawab.upper() == 'Y'):
        exit()
