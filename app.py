# -*- coding: utf-8 -*-

import os

from flask import Flask,send_from_directory, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
@app.route('/index')
def main_index():
    """Lists available Manga"""
    return render_template('index.html',mangas = os.listdir('./static/manga'))

@app.route('/current')
def listdir():
    return '\n'.join(os.listdir('.'))

@app.route('/<path:folder>')
def list_files(folder):
    print(folder)
    folder = folder.replace('%20', ' ')
    try:
        files = os.listdir('./static/manga/{}'.format(folder))
    except FileNotFoundError:
        return 'Title {} does not exist.'.format(folder)
    return str(files)

@app.route('/read/<path:subpath>')
def manga(subpath):
    listdir = os.listdir('./static/manga/{}'.format(subpath))
    images = list(filter(lambda x: '.' in x, listdir))
    images = ['{}/{}'.format(subpath, image) for image in images]
    
    folders = list(filter(lambda x: '.' not in x, listdir))
#    folders = ['{}/{}'.format(subpath, folder) for folder in folders]
    
    return render_template('image.html', images=images, folders=folders, root = subpath)
#    return str(images) + str(folders)
#    images_path = ['{}/{}'.format(subpath,image) for image in images]
#    images_path = [image.replace('\\','/') for image in images_path]
    
#    return render_template('image.html',images=images_path, dir_name=subpath)
#    return str(images_path)

#@app.route('/Chainsawman')
#def csman():
#    images = os.listdir('./static/manga/Chainsawman 001')
#    
#    images_path = ['Chainsawman 001/{}'.format(image) for image in images]
#
#    return render_template('image.html', images=images_path)
#    return str(images_path)



if  __name__ == '__main__':
    app.run(debug=False)
