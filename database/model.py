
from .db import db


class ImageCsv(db.Document):
    """
    ImageCsv model
    """
    name = db.StringField(max_length=255, required=True)
    description = db.StringField(max_length=255, required=True)
    