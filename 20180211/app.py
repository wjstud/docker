from flask import Flask,render_template,abort
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_pyfile('/home/shiyanlou/news/config.py')
engine = create_engine('mysql://root:@localhost/wjstud')
client = MongoClient('127.0.0.1',27017)

mg_db = client.shiyanlou
db = SQLAlchemy(app)

class File(db.Model):
    __tablename__ = 'file'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    content = db.Column(db.Text)
    category = db.relationship('Category')
    
    def __init__(self, title, created_time, category, content):
        self.title = title
        self.created_time = created_time
        self.category = category
        self.content = content

    def add_tag(self, tag_name):
        tag = mg_db.user.find_one({'file_id': self.id, 'tag': tag_name})
        if tag is None:
            return mg_db.user.insert_one({'file_id':self.id, 'tag': tag_name})
        else:
            return "tag is exist"

    def remove_tag(self, tag_name):
        tag = mg_db.user.find_one({'file_id': self.id, 'tag': tag_name})
        if tag is None:
            return "tag is not exist"
        else:
            return mg_db.user.delete_one({'file_id': self.id, 'tag': tag_name})
    
    @property
    def tags(self):
        return mg_db.user.find_one({'file_id': self.id})['tag']

    def __repr__(self):
        return '<File %s>' % self.title

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %s>' % self.name

@app.route('/')
def index():
    course = engine.execute('select id,title from file').fetchall()
    return render_template('index.html',course=course)

@app.route('/files/<file_id>')
def file(file_id):
    test_id = engine.execute('select id from category').fetchall()
    file_id_list = [i[0] for i in test_id]
    if int(file_id) in file_id_list:
        sql = 'select file.id,file.content,file.created_time,category.name from file,category where file.category_id=category.id and file.id={}'.format(file_id)
        value = engine.execute(sql).fetchall()
    else:
        abort(404)
    return render_template('file.html',value=value)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run(port=3000)


