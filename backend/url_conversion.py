import string

from flask import Blueprint, request, jsonify, Flask


shortener_bp = Blueprint('shortener', __name__)

BASE62 = string.digits + string.ascii_lowercase + string.ascii_uppercase

def to_base62(num):
    base62 = ""
    while num > 0:
        num, rem = divmod(num, 62)
        base62 = BASE62[rem] + base62_str
    return base62_str

url_map = {}
@shortener_bp.route("/test", methods=["POST"])
def test():
    data = request.get_json()
    url_id = hash(original_url)

