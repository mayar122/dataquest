import os
from flask import Flask, request, render_template

# Initialize Flask app
app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Home route
@app.route("/")
def index():
    return render_template("index.html")

# Upload and show image
@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return "No file uploaded"

    file = request.files["file"]
    if file.filename == "":
        return "No selected file"

    img_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(img_path)

    return render_template("result.html", image_url=img_path)

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)
