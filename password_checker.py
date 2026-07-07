"""
Password Strength Checker
===========================
Tool sederhana untuk mengecek kekuatan password berdasarkan:
- Panjang password
- Kombinasi huruf besar/kecil
- Kombinasi angka
- Kombinasi simbol
- Cek apakah termasuk password yang umum dipakai (rawan)
- Cek pola berulang/berurutan (misal "1234", "aaaa")

Cara pakai:
    python password_checker.py
"""

import re
import string

# Daftar password paling umum/lemah (contoh kecil, bisa diperluas dari wordlist rockyou.txt dll)
COMMON_PASSWORDS = {
    "123456", "password", "123456789", "12345678", "12345",
    "qwerty", "abc123", "111111", "123123", "admin",
    "letmein", "welcome", "monkey", "iloveyou", "password1"
}


def check_length(password):
    length = len(password)
    if length < 8:
        return 0, "Terlalu pendek (kurang dari 8 karakter)"
    elif length < 12:
        return 1, "Panjang cukup (8-11 karakter)"
    else:
        return 2, "Panjang bagus (12+ karakter)"


def check_character_variety(password):
    score = 0
    feedback = []

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Tambahkan huruf kecil")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Tambahkan huruf besar")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Tambahkan angka")

    if re.search(rf"[{re.escape(string.punctuation)}]", password):
        score += 1
    else:
        feedback.append("Tambahkan simbol (!@#$%^&* dll)")

    return score, feedback


def check_common_password(password):
    if password.lower() in COMMON_PASSWORDS:
        return False, "Password ini termasuk daftar password yang sering dipakai & mudah ditebak!"
    return True, None


def check_repetition_pattern(password):
    # Deteksi karakter berulang seperti "aaaa" atau "1111"
    if re.search(r"(.)\1{2,}", password):
        return False, "Terdapat karakter yang berulang terus-menerus (misal: aaa, 111)"

    # Deteksi urutan angka/huruf berurutan seperti "1234", "abcd"
    sequences = ["0123456789", "abcdefghijklmnopqrstuvwxyz"]
    lower_pw = password.lower()
    for seq in sequences:
        for i in range(len(seq) - 3):
            if seq[i:i+4] in lower_pw:
                return False, "Terdapat pola berurutan (misal: 1234, abcd)"

    return True, None


def evaluate_password(password):
    print(f"\nMengecek password: {'*' * len(password)}")
    print("-" * 40)

    total_score = 0
    all_feedback = []

    # 1. Cek panjang
    length_score, length_msg = check_length(password)
    total_score += length_score
    print(f"Panjang        : {length_msg}")

    # 2. Cek variasi karakter
    variety_score, variety_feedback = check_character_variety(password)
    total_score += variety_score
    print(f"Variasi karakter: {variety_score}/4 kriteria terpenuhi")
    all_feedback.extend(variety_feedback)

    # 3. Cek password umum
    is_safe, common_msg = check_common_password(password)
    if not is_safe:
        total_score = 0  # langsung dianggap lemah walau kriteria lain terpenuhi
        all_feedback.append(common_msg)

    # 4. Cek pola berulang/berurutan
    no_pattern, pattern_msg = check_repetition_pattern(password)
    if not no_pattern:
        total_score -= 1
        all_feedback.append(pattern_msg)

    # Tentukan level kekuatan (skor maksimal = 2 + 4 = 6)
    if total_score <= 1:
        level = "SANGAT LEMAH"
    elif total_score <= 3:
        level = "LEMAH"
    elif total_score <= 5:
        level = "SEDANG"
    else:
        level = "KUAT"

    print("-" * 40)
    print(f"Skor akhir     : {max(total_score, 0)}/6")
    print(f"Tingkat        : {level}")

    if all_feedback:
        print("\nSaran perbaikan:")
        for f in all_feedback:
            print(f"  - {f}")
    else:
        print("\nPassword ini sudah cukup baik!")

    return level


if __name__ == "__main__":
    print("=== Password Strength Checker ===")
    print("(Password tidak disimpan atau dikirim ke mana pun, hanya diproses lokal)")

    while True:
        pw = input("\nMasukkan password untuk dicek (atau ketik 'exit' untuk keluar): ")
        if pw.lower() == "exit":
            print("Selesai. Sampai jumpa!")
            break
        if pw == "":
            print("Password tidak boleh kosong.")
            continue

        evaluate_password(pw)
