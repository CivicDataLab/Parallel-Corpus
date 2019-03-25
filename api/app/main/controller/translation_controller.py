from flask import request
from flask_restplus import Resource

from app.main.service.translate_service import translate_text
from app.main.util.decorator import admin_token_required
from ..util.dto import TranslateDto

# from ..service.user_service import save_new_user, get_all_users, get_a_user

api = TranslateDto.api
_translate = TranslateDto.translate


@api.route('/')
@api.expect(_translate, validate=True)
class Translate(Resource):
    @api.doc('translate text')
    @api.marshal_with(_translate, envelope='data')
    def post(self):
        """get translation given english text"""
        post_data = request.json
        return translate_text(post_data)
