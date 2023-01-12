from flask import Flask, render_template , request
from routes.main_route import *
from model import *
import time
'''
CLI 명령어로 실행할 때에는 프로젝트 폴더 상위 디렉토리에서 다음과 같이 실행해 주면 됩니다.
FLASK_APP=flask_app flask run
'''
start = time.time()

app = Flask(__name__)       # 폴더이름이 __name__으로 넘겨져 flask_app이 앱의 이름이됨
app.register_blueprint(bp)  # 블루프린터를 통해서 라우트들을 따로 관리함으로서 본 파일에서는 @app.route('/')하나만 작성해놔도 됨
                            
                            # route 의 인자값에 다른 주소를 넣으면 URL 에 따라 실행하게 될 함수를 지정하는 역할
@app.route('/')             # @app.route('/') :애플리케이션의 루트 주소(127.0.0.1:5000)에 인자값 '/'를 더한것 즉 '127.0.0.1:5000/'에 접속했을 때에 밑의 함수를 실행하라
def index():
    return render_template('index.html')   #보낼수있는 타입: string, dict, tuple, response instance

@app.route('/condition/')             # @app.route('/') :애플리케이션의 루트 주소(127.0.0.1:5000)에 인자값 '/'를 더한것 즉 '127.0.0.1:5000/'에 접속했을 때에 밑의 함수를 실행하라
def condition():
    return render_template('condition.html')

@app.route('/introduce/')             # @app.route('/') :애플리케이션의 루트 주소(127.0.0.1:5000)에 인자값 '/'를 더한것 즉 '127.0.0.1:5000/'에 접속했을 때에 밑의 함수를 실행하라
def introduce():
    return render_template('introduce.html')

#time.sleep(1) 
@app.route('/result/', methods =['POST']) 
def result():
    time.sleep(1) 
    #foodtype, locate, capital 변수에 값을 받음
    capital = request.form['capital']
    locate = request.form['locate']
    foodtype = request.form['foodtype']
    
    if locate == 'seoul': 
        x, y, z = 0,1,0
    if locate == 'gyeonggi': 
        x, y, z = 1,0,0
    if locate == 'incheon': 
        x, y, z = 0,0,1

    if foodtype =='meat':
        a,b,c,d,e,f,g,h,i,j,k=1,0,0,0,0,0,0,0,0,0,0
    if foodtype =='dessert':
        a,b,c,d,e,f,g,h,i,j,k= 0,1,0,0,0,0,0,0,0,0,0
    if foodtype =='bakery':
        a,b,c,d,e,f,g,h,i,j,k= 0,0,1,0,0,0,0,0,0,0,0
    if foodtype =='bunsic':
        a,b,c,d,e,f,g,h,i,j,k=0,0,0,1,0,0,0,0,0,0,0
    if foodtype =='jp':
        a,b,c,d,e,f,g,h,i,j,k=0,0,0,0,1,0,0,0,0,0,0
    if foodtype =='ch':
        a,b,c,d,e,f,g,h,i,j,k=0,0,0,0,0,1,0,0,0,0,0
    if foodtype =='chicken':
        a,b,c,d,e,f,g,h,i,j,k=0,0,0,0,0,0,1,0,0,0,0
    if foodtype =='coffe':
        a,b,c,d,e,f,g,h,i,j,k=0,0,0,0,0,0,0,1,0,0,0
    if foodtype =='fast':
        a,b,c,d,e,f,g,h,i,j,k=0,0,0,0,0,0,0,0,1,0,0
    if foodtype =='fusion':
        a,b,c,d,e,f,g,h,i,j,k=0,0,0,0,0,0,0,0,0,1,0
    if foodtype =='korea':
        a,b,c,d,e,f,g,h,i,j,k=0,0,0,0,0,0,0,0,0,0,1
    
    #사용자 예외 처리
    try :
        capital = int(capital)
        a = income_predict(capital = capital, meat= a,dessert = b,bakery= c,bunsic = d ,jp= e,ch= f,chicken = g, coffe = h,fast= i,fusion= j,	korea = k,gyeonggi = x,	seoul = y,incheon= z)
        a = str(a)
        a = '해당 조건 프렌차이즈의 예상 수익은 ' + a + ' 만원 입니다. '
    except :        #숫자 문자열 말고 다른 입력값을 받았을때 int로 변환이 불가하고 오류발생
        a = "예산을 만원단위 숫자로 입력해주세요."
    
    print(f"{time.time()-start:.4f} sec")
    return render_template('result.html',income = a)

#print(f"{time.time()-start:.4f} sec")
'''
def create_app():
    app = Flask(__name__)

    from yourapplication.views.admin import admin
    from yourapplication.views.frontend import frontend
    app.register_blueprint(admin)
    app.register_blueprint(frontend)

    return app
'''

if __name__ == '__main__' :
    app.run()