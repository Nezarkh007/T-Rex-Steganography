from PIL import Image
from cryptography.fernet import Fernet
import base64
import stepic

def process_image(img):
    print("✅ Image loaded successfully!")
    print("Image format:", img.format)
    print("Image size:", img.size)
    print("Image mode:", img.mode)

def get_image_from_user():
    while True:
        image_path = input("🖼️ Enter the image file path (e.g., image.png): ").strip()
        try:
            img = Image.open(image_path)
            return img
        except Exception as e:
            print("❌ Could not open the image. Error:", e)

def generate_key(password):
    return base64.urlsafe_b64encode(password.ljust(32)[:32].encode())

def encrypt_message(text, password):
    key = generate_key(password)
    cipher = Fernet(key)
    encrypted = cipher.encrypt(text.encode())
    return encrypted.decode()

def steganography(img):
    text = input("📜 Give me the text that you want to hide in the image: ")
    password = input("🔐 Give me the password to encrypt it: ")

    encrypted_text = encrypt_message(text, password)

    encoded_img = stepic.encode(img, encrypted_text.encode())

    output_file = "stego_image.png"
    encoded_img.save(output_file)
    print(f"✅ The message has been hidden and saved as '{output_file}'.")

image = get_image_from_user()
process_image(image)
steganography(image)

