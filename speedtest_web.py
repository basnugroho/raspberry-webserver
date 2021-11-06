from flask import Blueprint
from flask import jsonify
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.chrome.options import Options
from time import sleep
from datetime import datetime
from speedtest import convert_time_to_wib
from typing import Text

speedtest_web_bp = Blueprint('speedtest_web', __name__)

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)

display = Display(visible=0, size=(800, 600))
web = "https://speedtest.net"
display.start()
driver.get(web)
print("browser ready")
print(web)
webs = ["https://speedtest.net", "https://youtube.com", "https://jakmall.com"]
data_glob  = ""

def speedtest_web(web):
    driver.get(web)
    print(web)
    time = convert_time_to_wib(datetime.now())
    # device info
    place = ""
    room = ""
    ssid = ""
    device = ""
    with open("/boot/info.txt") as file:
        text = file.readlines()
        place = text[0].strip()
        room = text[1].strip()
        ssid = text[2].strip()
        device = text[3].strip()

    go_button = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
    go_button.click()
    sleep(100)
    isp = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[4]/div/div[2]/div/div[1]/div/div[2]').text
    isp_ip = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[3]/div/div/div[1]/div[3]/div[2]').text
    server = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[3]/div/div/div[1]/div[2]/div[2]/a').text
    server_city = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[3]/div/div/div[1]/div[2]/div[3]').text
    ping = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
    download = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
    upload = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
    result_id = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[1]/div/div/div[2]/div[2]/a').text
    data = {
        "time": time,
        "place": place,
        "room": room,
        "ssid": ssid,
        "device": device, 
        "server": server,
        "server_city": server_city,
        "isp": isp,
        "isp_ip": isp_ip,
        "latency": ping+" ms",
        "download": download+" Mbps",
        "upload": upload+" Mbps",
        "result_url": f"https://www.speedtest.net/result/{result_id}"
        }
    #print(data)
    #driver.quit()
    return f"""{data}"""

@speedtest_web_bp.route('/speedtest_web/')
def speedtest_browser():
        return "speedtest remote di NOC dinonaktifkan"
