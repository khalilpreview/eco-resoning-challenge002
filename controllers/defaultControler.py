
from flask import Response, request
from database.model import ImageCsv
from flask_restful import Resource



class HomeController(Resource):

    def get(self):
        return {
            "detail" : "An API is required to request image frames based on  depth_min  and  depth_max .",
            "genral_data": "data",
            "api_valid_end_points":{
                "/api/" : "API home"
            } 
        }

class UploadCsvController(Resource):

    def get(self):

        images = ImageCsv.objects().to_json()

        return Response(images, mimetype="application/json", status=200)

    def post(self):

        data = request.get_json()

        img = ImageCsv(**data).save()

        id = img.id

        return {
            "detail" : f"{id} Image csv uploaded to the database"
        } 

class GetImageFramesController(Resource):

    def get(self):
        return {
            "detail" : "",
            "genral_data": "data"
        }