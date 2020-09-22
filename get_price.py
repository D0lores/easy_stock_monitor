
import sys
import  easyquotation




if __name__ == "__main__":

 	stock_code=sys.argv[1]
	quotation = easyquotation.use('sina') 



	a=quotation.real(stock_code)


	print (a[stock_code]['now']/a[stock_code]['close'] -1)*100
