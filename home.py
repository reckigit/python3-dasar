import os
import sys

# CETAK KETERANGAN BELUM SIAP DI LAYAR
os.system('clear')
print("Maaf, Ini masih dalam PENGERJAAN")
# exit()

# SEJUMLAH DICTIONARY
MainMenu = {1:{'Variable Types':{1:'Numbers',2:'String',3:'List',4:'Tuple',5:'Dictionary'}},
2:{'Conditions':{1:'IF'}}}
ActOnFile = {1:'Baca',2:'Jalankan'}

# FUNGSI CETAK BAGIAN KEPALA DI LAYAR
def head():
    print("Halo Teman ! (Python3)")
    print("="*22)

# FUNGSI CETAK MENU UTAMA DI LAYAR
def mainmenu():
    for Key in MainMenu:
        for Menu in MainMenu[Key]:
            print(f"{Key}. {Menu}")

# FUNGSI INPUT PROMPT OPSI MENU
def mainmenupromp():
    # CETAK DAN MENERIMA INPUT MENU PILIHAN DI LAYAR
    global menuselect
    menuselect = int(input("\nPilih Menu No. > "))
    domainmenupromp()

# FUNGSI JALANKAN MENU PILIHAN DENGAN KONDISI BERIKUT
def domainmenupromp():
    os.system('clear')
    try:
    except ValueError:
        print("Pilihan tidak ada")
    print("SUKSES")
    # dosubmenupromp()
    mainpromp()
    
# FUNGSI JALANKAN SUBMENU PILIHAN DENGAN KONDISI BERIKUT
def dosubmenupromp():
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

# FUNGSI INPUT PROMPT KEMBALI KE MENU UTAMA ATAU KELUAR
def mainpromp():
    # CETAK DAN MENERIMA INPUT KEMBALI KE MENU DI LAYAR
    global backto
    backto = input("\nKembali ke Menu (Apapun => ENTER), Keluar dari Program (Q)\n>")
    dorestartpromp()

# FUNGSI JALANKAN PILIHAN KEMBALI KE MENU UTAMA ATAU KELUAR
def domainpromp():
    # MELAKUKAN PILIHAN MULAI LAGI ATAU BERHENTI
    if (backto.upper() == 'Q'):
        exit()
    else:
        begin()

# FUNGSI MULAI PROGRAM
def begin():
    os.system('clear')
    head()
    mainmenu()
    mainmenupromp()

# JALANKAN FUNGSI begin()
begin()
