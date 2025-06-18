
# 🕵️‍♂️ T-Rex Steganography Tool v1.0

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

Install dependencies via `pip`:

```bash
pip install pillow stepic cryptography colorama
