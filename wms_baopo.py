import base64
import json
import requests

def test_wms(): 
	try:
		headers1={
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
		'Accept-Encoding': 'gzip, deflate',
		'DNT': '1',
		'X-Forwarded-For': '8.8.8.8',
		'Connection': 'close',
		'Upgrade-Insecure-Requests': '1'
		}
		url='http://127.0.0.1:8081/jeewms/randCodeImage'
		checkurl='http://127.0.0.1:8081/jeewms/loginController.do?checkuser'
		rq=requests.Session()
		res=rq.get(url=url,headers=headers1).content
		img=base64.b64encode(res).decode()
		code=api(img,1)
		#print(res)
		data={
		'userName':'admin',
		'password':'llg123',
		'randCode':code,
		'orgId':''
		}
		print(data)
		res=rq.post(url=checkurl,data=data).text
		print(res)
	except Exception as e:
		pass
def api(img,typeid):
	data = {"username": "xxx", "password": "xxx", "typeid": typeid, "image": img}
	result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
	if result['success']:
		return result["data"]["result"]
	else:
		return result["message"]
	return ""
def base64_api(uname,pwd,img,typeid):
	with open(img,'rb') as f:
		base64_data=base64.b64encode(f.read())
		b64=base64_data.decode()
	data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
	result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
	if result['success']:
		return result["data"]["result"]
	else:
		return result["message"]
	return ""
if __name__ == "__main__":
	test_wms()