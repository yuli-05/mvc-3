import web

urls = (
    '/delete/(.*)', 'mvc.controllers.alumnos.delete.Delete',
    '/', 'mvc.controllers.index.Index',
    '/insert', 'mvc.controllers.alumnos.insert.Insert',
    '/list', 'mvc.controllers.alumnos.list.List',
    '/update/(.*)', 'mvc.controllers.alumnos.update.Update',
    '/view/(.*)', 'mvc.controllers.alumnos.view.View',
)
app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()