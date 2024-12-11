from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


contacts = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify(contacts)

@app.route('/contacts', methods=['POST'])
def add_contact():
    data = request.get_json()


    if not isinstance(data.get('phone'), int):
        return jsonify({"error": "Phone number must be an integer!"}), 400

    
    if not data.get('name') or not data.get('email'):
        return jsonify({"error": "Name and email are required!"}), 400

    contacts.append(data)
    return jsonify({"message": "Contact added successfully!"}), 201

@app.route('/contacts/<int:index>', methods=['DELETE'])
def delete_contact(index):
    if 0 <= index < len(contacts):
        contacts.pop(index)
        return jsonify({"message": "Contact deleted successfully!"})
    return jsonify({"error": "Invalid contact index!"}), 404

if __name__ == '__main__':
    app.run(debug=True)
