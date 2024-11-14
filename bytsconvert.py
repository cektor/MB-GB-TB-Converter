import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

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
root.geometry("350x500")  # Uygulama boyutunu sabitle
root.config(bg="#2e3b4e")  # Arka plan rengini değiştir

# Pencerenin boyutlandırılmasını engelle
root.resizable(False, False)

# Başlık etiketi
title_label = tk.Label(root, text="MB-GB-TB Çevirici", font=("Helvetica", 18, "bold"), fg="#8eba00", bg="#2e3b4e")
title_label.pack(pady=20)

# Kullanıcıdan değer girmesini isteyen etiket ve giriş kutusu
entry_label = tk.Label(root, text="Bir Değer Girin:", font=("Helvetica", 12), fg="#ffffff", bg="#2e3b4e")
entry_label.pack()

entry_frame = tk.Frame(root, bd=2, relief="solid", bg="#ffffff", width=300)
entry_frame.pack(pady=10)

entry = tk.Entry(entry_frame, font=("Helvetica", 14), width=20, bd=0, relief="solid", justify="center")
entry.pack(ipady=5)

# Dönüşüm tipi için radyo butonları çerçevesi
conversion_frame = tk.Frame(root, bg="#2e3b4e")
conversion_frame.pack(pady=10)

conversion_type = tk.StringVar(value="MB")

mb_radio = tk.Radiobutton(conversion_frame, text="MB", variable=conversion_type, value="MB", font=("Helvetica", 12), fg="#ffffff", bg="#2e3b4e", selectcolor="#8eba00", activebackground="#8eba00", relief="solid")
mb_radio.grid(row=0, column=0, padx=10)

gb_radio = tk.Radiobutton(conversion_frame, text="GB", variable=conversion_type, value="GB", font=("Helvetica", 12), fg="#ffffff", bg="#2e3b4e", selectcolor="#8eba00", activebackground="#8eba00", relief="solid")
gb_radio.grid(row=0, column=1, padx=10)

tb_radio = tk.Radiobutton(conversion_frame, text="TB", variable=conversion_type, value="TB", font=("Helvetica", 12), fg="#ffffff", bg="#2e3b4e", selectcolor="#8eba00", activebackground="#8eba00", relief="solid")
tb_radio.grid(row=0, column=2, padx=10)

# Dönüşüm butonu
convert_button = tk.Button(root, text="Dönüştür", font=("Helvetica", 14), fg="#ffffff", bg="#8eba00", command=convert, relief="solid", bd=2, width=20, height=2)
convert_button.pack(pady=15)

# Sonuç etiketi
result_frame = tk.Frame(root, bd=2, relief="solid", bg="#ffffff", width=300)
result_frame.pack(pady=20)

result_label = tk.Label(result_frame, text="Sonuç: ", font=("Helvetica", 14), fg="#2e3b4e", bg="#ffffff", justify="left")
result_label.pack(padx=10, pady=10)

# Gölgeleme ve animasyonları sağlamak için metodlar
def on_enter_button(e):
    convert_button.config(bg="#7a9b00")

def on_leave_button(e):
    convert_button.config(bg="#8eba00")

convert_button.bind("<Enter>", on_enter_button)
convert_button.bind("<Leave>", on_leave_button)

# Pencereyi sürekli göster
root.mainloop()
