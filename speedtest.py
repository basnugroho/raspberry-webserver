from flask import Blueprint
from flask import jsonify
import re
import subprocess
import time
from datetime import datetime
import pytz

speedtest_bp = Blueprint('speedtest', __name__)

# record time
def convert_time_to_wib(dt_object):
  # set timezone ke Jakarta (WIB)
  tz = pytz.timezone("Asia/Jakarta")
  # tentukan timezone awal (dalam hal ini UTC)
  utc = pytz.timezone("UTC")
  # convert ke local datetime
  tz_aware_dt = utc.localize(dt_object)
  local_dt = tz_aware_dt.astimezone(tz)
  return local_dt.strftime("%Y-%m-%d %H:%M:%S")

@speedtest_bp.route('/speedtest/')
def speedtest():
  time = convert_time_to_wib(datetime.now())

  # run speedtest
  print(f"{time}: speed test begin")
  response = subprocess.Popen('/usr/bin/speedtest --accept-license --accept-gdpr', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')

  server = re.search('Server:\s+(.*?).*', response, re.MULTILINE)
  isp = re.search('ISP:\s+(.*?)\n', response, re.MULTILINE)
  ping = re.search('Latency:\s+(.*?)\s', response, re.MULTILINE)
  download = re.search('Download:\s+(.*?)\s', response, re.MULTILINE)
  upload = re.search('Upload:\s+(.*?)\s', response, re.MULTILINE)
  jitter = re.search('\((.*?)\s.+jitter\)\s', response, re.MULTILINE)
  packet_loss = re.search('Packet Loss:\s+(.*?)\.', response, re.MULTILINE)
  result_url = response.split("URL: ")[-1]

  # pack the data
  data = {
    "time": time,
    "server": server.group(0),
    "isp": isp.group(1),
    "latency": ping.group(1),
    "download": download.group(1),
    "download_data": re.search('Download:\s+(.*?)\s+Mbps\s+.data\s+used:\s+(.*?)\s+', response, re.MULTILINE).group().split()[-1],
    "upload": upload.group(1),
    "upload_data": re.search('Upload:\s+(.*?)\s+Mbps\s+.data\s+used:\s+(.*?)\s+', response, re.MULTILINE).group().split()[-1],
    "jitter": jitter.group(1),
    "packet_loss": packet_loss.group(1),
    "result_url": result_url
  }
  return jsonify(data)