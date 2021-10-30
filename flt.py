from flask import Blueprint
from flask import jsonify
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.chrome.options import Options

flt_bp = Blueprint('flt', __name__)

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)

display = Display(visible=0, size=(800, 600))
display.start()

webs = ["https://detik.com", "https://youtube.com", "https://jakmall.com"]
def page_loader_fe(web):
    driver.get(web)

    ''' Use Navigation Timing  API to calculate the timings that matter the most '''   

    # navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
    responseStart = driver.execute_script("return window.performance.timing.responseStart")
    domComplete = driver.execute_script("return window.performance.timing.domComplete")

    ''' Calculate the performance'''
    # backendPerformance_calc = responseStart - navigationStart
    frontendPerformance_calc = domComplete - responseStart

    print("testing %s:" %web)
    # print("Back End (ms): %s" % backendPerformance_calc)
    print("Front End (ms): %s" % frontendPerformance_calc)
    print("\n")
    driver.quit()
    return frontendPerformance_calc


@flt_bp.route('/flt/')
def flt():
    results = []
    for web in webs:
        results.append(page_loader_fe(web))
    data = {
        "detik.com": results[0],
        "youtube.com": results[1],
        "jakmall.com": results[2]
    }
    return jsonify(data)

@flt_bp.route('/flt/<string:web>/')
def flt(web):
    result = page_loader_fe(web)
    data = {
        web: result
    }
    return jsonify(data)