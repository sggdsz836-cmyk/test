from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage (resets on redeploy/restart; fine for testing)
messages = []


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name", "").strip()[:40]
        text = request.form.get("message", "").strip()[:200]
        if name and text:
            messages.insert(0, {"name": name, "text": text})
        return redirect(url_for("home"))
    return render_template("index.html", messages=messages[:20])


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=True)
