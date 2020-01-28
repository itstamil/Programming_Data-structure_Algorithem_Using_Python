def gcd(m, n):
	i = min(m,n)
	while i > 0:
		if (m%i) == 0 and (n%i) == 0:
			return(i)
		else:
			i = i-1

print("Enter Values to fing Greatest common Divider")
input1 = input("Enter the First Value :")
input2 = input("Enter the Second Value :")
GCD = gcd(int(input1), int(input2))
print('The common Diviser is',GCD)