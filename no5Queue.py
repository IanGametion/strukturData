# Christian 412024013 (Ini ambil referensi dari pertemuan lama)

class Queue:
    def __init__(self):
        self.array = []
    
    def isEmpty(self):
        return len(self.array) == 0
    
    def long(self):
        return len(self.array)
    
    def queFront(self):
        if self.isEmpty():
            return None
        return self.array[0]
    
    def addQue(self, data):
        print("Menambahkan", data, "ke antrian.")
        self.array.append(data)
        
    def remQue(self):
        if self.isEmpty():
            print("Tidak ada orang dalam antrian.")
            return None
        data = self.array[0]
        self.array.remove(data)
        return data
    
    def __str__(self): 
        ans = "["
        for i in range(self.long()):
            if len(ans) > 1:
                ans += ", "
            ans = ans + self.array[i]
        ans += "]"
        return ans
    
    
# Penggunaan Aplikasi dalam situasi bank antrian
antrian = Queue()
for orang in ['Christian', 'Michael', 'Davidson', 'Triemas', 'Austin', 'Ajeng', 'Nanda']:
    antrian.addQue(orang)
    
print("\nSetelah ditambahkan, totalnya", antrian.long(), "orang dalam antrian.")
print("Isi antrian: ", antrian)

# Menghapus antrian pertama dan kedua
print("\nMenghapus antrian:", antrian.remQue())
print("Isi antrian: ", antrian)
print("\nMenghapus antrian:", antrian.remQue())
print("Isi antrian: ", antrian)

# Mengecek siapa di depan antrian
print("\nOrang di depan antrian:", antrian.queFront())
print("Isi antrian: ", antrian)

# Mengecek apakah antrian kosong
print("\nApakah antrian kosong?", antrian.isEmpty())

# Christian 412024013 Pengerjaan no 5