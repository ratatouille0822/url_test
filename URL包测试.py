import urllib.request
import os

with urllib.request.urlopen("http://www.baidu.com") as req:
    html_code = req.read()
    print(html_code)
    req.close()

path = "/home/zhangshuo/test_url"
if not os.path.exists(path):
    os.mkdir(path, 0o777)
fp = open("/home/zhangshuo/test_url/1.html", "wb")
fp.write(html_code)
fp.close()
