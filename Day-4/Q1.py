from flask import Flask, jsonify, request, abort

# create a flask application
app = Flask(__name__)

# 1) ADD → URL params
# http://127.0.0.1:5000/add/10/20
@app.route("/add/<int:num1>/<int:num2>", methods=["GET"])
def add(num1, num2):
    result = num1 + num2
    return jsonify({"operation": "add", "result": result})


# 2) SUB → JSON payload
# http://127.0.0.1:5000/sub
# Body: {"num1": 10, "num2": 5}
@app.route("/sub", methods=["POST"])
def sub():
    data = request.get_json()

    if not data or "num1" not in data or "num2" not in data:
        abort(400, description="Invalid input")

    result = data["num1"] - data["num2"]
    return jsonify({"operation": "sub", "result": result})


# 3) MULT → query params style
# http://127.0.0.1:5000/mult?num1=5&num2=3
@app.route("/mult", methods=["GET"])
def mult():
    num1 = request.args.get("num1", type=int)
    num2 = request.args.get("num2", type=int)

    if num1 is None or num2 is None:
        abort(400, description="Missing query parameters")

    result = num1 * num2
    return jsonify({"operation": "multiply", "result": result})


# 4) QUOT → division
# http://127.0.0.1:5000/quot/5/2
@app.route("/quot/<int:num1>/<int:num2>", methods=["GET"])
def quot(num1, num2):
    if num2 == 0:
        abort(400, description="Division by zero not allowed")

    result = num1 / num2
    return jsonify({"operation": "division", "result": result})


# Default test API
@app.route("/api/v1/testing", methods=["GET"])
def greet():
    return jsonify({"mesg": "welcome to rest api"})


if __name__ == "__main__":
    app.run(debug=True)