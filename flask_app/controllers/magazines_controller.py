from crypt import methods
from re import M
from flask import render_template, redirect, session, request, flash
import flask 
from flask_app import app
from werkzeug.utils import secure_filename
import os


from flask_app.models.users import User

from flask_app.models.magazines import Magazine

@app.route('/new/shark')
def new_magazine():

    if 'usuario_id' not in session:
        return redirect('/')
    formulario = {
        "id": session['usuario_id']
    }

    user = User.get_by_id(formulario)
    
    return render_template('new_magazine.html', user=user)



@app.route('/create/magazine', methods=['POST'])
def create_magazine():
    if 'usuario_id' not in session: 
        return redirect('/')
    

    if not Magazine.valida_magazine(request.form): 
        return redirect('/new/shark')

    if 'imagen' not in request.files:
        flash('imagen no encontrada', 'revista')
        return redirect('/new/shark')
    
    imagen= request.files['imagen']

    if imagen.filename == '':
        flash('nombre de la imagen vacio','revista')
        return redirect ('/new/shark')
    
    nombre_imagen = secure_filename(imagen.filename)
    imagen.save(os.path.join(app.config['UPLOAD_FOLDER'], nombre_imagen))
    formulario= {
        "title" : request.form['title'],
        "description" : request.form['description'],
        "nombre_comun" : request.form['nombre_comun'],
        "habitos" : request.form['habitos'],
        "user_id": request.form['user_id'],
        "distribucion_col" : request.form['distribucion_col'],
        "imagen" : nombre_imagen
    }

    Magazine.save(formulario)
    return redirect('/dashboard')



@app.route('/like', methods= ['POST'])
def like_shark ():
    Magazine.likes(request.form)
    return redirect('/dashboard')

@app.route ('/tiburones', methods=['POST'])
def contar():
    Magazine.insert_like(request.form)
    return redirect ('/show/sharks/'+ request.form['magazine_id'] )



@app.route('/show/sharks/<int:id>') 
def show_magazine(id):
    if 'usuario_id' not in session:  
        return redirect('/')

    formulario = {
        "id": session['usuario_id']
    }
    user = User.get_by_id(formulario) 
    formulario_m = { "id": id }

    mgazine = Magazine.get_by_id(formulario_m)
    print(mgazine)
    mag = Magazine.get_all()
    likes=[]
    data = {}
    for revista in mag:
        num_likes= Magazine.contar_likes(revista.id)
        n = num_likes[0]['num_likes']
        data[revista]= n


    return render_template('show_magazine.html', user=user, magazine=mgazine, data=data)






@app.route('/delete/magazine/<int:id>')
def delete_magazine(id):
    if 'usuario_id' not in session: 
        return redirect('/')
    
    formulario = {"id": id}
    Magazine.delete(formulario)

    return redirect('/dashboard')


