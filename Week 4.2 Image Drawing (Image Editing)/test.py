import cv2 as cv

# 1. Membaca gambar asli
gambar = cv.imread('image.png')

# Pengecekan keamanan (seperti pelajaran sebelumnya)
if gambar is None:
    print("Error: File 'foto.jpg' tidak ditemukan! Pastikan foldernya benar.")
    exit() # Hentikan program

# --- 2. [MATERI PENTING] Mengambil Ukuran Gambar ---
# .shape mengembalikan 3 nilai: (Tinggi, Lebar, SaluranWarna)
# SaluranWarna biasanya 3 (BGR). Kita abaikan dengan underscore (_).
tinggi, lebar, _ = gambar.shape

print(f"Info Gambar: Lebar = {lebar} piksel, Tinggi = {tinggi} piksel")


# --- 3. MULAI MENGGAMBAR DI ATAS FOTO ---

# A. Membuat Bingkai Tipis di sekeliling pinggir foto (Biru Laut)
# Titik awal (0,0), titik akhir (lebar, tinggi)
cv.rectangle(gambar, (0, 0), (lebar, tinggi), (255, 255, 0), 5)


# B. Membuat "Kotak Label" solid di bagian bawah foto untuk alas teks
# Kita ingin kotak ini tingginya 50 piksel dari bawah.
bar_height = 50
p1_kotak = (0, tinggi - bar_height) # Pojok kiri atas kotak
p2_kotak = (lebar, tinggi)          # Pojok kanan bawah kotak
cv.rectangle(gambar, p1_kotak, p2_kotak, (0, 0, 0), -1) # Hitam solid (-1)


# C. Menambahkan Teks Judul di atas kotak label hitam tadi
teks = "STUDI KASUS: ANNOTASI GAMBAR STATIC"
font = cv.FONT_HERSHEY_SIMPLEX
skala_font = 0.7
warna_teks = (255, 255, 255) # Putih
ketebalan = 2

# Mengatur posisi teks sedikit ke kanan dan ke atas agar pas di tengah kotak hitam
# Koordinat teks adalah pojok kiri bawah huruf pertama.
posisi_teks = (15, tinggi - 15)

cv.putText(gambar, teks, posisi_teks, font, skala_font, warna_teks, ketebalan)


# --- 4. MENYIMPAN HASILNYA ---
# Selain menampilkan, kita juga bisa menyimpan gambar yang sudah dicoret
# menjadi file baru.
nama_file_baru = 'foto_berlabel.jpg'
cv.imwrite(nama_file_baru, gambar)
print(f"Hasil berhasil disimpan dengan nama: {nama_file_baru}")


# --- 5. TAMPILKAN HASILNYA DI LAYAR ---
cv.imshow("Hasil Annotasi Foto Statis", gambar)
cv.waitKey(0)
cv.destroyAllWindows()