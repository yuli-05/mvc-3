import mysql.connector

class Alumnos():

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user='m9120ef9m0v6hwgk', 
                password='jpjcqxmkvs72d536',
                host='x3ztd854gaa7on6s.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                port=3306,
                database='mm5gzlu0osfi6uv8'
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

    def update(self, Matricula,Nombre, lastname, lastname2, Edad, Fecha, Sexo, Estado): 
        try:
            self.connect()
            query = ("UPDATE alumnos SET Nombre=%s, lastname=%s, lastname2=%s, Edad=%s, Fecha=%s, Sexo=%s, Estado=%s WHERE Matricula=%s;")
            values = (Nombre, lastname, lastname2, Edad, Fecha, Sexo, Estado, Matricula)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False


    def delete(self, Matricula): 
        try:
            self.connect()
            query = ("DELETE FROM alumnos WHERE Matricula = %s;")
            values = (Matricula,)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

objeto = Alumnos()
#objeto.delete(1718110384)

for row in objeto.select():
    print(row)