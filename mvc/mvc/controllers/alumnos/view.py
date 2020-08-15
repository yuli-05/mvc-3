import web

import mvc.models.alumnos as alumnos

model_alumnos = alumnos.Alumnos()

render = web.template.render("mvc/views/alumnos/", base="template")

class View():

    def GET(self, Matricula):
        try:
            result = model_alumnos.view(Matricula)[0]
            return render.view(result) # renderizando formulario.html
        except Exception as e:
            return "Error " + str(e.args)