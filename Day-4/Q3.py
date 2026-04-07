from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

# create Flask app
app = Flask(__name__)

# database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///emps.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initialize ORM
db = SQLAlchemy(app)


# -------------------- MODEL --------------------
class Emp(db.Model):
    code = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    loc  = db.Column(db.String(100))

    def to_dict(self):
        return {
            "code": self.code,
            "name": self.name,
            "loc": self.loc
        }


# -------------------- ROUTES --------------------

# Home route (to avoid 404)
@app.route("/")
def home():
    return jsonify({"msg": "Employee API is running"})


# 1️⃣ CREATE (Insert)
@app.route("/create_emp", methods=["POST"])
def create_emp():
    data = request.get_json()

    if not data or not all(k in data for k in ("code", "name", "loc")):
        abort(400, description="Invalid input")

    # check if employee already exists
    if Emp.query.get(data["code"]):
        abort(400, description="Employee already exists")

    emp = Emp(code=data["code"], name=data["name"], loc=data["loc"])

    db.session.add(emp)
    db.session.commit()

    return jsonify({"status": "Employee added"}), 201


# 2️⃣ READ (List all)
@app.route("/list_emp", methods=["GET"])
def list_emps():
    emps = Emp.query.all()
    return jsonify([e.to_dict() for e in emps]), 200


# 3️⃣ UPDATE
@app.route("/update_emp/<int:code>", methods=["PUT"])
def update_emp(code):
    emp = Emp.query.get(code)

    if not emp:
        abort(404, description="Employee not found")

    data = request.get_json()

    if not data:
        abort(400, description="Invalid input")

    emp.name = data.get("name", emp.name)
    emp.loc  = data.get("loc", emp.loc)

    db.session.commit()

    return jsonify({"status": "Employee updated"}), 200


# 4️⃣ DELETE
@app.route("/delete_emp/<int:code>", methods=["DELETE"])
def delete_emp(code):
    emp = Emp.query.get(code)

    if not emp:
        abort(404, description="Employee not found")

    db.session.delete(emp)
    db.session.commit()

    return jsonify({"status": "Employee deleted"}), 200


# -------------------- MAIN --------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # create DB tables

    app.run(debug=True)


# FOR GET
## http://127.0.0.1:5000/list_emp 

# FOR POST
## http://127.0.0.1:5000/create_emp