num = int(input("Enter the number atleast 2 digits: "))

f = fact(num)
print(f)
s =sod(num)
print(s)
def fact(n):
	f=1
	for i in range(1, n+1):
		f=f*i
	return f
def sod(n):
	s=0
	while(n>0):
		d=n%10
		s+=d
		n=n//10

	return s