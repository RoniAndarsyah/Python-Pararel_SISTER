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
