def check_fsm(input_string):
  
    #validasi input: tidak boleh kosong dan hanya boleh berisi 0 atau 1
    if not input_string or not all(char in '01' for char in input_string):
        return False, "Input tidak valid! Hanya masukkan angka 0 dan 1.", []

    #definisi tabel Transisi FSM berdasarkan gambar
    transitions = {
        'S': {'0': 'A', '1': 'B'},
        'A': {'0': 'C', '1': 'B'},
        'B': {'0': 'A', '1': 'B'},
        'C': {'0': 'C', '1': 'C'} #ini trap state
    }

    current_state = 'S'
    path = ['S'] #untuk melacak jejak state yang dilewati

    #proses setiap karakter dalam string
    for char in input_string:
        current_state = transitions[current_state][char]
        path.append(current_state)

    #state B adalah satu-satunya Final State (lingkaran ganda)
    is_accepted = current_state == 'B'
    
    return is_accepted, "", path

def main():
    print("="*60)
    print("    SIMULASI FINITE STATE MACHINE (FSM)")
    print("    Mendeteksi akhiran '1' tanpa substring '00'")
    print("="*60)
    print("Ketik 'keluar' atau 'exit' untuk menghentikan program.\n")

    #looping interaktif agar pengguna mudah menginput berkali-kali
    while True:
        user_input = input("Masukkan string (0 atau 1) : ")

        if user_input.lower() in ['keluar', 'exit']:
            print("\nProgram dihentikan. Terima kasih!")
            break

        is_accepted, error_msg, path = check_fsm(user_input)

        if error_msg:
            print(f"-> ERROR: {error_msg}\n")
        else:
            print(f"-> Jejak State : {' -> '.join(path)}")
            print(f"-> State Akhir : {path[-1]}")
            if is_accepted:
                print("-> Kesimpulan  : [ DITERIMA ] - String dikenali oleh FSM\n")
            else:
                print("-> Kesimpulan  : [ DITOLAK ]  - String TIDAK dikenali oleh FSM\n")

if __name__ == "__main__":
    main()
