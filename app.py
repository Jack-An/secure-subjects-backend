import os
from flask import Flask, jsonify, render_template, request, url_for, send_from_directory
from werkzeug.utils import secure_filename
from serverless_db_sdk import database

IS_SERVERLESS = bool(os.environ.get('SERVERLESS'))
print(IS_SERVERLESS)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/users", methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        print(request.form)
        uid = request.form.get('uid');
        user = {'uid': uid, 'name': 'test1'}
        return jsonify(data=user)
    else:
        limit = request.args.get('limit')
        data = {
            'count': limit or 2,
            'users': [{'name': 'test1'}, {'name': 'test2'}]
        }
        return jsonify(data=data)


@app.route("/login", methods=["POST"])
def login():
    phone = request.json.get("phone")
    password = request.json.get("password")
    connection = database().connection(autocommit=False)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM user where phone='{phone}' and password='{password}'")
    user = cursor.fetchone()
    connection.close()
    if not user:
        data = {'ok': False, 'data': {}}
        return jsonify(data)
    data = {'ok': True, 'data': {'id': user[0], 'name': user[1]}}

    return jsonify(data)


@app.route("/subjects")
def get_subjects_by_type():
    s_type = request.args.get("type", "single")
    pass


def get_exam_history_summary():
    pass


def create_wrong_subjects():
    pass


def get_wrong_subjects():
    pass


def get_exam_subjects():
    pass


def create_sequence_num():
    pass


@app.route("/users/<id>")
def get_user(id):
    connection = database().connection(autocommit=False)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM user')
    myresult = cursor.fetchall()
    res = []
    for x in myresult:
        tmp = []
        for i in x:
            tmp.append(i)
        res.append(tmp)

    return jsonify(data={'name': res})


# 上传文件示例
@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        if 'avatar' not in request.files:
            res = {"error": "No avatar file upload"}
            return jsonify(data=res)
        avatar = request.files['avatar']

        if avatar.filename == '':
            res = {"error": "No avatar file selected"}
            return jsonify(data=res)

        if avatar:
            filename = secure_filename(avatar.filename)
            filePath = os.path.join(app.config['UPLOAD_DIR'], filename)
            avatar.save(filePath)
            uploadUrl = url_for('uploaded_file', filename=filename)
            res = {'upload': uploadUrl}
            return jsonify(data=res)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_DIR'], filename)


# 启动服务，监听 9000 端口，监听地址为 0.0.0.0
app.run(debug=IS_SERVERLESS != True, port=9000, host='0.0.0.0')
