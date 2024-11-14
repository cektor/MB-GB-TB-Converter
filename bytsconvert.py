import tkinter as tk
from tkinter import messagebox

# MB, GB, TB dönüşümü yapacak fonksiyon
def convert():
    try:
        # Kullanıcının girdiği değeri al
        value = float(entry.get())
        
        # MB'den GB ve TB'ye dönüşüm
        if conversion_type.get() == "MB":
            gb_result = value / 1024
            tb_result = value / (1024 * 1024)
            result_label.config(text=f"Sonuç:\n{value} MB = {gb_result:.4f} GB\n{value} MB = {tb_result:.6f} TB")
        
        # GB'den MB ve TB'ye dönüşüm
        elif conversion_type.get() == "GB":
            mb_result = value * 1024
            tb_result = value / 1024
            result_label.config(text=f"Sonuç:\n{value} GB = {mb_result:.0f} MB\n{value} GB = {tb_result:.4f} TB")
        
        # TB'den MB ve GB'ye dönüşüm
        elif conversion_type.get() == "TB":
            mb_result = value * (1024 * 1024)
            gb_result = value * 1024
            result_label.config(text=f"Sonuç:\n{value} TB = {mb_result:.0f} MB\n{value} TB = {gb_result:.4f} GB")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı giriniz!")

# Tkinter pencereyi oluştur
root = tk.Tk()
root.title("MB-GB-TB Çevirici")
root.geometry("300x460")  # Uygulama boyutunu sabitle
root.config(bg="#2e3b4e")  # Arka plan rengini değiştir

# Pencerenin boyutlandırılmasını engelle
root.resizable(False, False)

# Başlık etiketi
title_label = tk.Label(root, text="MB-GB-TB Çevirici", font=("Helvetica", 18, "bold"), fg="#8eba00", bg="#2e3b4e")
title_label.pack(pady=20)

# Kullanıcıdan değer girmesini isteyen etiket ve giriş kutusu
entry_label = tk.Label(root, text="Bir Değer Girin:", font=("Helvetica", 12), fg="#ffffff", bg="#2e3b4e")
entry_label.pack()

entry = tk.Entry(root, font=("Helvetica", 14), width=20, bd=2, relief="solid")
entry.pack(pady=10)

# Dönüşüm tipi için radyo butonları
conversion_type = tk.StringVar(value="MB")

mb_radio = tk.Radiobutton(root, text="MB", variable=conversion_type, value="MB", font=("Helvetica", 12), fg="#ffffff", bg="#2e3b4e", selectcolor="#8eba00")
mb_radio.pack()

gb_radio = tk.Radiobutton(root, text="GB", variable=conversion_type, value="GB", font=("Helvetica", 12), fg="#ffffff", bg="#2e3b4e", selectcolor="#8eba00")
gb_radio.pack()

tb_radio = tk.Radiobutton(root, text="TB", variable=conversion_type, value="TB", font=("Helvetica", 12), fg="#ffffff", bg="#2e3b4e", selectcolor="#8eba00")
tb_radio.pack(pady=10)

# Dönüşüm butonu
convert_button = tk.Button(root, text="Dönüştür", font=("Helvetica", 14), fg="#ffffff", bg="#8eba00", command=convert, relief="solid", bd=2)
convert_button.pack(pady=10)

# Sonuç etiketi
result_label = tk.Label(root, text="Sonuç: ", font=("Helvetica", 14), fg="#ffffff", bg="#2e3b4e")
result_label.pack(pady=10)

# Pencereyi sürekli göster
root.mainloop()
