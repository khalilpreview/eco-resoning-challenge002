from flask import redirect
from controllers import defaultControler



def configure_routes(api, app):

    api.add_resource(defaultControler.HomeController, '/api/', endpoint="api")
    api.add_resource(defaultControler.UploadCsvController , '/api/upload-csv/', endpoint="api-upload-csv")
    # api.add_resource(defaultControler. , '/api/', endpoint="")


    @app.route('/')
    def default_api_home():
        return redirect("/api/")


    @app.errorhandler(404)
    def not_found(e):
        return redirect("/api/")

