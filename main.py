from flask import Flask
from speedtest import speedtest_bp
from flt import flt_bp

app = Flask(__name__)
app.register_blueprint(speedtest_bp, url_prefix='/speedtest')
app.register_blueprint(flt_bp, url_prefix='/flt')

app.run(host='0.0.0.0', port=443)