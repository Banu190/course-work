import tkinter as tk
from tkinter import messagebox
import hashlib
import rsa

def show_caesar():
    hide_all_frames()
    caesar_frame.pack()
    
def show_md5():
    hide_all_frames()
    md5_frame.pack()

def show_rsa():
    hide_all_frames()
    rsa_frame.pack()

def hide_all_frames():
    caesar_frame.pack_forget()
    md5_frame.pack_forget()
    rsa_frame.pack_forget()

def caesar_encrypt():
    text = caesar_text_entry.get()
    shift = int(caesar_shift_entry.get())
    encrypted_text = "".join(
        chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else
        chr((ord(char) - 97 + shift) % 26 + 97) if char.islower() else char
        for char in text
    )
    caesar_result_label.config(text=f"Зашифрованный текст: {encrypted_text}")

def md5_encrypt():
    text = md5_text_entry.get()
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    md5_result_label.config(text=f"MD5 хэш: {md5_hash}")

def rsa_encrypt():
    text = rsa_text_entry.get()
    public_key, private_key = rsa.newkeys(512)
    encrypted_text = rsa.encrypt(text.encode(), public_key)
    rsa_result_label.config(text=f"Зашифрованный текст (RSA): {encrypted_text}")
    rsa_private_key_label.config(text=f"Приватный ключ: {private_key}")

root = tk.Tk()
root.title("Шифрование")

# Основные кнопки для выбора шифрования
caesar_button = tk.Button(root, text="Цезарь", command=show_caesar)
caesar_button.pack(pady=10)

md5_button = tk.Button(root, text="MD5", command=show_md5)
md5_button.pack(pady=10)

rsa_button = tk.Button(root, text="RSA", command=show_rsa)
rsa_button.pack(pady=10)

# Фрейм для шифрования Цезарем
caesar_frame = tk.Frame(root)
tk.Label(caesar_frame, text="Введите текст для шифрования (Цезарь):").pack()
caesar_text_entry = tk.Entry(caesar_frame)
caesar_text_entry.pack()
tk.Label(caesar_frame, text="Введите сдвиг:").pack()
caesar_shift_entry = tk.Entry(caesar_frame)
caesar_shift_entry.pack()
tk.Button(caesar_frame, text="Зашифровать", command=caesar_encrypt).pack()
caesar_result_label = tk.Label(caesar_frame, text="")
caesar_result_label.pack()

# Фрейм для MD5 шифрования
md5_frame = tk.Frame(root)
tk.Label(md5_frame, text="Введите текст для MD5 хэша:").pack()
md5_text_entry = tk.Entry(md5_frame)
md5_text_entry.pack()
tk.Button(md5_frame, text="Получить MD5 хэш", command=md5_encrypt).pack()
md5_result_label = tk.Label(md5_frame, text="")
md5_result_label.pack()

# Фрейм для RSA шифрования
rsa_frame = tk.Frame(root)
tk.Label(rsa_frame, text="Введите текст для RSA шифрования:").pack()
rsa_text_entry = tk.Entry(rsa_frame)
rsa_text_entry.pack()
tk.Button(rsa_frame, text="Зашифровать RSA", command=rsa_encrypt).pack()
rsa_result_label = tk.Label(rsa_frame, text="")
rsa_result_label.pack()
rsa_private_key_label = tk.Label(rsa_frame, text="")
rsa_private_key_label.pack()

root.mainloop()
