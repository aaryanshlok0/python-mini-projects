# 🔐 Text Encoder and Decoder

## 📌 Overview
This Python script provides a simple way to encode and decode text using a predefined character mapping. It allows users to enter text and choose whether to encode or decode it. The encoding process involves character substitution, random string insertion, and minor rearrangements to enhance security.

## ✨ Features
✅ Encode text using a predefined dictionary-based character mapping.
✅ Decode encoded text back to its original form.
✅ Handles special cases for short text (less than 3 characters).
✅ Uses `str.maketrans()` for efficient character substitution.
✅ Adds random characters during encoding to obscure patterns.

## ⚙️ How It Works
1️⃣ The user is prompted to enter their name.
2️⃣ The user inputs the text they want to encode or decode.
3️⃣ The user selects one of the following options:
   - Press `1️⃣` to encode the text.
   - Press `2️⃣` to decode the text.
4️⃣ The program performs the respective operation and outputs the result.

## 🔄 Encoding Process
- 📝 If the text has fewer than 3 characters, it is simply reversed.
- 📝 If the text has 3 or more characters:
  - The first character is moved to the end.
  - A random 3-character string is added at the beginning.
  - The resulting string undergoes character substitution using a dictionary.

## 🔄 Decoding Process
- 🔄 If the text has fewer than 3 characters, it is simply reversed.
- 🔄 If the text has 3 or more characters:
  - The first 3 characters are removed.
  - The last character is moved to the front.
  - The character substitution is reversed using the decoding dictionary.

## 🎯 Example
### 🔒 Encoding
#### 📝 Input:
```
hello
```
#### 🔑 Output (Example):
```
tqozdduo
```

### 🔓 Decoding
#### 📝 Input:
```
tqozdduo
```
#### 🔑 Output:
```
hello
```

## 🛠️ Requirements
- ✅ Python 3.x

## 🚀 How to Run
1️⃣ Copy the script into a Python file (e.g., `encoder_decoder.py`).
2️⃣ Run the script using:
   ```sh
   python encoder_decoder.py
   ```
3️⃣ Follow the on-screen instructions.

## 📜 License
This project is open-source and free to use. 🔓

