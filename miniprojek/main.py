from tkinter import Tk, Button, filedialog, Scale, HORIZONTAL, Label
from PIL import Image, ImageEnhance, ImageTk

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        load_image(file_path)



def load_image(path):
    
    global img_label, img_pil, img_tk, btn_contrast, btn_brightness, btn_saturation, \
        scale_contrast, scale_brightness, scale_saturation, original_img_pil, edited_img_pil
    img_pil = Image.open(path)
    original_img_pil = img_pil.copy()
    img_pil.thumbnail((300, 300))
    img_tk = ImageTk.PhotoImage(img_pil)
    
    if img_label:
        img_label.destroy()
        btn_contrast.destroy()
        btn_brightness.destroy()
        btn_saturation.destroy()

    img_label = Label(root, image=img_tk)
    img_label.image = img_tk
    img_label.pack()
    

    btn_contrast = Button(root, text="Kontras", command=toggle_contrast)
    btn_contrast.pack(pady=5)

    btn_brightness = Button(root, text="Kecerahan", command=toggle_brightness)
    btn_brightness.pack(pady=5)

    btn_saturation = Button(root, text="Saturasi", command=toggle_saturation)
    btn_saturation.pack(pady=5)

    scale_contrast = Scale(root, from_=0.5, to=2.0, resolution=0.1, orient=HORIZONTAL, label="Kontras",
                            command=enhance_contrast, length=200)
    scale_contrast.set(1.0)

    scale_brightness = Scale(root, from_=0.5, to=2.0, resolution=0.1, orient=HORIZONTAL, label="Kecerahan",
                                command=enhance_brightness, length=200)
    scale_brightness.set(1.0)

    scale_saturation = Scale(root, from_=0.5, to=2.0, resolution=0.1, orient=HORIZONTAL, label="Saturasi",
                                command=enhance_saturation, length=200)
    scale_saturation.set(1.0)

    edited_img_pil = img_pil.copy()  # Salin gambar yang diedit saat gambar dimuat

def toggle_contrast():
    global scale_contrast
    if scale_contrast.winfo_ismapped():
        scale_contrast.pack_forget()  # Sembunyikan slider kontras
    else:
        scale_contrast.pack()  # Tampilkan slider kontras

def toggle_brightness():
    global scale_brightness
    if scale_brightness.winfo_ismapped():
        scale_brightness.pack_forget()  # Sembunyikan slider kecerahan
    else:
        scale_brightness.pack()  # Tampilkan slider kecerahan

def toggle_saturation():
    global scale_saturation
    if scale_saturation.winfo_ismapped():
        scale_saturation.pack_forget()  # Sembunyikan slider saturasi
    else:
        scale_saturation.pack()  # Tampilkan slider saturasi

def enhance_contrast(value):
    global img_pil, img_tk, edited_img_pil
    enhanced_img = ImageEnhance.Contrast(img_pil)
    img_pil = enhanced_img.enhance(float(value))
    img_tk = ImageTk.PhotoImage(img_pil)
    img_label.configure(image=img_tk)
    img_label.image = img_tk
    edited_img_pil = img_pil.copy()  # Simpan salinan gambar yang diedit

def enhance_brightness(value):
    global img_pil, img_tk, edited_img_pil
    enhanced_img = ImageEnhance.Brightness(img_pil)
    img_pil = enhanced_img.enhance(float(value))
    img_tk = ImageTk.PhotoImage(img_pil)
    img_label.configure(image=img_tk)
    img_label.image = img_tk
    edited_img_pil = img_pil.copy()  # Simpan salinan gambar yang diedit

def enhance_saturation(value):
    global img_pil, img_tk, edited_img_pil
    enhanced_img = ImageEnhance.Color(img_pil)
    img_pil = enhanced_img.enhance(float(value))
    img_tk = ImageTk.PhotoImage(img_pil)
    img_label.configure(image=img_tk)
    img_label.image = img_tk
    edited_img_pil = img_pil.copy()  # Simpan salinan gambar yang diedit

root = Tk()
root.title("Projek Pengolahan Citra")
root.geometry("400x600")
root.configure(bg="#f0f0f0")


def update_image():
    global img_label, img_tk
    img_label.configure(image=img_tk)
    img_label.image = img_tk

def reset_image():
    global img_pil, img_tk, img_label, original_img_pil
    img_pil = original_img_pil.copy()
    img_tk = ImageTk.PhotoImage(img_pil)
    img_label.configure(image=img_tk)
    img_label.image = img_tk

title_label = Label(root, text="Penerapan Filter pada foto dengan Aplikasi\nPengolahan Citra untuk meningkatkan estetika", font=("Arial", 12, "bold"), bg="#f0f0f0", anchor="w")
title_label.pack(pady=10)

# Label nama kelompok (rata kiri di ujung kiri)
names_text = "Nama-Nama Kelompok:\n- Uria Dutu\n- Gwent Labada\n- Inda Rondunuwu\n- Anisya Rengkuan"
function_label = Label(root, text=names_text, font=("Arial", 12), bg="#f0f0f0", justify="left")
function_label.pack(pady=5, padx=10, anchor="w")

# Tombol unggah gambar (rata kiri)
upload_button = Button(root, text="Unggah Gambar", command=open_file, bg="orange", fg="white", anchor="w")
upload_button.pack(pady=20, padx=10, anchor="w")

img_label = None
img_pil = None
img_tk = None
original_img_pil = None
edited_img_pil = None
scale_contrast = None
scale_brightness = None
scale_saturation = None
btn_contrast = None
btn_brightness = None
btn_saturation = None



root.mainloop()
