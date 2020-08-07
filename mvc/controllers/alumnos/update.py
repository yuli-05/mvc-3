import web

import mvc.models.alumnos as alumnos

model_alumnos = alumnos.Alumnos()

render = web.template.render("mvc/views/alumnos/", base="template")

class Update():

    def GET(self, Matricula):
        try:
            result = model_alumnos.view(Matricula)[0]
            return render.update(result) # renderizando formulario.html
        except Exception as e:
            return "Error " + str(e.args)
    
    def POST(self, Matricula):
        try:
            form = web.input()
            Matricula = form.Matricula
            Nombre = form.Nombre
            lastname = form.lastname
            lastname2 = form.lastname2
            Edad = form.Edad
            Fecha = form.Fecha
            Sexo = form.Sexo
            Estado = form.Estado
            result = model_alumnos.update( Matricula,Nombre, lastname, lastname2, Edad, Fecha, Sexo, Estado)
        
            web.seeother('/list')
        except Exception as e:
            print(e)
            return "error"