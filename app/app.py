from flask import Flask, request, jsonify, render_template, redirect, url_for
import mysql.connector
import os

app = Flask(__name__)

# Database configuration
db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
}

# Serve the form at /add_data
@app.route("/add_data", methods=["GET", "POST"])
def add_data():
    if request.method == "POST":
        # Handle form submission
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        dob = request.form.get("dob")

        if not first_name or not last_name or not dob:
            return jsonify({"error": "All fields are required"}), 400

        try:
            # Connect to the database
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            # Insert data into the database
            query = "INSERT INTO data_table (first_name, last_name, dob) VALUES (%s, %s, %s)"
            cursor.execute(query, (first_name, last_name, dob))
            connection.commit()

            cursor.close()
            connection.close()

            return redirect("/add_data")  # Redirect back to the form after submission

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # Serve the form for GET requests
    return render_template("index.html")

# View All Data
@app.route("/view_data", methods=["GET"])
def view_data():
    try:
        # Connect to the database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Fetch all data from the database
        query = "SELECT * FROM data_table"
        cursor.execute(query)
        data = cursor.fetchall()

        cursor.close()
        connection.close()

        return render_template("view_data.html", data=data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)