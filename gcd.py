def gcd(m, n):
	fm = []
	for i in range(1,m+1):
		if (m%i) == 0:
			fm.append(i)
	fn = []
	for j in range(1,n+1):
		if (n%j) == 0:
			fn.append(j)
	cf = []
	for k in fm:
		if k in fn:
			cf.append(k)
	return(cf[-1])

print("Enter Values to fing Greatest comman Divider")
val1 = input("Enter the First Value :")
val2 = input("Enter the Second Value :")
GCD = gcd(int(val1), int(val2))
print('The comman Diviser is',GCD)