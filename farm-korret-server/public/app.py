"""
Farm Korret Nig. — Python web application
Landing page for Agribusiness, Finance, Heavy Equipment & Veterinary Health.
RC-8163754
"""

from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "farm-korret-dev-key-change-in-production"

# In-memory store for demo enquiries (replace with DB in production)
enquiries = []


@app.route("/")
def index():
    """Serve the main landing page."""
    return render_template("index.html")


@app.route("/api/enquiry", methods=["POST"])
def submit_enquiry():
    """Accept contact / order enquiries from the landing page form."""
    data = request.get_json(silent=True) or request.form.to_dict()

    required = ["name", "phone", "interest", "location"]
    missing = [f for f in required if not data.get(f)]
    if missing:
        return jsonify({"ok": False, "error": f"Missing fields: {', '.join(missing)}"}), 400

    entry = {
        "id": len(enquiries) + 1,
        "name": data.get("name", "").strip(),
        "phone": data.get("phone", "").strip(),
        "email": data.get("email", "").strip(),
        "interest": data.get("interest", "").strip(),
        "location": data.get("location", "").strip(),
        "message": data.get("message", "").strip(),
        "received_at": datetime.utcnow().isoformat() + "Z",
    }
    enquiries.append(entry)

    # In production: send email, WhatsApp notification, save to DB, etc.
    print(f"[Enquiry #{entry['id']}] {entry['name']} · {entry['interest']} · {entry['location']}")

    return jsonify({
        "ok": True,
        "message": "Enquiry received. We'll get back to you shortly.",
        "id": entry["id"],
    })


@app.route("/api/enquiries")
def list_enquiries():
    """Admin-style list of received enquiries (demo only)."""
    return jsonify({"count": len(enquiries), "enquiries": enquiries})


@app.route("/health")
def health():
    return jsonify({"status": "ok", "service": "Farm Korret Nig.", "rc": "RC-8163754"})


if __name__ == "__main__":
    print("=" * 50)
    print("  Farm Korret Nig. — Agribusiness Platform")
    print("  RC-8163754")
    print("  Open http://127.0.0.1:5000")
    print("=" * 50)
    app.run(host="0.0.0.0", port=5000, debug=True)
