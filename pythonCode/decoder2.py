from flask import jsonify,Flask,make_response,request

app=Flask(__name__)

stock={"fruit":
    {
        "apple":100,
        "bannana":500
    },
"veg":
    {
        "methe":60,
        "palak":70
    }
}
@app.route('/stock')
def get_stock():
    res = make_response(jsonify(stock),200)
    return res

@app.route("/stock/<collection>")
def get_collection(collection):
    if collection in stock:
        res = make_response(jsonify(stock[collection]),200)
        return res
    res = make_response(jsonify({"error":"not found"}),404)
    return res

@app.route("/stock/<collection>/<member>")
def get_member(collection,member):
    if collection in stock:
        member = stock[collection].get(member)
        if member:
            res = make_response(jsonify(member),200)
            return res
        res = make_response(jsonify({"error":"not found"}),484)
        return res
    res = make_response(jsonify({"error":"not found"}),404)
    return res

@app.route("/stock/<collection>",methods = ["put"])
def put_collection(collection):
    req = request.get_json()
    if collection in stock:
        stock[collection] = req
        res = make_response(jsonify({"msg":"collection updated.."}),200)
        return res
    stock[collection] = req
    res = make_response(jsonify({"msg":"collection created"}),201)
    return res
    res = make_response(jsonify({"Error": "Not Found"}), 404)
    return res

@app.route("/stock/<collection>", methods=["DELETE"])
def delete_collection(collection):
    if collection in stock:
        del stock[collection]
        res = make_response(jsonify({"msg": "Deleted...."}), 204)
        return res
    else:
        res = make_response(jsonify({"Erro": "Collection not present"}), 404)
        return res
    # handle errors
"""
@app.route("/stock/<collection>,<member>", methods=["DELETE"])
def delete_collection(collection,member):
    if collection in stock:
        if member in stock[collection]:
            del stock[collection][member]
            res = make_response(jsonify({"msg": "Deleted...."}), 204)
            return res
        res = make_response(jsonify({"error ":"member not found"}),404)
        return res


    res = make_response(jsonify({"Erro": "Collection not present"}), 404)
    return res
 """
@app.route("/stock/<collection>/<member>",methods=["DELETE"])
def del_member(member,collection):
    if collection in stock:
        if member in stock[collection]:
            del stock[collection][member]
            return make_response(jsonify({"msg": "deleted"}), 200)
        return make_response(jsonify({"msg": "no member to delete"}))
    return make_response(jsonify({"msg": "no collection to delete"}))




if __name__ == '__main__':
    app.run(debug=True)

"""
@app.route("/stock/<collection>", methods=["PUT"])
def put_collection(collection):
    req=request.get_json()
    if collection in stock:
        stock[collection]=req
        res=make_response(jsonify({"msg":"collection updated"}),200)
        return res
    #either create or we need to send error saiung record not found for updation
    stock[collection]=req
    res=make_response(jsonify({"msg":"collection cteated"}),201)
    return res
    
    @app.route("/stock/<collection>", methods=["PUT"])
def put_collection(collection):
    req = request.get_json()
    if collection in stock:
        # original = stock[collection]
        # for key,value in req.items():
        #     if key in original:
        #         original[key] = value
        #     else:
        #         original[key] = value
        stock[collection] = req
        res = make_response(jsonify({"msg":"Collection updated.."}), 200)
        return res
    # stock[collection] = req
    # res= make_response(jsonify({"msg ":"collection updated.."}), 200)
    #         return res
    #     # stock[collection] = req
    #     # res= make_response(jsonify({"msg

onkar code 
@app.route("/stock/<collection>", methods=["PUT"])
def put_collection(collection):
    req = request.get_json()
    if collection in stock:
        stock[collection] = req
        res = make_response(jsonify({"msg":"collection updated.."}), 200)
        return res
    # either create or we need send error saying record not found for updation
    stock[collection] = req
    res = make_response(jsonify({"msg": "collection created..."}), 201)
    return res



"""