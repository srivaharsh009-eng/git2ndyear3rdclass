num = int(input("Enter the number atleast 2 digits: "))

f = fact(num)
print(f)

def fact(n):
	f=1
	for i in range(1, n+1):
		f=f*i
	return f
