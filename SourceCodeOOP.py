# Contoh kode program OOP pada python
# Membuat kelas Mahasiswa dan menggunakan metode untuk menampilkan nama dan jurusan
class Mahasiswa:
  def __init__(self, nama, jurusan):
    self.nama = nama
    self.jurusan = jurusan
  
  def tampilkan_nama(self):
    print("Nama:", self.nama)
    
  def tampilkan_jurusan(self):
    print("Jurusan:", self.jurusan)

# Membuat objek mahasiswa1 dan mahasiswa2
mahasiswa1 = Mahasiswa("Atika Oktavinti", "Sistem Informasi")
mahasiswa2 = Mahasiswa("Atika Oktavianti", "Informatika")

# Memanggil metode untuk menampilkan nama dan jurusan
mahasiswa1.tampilkan_nama() # Output: Nama: Atika Oktavianti
mahasiswa2.tampilkan_jurusan() # Output: Jurusan: Informatika
