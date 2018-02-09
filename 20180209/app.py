from flask import Flask,render_template,abort

app = Flask(__name__)
app.config.from_pyfile('/home/shiyanlou/Code/config.py')

@app.route('/')
def index():
    teacher = {
            'name': 'Aiden',
            'email': 'luojin@simplecloud.cn'
            }
    course = {
            'name': 'Python Basic',
            'teacher': teacher,
            'user_count': 5348,
            'price': 199.0,
            'lab': None,
            'is_private': False,
            'is_member_course': True,
            'tags': ['python', 'big data', 'linux']
            }
    return render_template('index.html',course=course)

@app.route('/user/<username>')
def user_index(username):
    if username == 'wjstud':
        abort(404)
    return render_template('user_index.html',username=username)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run()
