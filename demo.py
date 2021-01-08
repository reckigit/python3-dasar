import os

MainMenu = {1:{'Variable Types':{1:'Numbers',2:'String',3:'List',4:'Tuple',5:'Dictionary'}},2:{'Conditions':{1:'IF ELSE'}}}

os.system('clear')
for Key in MainMenu:
	for Menu in MainMenu[Key]:
		print(f"{Key}. {Menu}")
		for SubMenu in MainMenu[Key][Menu]:
			print(f"{SubMenu}. {MainMenu[Key][Menu][SubMenu]}")

print("\n" *2)
pilihan = int(input("Pilih> "))

for SubMenu in MainMenu[pilihan][Menu]:
	print(f"{SubMenu}. {MainMenu[pilihan][SubMenu]}")
