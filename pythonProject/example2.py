from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

income = [{"desc": "salary", "amount": 500}]


@app.route("/")
def index():
    return "<h1>Hello World</h1>"


@app.route("/income")
def get_income():
    return jsonify(income)


@app.route("/income", methods=["post"])
def add_income():
    income.append(request.get_json())
    res = make_response(jsonify(income), 201)
    return res


@app.route("/user/<name>")
def user(name):
    return "Hello " + name


@app.route("/headers")
def headers():
    return request.headers.get('User-Agent')


stock = {
    "fruit": {
        "apple": 100,
        "banana": 45,
        "cherry": 1000
    }
}


@app.route("/stock")
def get_collection():
    return make_response(jsonify(stock), 200)


@app.route("/stock/<collection>", methods=["put"])
def put_collection(collection):
    req = request.get_json()
    if collection in stock:
        stock[collection].update(req)
        res = make_response(jsonify({"msg": "collection updated..."}), 200)
        return res
    res = make_response(jsonify({"msg": "collection not found"}), 404)
    return res


@app.route("/stock/<collection>/<member>", methods=["delete"])
def delete_collection(collection, member):
    if collection in stock:
        if stock[collection][member]:
            del stock[collection][member]
            res = make_response(jsonify({}), 204)
            return res
        res = make_response(jsonify({"error": "member not found"}), 404)
        return res
    res = make_response(jsonify({"error": "collection not found"}), 404)
    return res


if __name__ == "__main__":
    app.run(debug=True)
