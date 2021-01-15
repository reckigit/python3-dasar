'''
Dictionary diapit oleh tanda kurung kurawal ({}) 
dan nilai bisa ditetapkan 
dan diakses menggunakan tanda kurung siku ([])
'''
itsnum = {}
itsnum['satu'] = 'Ini adalah 1'
itsnum[2] = 'Ini adalah 2'
itsme = {'myname':'Recki','myjob':'coding','myhobby':'menulis'}
print(itsnum)               # CETAK LENGKAP DICTIONARY itsnum DI LAYAR DI LAYAR
print(itsnum['satu'])       # CETAK DICTIONARY itsnum MENGGUNAKAN KEY satu DI LAYAR
print(itsnum[2])            # CETAK DICTIONARY itsnum MENGGUNAKAN KEY 2 DI LAYAR
print(itsme)                # CETAK LENGKAP DICTIONARY itsme DI LAYAR
print(itsme['myname'])      # CETAK DICTIONARY itsme MENGGUNAKAN KEY myname DI LAYAR
print(itsme['myjob'])       # CETAK DICTIONARY itsme MENGGUNAKAN KEY myjob DI LAYAR
print(itsme['myhobby'])     # CETAK DICTIONARY itsme MENGGUNAKAN KEY myhobby DI LAYAR
print(itsme.keys())         # CETAK KEYS DICTIONARY DI LAYAR
print(itsme.values())       # CETAK VALUES DICTIONARY DI LAYAR
