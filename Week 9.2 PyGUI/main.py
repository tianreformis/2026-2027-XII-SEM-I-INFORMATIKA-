import tkinter as tk
from tk import *

#main windows 
window = tk.Tk()
window.title("Aplikasi XII A")
window.geometry("400x700")  #lebar * tinggi

label = tk.Label(window, text="Welcome Home", font=("Poppins Bold", 16))
#Pack adalah layout
label.pack(pady=20)

button = tk.Button(window, text="Click Me", font=("Poppins Bold", 12), command=lambda: label.config(text="Button Clicked!"))
button.pack(pady=10)

#inputfield, textarea, textbox
inputfield = tk.Entry(window, font=("Poppins", 12))
inputfield.pack(pady=10)

#checkbutton
jawaban_a = tk.IntVar()
checkbutton = tk.Checkbutton(window, text="Jawaban A", variable=jawaban_a, font=("Poppins", 12))
checkbutton.pack(pady=10)

jawaban_b = tk.IntVar()
checkbutton2 = tk.Checkbutton(window, text="Jawaban B", variable=jawaban_b, font=("Poppins", 12))
checkbutton2.pack(pady=10)

#radiobutton
radioButton = tk.IntVar()
radiobutton1 = tk.Radiobutton(window, text="Pilihan 1", variable=radioButton, value=1, font=("Poppins", 12))
radiobutton1.pack(pady=5)
#main looping, aplikasi akan terus berjalan sampai kita menghentikannya
window.mainloop()