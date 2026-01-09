# Caeser Cipher – Flask Frontend

This project is a simple **Flask-based frontend** for a **Caeser Cipher program**.  
It provides a clean user interface to encrypt plaintext using a numeric shift key.

---

## Features

- User-friendly web interface
- Accepts an integer key (positive or negative)
- Preserves:
  - Uppercase and lowercase letters
  - Non-alphabetic characters
- Supports wrap-around shifting (A ↔ Z)
- Displays ciphertext in a read-only output box
- Reset button to clear inputs and output
- Clean and stable UI

---

## Tech Stack

- **Python**
- **Flask**
- **HTML & CSS**

---

## Project Structure

```bash
caeser-cipher/
├── app.py
├── templates/
│ └── index.html
├── static/
│ └── style.css
└── README.md
```

---

## How It Works

1. The user enters a numeric shift key and plaintext.
2. The form submits the data to Flask using a POST request.
3. Flask validates the key as an integer.
4. Each alphabetic character is shifted by the given key.
5. The ciphertext is displayed on the same page.

The encryption logic is implemented in Python and closely follows the logic of a traditional [C-based caeser cipher program](https://github.com/mariaali111/encryption-projects/blob/main/caeser.c).

---

## How to Run the Project

### 1. Install Flask

```bash
pip install flask
```

### 2. Run the application

```bash
python app.py
```

### 3. Open in browser
Go to:<br>
http://127.0.0.1:5000

---
