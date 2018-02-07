from flask import Flask,render_template,abort
import os,json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    titles = []
    files_path = '/home/shiyanlou/files/'
    files_list = os.listdir(files_path)
    file_path_list = [files_path+i for i in files_list]
    for i in file_path_list:
        with open(i) as f:
            file_dict = json.loads(f.read())
            titles.append(file_dict['title'])
    return render_template('index.html',titles=titles)

@app.route('/files/<filename>')
def file(filename):
    if filename == 'helloshiyanlou':
        with open('/home/shiyanlou/files/{}.json'.format(filename)) as f:
            value = f.read()
    elif filename == 'helloworld':
        with open('/home/shiyanlou/files/{}.json'.format(filename)) as f:
            value = f.read()
    else:
        abort(404)
    return render_template('file.html',value=value)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run(port=3000,debug=True)
