def buat_matriks(baris, kolom, nama):
    print(f"\nMasukkan elemen matriks {nama}:")
    matriks = []
    for i in range(baris):
        baris_matriks = []
        for j in range(kolom):
            elemen = float(input(f"{nama}[{i+1}][{j+1}]: "))
            baris_matriks.append(elemen)
        matriks.append(baris_matriks)
    return matriks

def cetak_matriks(matriks, nama):
    print(f"\nMatriks {nama}:")
    for baris in matriks:
        print("|", end=" ")
        for elemen in baris:
            print(f"{elemen:5.1f}", end=" ")
        print("|")

def kali_matriks(A, B):
    baris_A = len(A)
    kolom_A = len(A[0])
    baris_B = len(B)
    kolom_B = len(B[0])
    
    if kolom_A != baris_B:
        print("\nError: Jumlah kolom matriks A tidak sama dengan jumlah baris matriks B")
        print(f"Kolom A: {kolom_A}, Baris B: {baris_B}")
        return None
    
    # Inisialisasi matriks hasil dengan nol
    hasil = [[0 for _ in range(kolom_B)] for _ in range(baris_A)]
    
    # Proses perkalian matriks
    for i in range(baris_A):
        for j in range(kolom_B):
            for k in range(kolom_A):
                hasil[i][j] += A[i][k] * B[k][j]
    
    return hasil

def transpose_matriks(matriks):
    return [list(baris) for baris in zip(*matriks)]

# Program utama
print("PROGRAM PERKALIAN MATRIKS")
print("-------------------------")

# Input matriks A
baris_A = int(input("\nMasukkan jumlah baris matriks A: "))
kolom_A = int(input("Masukkan jumlah kolom matriks A: "))
A = buat_matriks(baris_A, kolom_A, "A")

# Input matriks B
baris_B = int(input("\nMasukkan jumlah baris matriks B: "))
kolom_B = int(input("Masukkan jumlah kolom matriks B: "))
B = buat_matriks(baris_B, kolom_B, "B")

# Cetak matriks input
cetak_matriks(A, "A")
cetak_matriks(B, "B")

# Perkalian matriks
C = kali_matriks(A, B)
if C:
    cetak_matriks(C, "Hasil (A x B)")

# Transpose matriks
print("\nTranspose Matriks:")
At = transpose_matriks(A)
cetak_matriks(At, "A Transpose")

Bt = transpose_matriks(B)
cetak_matriks(Bt, "B Transpose")

if C:
    Ct = transpose_matriks(C)
    cetak_matriks(Ct, "Hasil Transpose")