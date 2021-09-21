from flask import jsonify,Flask,request

app=Flask(__name__)

income = [
    {
        "description":"salary",
        "amount":10000
    }
]
@app.route("/income")
def get_income():
    return jsonify(income)

if __name__ == '__main__':
    app.run(debug=True)