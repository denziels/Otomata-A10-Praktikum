# Penjelasan Kode **FSA.html** (Multi‑Language Lexical Analyzer)

---

## 🎯 Tujuan Umum
File **FSA.html** merupakan aplikasi web mandiri yang dapat melakukan **analisis leksikal** (tokenisasi) pada tiga bahasa pemrograman:
- **C++** (ISO Standard)
- **C** (ANSI C)
- **Python 3.x**

Pengguna cukup menempelkan kode sumber, memilih bahasa yang diinginkan, lalu menekan tombol **Proses Token**. Hasil token akan ditampilkan secara terstruktur pada halaman.

---

## ✨ Fitur Utama
| Fitur | Deskripsi |
|---|---|
| **Pemilihan bahasa** | Dropdown dengan tiga pilihan (C++, C, Python). |
| **Deteksi karakter ilegal** | Jika ada karakter yang tidak dikenali, ditampilkan pada bagian *error‑log* dengan posisi indeks. |

---

## 🖥️ Struktur File
```
FSA.html
├─ <head>
│   ├─ <meta charset="UTF-8">
│   ├─ <title>Multi‑Language Lexical Analyzer</title>
│   └─ <style>…</style>
├─ <body>
│   └─ <div class="container">
│       ├─ <h2>Multi-Language Scanner / Lexical Analyzer</h2>
│       ├─ <div class="controls">
│       │   ├─ <label>Pilih Bahasa Pemrograman:</label>
│       │   ├─ <select id="langSelect">…</select>
│       │   └─ <button onclick="analyzeCode()">Proses Token</button>
│       ├─ <textarea id="codeInput"></textarea>
│       ├─ <div id="errorLog" class="error‑log"></div>
│       └─ <div id="resultDisplay" class="results"></div>
│   </div>
└─ <script>…</script>
```

---

## 🧩 Penjelasan Bagian‑Bagian Kode
### 1. CSS (Bagian `<style>`)
- **Desain bersih**: `font-family: 'Segoe UI', sans-serif;` dan warna latar `#eceff1` (abu‑abu muda) memberikan kesan profesional.
- **Container**: lebar maksimum `1000px`, padding `30px`, radius `12px`, shadow ringan.
- **Controls**: Flexbox untuk menata label, dropdown, dan tombol.
- **Tag token**: `.tag` menampilkan token dalam kotak biru muda dengan border tipis, memudahkan visualisasi.
- **Error log**: `.error‑log` berwarna merah gelap untuk menonjolkan kesalahan.

### 2. JavaScript (Bagian `<script>`)
#### a. `languageRules`
Objek berisi **aturan regex** untuk masing‑masing bahasa:
```js
cpp: { reserved: /.../, math: /.../, operators: /.../ }
c:   { reserved: /.../, math: /.../, operators: /.../ }
python:{ reserved: /.../, math: /.../, operators: /.../ }
```
- **`reserved`** – kata kunci bahasa.
- **`math`** – literal numerik (integer, floating, eksponen, suffix).
- **`operators`** – operator spesifik bahasa (<<, >>, ::, ->, &&, ||, dsb.).

#### b. `analyzeCode()`
1. **Ambil kode** dari textarea & bahasa yang dipilih.
2. **Bersihkan UI** (`resultDisplay`, `errorLog`).
3. **Susun pola token** (`patterns`) dengan urutan penting: preprocessor → string/header → kata kunci → angka → operator → simbol lainnya → variabel → skip → mismatch.
4. **Loop manual** pada string kode (`while (pos < code.length)`) untuk meng‑match regex satu‑per‑satu. Ini penting agar **`MISMATCH`** dapat dideteksi secara akurat.
5. **Simpan token** ke dalam `results` yang berupa `Set` (menghindari duplikasi). Token yang tidak termasuk kategori standar masuk ke *error log*.
6. **Render hasil**: tiap kategori menjadi `.category-box` dengan token‑token dibungkus elemen `.tag`. Jika tidak ada token, ditampilkan `-`.
7. **Escape HTML** – fungsi `escapeHtml()` mencegah token mengacaukan markup.

#### c. `escapeHtml(text)`
Membuat `div.textContent = text` lalu mengembalikan `div.innerHTML` untuk meng‑escape karakter khusus (mis. `<`, `>`).

---

## 📋 Cara Pakai
1. Buka **FSA.html** di browser (mis. `http://localhost:8080/FSA.html`).
2. Pilih bahasa pada dropdown **Pilih Bahasa Pemrograman**.
3. Tempelkan atau ketik kode sumber pada area teks.
4. Tekan **Proses Token**.
5. Hasil token muncul di bagian bawah dalam kotak‑kotak berwarna biru muda.
6. Jika ada karakter yang tidak dikenali, pesan error akan muncul di bawah textarea.


## Notes
- **Regex bersifat case‑sensitive** pada kata kunci; bahasa yang dipilih sudah meng‑cover huruf kecil/kapital umum.
- **`SKIP`** menangani spasi, tab, dan newline sehingga tidak muncul di hasil.
- **`MISMATCH`** hanya menampilkan karakter yang **bukan whitespace**; karakter spasi diabaikan.
- Karena semua token disimpan dalam `Set`, token yang muncul berulang kali hanya ditampilkan sekali.
