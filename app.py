from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'snippets',
    'port': 3306
}

# Function to establish a connection to the MySQL database
def get_database_connection():
    return mysql.connector.connect(**db_config)

# GET request to retrieve all code snippets
@app.route('/code_snippets', methods=['GET'])
def get_code_snippets():
    try:
        connection = get_database_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT name, code FROM code_snippets")
        snippets = [{"name": name, "code": code} for (name, code) in cursor.fetchall()]
        cursor.close()
        connection.close()
        return {"code_snippets": snippets}
    except Exception as e:
        return {"error": str(e)}

# POST request to create a new code snippet
@app.route('/code_snippets', methods=['POST'])
def create_code_snippet():
    try:
        data = request.get_json(force=True)
        name = data['name']
        code = data['code']
        connection = get_database_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO code_snippets (name, code) VALUES (%s, %s)", (name, code))
        connection.commit()
        cursor.close()
        connection.close()
        return {"message": "Code snippet created successfully!"}
    except Exception as e:
        return {"error": str(e)}

# PUT request to update an existing code snippet
@app.route('/code_snippets/<snippet_name>', methods=['PUT'])
def update_code_snippet(snippet_name):
    try:
        data = request.get_json(force=True)
        code = data['code']
        connection = get_database_connection()
        cursor = connection.cursor()
        cursor.execute("UPDATE code_snippets SET code = %s WHERE name = %s", (code, snippet_name))
        connection.commit()
        cursor.close()
        connection.close()
        return {"message": "Code snippet updated successfully!"}
    except Exception as e:
        return {"error": str(e)}

# DELETE request to delete a code snippet
@app.route('/code_snippets/<snippet_name>', methods=['DELETE'])
def delete_code_snippet(snippet_name):
    try:
        connection = get_database_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM code_snippets WHERE name = %s", (snippet_name,))
        connection.commit()
        cursor.close()
        connection.close()
        return {"message": "Code snippet deleted successfully!"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    app.run()
