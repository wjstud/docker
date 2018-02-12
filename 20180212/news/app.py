from flask import Flask,render_template
from flask.ext.sqlalchemy import SQLAlchemy
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_pyfile('/home/shiyanlou/news/config.py')
client = MongoClient('127.0.0.1',27017)
mongo = client.shiyanlou
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
        file_item = mongo.file_tag.find_one({'file_id': self.id})
        if file_item:
            tags = file_item['tags']
            if tag_name not in tags:
                tags.append(tag_name)
            mongo.file_tag.update_one({'file_id': self.id},{'$set': {'tags':tags}})
        else:
            tags = [tag_name]
            mongo.file_tag.insert_one({'file_id': self.id,'tags': tags})
        return tags

    def remove_tag(self, tag_name):
        file_item = mongo.file_tag.find_one({'file_id': self.id})
        if file_item:
            tags = file_item['tags']
            try:
                new_tags = tags.remove(tag_name)
            except:
                return '%s is not exist' % tag_name
            mongo.file_tag.update_one({'file_id': self.id},{'$set': {'tags': new_tags}})
            return '%s is remove' % tag_name
        return 'file_item is error'
    
    @property
    def get_tags(self):
        file_item = mongo.file_tag.find_one({'file_id': self.id})
        if file_item:
            tags = file_item['tags']
            return tags
        else:
            return 'file_item is error'

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
    return render_template('index.html',files=File.query.all())

@app.route('/files/<file_id>')
def file(file_id):
    file_item = File.query.get_or_404(file_id)
    return render_template('file.html',file_item=file_item)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run(port=3000)


