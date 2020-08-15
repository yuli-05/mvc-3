import web

import mvc.models.alumnos as alumnos

model_alumnos = alumnos.Alumnos()

render = web.template.render("mvc/views/alumnos/", base="template")

class Delete():

    def GET(self, Matricula):
        try:
            result = model_alumnos.view(Matricula)[0]
            return render.delete(result) # renderizando formulario.html
        except Exception as e:
            return "Error " + str(e.args)

    def POST(self, Matricula):
        try:
            form = web.input()
            Matricula = form['Matricula']
            result = model_alumnos.delete(Matricula)
            web.seeother('/list')
        except Exception as e:
            print(e)
            return "error"