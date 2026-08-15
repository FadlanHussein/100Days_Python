import os
from PIL import Image

# Daftar karakter ASCII dari gelap ke terang
ASCII_CHARS = "@%#*+=-:. "

def load_image(image_path, new_width=100):
    img = Image.open(image_path)
    aspect_ratio = img.height / img.width
    new_height = int(new_width * aspect_ratio * 0.55)
    img = img.resize((new_width, max(1, new_height)))
    return img

def convert_to_grayscale(img):
    return img.convert("L")

def map_pixels_to_ascii(img):
    num_chars = len(ASCII_CHARS)
    ascii_str = "".join([ASCII_CHARS[min(pixel * num_chars // 256, num_chars - 1)] for pixel in img.getdata()])
    return ascii_str

def generate_ascii_art(image_path, new_width=100):
    img = load_image(image_path, new_width)
    gray_img = convert_to_grayscale(img)
    ascii_str = map_pixels_to_ascii(gray_img)

    width = gray_img.width
    ascii_art = ""
    for i in range(0, len(ascii_str), width):
        ascii_art += ascii_str[i:i + width] + "\n"
    return ascii_art

def save_ascii_art(ascii_art, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(ascii_art)
    print(f"\nASCII art saved to: {output_file}")

def main():
    print("=" * 45)
    print("     Welcome to the ASCII Art Generator!     ")
    print("=" * 45)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    default_img = os.path.join(base_dir, "images", "sample_smile.png")

    image_path = input(f"Enter the path to the image (default: sample_smile.png): ").strip()
    if not image_path:
        image_path = default_img
    elif not os.path.isabs(image_path) and not os.path.exists(image_path):
        check_path = os.path.join(base_dir, "images", image_path)
        if os.path.exists(check_path):
            image_path = check_path

    width_input = input("Enter the desired width (default: 80): ").strip()
    new_width = int(width_input) if width_input.isdigit() else 80

    output_path = os.path.join(base_dir, "output.txt")

    try:
        ascii_art = generate_ascii_art(image_path, new_width)
        print("\n" + ascii_art)
        save_ascii_art(ascii_art, output_path)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
