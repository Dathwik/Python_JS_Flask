# main.py
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# ------------------ App & CORS Setup ------------------
app = Flask(__name__)

# Enable CORS for your deployed frontend
CORS(
    app,
    origins=["https://python-js-flask.onrender.com"],  # replace with your frontend URL
    supports_credentials=True,
    allow_headers=["Content-Type", "Authorization"],
    methods=["GET", "POST", "PATCH", "DELETE", "OPTIONS"]
)

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "https://python-js-flask.onrender.com"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,PATCH,DELETE,OPTIONS"
    return response

# ------------------ Database Setup ------------------
DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set!")

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ------------------ Models ------------------
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email
        }

# ------------------ Routes ------------------
@app.route("/")
def root():
    return "Backend is running", 200

@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    return jsonify({"contacts": [c.to_json() for c in contacts]})

@app.route("/create_contact", methods=["POST"])
def create_contact():
    try:
        data = request.json
        first_name = data.get("firstName")
        last_name = data.get("lastName")
        email = data.get("email")

        if not first_name or not last_name or not email:
            return jsonify({"message": "You must provide first name, last name, and email"}), 400

        if Contact.query.filter_by(email=email).first():
            return jsonify({"message": "Email already exists"}), 400

        new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
        db.session.add(new_contact)
        db.session.commit()
        return jsonify(new_contact.to_json()), 201

    except Exception as e:
        return jsonify({"message": str(e)}), 500

@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    try:
        contact = Contact.query.get(user_id)
        if not contact:
            return jsonify({"message": "User not found"}), 404

        data = request.json
        contact.first_name = data.get("firstName", contact.first_name)
        contact.last_name = data.get("lastName", contact.last_name)
        contact.email = data.get("email", contact.email)

        db.session.commit()
        return jsonify(contact.to_json()), 200

    except Exception as e:
        return jsonify({"message": str(e)}), 500

@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    try:
        contact = Contact.query.get(user_id)
        if not contact:
            return jsonify({"message": "User not found"}), 404

        db.session.delete(contact)
        db.session.commit()
        return jsonify({"message": "User deleted!"}), 200

    except Exception as e:
        return jsonify({"message": str(e)}), 500

# ------------------ Create Tables on Startup ------------------
with app.app_context():
    db.create_all()
