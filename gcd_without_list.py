def gcd(m, n):
	cf = []
	for i in range(1,min(m,n)+1):
		if (m%i) == 0 and (n%i) == 0:
			# most recent comman factor
			mrcf = i
	return(mrcf)

print("Enter Values to fing Greatest common Divider")
input1 = input("Enter the First Value :")
input2 = input("Enter the Second Value :")
GCD = gcd(int(input1), int(input2))
print('The common Diviser is',GCD)