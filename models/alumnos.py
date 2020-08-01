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


    def view(self,Matricula):
        try:
            self.connect()
            query = ("SELECT * from alumnos where Matricula = %s;")
            values = (Matricula,)
            self.cursor.execute(query, values)
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
            #result = 
            #return result


    def insert(self, Nombre, lastname, lastname2, Matricula, Edad, Fecha, Sexo, Estado):
        try:
            self.connect()
            query = ("INSERT INTO alumnos(Nombre, lastname, lastname2, Matricula, Edad, Fecha, Sexo, Estado) values(%s,%s,%s,%s,%s,%s,%s,%s);")
            values = (Nombre, lastname, lastname2, Matricula, Edad, Fecha, Sexo, Estado)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False
            


objeto = Alumnos()
objeto.connect()
#objeto.insert("lupita","Espinoza","Riveros",1718110388,20,"2000/04/05","Femenino","Soltera")

for row in objeto.select():
    print(row)