import sys
import re
import math
if __name__ == '__main__':
	if len(sys.argv) != 5:
		print("emi.py <emi_type flat/rbm> <interest_rate flat(f)/monthly(m)/yearlly(m)> <borrowed money> <time month(m)/year(m)>")
		print("eg. python emi.py flat/rbm 1.0m/12.0y 12000 6m/20y")
		exit(0)
	emi_type = sys.argv[1]
	rate = sys.argv[2]
	principal = sys.argv[3]
	time = sys.argv[4]
	
	if emi_type not in ['flat', 'rbm']:
		print("please mention correct emi_type")
		exit(0)
	if bool(re.match('^[1-9][0-9]?\.[0-9][myf]$', rate)) == False:
		print("please mention correct interest rate")
		exit(0)
	if bool(re.match('(^([1-9]|1[0-2])m$)|(^[1-9][0-9]?y$)', time)) == False:
		print("please mention correct time")
		exit(0)
	
	P = int(principal)

	# duration in month
	if time[-1] == 'y':
		N = int(time[:-1])*12
	else:
		N = int(time[:-1])

	
	R = float(rate[:-1])
	
	if rate[-1] == 'y':
		R = (R/(12*100))
	else:
		R = R/100

	if emi_type == 'flat':
		emi = (P + R*P) / N
	if emi_type == 'rbm':
		emi = P*R*(pow((1+R),N)/(pow((1+R),N)-1)) 	
	
	print("monthly emi : {}".format(int(math.floor(emi))))
	print("interest paid : {}".format(int(math.ceil(emi*N - P))))
	print("total amount paid : {} in {} month".format(int(math.ceil(emi * N)), N))
	

	 
