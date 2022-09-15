def recur_fibo(n):
	if n <=1:
		return n
	else:
		return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input("How many terms? "))

if nterms <= 0:
	print("Only works for positive integers")
else:
	print("Fibonacci sequence:")
	for i in range(nterms):
		print(i + 1, ":", recur_fibo(i))


