from flask import Flask, render_template, json, request
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'Bucketlist'
app.config['MYSQL_HOST'] = '0.0.0.0'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/signup')
def showSignUp():
    return render_template('signup.html')


@app.route('/api/signup', methods=['POST'])
def signUp():

        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        conn = mysql.connection
        cursor = conn.cursor()
        _hashed_password = generate_password_hash(_password)
        cursor.callproc('sp_createUser', (_name, _email, _hashed_password))

        data = cursor.fetchall()


        if len(data) is 0:
         conn.commit()
         return json.dumps({'message':'User created successfully !'})
        else:
         return json.dumps({'error':str(data[0])})



if __name__ == "__main__":
    app.run()