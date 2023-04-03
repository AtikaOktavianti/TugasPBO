# Contoh kode program Functional programming (FP) pada python:
# Fungsi untuk menghitung jumlah angka dalam sebuah list menggunakan map dan reduce

from functools import reduce
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, map(lambda x: 1, numbers))

print(total) # Output: 5
