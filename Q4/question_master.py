from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200))
    op1 = db.Column(db.String(100))
    op2 = db.Column(db.String(100))
    op3 = db.Column(db.String(100))
    op4 = db.Column(db.String(100))
    correct = db.Column(db.String(10))


with app.app_context():
    db.create_all()


@app.route("/add_question", methods=["POST"])
def add_question():
    data = request.json
    q = Question(
        question=data['question'],
        op1=data['op1'],
        op2=data['op2'],
        op3=data['op3'],
        op4=data['op4'],
        correct=data['correct']
    )
    db.session.add(q)
    db.session.commit()
    return jsonify({"msg": "Question Added"})


@app.route("/get_questions", methods=["GET"])
def get_questions():
    questions = Question.query.all()
    result = []
    for q in questions:
        result.append({
            "id": q.id,
            "question": q.question,
            "op1": q.op1,
            "op2": q.op2,
            "op3": q.op3,
            "op4": q.op4,
            "correct": q.correct
        })
    return jsonify(result)


@app.route("/search_question/<int:id>", methods=["GET"])
def search_question(id):
    q = Question.query.get(id)
    if not q:
        return jsonify({"msg": "Not found"}), 404
    return jsonify({
        "id": q.id,
        "question": q.question,
        "op1": q.op1,
        "op2": q.op2,
        "op3": q.op3,
        "op4": q.op4,
        "correct": q.correct
    })


@app.route("/update_question/<int:id>", methods=["PUT"])
def update_question(id):
    q = Question.query.get(id)
    if not q:
        return jsonify({"msg": "Not found"}), 404
    data = request.json
    q.question = data['question']
    q.op1 = data['op1']
    q.op2 = data['op2']
    q.op3 = data['op3']
    q.op4 = data['op4']
    q.correct = data['correct']
    db.session.commit()
    return jsonify({"msg": "Updated"})


@app.route("/delete_question/<int:id>", methods=["DELETE"])
def delete_question(id):
    q = Question.query.get(id)
    if not q:
        return jsonify({"msg": "Not found"}), 404
    db.session.delete(q)
    db.session.commit()
    return jsonify({"msg": "Deleted"})


if __name__ == "__main__":
    app.run(debug=True)