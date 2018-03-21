import requests
import demjson

cookies = {
    'JSESSIONID': '405ACCA6CA24FD50717D3701193A045A',
}

headers = {
    'Origin': 'http://cs.whxueying.com',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-HK;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'http://cs.whxueying.com/managerJumpAction.action?firstMenu=1&secondMenu=11',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

data = [
  ('pid', '1'),
]

response = requests.post('http://cs.whxueying.com/allGpsAndStateAction.action', headers=headers, cookies=cookies, data=data)

text = response.text
d = demjson.decode(text)
print(d.get("list"))
