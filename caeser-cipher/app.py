from flask import Flask, render_template, request

app = Flask(__name__)


# Cipher logic
def encipher(key, plaintext):
    result = ""

    for char in plaintext:
        if char.islower():
            result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        elif char.isupper():
            result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            result += char

    return result


# Flask route
@app.route("/", methods=["GET", "POST"])
def index():
    key = ""
    plaintext = ""
    ciphertext = ""
    error = None

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
        
        key_input = request.form.get("key", "")
        plaintext = request.form.get("plaintext", "")

        # Validate key
        try:
            key = int(key_input)
            ciphertext = encipher(key, plaintext)
        except ValueError:
            error = "Key must be an integer."


    return render_template(
        "index.html",
        key=key,
        plaintext=plaintext,
        ciphertext=ciphertext,
        error=error
    )



if __name__ == "__main__":
    app.run(debug=True)
