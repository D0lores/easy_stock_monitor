import sys
import time
import  easyquotation


def get_price(quotation,stock_code):
	a=quotation.real(stock_code)
	a[stock_code]['zdf']='%.2f%%'%((a[stock_code]['now']/a[stock_code]['close'] -1)*100)


	#print('%.2f%%'%((a[stock_code]['now']/a[stock_code]['close'] -1)*100))
	print('time:%s\nprice:%.3f\nzdf:%s\n'%(time.ctime(),a[stock_code]['now'],a[stock_code]['zdf']))

if __name__ == "__main__":

	stock_code=sys.argv[1]
	quotation = easyquotation.use('sina') 

	timeout = time.time() + 5
	while True:
		time.sleep(1)
		if time.time() > timeout:
			get_price(quotation,stock_code)
			timeout=time.time() + 5
	
