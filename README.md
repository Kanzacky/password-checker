# Password Strength Checker

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)

A simple Command Line Interface (CLI) tool using Python to evaluate and check the strength of a password.

## Key Features

- **Password Length Check**: Evaluates based on the number of characters (less than 8, 8-11, or 12+ characters).
- **Character Variety**: Checks for a combination of uppercase letters, lowercase letters, numbers, and symbols.
- **Common Password Detection**: Checks if the password is included in a list of commonly used and vulnerable passwords (e.g., `123456`, `password`, `admin`).
- **Repetitive Pattern Detection**: Identifies repeating characters (e.g., `aaaa`) or easily guessable sequences of characters/numbers (e.g., `1234`, `abcd`).
- **Improvement Suggestions**: Provides specific feedback (such as adding symbols or uppercase letters) to improve password strength.
- **Privacy Guaranteed**: Passwords are only processed locally and are not saved or sent anywhere.

## Prerequisites

Make sure you have installed:
- [Python 3.6](https://www.python.org/downloads/) or a newer version.

*Note: This tool only uses built-in Python libraries (`re`, `string`), so no external library installation is required.*

## Installation and Usage

1. **Clone this repository** (or download the file manually):
   ```bash
   git clone https://github.com/Kanzacky/password-checker.git
   cd paswordchecher
   ```

2. **Run the Python script**:
   ```bash
   python password_checker.py
   ```

3. **Enter a password** when prompted by the program, and see the evaluation results along with the score and strength level of your password. Type `exit` to exit the program.

## Usage Example

```text
=== Password Strength Checker ===
(Password tidak disimpan atau dikirim ke mana pun, hanya diproses lokal)

Masukkan password untuk dicek (atau ketik 'exit' untuk keluar): 123

Mengecek password: ***
----------------------------------------
Panjang        : Terlalu pendek (kurang dari 8 karakter)
Variasi karakter: 1/4 kriteria terpenuhi
----------------------------------------
Skor akhir     : 1/6
Tingkat        : SANGAT LEMAH

Saran perbaikan:
  - Tambahkan huruf kecil
  - Tambahkan huruf besar
  - Tambahkan simbol (!@#$%^&* dll)
```

## Contributing

Contributions are always welcome! If you want to add features, expand the common password list (e.g., integrating wordlists like *rockyou.txt*), or fix bugs, please create a *Pull Request* or open an *Issue*.

1. Fork this repository
2. Create your feature branch (`git checkout -b new-feature`)
3. Commit your changes (`git commit -m 'Add a new feature'`)
4. Push to the branch (`git push origin new-feature`)
5. Open a Pull Request

---
*Created to simplify checking and raise awareness about password security.*
