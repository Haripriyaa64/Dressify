from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
import sqlite3
import uuid
from werkzeug.utils import secure_filename

from ml.color_detector import detect_color_combination
from ml.recommender import recommend

app = Flask(__name__)
app.secret_key = "wardrobe_secret_2024"

UPLOAD_FOLDER = os.path.join("static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ---------------- DB ----------------

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS dresses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            image TEXT,
            wear_type TEXT,
            dress_type TEXT,
            color TEXT
        )
    """)

    conn.commit()
    conn.close()


def get_db():
    conn = sqlite3.connect("database.db", timeout=10)
    conn.row_factory = sqlite3.Row
    return conn


# ---------------- USER SESSION ----------------

@app.before_request
def set_user():
    if "user_id" not in session:
        session["user_id"] = str(uuid.uuid4())


# ---------------- ROUTES ----------------

@app.route("/", methods=["GET", "POST"])
def upload():
    user_id = session["user_id"]

    if request.method == "POST":
        image = request.files.get("image")
        wear_type = request.form.get("wear_type", "")
        dress_type = request.form.get("dress_type", "")

        if not image or image.filename == "":
            flash("Please select an image.", "error")
            return redirect(url_for("upload"))

        filename = secure_filename(image.filename)
        save_path = os.path.join(UPLOAD_FOLDER, filename)
        image.save(save_path)

        colors = detect_color_combination(save_path)
        color_str = ", ".join(colors)

        conn = get_db()
        conn.execute(
            """
            INSERT INTO dresses (user_id, image, wear_type, dress_type, color)
            VALUES (?, ?, ?, ?, ?)
            """,
            (user_id, filename, wear_type, dress_type, color_str)
        )
        conn.commit()
        conn.close()

        flash(f"✓ Outfit uploaded! Detected colors: {color_str}", "success")
        return redirect(url_for("upload"))

    return render_template("upload.html")


@app.route("/delete/<int:dress_id>", methods=["POST"])
def delete_dress(dress_id):
    user_id = session["user_id"]

    conn = get_db()
    row = conn.execute(
        "SELECT image FROM dresses WHERE id=? AND user_id=?",
        (dress_id, user_id)
    ).fetchone()

    if row:
        img_path = os.path.join(UPLOAD_FOLDER, row["image"])
        if os.path.exists(img_path):
            os.remove(img_path)

        conn.execute(
            "DELETE FROM dresses WHERE id=? AND user_id=?",
            (dress_id, user_id)
        )
        conn.commit()

    conn.close()
    flash("Outfit deleted.", "info")
    return redirect(url_for("mood"))


@app.route("/mood", methods=["GET", "POST"])
def mood():
    user_id = session["user_id"]

    if request.method == "POST":
        mood_val = request.form.get("mood", "")
        occasion = request.form.get("occasion", "")
        wear_type = request.form.get("wear_type", "")

        conn = get_db()
        rows = conn.execute(
            "SELECT * FROM dresses WHERE user_id=?",
            (user_id,)
        ).fetchall()
        conn.close()

        dresses = [dict(r) for r in rows]
        results = recommend(
            dresses,
            mood=mood_val,
            occasion=occasion,
            wear_type=wear_type
        )

        return render_template("result.html", results=results)

    return render_template("select_mood.html")


# ---------------- RUN ----------------

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=7860, debug=True)