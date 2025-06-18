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

Install dependencies via `pip`:

```bash
pip install pillow stepic cryptography colorama
```

---

## 🚀 Usage

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

### 🔓 Decode
1. Load the encoded image
2. If encrypted, enter password to decrypt
3. View or save the decoded message

---

## 🧪 Example

**Encoding a message:**
```text
Enter image name or path: input.png
[01] Enter text manually
Enter the text to encode: Hello world!
Do you want to provide a password? (Y/N): y
Enter password: mysecret123
Enter filename to save: secret_output.png
✅ Encoded image saved as secret_output.png
```

**Decoding a message:**
```text
Enter encoded image path: secret_output.png
🔒 This image has a password-protected message.
Enter password: mysecret123
✅ Decoded message: Hello world!
```

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
