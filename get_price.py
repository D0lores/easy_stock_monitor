import sys
import time
import  easyquotation

import hmac
import hashlib
import base64
import urllib.parse

import requests

import requests

def get_sign(secret_in):
	timestamp = str(round(time.time() * 1000))
	secret = secret_in
	secret_enc = secret.encode('utf-8')
	string_to_sign = '{}\n{}'.format(timestamp, secret)
	string_to_sign_enc = string_to_sign.encode('utf-8')
	hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
	sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
	print(timestamp)
	print(sign)
	return timestamp,sign


def get_price(quotation,stock_code):
	a=quotation.real(stock_code)
	a[stock_code]['zdf']='%.2f%%'%((a[stock_code]['now']/a[stock_code]['close'] -1)*100)

	result='time:%s\nprice:%.3f\nzdf:%s\n'%(time.ctime(),a[stock_code]['now'],a[stock_code]['zdf'])

	#print('%.2f%%'%((a[stock_code]['now']/a[stock_code]['close'] -1)*100))
	print(result)
	return result
	
	
def dingtalk_notify(access_token,timestamp,sign,content):
	url = 'https://oapi.dingtalk.com/robot/send?access_token='+access_token+'&timestamp='+timestamp+'&sign='+sign
	myjson={"msgtype": "text", "text": {"content": content}	}
	x = requests.post(url, json = myjson)
	print(x.text)


if __name__ == "__main__":

	 stock_code=sys.argv[1]
	 quotation = easyquotation.use('sina') 

	 timeout = time.time() + 5
	 while True:
		 time.sleep(1)
		 if time.time() > timeout:
			 content=get_price(quotation,stock_code)
			 ts,sign=get_sign('you_sec_here')
			 dingtalk_notify('you_access_token_here',ts,sign,content)
			 timeout=time.time() + 5
	
