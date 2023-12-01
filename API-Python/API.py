from flask import Flask, request, jsonify

app = Flask(__name__)

#GET - Request data from a specified resource
#POST - Create a resource
#PUT  - Update a resource
#DELETE - Delete a resource

@app.route("/get-user/<user_id>", methods=["GET"])
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Enri Daja",
        "email": "enridaja9@gmail.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data)

#TESTED AND RAN ON "POSTMAN"(API TESTER APP)
@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)