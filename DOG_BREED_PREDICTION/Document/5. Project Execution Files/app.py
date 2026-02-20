from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    breeds = []
    train_path = os.path.join(app.config["UPLOAD_FOLDER"], "train")

    if os.path.exists(train_path):
        for breed in os.listdir(train_path)[:8]:  # show 8 breeds only
            img_folder = os.path.join(train_path, breed)
            if os.path.isdir(img_folder):
                img = os.listdir(img_folder)[0]
                breeds.append({
                    "name": breed.replace("_", " ").title(),
                    "img": f"/{train_path}/{breed}/{img}"
                })

    return render_template("about.html", breeds=breeds)


@app.route("/predict")
def predict():
    return render_template("predict.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/output", methods=["POST"])
def output():
    file = request.files["image"]
    path = os.path.join("uploads", file.filename)
    file.save(path)

    return render_template("output.html",
                           breed="German Shepherd",
                           confidence="99.87%")


if __name__ == "__main__":
    app.run(debug=True)
