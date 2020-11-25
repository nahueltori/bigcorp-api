from api import create_app
from flask_cors import CORS

api = create_app()
cors = CORS(api)
