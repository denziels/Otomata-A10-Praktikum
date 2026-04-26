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

## Screenshot


# Soal 2 - FSM

## Deskripsi

Membuat program FSM (*Finite State Machine*) yang dapat mengecek apakah sebuah input string merupakan anggota dari bahasa yang ditentukan.

### Bahasa yang diterima (L)

**L = { x ∈ (0 + 1)+ |**
- karakter terakhir pada string x adalah **1**
- dan x **tidak memiliki substring 00**  
**}**

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

### Format dan Batasan (Validasi): Input hanya diperbolehkan berupa kombinasi angka `0` dan `1` (merupakan alfabet/himpunan simbol dari bahasa L).
- Input tidak boleh dibiarkan kosong (tekan Enter tanpa teks).
- Input tidak boleh mengandung spasi, huruf (abjad), atau angka selain 0 dan 1.

### Pengguna mengetikkan string secara langsung ketika program meminta: `Masukkan string (0 atau 1) : .`
