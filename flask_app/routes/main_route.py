# 플라스크 파일에 라우터들을 계속쓰면 너무 더럽고 너무 많음
# 라우터들을 기능별로 라우터 파일들을 만들어 따로 보관
from flask import Blueprint

'''
'main' : 블루프린트의 명칭
__name__ : 블루프린트의 import 이름
url_prefix='/main' : URL 접두어 설정 (해당 블루프린트의 라우트는 URL 앞에 '/main' 가 자동으로 붙게 됩니다.)
'''
bp = Blueprint('main', __name__, url_prefix='/main')

@bp.route('/')          # 127.0.0.1.:5000 (root) + '/main' (url_prefix) +'/'(route()로 넘겨받은 인수)
def index():
    return 'User index page'