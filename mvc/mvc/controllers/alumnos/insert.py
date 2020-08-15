import web

import mvc.models.alumnos as alumnos

model_alumnos = alumnos.Alumnos()

render = web.template.render("mvc/views/alumnos/", base="template")

class Insert():

    def GET(self):
        try:
            return render.insert() # renderizando formulario.html
        except Exception as e:
            return "Error " + str(e.args)

    def POST(self):
        try:
            form = web.input()
            firstname = form.firstname
            lastname = form.lastname
            lastname2 = form.lastname2
            Matricula = form.Matricula
            Edad = form.Edad
            Fecha = form.Fecha
            Sexo = form.Sexo
            Estado = form.Estado
            model_alumnos.insert(firstname, lastname, lastname2, Matricula, Edad, Fecha, Sexo, Estado)
            web.seeother('/list')
        except Exception as e:
            print(e)
            return render.insert()