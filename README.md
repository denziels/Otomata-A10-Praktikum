# Otomata Kelompok A10 - Praktikum

| Nama Anggota | NRP |
|---------|---------|
| Putu Ardanatha Pratama   | 5025231156  | 
| Bramantya Saputra   | 5025241098   | 
| Denzel Daniels  | 5025241228   |

# Soal 1 - FSA Multi-Language Scanner / Lexical Analyzer 

<img width="967" height="654" alt="image" src="https://github.com/user-attachments/assets/203a2ef2-4ec7-4e35-a5e4-e8717fc90e9d" />

## Deskripsi
Multi-Language Scanner / Lexical Analyzer adalah sebuah perangkat lunak berbasis web yang berfungsi untuk melakukan analisis leksikal (lexing) terhadap source code C, C++, dan Python. Program ini implementasi dari konsep Finite State Automata (FSA) dalam teori otomata, setiap karakter dalam kode input dibaca dan dikelompokkan ke dalam kategori token yang sesuai berdasarkan aturan sintaksis masing-masing bahasa.
## Input
### Mekanisme Input
Program menerima input berupa teks mentah (raw string) yang dimasukkan pengguna melalui area teks di antarmuka web.

*Komponen input:*
1. *Selection (Dropdown):* Pengguna memilih target bahasa pemrograman (C, C++, atau Python). Pilihan ini akan menentukan tabel transisi/aturan yang digunakan oleh mesin scanner.
2. *Code Area (Textarea):* Pengguna menempelkan atau mengetikkan kode sumber yang ingin dianalisis.
3. *Action Trigger:* Tombol "Proses Token" yang memicu fungsi JavaScript untuk mulai memindai teks dari indeks 0 hingga akhir karakter.

### Contoh Input:
#include <iostream>
int main() {
    int angka = 10;
    return 0;
}

## Output
Output adalah berupa visualisasi kartu kategori yang memisahkan setiap token yang ditemukan secara unik (distinct).

*Kategori Output:*
- Reserve Words: Menampilkan kata kunci yang telah dipesan oleh bahasa (misal: if, while, def, int).
- Preprocessor: (Khusus C/C++) Menampilkan direktif seperti #include atau #define.
- Simbol & Tanda Baca: Menampilkan operator aritmatika, logika, serta tanda baca seperti kurung, koma, dan titik koma.
- Variabel: Menampilkan nama identifier yang ditentukan oleh pengguna.
- Ekspresi Matematika/Literal: Menampilkan nilai numerik (integer maupun float).
- String/Header: Menampilkan teks di dalam tanda kutip atau nama pustaka di dalam < >.
- Error Log: Menampilkan pesan peringatan jika ditemukan karakter ilegal yang tidak dikenali oleh alfabet bahasa yang dipilih.

### Contoh Output:
- Preprocessor: #include
- String/Header: <iostream>
- Reserve Words: int, return, main
- Variabel: angka
- Simbol & Tanda Baca: =, ;, {, }, (, )
- Ekspresi Matematika: 10, 0

# Soal 2 - FSM

<img width="716" height="536" alt="Screenshot 2026-04-26 at 18 15 24" src="https://github.com/user-attachments/assets/200ec61c-9d06-4282-acf3-46d96a7a5a3f" />

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

### Tipe Data: 
String (deretan karakter)

### Format dan Batasan (Validasi): 
Input hanya diperbolehkan berupa kombinasi angka `0` dan `1` (merupakan alfabet/himpunan simbol dari bahasa L)
- Input tidak boleh dibiarkan kosong (tekan Enter tanpa teks).
- Input tidak boleh mengandung spasi, huruf (abjad), atau angka selain 0 dan 1.

### Pengguna mengetikkan string secara langsung ketika program meminta: 
`Masukkan string (0 atau 1) :`

## Output

### Jejak State (State Path): 
Program menampilkan urutan transisi atau perpindahan state dari awal pembacaan karakter pertama hingga karakter terakhir. Ini berfungsi sebagai bukti langkah-langkah mesin dalam mengeksekusi string sesuai diagram. (Contoh: S -> A -> B).

### State Akhir (Final Destination):
Program mencetak state terakhir tempat mesin berhenti setelah seluruh input selesai dibaca. Ini menjadi penentu utama status penerimaan.

### Kesimpulan (Status Penerimaan):

- `[ DITERIMA ]`: Ditampilkan jika mesin berhenti di State B (karena B adalah satu-satunya Accept / Final State). Artinya, string tersebut adalah anggota dari bahasa L (diakhiri '1' dan tidak memiliki '00').

- `[ DITOLAK ]`: Ditampilkan jika mesin berhenti di State S, A, atau C. Artinya, string tersebut bukan anggota bahasa L karena melanggar aturan (entah berakhiran '0' atau terperangkap di state C karena ada substring '00').

### Pesan Error (Pengecualian):
Jika pengguna memasukkan input di luar batasan (misal: "`abc`" atau "`123`"), output yang keluar adalah pesan peringatan: -> `ERROR: Input tidak valid! Hanya masukkan angka 0 dan 1.` dan mesin tidak akan memprosesnya.

## Contoh Pengujian FSM

| Input String | Jejak State (Path)     | State Akhir | Output (Kesimpulan) | Alasan Berdasarkan Logika FSM |
|--------------|------------------------|-------------|---------------------|--------------------------------|
| 101          | S -> B -> A -> B       | B           | DITERIMA            | Berakhir 1 dan tidak ada angka 0 berurutan. Berhenti di Final State B. |
| 1001         | S -> B -> A -> C -> C  | C           | DITOLAK             | Terdapat substring 00 yang membuat mesin terperangkap di Dead State C. |
| 10           | S -> A -> B -> A       | A           | DITOLAK             | Meskipun tidak ada 00, namun string berakhir 0, sehingga mesin berhenti di State A (bukan Final State). |
| abc          | (Tidak ada jejak)      | -           | ERROR               | String mengandung karakter selain 0 dan 1, ditolak oleh sistem validasi. |
