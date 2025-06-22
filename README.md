STILL WORKING ON IT 👍

# 🕵️‍♂️ T-Rex Steganography Tool 

A simple yet powerful Python-based **steganography tool** that lets you hide secret messages inside images.  
It supports **password-protected encryption**, **manual or file-based input**, and works with **PNG/BMP images** using LSB (Least Significant Bit) encoding.

---

## 🎯 Features

- ✅ Hide text messages inside images using **LSB steganography** (`stepic`)
- 🔐 Optional **AES-128 encryption** using `cryptography.Fernet` with user password
- 📄 Supports **manual input** or **text file loading**
- 📷 Supports **.png** and **.bmp** image formats
- ⚠️ Smart file size validation (message size vs image capacity)
- 🧠 Clean CLI interface with colored prompts (`colorama`)
- ✍️ Typewriter-style banner intro
- 📂 Option to save long decoded messages to `.txt`

---

## 🛠️ Requirements

```bash
pip install -r requirements.txt
```
---

## 🚀 Usage encrypte

Run the tool:

```bash
python steganography_tool.py
```

Then follow the CLI instructions to:

### 🔏 Encode
1. Choose your carrier image (PNG/BMP)
2. Enter message manually or load from `.txt`
3. Optionally encrypt with a password
4. Save the new stego image

## 🚀 Usage decrypte

Run the tool:

```bash
python decryption.py
```
### 🔓 Decode
1. Load the encoded image
2. If encrypted, enter password to decrypt
3. View or save the decoded message

---

## 🧪 Example

🖼️ Enter the image file path (e.g., image.png): my_image.png
✅ Image loaded successfully!
Image format: PNG
Image size: (512, 512)
Image mode: RGB
📜 Give me the text that you want to hide in the image: Hello Nezar
🔐 Give me the password to encrypt it: nezar2025
✅ The message has been hidden and saved as 'stego_image.png'.


---

## ⚠️ Disclaimer

> This tool is intended for **educational and ethical use only**.  
> The author is not responsible for any misuse of the software.

---


## 🙋‍♂️ Author

NEZAR T-Rex

---

## ⭐ Contributions

Contributions, feature suggestions, or bug reports are welcome!  
Feel free to fork this repo or open a pull request.
