class Karyawan:
   def __init__(self, nama, gaji):
      self.nama = nama
      self.gaji = gaji
   
   def displayKaryawan(self):
      print ("nama : ", self.nama,  ", gaji: ", self.gaji)

emp1 = Karyawan("Udin Wazowski", 2000)
emp2 = Karyawan("Astoria Greengrass", 5000)

emp1.displayKaryawan()
emp2.displayKaryawan()

emp1 = Karyawan("Koro koro", 8000)
emp2 = Karyawan("Kucu kucu", 5000)

emp1.displayKaryawan()
emp2.displayKaryawan()

class Posisi(Karyawan):
   def __init__(self, nama, posisi, gaji):
       self.nama = nama
       self.posisi = posisi
       self.gaji = gaji
   
   def display(self):
      print("Nama : ", self.nama, ", posisi : ", self.posisi, ", gaji : ", self.gaji)

emp1 = Posisi("TTesting", 'Software Engineer', 4000)
emp2 = Posisi("Astoria", 'HRD', 5000)

emp1.display()
emp2.display()
