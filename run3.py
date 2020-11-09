from flask import *
from functools import wraps
import sqlite3
import time


DATABASE = 'dataweb.db'

app = Flask(__name__)
app.secret_key = 'mysecretkey'
app.config.from_object(__name__)

def connect_db():
    con = sqlite3.connect('dataweb.db')
    cursor = con.cursor()
    print('La base funcionò bien')

def run_query(query='',parameters=()):
    conn = sqlite3.connect('dataweb.db')
    cursor = conn.cursor()                 # Crear un cursor
    cursor.execute(query, parameters)                  # Ejecutar una consulta
    if query.upper().startswith('SELECT'):
       data= cursor.fetchall()               # Traer los resultados de un select
       
    else:
        conn.commit()                          # Hacer efectiva la escritura de datos
        data = None
         
    #cursor.close()                         # Cerrar el cursor
    #conn.close()                           # Cerrar la conexión
    #conn.close()                           # Cerrar la conexión
    
    return data




@app.route('/consultar')
def consultar():

    query = 'SELECT * FROM datosclientes'
    curs  = run_query(query)
    return render_template('consultar_v1.html', contacts = curs)

#index()

@app.route('/ajax', methods=['GET', 'POST'])             
def ajax():
        
        #a= request.args
        a = request.values.get("x", "")
        print(a)
        nombre = request.values.get("fname", "")
        #print(nombre)

    
        apellido = request.values.get("lname", "")
        #print(apellido)

        #return ('Hola Mundo')
        return render_template('tabla_v1.html', nombre = nombre, apellido = apellido, json = a)


if __name__ == '__main__':
    app.run(port = 3000, debug=True)





#connect_db()
#index()
#run_query()