# Substitution Cipher – Flask Frontend

This project is a simple **Flask-based frontend** for a **Substitution Cipher program**.  
It provides a clean user interface to encrypt plaintext using a 26-letter substitution key, replacing the need to run the program from the terminal.

---

## Features

- User-friendly web interface
- Validates the substitution key:
  - Must contain exactly 26 characters
  - Must contain only alphabetic characters
  - Must not contain duplicate letters (case-insensitive)
- Preserves:
  - Uppercase and lowercase letters
  - Non-alphabetic characters
- Displays ciphertext in a read-only output box
- Reset button to clear inputs and output
- Clean and stable UI (no layout shifting)

---

## Tech Stack

- **Python**
- **Flask**
- **HTML & CSS**

---

## Project Structure

```bash
substitution-cipher/
├── app.py
├── templates/
│ └── index.html
├── static/
│ └── style.css
└── README.md
```

---

## How It Works

1. The user enters a 26-letter substitution key and plaintext.
2. The form submits the data to Flask using a POST request.
3. Flask validates the key.
4. If valid, the plaintext is encrypted using substitution logic.
5. The ciphertext is displayed on the same page.

The encryption logic is implemented in Python and closely follows the logic of a traditional [C-based substitution cipher program](https://github.com/mariaali111/encryption-projects/blob/main/substitution.c).

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
