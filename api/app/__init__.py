from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.translation_controller import api as translate_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Samantar api',
          version='1.0',
          description='tranaslation for Samantar project'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(translate_ns)