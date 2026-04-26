# Otomata Kelompok A10 - Praktikum

| Nama Anggota | NRP |
|---------|---------|
| Putu Ardanatha Pratama   | 5025231156  | 
| Bramantya Saputra   | 5025241098   | 
| Denzel Daniels  | 5025241228   |

# Soal 1 - (nama)

## Deskripsi

## Input

## Output


# Soal 2 - FSM

## Deskripsi

Membuat program FSM (*Finite State Machine*) yang dapat mengecek apakah sebuah input string merupakan anggota dari bahasa yang ditentukan.

### Bahasa yang diterima (L)

**L = { x ∈ (0 + 1)+ |**
- karakter terakhir pada string x adalah **1**
- dan x **tidak memiliki substring 00**

### Syarat Penerimaan (Acceptance)

1. Input hanya boleh berisi karakter `0` dan `1`.
2. Karakter paling akhir harus `1`.
3. Tidak boleh ada dua angka nol yang berurutan (`00`) di dalam string.

### Analisis Diagram FSM

- **State S (Start)**  
  State awal.

- **State A**  
  State yang dicapai jika membaca `0` tunggal.  
  - Jika mendapat `1`, pindah ke **State B**  
  - Jika mendapat `0` lagi (menjadi `00`), pindah ke **State C**

- **State B (Final / Accept State)**  
  Ditandai dengan lingkaran ganda.  
  State ini dicapai setiap kali mesin membaca `1` tanpa melanggar aturan `00`.  
  Mesin harus berakhir di state ini agar string diterima.

- **State C (Trap / Dead State)**  
  Jika mesin membaca substring `00`, mesin akan masuk ke state ini dan tidak bisa keluar lagi (terperangkap).  
  Sehingga otomatis ditolak (karena bukan final state).

## Input

### Tipe Data: String (deretan karakter).

### Format dan Batasan (Validasi): 
Input hanya diperbolehkan berupa kombinasi angka `0` dan `1` (merupakan alfabet/himpunan simbol dari bahasa L)
- Input tidak boleh dibiarkan kosong (tekan Enter tanpa teks).
- Input tidak boleh mengandung spasi, huruf (abjad), atau angka selain 0 dan 1.

### Pengguna mengetikkan string secara langsung ketika program meminta: `Masukkan string (0 atau 1) : .`

## Output

### Jejak State (State Path): 
Program menampilkan urutan transisi atau perpindahan state dari awal pembacaan karakter pertama hingga karakter terakhir. Ini berfungsi sebagai bukti langkah-langkah mesin dalam mengeksekusi string sesuai diagram. (Contoh: S -> A -> B).

### State Akhir (Final Destination):
Program mencetak state terakhir tempat mesin berhenti setelah seluruh input selesai dibaca. Ini menjadi penentu utama status penerimaan.

### Kesimpulan (Status Penerimaan):

- `[ DITERIMA ]`: Ditampilkan jika mesin berhenti di State B (karena B adalah satu-satunya Accept / Final State). Artinya, string tersebut adalah anggota dari bahasa L (diakhiri '1' dan tidak memiliki '00').

- `[ DITOLAK ]`: Ditampilkan jika mesin berhenti di State S, A, atau C. Artinya, string tersebut bukan anggota bahasa L karena melanggar aturan (entah berakhiran '0' atau terperangkap di state C karena ada substring '00').

### Pesan Error (Pengecualian):
Jika pengguna memasukkan input di luar batasan (misal: "abc" atau "123"), output yang keluar adalah pesan peringatan: -> ERROR: Input tidak valid! Hanya masukkan angka 0 dan 1. dan mesin tidak akan memprosesnya.
