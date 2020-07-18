import mysql.connector

class Alumnos():

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user='root', 
                password='',
                host='127.0.0.1',
                port=3306,
                database='escuela'
                )
            self.cursor = self.cnx.cursor()
        except Exception as e:
            print(e)

    def select(self):
        try:
            self.connect()
            query = ("SELECT * from alumnos;")
            self.cursor.execute(query)
            result = []
            for row in self.cursor:
                r = {
                    'id_alumno':row[0],
                    'Nombre':row[1],
                    'lastname':row[2],
                    'lastname2':row[3],
                    'Matricula':row[4],
                    'Edad':row[5],
                    'Fecha':row[6],
                    'Sexo':row[7],
                    'Estado':row[8]
                }
                result.append(r)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
            result = []
            return result

objeto = Alumnos()
objeto.connect()

for row in objeto.select():
    print(row)