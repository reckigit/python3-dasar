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
def opt():
    global menuselect
    while True:
        try:
            menuselect = int(input("\nPilih Menu No. > "))
            break
        except ValueError:
            print("\nAnda belum memilih,")
            continu = input("Apakah anda masih ingin melanjutkan program ? (Y/y)\n> ")
            if (continu.upper() == 'Y'):
                opt()
            else:
                exit()

# FUNGSI CETAK MENU UTAMA DI LAYAR
def mainmenu():
    for Key in MainMenu:
        for Menu in MainMenu[Key]:
            print(f"{Key}. {Menu}")
    opt()
    global menu1selected
    menu1selected = menuselect
    gosubmenu()
    
# FUNGSI CETAK SUBMENU DI LAYAR
def gosubmenu():
    os.system('clear')
    try:
        for Menu in MainMenu[menuselect]:
            print(f"{Menu}, terdapat pilihan :")
            for SubMenu in MainMenu[menuselect][Menu]:
                print(f"{SubMenu}. {MainMenu[menuselect][Menu][SubMenu]}")
        opt()
        global menu
        menu = Menu
        reading()
    except KeyError:
        begin()
    
def reading():
    os.system('clear')
    container = menu.lower().replace(" ","-")
    # ignore•me -- print(container,menu1selected,menu,menuselect)
    try:
        filereading = f"{(MainMenu[menu1selected][menu][menuselect]).lower()}.py"
        print(f"Sedang membaca file : '{filereading}'")
        print('•'*48)
        os.system(f"cat {container}/{filereading}")
        print('•'*48)
        dorunning = input("\nIngin menjalankan skrip tersebut ? (Y/y)\n> ")
        if (dorunning.upper() == 'Y'):
            running()
        else:
            pass
    except KeyError:
        begin()

def running():
    container = menu.lower().replace(" ","-")
    # ignore•me -- print(container,menu1selected,menu,menuselect)
    try:
        filereading = f"{(MainMenu[menu1selected][menu][menuselect]).lower()}.py"
        print(f"\nBerikut hasil menjalankan '{filereading}'")
        print('•'*48)
        os.system(f"python3 {container}/{filereading}")
        print('•'*48)
    except KeyError:
        begin()    

# FUNGSI MULAI PROGRAM
def begin():
    os.system('clear')
    head()
    mainmenu()

# JALANKAN FUNGSI begin()
begin()
