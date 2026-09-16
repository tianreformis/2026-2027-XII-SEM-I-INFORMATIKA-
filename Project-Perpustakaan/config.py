"""
config.py
---------
Konfigurasi bersama untuk seluruh halaman aplikasi:
- Ukuran window
- Palet warna & font
- Util penyimpanan user (JSON) + hashing password
- Komponen HoverButton yang dipakai di banyak halaman
- Data dummy artikel untuk blog sederhana di Home Page
"""

import tkinter as tk
import json
import os
import hashlib


APP_WIDTH = 1280
APP_HEIGHT = 720

USERS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "users.json")


COLOR_PRIMARY = "#2c3e50"     # biru dongker (header/navbar)
COLOR_ACCENT = "#2980b9"      # biru terang (tombol utama)
COLOR_ACCENT_DARK = "#1c5980"
COLOR_BG = "#f4f6f7"          # latar halaman
COLOR_CARD = "#ffffff"        # kartu artikel
COLOR_TEXT = "#2c3e50"
COLOR_MUTED = "#7f8c8d"
COLOR_SUCCESS = "#27ae60"
COLOR_DANGER = "#c0392b"


FONT_TITLE = ("Segoe UI", 26, "bold")
FONT_SUBTITLE = ("Segoe UI", 12)
FONT_NAV = ("Segoe UI", 11, "bold")
FONT_CARD_TITLE = ("Segoe UI", 14, "bold")
FONT_CARD_BODY = ("Segoe UI", 10)
FONT_LABEL = ("Segoe UI", 11)
FONT_BUTTON = ("Segoe UI", 11, "bold")



ARTIKEL_PERPUSTAKAAN = [
    {
        "judul": "5 Rekomendasi Buku Fiksi Bulan Ini",
        "ringkasan": "Temukan lima judul fiksi terbaru yang tersedia di rak perpustakaan "
                     "kami, mulai dari novel misteri hingga fantasi epik.",
        "kategori": "Rekomendasi",
    },
    {
        "judul": "Tips Efektif Membaca Cepat",
        "ringkasan": "Pelajari teknik speed reading sederhana agar kamu bisa menyelesaikan "
                     "lebih banyak buku tanpa kehilangan pemahaman isi bacaan.",
        "kategori": "Tips & Trik",
    },
    {
        "judul": "Jadwal Kunjungan & Jam Operasional",
        "ringkasan": "Perpustakaan buka setiap hari Senin-Sabtu pukul 08.00-16.00. "
                     "Cek jadwal lengkap dan agenda kegiatan bulanan di sini.",
        "kategori": "Pengumuman",
    },
    {
        "judul": "Cara Meminjam Buku Secara Online",
        "ringkasan": "Setelah login, anggota dapat memesan buku secara online dan "
                     "mengambilnya langsung di meja sirkulasi perpustakaan.",
        "kategori": "Panduan",
    },
]


def hash_password(password: str) -> str:
    """Hash password dengan SHA-256 supaya tidak disimpan dalam plain text."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def load_users() -> dict:
    if not os.path.exists(USERS_FILE):
        return {}
    try:
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}


def save_users(users: dict) -> None:
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=2, ensure_ascii=False)


def register_user(username: str, email: str, password: str) -> tuple[bool, str]:
    users = load_users()
    if username in users:
        return False, "Username sudah terdaftar. Silakan gunakan username lain."
    for data in users.values():
        if data.get("email", "").lower() == email.lower():
            return False, "Email sudah terdaftar. Silakan gunakan email lain."
    users[username] = {
        "email": email,
        "password": hash_password(password),
    }
    save_users(users)
    return True, "Pendaftaran berhasil! Silakan login."


def verify_login(username: str, password: str) -> tuple[bool, str]:
    users = load_users()
    if username not in users:
        return False, "Username tidak ditemukan."
    if users[username]["password"] != hash_password(password):
        return False, "Password salah."
    return True, "Login berhasil!"


class HoverButton(tk.Button):
    def __init__(self, master, bg_normal, bg_hover, **kwargs):
        super().__init__(master, bg=bg_normal, activebackground=bg_hover, **kwargs)
        self.bg_normal = bg_normal
        self.bg_hover = bg_hover
        self.bind("<Enter>", lambda e: self.config(bg=self.bg_hover))
        self.bind("<Leave>", lambda e: self.config(bg=self.bg_normal))