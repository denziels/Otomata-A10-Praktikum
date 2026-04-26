Validasi Input:

if not input_string or not all(char in '01' for char in input_string):
    return False, "Input tidak valid! Hanya masukkan angka 0 dan 1.", []

Definisi Tabel:
transitions = {
    'S': {'0': 'A', '1': 'B'},
    'A': {'0': 'C', '1': 'B'},
    'B': {'0': 'A', '1': 'B'},
    'C': {'0': 'C', '1': 'C'} #trap state
}

Inisialisasi dan Proses Membaca Input:

current_state = 'S'
path = ['S'] #untuk melacak jejak state yang dilewati

for char in input_string:
    current_state = transitions[current_state][char]
    path.append(current_state)

Evaluasi State Akhir:

#state B adalah satu-satunya Final State (lingkaran ganda)
is_accepted = current_state == 'B'

return is_accepted, "", path

UI Looping (Pengguna bisa mengirim imput berkali-kali):
while True:
    user_input = input("Masukkan string (0 atau 1) : ")

    if user_input.lower() in ['keluar', 'exit']:
        print("\nProgram dihentikan. Terima kasih!")
        break
