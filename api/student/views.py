

from flask import Blueprint
from flask import jsonify
from .models import Student,Teacher
crud_blueprint = Blueprint('crud', __name__, url_prefix='/')

@crud_blueprint.route('',methods=['POST','GET','PUT','DELETE'])
def index():
    return success({},"SUCCESS")

def success(content, msg, message=None):
    res = {}
    res['content'] = content
    resp = {}
    resp['status'] = 200
    resp['message'] = f'Successfully {msg}'
    if message:
        resp['message'] = message
    res['response'] = resp
    response = jsonify(res)
    response.status_code = 200
    response.content_type = "application/json"
    return response