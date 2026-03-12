from flask import Flask, request, jsonify 
app = Flask(__name__) 
users = []

# CREATE 
@app.route("/users", methods=["POST"]) 
def create_user(): 
    data = request.json 
    users.append(data) 
    return jsonify(data), 201

# READ ALL 
@app.route("/users", methods=["GET"]) 
def get_users(): 
    return jsonify(users), 200

# READ ONE 
@app.route("/users/<int:index>", methods=["GET"]) 
def get_user(index): 
 if index <= len(users): 
   return jsonify(users[index-1]), 200 
 return jsonify({"error": "Utilisateur non trouvé"}), 404

# UPDATE 
@app.route("/users/<int:index>", methods=["PUT"]) 
def update_user(index): 
 if index < len(users): 
    users[index-1] = request.json 
    return jsonify(users[index-1]), 200 
 return jsonify({"error": "Utilisateur non trouvé"}), 404

if __name__ == "__main__": 
    app.run(debug=True)