from PIL import Image
import stepic
from cryptography.fernet import Fernet
import base64

# Generate Fernet key from password (same as encryption)
def generate_key(password):
    return base64.urlsafe_b64encode(password.ljust(32)[:32].encode())

# Decrypt the message using Fernet
def decrypt_message(encrypted_text, password):
    key = generate_key(password)
    cipher = Fernet(key)
    decrypted = cipher.decrypt(encrypted_text.encode())
    return decrypted.decode()

# Extract and decrypt hidden message from image
def decode_steganography(image_path):
    try:
        img = Image.open(image_path)
    except Exception as e:
        print(f"❌ Could not open image: {e}")
        return None

    try:
        encrypted_text = stepic.decode(img)
        if not encrypted_text:
            print("❌ No hidden message found in this image.")
            return None
    except Exception as e:
        print(f"❌ Error decoding image: {e}")
        return None

    password = input("🔐 Enter the password to decrypt the message: ")

    try:
        decrypted_text = decrypt_message(encrypted_text, password)
        print("✅ Decrypted message:")
        print(decrypted_text)
        return decrypted_text
    except Exception as e:
        print("❌ Incorrect password or corrupted data.")
        return None

# Example usage:
if __name__ == "__main__":
    image_path = input("🖼️ Enter the path to the image with hidden message: ").strip()
    decode_steganography(image_path)
