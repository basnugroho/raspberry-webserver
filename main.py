from flask import Flask
from speedtest import speedtest_bp
from speedtest_web import speedtest_web_bp
from flt import flt_bp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Siap!"

app.register_blueprint(speedtest_bp, url_prefix='/')
app.register_blueprint(speedtest_web_bp, url_prefix='/')
app.register_blueprint(flt_bp, url_prefix='/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443)
