import os
import sys

# CETAK KETERANGAN BELUM SIAP DI LAYAR
os.system('clear')
print("Maaf, Ini masih dalam PENGERJAAN")
# exit()

# SEJUMLAH DICTIONARY
MainMenu = {1:{'Variable Types':{1:'Numbers',2:'String',3:'List',4:'Tuple',5:'Dictionary'}},
2:{'Conditions':{1:'IF'}}}

# FUNGSI CETAK BAGIAN KEPALA DI LAYAR
def head():
    print("Halo Teman ! (Python3)")
    print("="*22)

# FUNGSI INPUT PROMPT MENU
def promp():
    global menuselect
    try:
        menuselect = int(input("\nPilih Menu No. > "))
    except ValueError:
        print("\nAnda belum memilih,")
        continu = input("Apakah anda masih ingin melanjutkan program ? (Y/y)\n> ")
        if (continu.upper() == 'Y'):
            promp()
        else:
            exit()

# FUNGSI CETAK MENU UTAMA DI LAYAR
def mainmenu():
    for Key in MainMenu:
        for Menu in MainMenu[Key]:
            print(f"{Key}. {Menu}")
    promp()
    gosubmenu()
    
# FUNGSI CETAK SUBMENU DI LAYAR
def gosubmenu():
    os.system('clear')
    for Menu in MainMenu[menuselect]:
        print(f"{Menu}, terdapat pilihan :")
        for SubMenu in MainMenu[menuselect][Menu]:
            print(f"{SubMenu}. {MainMenu[menuselect][Menu][SubMenu]}")
    promp()
    global menu,selected
    menu = Menu
    selected = menuselect
    reading()
    
def reading():
    os.system('clear')
    container = (MainMenu[selected]).lower()).strip(" ","-")
    filereading = f"{(MainMenu[selected][menu][menuselect]).lower()}.py"
    print(filereading)
    print('•'*48)
    os.system(f"cat {container}/{filereading}")
    print('•'*48)

# FUNGSI MULAI PROGRAM
def begin():
    os.system('clear')
    head()
    mainmenu()

# JALANKAN FUNGSI begin()
begin()
