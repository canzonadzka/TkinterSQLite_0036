import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Database setup
conn = sqlite3.connect("prediksi_diabetes.db")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS pasien (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_pasien TEXT,
    usia INTEGER,
    gula_darah REAL,
    bmi REAL,
    riwayat_ortu TEXT,
    hasil_prediksi TEXT)""")
conn.commit()

# Prediksi
def prediksi(gula, bmi, riwayat):
    if gula >= 200:
        if bmi >= 30 or riwayat == "Ya":
            return "Sangat Tinggi"
        return "Tinggi"
    elif gula >= 140:
        if bmi >= 30 or riwayat == "Ya":
            return "Tinggi"
        return "Sedang"
    else:
        if bmi >= 30:
            if riwayat == "Ya":
                return "Sedang"
            return "Waspada"
        if riwayat == "Ya":
            return "Waspada"
        return "Rendah"

# Tampilan GUI
root = tk.Tk()
root.title("Prediksi Risiko Diabetes")

tk.Label(root, text="Nama Pasien").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_nama = tk.Entry(root, width=25)
entry_nama.grid(row=0, column=1)

tk.Label(root, text="Usia").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_usia = tk.Entry(root, width=25)
entry_usia.grid(row=1, column=1)

tk.Label(root, text="Gula Darah (mg/dL)").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_gula = tk.Entry(root, width=25)
entry_gula.grid(row=2, column=1)

tk.Label(root, text="BMI").grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_bmi = tk.Entry(root, width=25)
entry_bmi.grid(row=3, column=1)

tk.Label(root, text="Riwayat Diabetes Ortu").grid(row=4, column=0, padx=10, pady=5, sticky="w")
combo_riwayat = ttk.Combobox(root, values=["Ya", "Tidak"], state="readonly", width=22)
combo_riwayat.grid(row=4, column=1)

root.mainloop()
conn.close()

