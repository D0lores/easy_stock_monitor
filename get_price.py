import sys
import  easyquotation




if __name__ == "__main__":

	stock_code=sys.argv[1]
	quotation = easyquotation.use('sina') 



	a=quotation.real(stock_code)
	a[stock_code]['zdf']='%.2f%%'%((a[stock_code]['now']/a[stock_code]['close'] -1)*100)


	#print('%.2f%%'%((a[stock_code]['now']/a[stock_code]['close'] -1)*100))
	print('now:%.3f\nzdf:%s\n'%(a[stock_code]['now'],a[stock_code]['zdf']))
