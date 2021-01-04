import os
import sys

def mainmenu():
    # CETAK KE LAYAR
    print("Halo Teman !")
    print("="*12)
    print("{001} Numbers")

def menupromp():
    # CETAK DAN MENERIMA INPUT MENU PILIHAN DI LAYAR
    global menuselect
    menuselect = input("\nBaca bagian/> ")
    domenupromp()

def restartpromp():
    # CETAK DAN MENERIMA INPUT KEMBALI KE MENU DI LAYAR
    global backto
    backto = input("\nKembali ke Menu (Apapun => ENTER), Keluar dari Program (Q)\n>")
    dorestartpromp()

def domenupromp():
    # BACALAH FILE PYTHON BERDASARKAN PILIHAN
    os.system('clear')
    try:
        if int(menuselect) == 1:
            print("tipe2-variabel/numbers.py")
            print('•'*48)
            os.system('cat tipe2-variabel/numbers.py')
            print('•'*48)
    except ValueError:
        print("Pilihan tidak ada")
    restartpromp()

def dorestartpromp():
    # MELAKUKAN PILIHAN MULAI LAGI ATAU BERHENTI
    if (backto.upper() == 'Q'):
        exit()
    else:
        begin()

def begin():
    # BERSIHKAN LAYAR
    os.system('clear')
    mainmenu()
    menupromp()

begin()
