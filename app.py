from flask import Flask, request
import sqlite3
import json
app = Flask(__name__)



@app.route("/get/data", methods=("GET","POST"))
def login():
    connection = sqlite3.connect('database.db')
    conn = connection.cursor()
    response = conn.execute('SELECT * FROM vacation')
    response = response.fetchall()
    connection.close()
    return response
            


@app.route('/post/data',methods=['GET','POST'])
def apply():
    if request.method == "POST":
        data = json.loads(request.data)
        name = data['name']
        email = data['email']
        phone = data['phone']
        country = data['country']
        message = data['message']
        print(name,email,phone,country,message)
        connection = sqlite3.connect('database.db')
        cur = connection.cursor()
        cur.execute(
            "INSERT INTO vacation (name,email,phone,country,message) VALUES (?, ?, ?, ?, ?)",
                (name,email,phone,country,message)
                        )
        connection.commit()
        # response = cur.execute('SELECT * FROM apply WHERE name = ?', (name,))
        # has_courses = response.fetchone()
        connection.close()
        return {"status":"success", "message":"data submitted successfully"}



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088, debug=True)