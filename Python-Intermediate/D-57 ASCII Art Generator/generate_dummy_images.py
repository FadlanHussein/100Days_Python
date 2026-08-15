import os
from PIL import Image, ImageDraw

def create_dummy_images():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    img_dir = os.path.join(base_dir, "images")
    os.makedirs(img_dir, exist_ok=True)

    # 1. Gambar Smiley Face (Kontras Hitam Putih)
    smile_img = Image.new("RGB", (200, 200), color=(255, 255, 255))
    draw = ImageDraw.Draw(smile_img)
    draw.ellipse((20, 20, 180, 180), fill=(255, 220, 0), outline=(0, 0, 0), width=4) # Wajah
    draw.ellipse((60, 70, 80, 90), fill=(0, 0, 0)) # Mata kiri
    draw.ellipse((120, 70, 140, 90), fill=(0, 0, 0)) # Mata kanan
    draw.arc((60, 90, 140, 150), start=0, end=180, fill=(0, 0, 0), width=5) # Senyum
    smile_img.save(os.path.join(img_dir, "sample_smile.png"))

    # 2. Gambar Heart / Logo
    heart_img = Image.new("RGB", (200, 200), color=(255, 255, 255))
    draw_heart = ImageDraw.Draw(heart_img)
    draw_heart.polygon([(100, 170), (30, 90), (50, 40), (100, 70), (150, 40), (170, 90)], fill=(230, 40, 40))
    heart_img.save(os.path.join(img_dir, "sample_heart.png"))

    # 3. Gambar Gradient (Bagus untuk uji karakter ASCII grayscale)
    grad_img = Image.new("L", (200, 200))
    for x in range(200):
        for y in range(200):
            grad_img.putpixel((x, y), int((x / 200) * 255))
    grad_img.save(os.path.join(img_dir, "sample_gradient.png"))

    print(f"[OK] Berhasil membuat 3 sample gambar di: {img_dir}")

if __name__ == "__main__":
    create_dummy_images()
