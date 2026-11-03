
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Contact Form API
@app.route("/contact", methods=["POST"])
def contact():

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    if not name or not email or not message:
        return jsonify({
            "success": False,
            "message": "Please fill in all fields."
        }), 400

    # Save contact message in a text file
    with open("messages.txt", "a", encoding="utf-8") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Message: {message}\n")
        file.write("-" * 40 + "\n")

    return jsonify({
        "success": True,
        "message": "Your message has been submitted successfully!"
    })


if __name__ == "__main__":
    app.run(debug=True)
