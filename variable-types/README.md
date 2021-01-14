# variable-types

**Variabel** hanyalah lokasi memori yang dicadangkan untuk menyimpan nilai. 
Artinya, saat Anda membuat **variabel**, 
Anda menyediakan beberapa ruang di memori.

Berdasarkan **tipe data** variabel, 
interpreter mengalokasikan memori dan memutuskan apa yang dapat disimpan dalam memori yang dipesan.
Oleh karena itu, 
dengan menetapkan **tipe data** yang berbeda ke **variabel**, 
Anda dapat menyimpan bilangan bulat, 
desimal atau karakter dalam **variabel** ini.


## Assigning Values to Variables

Variabel Python *tidak membutuhkan deklarasi eksplisit* untuk memesan ruang memori. 
Deklarasi terjadi secara otomatis saat Anda **menetapkan nilai ke variabel**. 
Tanda sama dengan (=) digunakan untuk **menetapkan nilai ke variabel**.


## Multiple Assignment

Python memungkinkan Anda untuk *menetapkan satu nilai* 
ke **beberapa variabel secara bersamaan**.


## Standard Data Types

Jenis data yang disimpan dalam memori dapat bermacam-macam. 
Misalnya, usia seseorang disimpan sebagai nilai numerik 
dan alamatnya disimpan sebagai karakter alfanumerik.

Python memiliki berbagai **tipe data standar** 
yang digunakan untuk menentukan kemungkinan operasi pada mereka 
dan metode penyimpanan untuk masing-masingnya.

Python memiliki lima Standard Data Types : 
1. Number
2. String
3. List
4. Tuple
5. Dictionary


### Python Numbers

Python mendukung tiga Tipe Numerik yang berbeda :
1. int (signed integers)
2. float (floating point real values)
3. complex (complex numbers)

Semua **bilangan bulat** di Python3 direpresentasikan 
sebagai *long integers*. 
Oleh karena itu, *tidak ada tipe separate number sebagai long*.

***Tabel beberapa contoh angka, berikut :***

<img src="img/tabel-beberapa-contoh-angka.png" width="300"/>

**Bilangan kompleks** terdiri dari pasangan terurut *bilangan* titik-mengambang nyata 
yang dilambangkan dengan *x + yj*, 
di mana *x* dan *y* adalah ***bilangan real*** 
dan *j* adalah **unit imajiner**.


### Python Strings

**String** dalam Python diidentifikasi sebagai *sekumpulan karakter* 
yang berdekatan yang direpresentasikan dalam tanda kutip. 
Python mengizinkan pasangan *tanda kutip tunggal* atau *ganda*. 
Himpunan bagian dari **string** dapat diambil menggunakan *operator slice ([] dan [:])* 
dengan *indeks yang dimulai dari 0 di awal* **string** 
dan *bekerja dari -1 hingga akhir*.


### Python Lists

**List** adalah *tipe data* gabungan Python yang paling serbaguna. 
Sebuah **list** berisi *item yang dipisahkan dengan koma* 
dan *diapit oleh tanda kurung siku ([])*.
> Untuk beberapa hal, **list** mirip dengan *array di C*. 
> Salah satu perbedaan di antara mereka adalah 
> bahwa semua item yang termasuk dalam list 
> bisa dari tipe data yang berbeda.

Nilai yang disimpan dalam **list** dapat diakses menggunakan *operator slice ([] dan [:])* 
dengan *indeks yang dimulai dari 0 di awal* **list** dan *bekerja hingga akhir -1*.


### Python Tuples

**Tuple** adalah *tipe data* urutan lain yang mirip dengan *list*. 
*Tupel* terdiri dari *sejumlah nilai yang dipisahkan dengan koma*. 

> Perbedaan utama antara **list** dan *tuple* adalah 
> *List* diapit oleh tanda kurung ([]) dan elemen 
> serta ukurannya dapat diubah, 
> sedangkan **tupel** diapit dalam tanda kurung (()) 
> dan tidak dapat diperbarui
