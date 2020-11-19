from flask import abort, Flask, jsonify, render_template, request
from flask_cors import CORS
#from flaskext.mysql import MySQL 
#from flask_mysql_connector import MySQL # eki bug fix
import yaml
from flask_mysqldb import MySQL

app = Flask(__name__)

db = yaml.load(open('database.yaml'))
app.config['MYSQL_HOST'] = db['host']
app.config['MYSQL_USER'] = db['user']
app.config['MYSQL_PASSWORD'] = db['pass']
app.config['MYSQL_DB'] = db['db']
app.config['MYSQL_PORT'] = db['port']


# app.config['MYSQL_HOST'] = '127.0.0.1'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'eki-py-rest-mysql'
# app.config['MYSQL_PORT'] = 3308 # done solved


mysql = MySQL(app)

# mysql = MySQL() # bug fix eki
# mysql.init_app(app) # bug fix eki  #mysql = MySQL(app)
# conn = mysql.connect() # bug fix eki
# cursor =conn.cursor() 
CORS(app)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/data', methods=['POST', 'GET'])
def data():
    
    # POST a data to database
    if request.method == 'POST':
        body = request.json
        name = body['name']
        age = body['age']

        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO users VALUES(null, %s, %s)', (str(name), str(age)))
        mysql.connection.commit()
        cursor.close()
        return jsonify({
            'status': 'Data is posted to MySQL!',
            'name': name,
            'age': age
        })
    
    # GET all data from database
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        allData = []

        for i in range(len(users)):
            id = users[i][0]
            name = users[i][1]
            age = users[i][2]
            dataDict = {
                "id": id,
                "name": name,
                "age": age
            }
            allData.append(dataDict)

        return jsonify(allData)

@app.route('/data/<string:id>', methods=['GET', 'DELETE', 'PUT'])
def onedata(id):

    # GET a specific data by id
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE id = %s', (id))
        users = cursor.fetchall()
        print(users)
        data = []
        for i in range(len(users)):
            id = users[i][0]
            name = users[i][1]
            age = users[i][2]
            dataDict = {
                "id": id,
                "name": name,
                "age": age
            }
            data.append(dataDict)
        return jsonify(data)
        
    # DELETE a data
    if request.method == 'DELETE':
        cursor = mysql.connection.cursor()
        cursor.execute('DELETE FROM users WHERE id = %s', (id))
        mysql.connection.commit()
        cursor.close()
        return jsonify({'status': 'Data '+id+' is deleted on MySQL!'})

    # UPDATE a data by id
    if request.method == 'PUT':
        body = request.json
        name = body['name']
        age = body['age']

        cursor = mysql.connection.cursor()
        cursor.execute('UPDATE users SET name = %s, age = %s WHERE id = %s', (name, age, id))
        mysql.connection.commit()
        cursor.close()
        return jsonify({'status': 'Data '+id+' is updated on MySQL!'})

if __name__ == '__main__':
    app.run(debug = True)