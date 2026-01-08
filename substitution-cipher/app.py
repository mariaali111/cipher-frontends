from flask import Flask, render_template, request

app = Flask(__name__)


# Cipher logic
def encipher(key, plaintext):
    result = ""

    for char in plaintext:
        if char.isupper():
            index = ord(char) - ord('A')
            result += key[index].upper()
        elif char.islower():
            index = ord(char) - ord('a')
            result += key[index].lower()
        else:
            result += char

    return result

def validate_key(key):
    if len(key) != 26:
        error = "Key must contain exactly 26 characters."

    if not key.isalpha():
        error = "Key must only contain alphabetic characters."
        
    if len(set(key.lower())) != 26:
        error = "Key must not contain repeated characters."

    return None


# Flask route
@app.route("/", methods=["GET", "POST"])
def index():
    key = ""
    plaintext = ""
    ciphertext = ""
    error = ""

    if request.method == "POST":
        # Handle reset
        if request.form.get("reset"):
            return render_template(
                "index.html",
                key="",
                plaintext="",
                ciphertext="",
                error=None
            )
        
        key = request.form.get("key")
        plaintext = request.form.get("plaintext", "")

        error = validate_key(key)
                 
        if not error:
            ciphertext = encipher(key, plaintext)

    return render_template(
        "index.html", 
        error=error, 
        ciphertext=ciphertext,
        key=key,
        plaintext=plaintext
    )



if __name__ == "__main__":
    app.run(debug=True)