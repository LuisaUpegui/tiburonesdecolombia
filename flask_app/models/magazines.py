from pickle import TRUE
from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Magazine:

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.nombre_comun = data['nombre_comun']
        self.habitos = data['habitos']
        self.distribucion_col = data['distribucion_col']
        self.user_id=data['user_id']

        self.imagen=data['imagen']

        self.update_at=data['updated_at']
        self.created_at=data['created_at']

        self.first_name = data['first_name']
        self.last_name = data['last_name']



    

    #Funcion que valida los datos 
    @staticmethod
    def valida_magazine(formulario):
        es_valido = True
        

        if len(formulario['title']) < 4:
            flash("El nombre del tiburón debe tener al menos 4 caracteres", "revista")
            es_valido = False
        
        if len(formulario['description']) < 10:
            flash("La descripción del tiburón debe tener al menos 10 caracteres", "revista")
            es_valido = False
                
        
        return es_valido 
    
    #Funcion para guardar 
    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO magazines (title,  description,nombre_comun, habitos, distribucion_col,imagen, user_id) VALUES ( %(title)s, %(description)s, %(nombre_comun)s,%(habitos)s,%(distribucion_col)s,%(imagen)s,%(user_id)s )"
        nuevoId = connectToMySQL('shark').query_db(query, formulario)
        return nuevoId

##ACA SERIA EL ORDER BY 
    @classmethod
    def get_all(cls):
        query = "SELECT magazines.*, first_name, last_name FROM magazines LEFT JOIN users ON users.id = magazines.user_id ORDER BY magazines.title" 
        results = connectToMySQL('shark').query_db(query) 
        magazines = []
        for m in results:
            magazines.append(cls(m)) 
        return magazines

    #Me trae toda la info de las spp
    @classmethod
    def get_by_id(cls, formulario): 
        query = "SELECT magazines.*, first_name, last_name FROM magazines LEFT JOIN users ON users.id = magazines.user_id WHERE magazines.id = %(id)s "
        result = connectToMySQL('shark').query_db(query, formulario) 
        m= cls(result[0]) 
        return m
    

    @classmethod
    def get_user_magazines(cls, formulario):
        query = "SELECT * FROM magazines LEFT JOIN users ON users.id = magazines.user_id WHERE users.id = %(id)s "
        results = connectToMySQL('shark').query_db(query, formulario)
        magazines= []
        for a in results:
            magazines.append(cls(a))
        return magazines

    #Elimina la info de la sp
    @classmethod
    def delete(cls, formulario): 
        query = "DELETE FROM magazines WHERE id = %(id)s"
        result = connectToMySQL('shark').query_db(query, formulario)
        return result

    #Agrega los like a la bd
    @classmethod
    def likes(cls, formulario): 
        query = "INSERT INTO likes (user_id, magazine_id) VALUES (%(user_id)s,%(magazine_id)s)"
        result = connectToMySQL('shark').query_db(query, formulario)
        return result

    #Cuenta los likes y "crea la nueva vble num_likes"
    @classmethod
    def contar_likes(cls, data):
        id={"id":data}
        query= "SELECT count(magazine_id) as num_likes from likes where magazine_id= %(id)s"
        result = connectToMySQL('shark').query_db(query, id)
        return result

    #Permite que el usuario de SOLO like una vez
    @classmethod
    def insert_like(cls, data): 
        query= "SELECT * FROM likes WHERE magazine_id = %(magazine_id)s && user_id= %(user_id)s"
        result= connectToMySQL('shark').query_db(query,data)
        if result: 
            return  flash("Lo siento, ya le diste like" ,'revista')
        else : 
            cls.likes(data)
            return TRUE



