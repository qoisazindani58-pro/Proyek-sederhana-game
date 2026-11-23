# Petualangan Dungeon — Proyek OOP Python

Game petualangan berbasis terminal/console. Pemain membuat hero, melawan tiga monster, menggunakan potion, dan berusaha menyelesaikan dungeon.

## 1. Tujuan Proyek
Proyek ini dibuat sebagai contoh penerapan konsep Object-Oriented Programming (OOP) menggunakan Python.

## 2. Fitur
- Membuat karakter hero dengan nama pilihan pemain.
- Melawan Goblin, Orc, dan Naga Kecil.
- Memilih aksi menyerang, menggunakan potion, atau melihat status.
- Sistem HP, damage, potion, dan XP.
- Kondisi menang dan game over.

## 3. Konsep OOP yang diterapkan
| Konsep | Implementasi |
|---|---|
| Class dan Object | `Character`, `Hero`, `Monster`, `Game`; objek dibuat saat program berjalan. |
| Attribute | `name`, `_health`, `attack_power`, `potions`, `level`, `reward_xp`. |
| Constructor | `__init__()` menginisialisasi data objek. |
| Method | `attack()`, `take_damage()`, `use_potion()`, `battle()`, `show_status()`. |
| Encapsulation | `_health` disimpan sebagai atribut internal dan diakses melalui property `health`; perubahan HP dilakukan melalui method. |
| Inheritance | `Hero` dan `Monster` mewarisi `Character`. |
| Polymorphism | `Hero.attack()` dan `Monster.attack()` memiliki implementasi berbeda dengan nama method yang sama. |
| Abstraction | `Character` adalah abstract class dan `attack()` adalah abstract method. |
| Composition/has-a | Objek `Game` mengelola objek hero dan kumpulan objek monster. |

## 4. Struktur Folder
```text
Proyek_OOP_Petualangan_Dungeon/
├── main.py
├── README.md
└── src/
    ├── __init__.py
    ├── character.py
    └── game.py
```

## 5. Cara Menjalankan
1. Pastikan Python 3.9 atau lebih baru sudah terpasang.
2. Buka folder proyek di VS Code atau terminal.
3. Jalankan perintah:

```bash
python main.py
```

Tidak membutuhkan library tambahan.

## 6. Cara Bermain
1. Masukkan nama hero.
2. Saat bertemu monster, pilih:
   - `1` untuk menyerang.
   - `2` untuk menggunakan potion yang memulihkan 30 HP.
   - `3` untuk melihat status hero.
3. Kalahkan ketiga monster untuk menang.
4. Jika HP hero mencapai 0, permainan berakhir.

## 7. Pengujian Sederhana
- Jalankan `python main.py`.
- Masukkan nama, misalnya `Budi`.
- Pilih aksi `1` untuk menyerang dan amati HP monster berkurang.
- Pilih `2` untuk menggunakan potion (pastikan HP kurang dari 100).
- Kalahkan semua monster untuk melihat pesan kemenangan.
- Ulangi permainan dan biarkan HP mencapai 0 untuk menguji kondisi game over.

## 8. Identitas Mahasiswa
- Nama: Qois Azindani
- NPM: 14012500039

## 9. Catatan Pengumpulan
Proyek ini dikerjakan secara individu. Unggah proyek ke repository pada akun GitHub pribadi, lalu bagikan link profil GitHub ke grup dengan mencantumkan nama dan NPM.
