"""
main.py
-------
Entry point aplikasi desktop Perpustakaan Digital.

Struktur file:
- config.py    -> konfigurasi warna/font, util penyimpanan user, HoverButton
- homepage.py  -> Halaman Home (blog sederhana + tombol Login/Sign Up)
- signup.py    -> Halaman Sign Up (khusus daftar)
- signin.py    -> Halaman Sign In (khusus login)
- main.py      -> file ini, controller yang menggabungkan semua halaman

Jalankan dengan:
    python main.py
"""

import tkinter as tk

from config import APP_WIDTH, APP_HEIGHT, COLOR_BG
from homepage import HomePage
from signup import SignUpPage
from signin import SignInPage


class PerpustakaanApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Perpustakaan Digital")
        self.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")
        self.resizable(False, False)
        self.configure(bg=COLOR_BG)

        # Status user yang sedang login (None jika belum login)
        self.current_user = None

        # Container utama tempat semua halaman ditumpuk
        container = tk.Frame(self, bg=COLOR_BG)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for PageClass in (HomePage, SignUpPage, SignInPage):
            page_name = PageClass.__name__
            frame = PageClass(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name: str):
        """Tampilkan halaman berdasarkan nama kelasnya."""
        frame = self.frames[page_name]
        if hasattr(frame, "on_show"):
            frame.on_show()
        frame.tkraise()

    def set_current_user(self, username: str):
        self.current_user = username

    def logout(self):
        self.current_user = None
        self.show_frame("HomePage")


if __name__ == "__main__":
    app = PerpustakaanApp()
    app.mainloop()