import sqlite3 as sql
def crearTabla():
  con = sql.connect('colegio.db')
  cur = con.cursor()
  query = "CREATE TABLE IF NOt EXISTS Alumnos (ID INTEGER PRIMARY KEY NOT NULL, NOMBRE TEXT NOT NULL, APELLIDO TEXT NOT NULL);"
  cur.execute(query)
  con.commit()
  cur.close()
  con.close()

def insertData():
  alumnos = [
    (1,'Juan','Montalvo'),
    (2,'Jaime','Lopez'),
    (3,'Pedro','Gómez'),
    (4,'Cristobal','Colón'),
    (5,'Pedro','Pascal'),
    (6,'José','Llanos'),
    (7,'Eva','Espín'),
    (8,'Frank','Posso'),
  ]
  con = sql.connect('colegio.db')
  cur = con.cursor()
  query = "INSERT INTO Alumnos VALUES (?,?,?)"
  cur.executemany(query,alumnos)
  con.commit()
  cur.close()
  con.close()

def buscaAlumno(nombre):
  con = sql.connect('colegio.db')
  cur = con.cursor()
  query = f"SELECT * FROM Alumnos WHERE NOMBRE like '{nombre}%';"
  dset = cur.execute(query)  
  for d in dset:
    print(d)        
  cur.close()
  con.close()


crearTabla()
insertData()
buscaAlumno('J')
