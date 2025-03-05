import math

# Fungsi untuk menghitung jarak Euclidean antara dua titik
def jarak_euclidean(titik1, titik2):
    return math.sqrt((titik1[0] - titik2[0])**2 + (titik1[1] - titik2[1])**2)

# Algoritma Brute Force untuk kasus dengan sedikit titik
def pasangan_terdekat_brute_force(titik):
    jarak_minimum = float("inf")
    jumlah_titik = len(titik)
    
    for i in range(jumlah_titik):
        for j in range(i + 1, jumlah_titik):
            jarak = jarak_euclidean(titik[i], titik[j])
            jarak_minimum = min(jarak_minimum, jarak)
    
    return jarak_minimum

# Fungsi utama Divide and Conquer untuk menemukan pasangan terdekat
def pasangan_terdekat_rekursif(titik_urut_x, titik_urut_y):
    jumlah_titik = len(titik_urut_x)
    
    # Basis kasus: jika jumlah titik kecil, gunakan brute-force
    if jumlah_titik <= 3:
        return pasangan_terdekat_brute_force(titik_urut_x)
    
    # Bagi titik menjadi dua bagian
    tengah = jumlah_titik // 2
    kiri_x = titik_urut_x[:tengah]
    kanan_x = titik_urut_x[tengah:]
    
    titik_tengah = titik_urut_x[tengah][0]

    kiri_y = list(filter(lambda t: t[0] <= titik_tengah, titik_urut_y))
    kanan_y = list(filter(lambda t: t[0] > titik_tengah, titik_urut_y))
    
    # Rekursif ke dua bagian
    jarak_kiri = pasangan_terdekat_rekursif(kiri_x, kiri_y)
    jarak_kanan = pasangan_terdekat_rekursif(kanan_x, kanan_y)
    jarak_minimum = min(jarak_kiri, jarak_kanan)

    # Cari pasangan titik yang melewati garis tengah dalam strip selebar 2 * jarak_minimum
    strip = [t for t in titik_urut_y if abs(t[0] - titik_tengah) < jarak_minimum]
    
    # Periksa titik dalam strip (hanya hingga 6 titik berikutnya)
    jarak_strip_minimum = jarak_minimum
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):  # Hanya periksa hingga 6 titik setelahnya
            jarak = jarak_euclidean(strip[i], strip[j])
            jarak_strip_minimum = min(jarak_strip_minimum, jarak)
    
    return jarak_strip_minimum

# Fungsi utama untuk menjalankan algoritma
def pasangan_terdekat(titik):
    titik_urut_x = sorted(titik, key=lambda t: t[0])  # Urutkan berdasarkan x
    titik_urut_y = sorted(titik, key=lambda t: t[1])  # Urutkan berdasarkan y
    return pasangan_terdekat_rekursif(titik_urut_x, titik_urut_y)

# Contoh penggunaan
titik = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print("Jarak pasangan terdekat:", pasangan_terdekat(titik))